# Copyright (c) 2026 SenseTime. All Rights Reserved.
# Author: LazyLLM Team,  https://github.com/LazyAGI/LazyLLM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""模型微调模块的 Swagger 定义"""

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']
FINETUNING_TYPE_ENUM = ['LoRA', 'QLoRA', 'Full']
TRAINING_TYPE_ENUM = ['PT', 'SFT', 'RM', 'PPO', 'DPO']

# ==================== Schema 定义 ====================

ACCOUNT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'avatar': {'type': 'string'},
    },
}

FINETUNE_DETAIL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '任务ID'},
        'name': {'type': 'string', 'description': '任务名称'},
        'description': {'type': 'string', 'description': '任务描述'},
        'base_model': {'type': 'string', 'description': '基础模型UUID'},
        'base_model_key': {'type': 'string', 'description': '基础模型key'},
        'target_model_name': {'type': 'string', 'description': '微调后的模型名称'},
        'target_model': {'type': 'string', 'description': '目标模型UUID'},
        'status': {'type': 'string', 'description': '任务状态'},
        'status_label': {'type': 'string', 'description': '任务状态（中文）'},
        'created_from_info': {'type': 'string', 'description': '创建来源'},
        'train_runtime': {'type': 'integer', 'description': '训练运行时间（秒）'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'created_by_account': ACCOUNT_SCHEMA,
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
        'log_path': {'type': 'string', 'description': '日志路径'},
        'finetuning_type': {'type': 'string', 'description': '微调类型'},
        'finetune_config': {'type': 'object', 'description': '微调配置'},
        'train_end_time': {'type': 'string', 'format': 'date-time'},
        'user_name': {'type': 'string', 'description': '用户名'},
    },
}

FINETUNE_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'limit': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': FINETUNE_DETAIL_SCHEMA,
            'description': '微调任务列表'
        },
    },
}

CUSTOM_PARAM_ITEM_SCHEMA = {
    'type': 'object',
    'properties': {
        'training_type': {'type': 'string', 'description': '训练模式 (PT, SFT, RM, PPO, DPO)'},
        'val_size': {'type': 'number', 'description': '验证集占比'},
        'num_epochs': {'type': 'integer', 'description': '重复次数'},
        'learning_rate': {'type': 'number', 'description': '学习率'},
        'lr_scheduler_type': {'type': 'string', 'description': '学习率调整策略'},
        'batch_size': {'type': 'integer', 'description': '批次大小'},
        'cutoff_len': {'type': 'integer', 'description': '序列最大长度'},
        'lora_r': {'type': 'integer', 'description': 'LoRa秩'},
        'lora_rate': {'type': 'integer', 'description': '微调占比'},
        'lora_alpha': {'type': 'integer', 'description': 'LoRa alpha'},
        'num_gpus': {'type': 'integer', 'description': 'GPU数量'},
    },
}

FINETUNE_PARAM_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '参数ID'},
        'name': {'type': 'string', 'description': '参数名称'},
        'is_default': {'type': 'boolean', 'description': '是否默认'},
        'finetune_config': CUSTOM_PARAM_ITEM_SCHEMA,
    },
}

# ==================== 参数定义 ====================

def task_id_path_param():
    """任务ID路径参数"""
    return {
        'name': 'task_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '微调任务ID'
    }

def finetune_create_params():
    """创建微调任务参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'base': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'required': True, 'description': '任务名称'},
                            'base_model': {'type': 'string', 'description': '基础模型UUID，调用ft接口后固定传0'},
                            'base_model_key': {'type': 'string', 'required': True, 'description': '调用ft接口获取的模型名字（格式：model_key:ams）'},
                            'target_model_name': {'type': 'string', 'required': True, 'description': '微调后的模型名称'},
                            'created_from_info': {'type': 'string', 'description': '创建来源'},
                            'datasets': {
                                'type': 'array',
                                'items': {'type': 'string', 'format': 'uuid'},
                                'required': True,
                                'description': '数据集UUID列表'
                            },
                            'datasets_type': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': '数据集类型列表'
                            },
                            'finetuning_type': {
                                'type': 'string',
                                'enum': FINETUNING_TYPE_ENUM,
                                'required': True,
                                'description': '微调类型：LoRA/QLoRA/Full'
                            },
                        },
                        'required': ['name', 'base_model_key', 'target_model_name', 'datasets', 'finetuning_type']
                    },
                    'finetune_config': {
                        'type': 'object',
                        'properties': {
                            'num_gpus': {'type': 'integer', 'description': 'GPU数量'},
                            'training_type': {
                                'type': 'string',
                                'enum': TRAINING_TYPE_ENUM,
                                'description': '训练模式：PT/SFT/RM/PPO/DPO'
                            },
                            'val_size': {'type': 'number', 'description': '验证集占比'},
                            'num_epochs': {'type': 'integer', 'description': '重复次数'},
                            'learning_rate': {'type': 'number', 'description': '学习率'},
                            'lr_scheduler_type': {'type': 'string', 'description': '学习率调整策略'},
                            'batch_size': {'type': 'integer', 'description': '批次大小'},
                            'cutoff_len': {'type': 'string', 'description': '序列最大长度'},
                            'lora_r': {'type': 'integer', 'description': 'LoRa秩'},
                            'lora_rate': {'type': 'integer', 'description': '微调占比'},
                        },
                        'required': []
                    },
                },
                'required': ['base', 'finetune_config']
            },
        },
    ]

def finetune_list_page_params():
    """微调任务列表查询参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {
                        'type': 'integer',
                        'default': 1,
                        'minimum': 1,
                        'maximum': 99999,
                        'description': '页码，从1开始'
                    },
                    'limit': {
                        'type': 'integer',
                        'default': 20,
                        'minimum': 1,
                        'maximum': 100,
                        'description': '每页数量'
                    },
                    'qtype': {
                        'type': 'string',
                        'enum': QTYPE_ENUM,
                        'default': 'already',
                        'description': '查询类型：mine（我的）/group（组内）/builtin（内置）/already（已访问）'
                    },
                    'search_name': {
                        'type': 'string',
                        'default': '',
                        'description': '任务名称搜索关键词'
                    },
                    'status': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'default': [],
                        'description': '状态过滤列表'
                    },
                    'user_id': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'default': [],
                        'description': '用户ID过滤列表'
                    },
                },
                'required': []
            },
        },
    ]

def finetune_model_params():
    """获取微调模型列表参数"""
    return [
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'enum': QTYPE_ENUM,
            'default': 'already',
            'required': True,
            'description': '查询类型：mine/group/builtin/already'
        },
    ]

def finetune_dataset_params():
    """获取微调数据集列表参数"""
    return [
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'enum': QTYPE_ENUM,
            'default': 'already',
            'required': True,
            'description': '查询类型：mine/group/builtin/already'
        },
    ]

def finetune_custom_param_post_params():
    """保存自定义参数参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'required': True, 'description': '参数名称'},
                    'finetune_config': {
                        'type': 'object',
                        'properties': CUSTOM_PARAM_ITEM_SCHEMA['properties'],
                        'required': True,
                        'description': '微调配置'
                    },
                },
                'required': ['name', 'finetune_config']
            },
        },
    ]

def finetune_custom_param_delete_params():
    """删除自定义参数参数"""
    return [
        {
            'name': 'record_id',
            'in': 'query',
            'type': 'integer',
            'default': 0,
            'description': '记录ID'
        },
    ]
