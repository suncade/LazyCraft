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

"""模型微调模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    FINETUNE_DETAIL_SCHEMA,
    FINETUNE_PAGINATION_SCHEMA,
    FINETUNE_PARAM_SCHEMA,
    task_id_path_param,
    finetune_create_params,
    finetune_list_page_params,
    finetune_model_params,
    finetune_dataset_params,
    finetune_custom_param_post_params,
    finetune_custom_param_delete_params,
)


# ==================== 微调任务管理相关接口 ====================

# 创建微调任务
finetune_create_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '创建微调任务',
    'description': '创建新的模型微调任务，需要登录和写入权限',
    'parameters': finetune_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': FINETUNE_DETAIL_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取微调任务分页列表
finetune_list_page_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取微调任务列表',
    'description': '分页获取微调任务列表，支持按任务名称、状态、用户ID等条件筛选，需要登录',
    'parameters': finetune_list_page_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': FINETUNE_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取微调任务详情
finetune_detail_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取微调任务详情',
    'description': '获取指定微调任务的详细信息，需要登录',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': FINETUNE_DETAIL_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除微调任务
finetune_delete_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '删除微调任务',
    'description': '删除指定的微调任务，需要登录和管理员权限',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 取消微调任务
finetune_cancel_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '取消微调任务',
    'description': '取消正在进行的微调任务，需要登录和写入权限',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '取消成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 启动微调任务
finetune_start_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '启动微调任务',
    'description': '异步启动指定的微调任务，需要登录和写入权限',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '启动成功',
            'schema': {
                'type': 'boolean',
                'example': True,
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 暂停微调任务
finetune_pause_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '暂停微调任务',
    'description': '暂停正在进行的微调任务，需要登录和写入权限',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '暂停成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '操作成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 恢复微调任务
finetune_resume_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '恢复微调任务',
    'description': '恢复已暂停的微调任务，需要登录和写入权限',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '恢复成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '操作成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取微调任务运行指标
finetune_running_metrics_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取微调任务运行指标',
    'description': '获取指定微调任务的实时运行指标，需要登录',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {'type': 'object', 'description': '运行指标数据'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取微调任务日志
finetune_log_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取微调任务日志',
    'description': '获取指定微调任务的日志内容，需要登录',
    'parameters': [
        task_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'file',
                'description': '日志文件内容'
            },
        },
    },
    'security': AUTH_SECURITY,
}


# ==================== 模型和数据集相关接口 ====================

# 获取可用于微调的模型列表
finetune_model_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取可用于微调的模型列表',
    'description': '根据查询类型获取可用于微调的模型列表，需要登录',
    'parameters': finetune_model_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '模型列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取可用于微调的数据集列表
finetune_dataset_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取可用于微调的数据集列表',
    'description': '根据查询类型获取可用于微调的数据集列表（树形结构），需要登录',
    'parameters': finetune_dataset_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {'type': 'object', 'description': '数据集树形结构'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取FT模型列表
finetune_ft_model_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取FT模型列表',
    'description': '获取可用的FT模型列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                    'data': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'FT模型列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}


# ==================== 自定义参数相关接口 ====================

# 获取自定义参数列表
finetune_custom_param_get_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '获取自定义参数列表',
    'description': '获取当前用户的自定义参数列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {
                        'type': 'array',
                        'items': FINETUNE_PARAM_SCHEMA,
                        'description': '自定义参数列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 保存自定义参数
finetune_custom_param_post_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '保存自定义参数',
    'description': '保存用户的自定义参数配置，需要登录和写入权限',
    'parameters': finetune_custom_param_post_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '保存成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': FINETUNE_PARAM_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除自定义参数
finetune_custom_param_delete_spec: Dict[str, Any] = {
    'tags': ['模型微调'],
    'summary': '删除自定义参数',
    'description': '删除指定的自定义参数记录，需要登录和写入权限',
    'parameters': finetune_custom_param_delete_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}
