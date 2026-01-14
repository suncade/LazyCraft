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

"""模型评测模块的 Swagger 定义"""

# ==================== Schema 定义 ====================

TASK_INFO_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '任务ID'},
        'name': {'type': 'string', 'description': '任务名称'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'evaluation_method': {'type': 'string', 'description': '评估方法（manual/ai）'},
        'created_time': {'type': 'string', 'format': 'date-time'},
        'username': {'type': 'string', 'description': '创建者用户名'},
        'status': {'type': 'string', 'description': '任务状态'},
        'status_zh': {'type': 'string', 'description': '任务状态（中文）'},
        'ai_eva_success': {'type': 'integer', 'description': 'AI评估成功数'},
        'ai_eva_fail': {'type': 'integer', 'description': 'AI评估失败数'},
        'ai_evaluator_name': {'type': 'string', 'description': 'AI评估器名称'},
        'process': {'type': 'string', 'description': '任务进度'},
    },
}

TASK_LIST_ITEM_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '任务ID'},
        'name': {'type': 'string', 'description': '任务名称'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'evaluation_method': {'type': 'string', 'description': '评估方法'},
        'process': {'type': 'string', 'description': '任务进度'},
        'status': {'type': 'string', 'description': '任务状态'},
        'status_zh': {'type': 'string', 'description': '任务状态（中文）'},
        'created_time': {'type': 'string', 'format': 'date-time'},
        'creator': {'type': 'string', 'description': '创建者'},
    },
}

TASK_LIST_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'tasks': {
            'type': 'array',
            'items': TASK_LIST_ITEM_SCHEMA,
            'description': '任务列表'
        },
        'total': {'type': 'integer', 'description': '总记录数'},
        'pages': {'type': 'integer', 'description': '总页数'},
        'current_page': {'type': 'integer', 'description': '当前页码'},
        'per_page': {'type': 'integer', 'description': '每页数量'},
    },
}

DIMENSION_OPTION_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '选项ID'},
        'option_description': {'type': 'string', 'description': '选项描述'},
        'value': {'type': 'integer', 'description': '选项分值'},
    },
}

EVALUATION_DIMENSION_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '维度ID'},
        'dimension_name': {'type': 'string', 'description': '维度名称'},
        'dimension_description': {'type': 'string', 'description': '维度描述'},
        'ai_base_score': {'type': 'integer', 'description': 'AI基础分值'},
        'options': {
            'type': 'array',
            'items': DIMENSION_OPTION_SCHEMA,
            'description': '维度选项列表'
        },
    },
}

EVALUATION_SUMMARY_DIMENSION_SCHEMA = {
    'type': 'object',
    'properties': {
        'dimension_name': {'type': 'string', 'description': '维度名称'},
        'average_score': {'type': 'number', 'description': '平均分'},
        'std_dev': {'type': 'number', 'description': '标准差'},
        'total_score': {'type': 'number', 'description': '总分'},
        'indicators': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'option_id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'score': {'type': 'number'},
                    'total_score': {'type': 'number'},
                    'percentage': {'type': 'string'},
                },
            },
            'description': '指标列表（仅人工测评）'
        },
    },
}

EVALUATION_SUMMARY_SCHEMA = {
    'type': 'object',
    'properties': {
        'task_name': {'type': 'string', 'description': '任务名称'},
        'created_by': {'type': 'string', 'description': '创建者'},
        'evaluation_method': {'type': 'string', 'description': '评估方法'},
        'progress': {'type': 'string', 'description': '任务进度'},
        'dimensions': {
            'type': 'array',
            'items': EVALUATION_SUMMARY_DIMENSION_SCHEMA,
            'description': '维度总结列表'
        },
    },
}

# ==================== 参数定义 ====================

def upload_dataset_params():
    """上传数据集参数"""
    return [
        {
            'name': 'files',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '要上传的文件列表，支持格式：json、csv、xlsx、zip、tar.gz。单个文件最大1GB'
        },
    ]

def create_task_params():
    """创建评估任务参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'task_name': {
                        'type': 'string',
                        'required': True,
                        'description': '任务名称'
                    },
                    'dataset_id': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'required': True,
                        'description': '数据集ID列表'
                    },
                    'evaluation_method': {
                        'type': 'string',
                        'enum': ['manual', 'ai'],
                        'required': True,
                        'description': '评估方法：manual（人工测评）/ai（AI测评）'
                    },
                    'model_name': {
                        'type': 'string',
                        'required': True,
                        'description': '测评模型名称'
                    },
                    'evaluation_type': {
                        'type': 'string',
                        'enum': ['offline', 'online'],
                        'required': True,
                        'description': '评估类型：offline（离线）/online（在线）'
                    },
                    'dimensions': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'dimension_name': {'type': 'string'},
                                'dimension_description': {'type': 'string'},
                                'ai_base_score': {'type': 'integer'},
                                'options': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'option_description': {'type': 'string'},
                                            'value': {'type': 'integer'},
                                        },
                                    },
                                },
                            },
                        },
                        'required': True,
                        'description': '评估维度列表'
                    },
                    'ai_evaluator_name': {
                        'type': 'string',
                        'required': False,
                        'description': 'AI评估器名称（当evaluation_method为ai时必填）'
                    },
                    'prompt': {
                        'type': 'string',
                        'required': False,
                        'description': 'AI评估prompt（当evaluation_method为ai时可选，需包含{scene}、{scene_descrp}、{standard}、{instruction}、{output}、{response}占位符）'
                    },
                },
                'required': ['task_name', 'dataset_id', 'evaluation_method', 'model_name', 'evaluation_type', 'dimensions']
            },
        },
    ]

def task_id_path_param():
    """任务ID路径参数"""
    return {
        'name': 'task_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '任务ID'
    }

def task_list_params():
    """任务列表查询参数"""
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'default': 1,
            'description': '页码，从1开始'
        },
        {
            'name': 'per_page',
            'in': 'query',
            'type': 'integer',
            'default': 10,
            'description': '每页数量'
        },
        {
            'name': 'keyword',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '搜索关键词'
        },
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '查询类型'
        },
    ]

def evaluate_params():
    """执行评估参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'task_id': {
                        'type': 'integer',
                        'required': True,
                        'description': '任务ID'
                    },
                    'data_id': {
                        'type': 'integer',
                        'required': True,
                        'description': '数据ID'
                    },
                    'evaluations': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'dimension_id': {'type': 'integer', 'description': '维度ID'},
                                'option_select_id': {'type': 'integer', 'description': '选项ID（人工测评）'},
                                'score': {'type': 'integer', 'description': '评分（AI测评）'},
                            },
                        },
                        'required': True,
                        'description': '评估数据列表'
                    },
                },
                'required': ['task_id', 'data_id', 'evaluations']
            },
        },
    ]

def evaluation_data_paginator_params():
    """评估数据分页查询参数"""
    return [
        task_id_path_param(),
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': '页码'
        },
        {
            'name': 'option_select_id',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': '选项ID（用于报告查看）'
        },
    ]

def download_report_excel_params():
    """下载评估报告参数"""
    return [
        task_id_path_param(),
        {
            'name': 'token',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '认证令牌'
        },
    ]

def download_dataset_tpl_path_param():
    """下载数据集模板路径参数"""
    return {
        'name': 'template_type',
        'in': 'path',
        'type': 'string',
        'enum': ['xlsx', 'csv', 'json'],
        'required': True,
        'description': '模板类型：xlsx/csv/json'
    }
