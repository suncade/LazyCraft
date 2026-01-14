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

"""模型评测模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    TASK_INFO_SCHEMA,
    TASK_LIST_PAGINATION_SCHEMA,
    EVALUATION_DIMENSION_SCHEMA,
    EVALUATION_SUMMARY_SCHEMA,
    upload_dataset_params,
    create_task_params,
    task_id_path_param,
    task_list_params,
    evaluate_params,
    evaluation_data_paginator_params,
    download_report_excel_params,
    download_dataset_tpl_path_param,
)


# ==================== 数据集相关接口 ====================

# 上传数据集
upload_dataset_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '上传评估数据集',
    'description': '上传评估数据集文件，支持格式：json、csv、xlsx、zip、tar.gz。单个文件最大1GB，需要登录',
    'parameters': upload_dataset_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '上传文件成功'},
                    'result': {
                        'type': 'object',
                        'properties': {
                            'dataset_id': {'type': 'integer', 'description': '数据集ID'},
                        },
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 下载数据集模板
download_dataset_tpl_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '下载数据集模板',
    'description': '下载评估数据集的模板文件，支持xlsx、csv、json三种格式，不需要登录',
    'parameters': [
        download_dataset_tpl_path_param(),
    ],
    'responses': {
        **standard_error_responses(include_403=False, include_404=True),
        '200': {
            'description': '下载成功',
            'schema': {
                'type': 'file',
            },
        },
    },
}


# ==================== 任务管理相关接口 ====================

# 创建评估任务
create_task_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '创建评估任务',
    'description': '创建新的评估任务，支持人工测评和AI测评两种方式，需要登录和写入权限',
    'parameters': create_task_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '任务创建成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取任务列表
task_list_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取任务列表',
    'description': '分页获取评估任务列表，支持按关键词和查询类型筛选，需要登录',
    'parameters': task_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'result': TASK_LIST_PAGINATION_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取任务详情
task_info_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取任务详情',
    'description': '获取指定评估任务的详细信息，需要登录',
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
                    'result': {
                        'type': 'object',
                        'properties': {
                            'task_info': TASK_INFO_SCHEMA,
                        },
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除任务
delete_task_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '删除任务',
    'description': '删除指定的评估任务，需要登录和管理员权限',
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
                    'message': {'type': 'string', 'example': '任务删除成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}


# ==================== 评估相关接口 ====================

# 获取评估维度
evaluation_dimension_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取评估维度',
    'description': '获取指定任务的评估维度信息，包括维度选项，需要登录',
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
                    'result': {
                        'type': 'array',
                        'items': EVALUATION_DIMENSION_SCHEMA,
                        'description': '评估维度列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 执行评估
evaluate_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '执行评估',
    'description': '提交评估结果，支持人工测评和AI测评，需要登录和管理员权限',
    'parameters': evaluate_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '提交成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '提交成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取评估数据分页
evaluation_data_paginator_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取评估数据',
    'description': '分页获取指定任务的评估数据，支持按选项筛选，需要登录',
    'parameters': evaluation_data_paginator_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'result': {'type': 'object', 'description': '评估数据分页结果'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}


# ==================== 模型和数据相关接口 ====================

# 获取所有模型
evaluation_model_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取所有模型',
    'description': '获取可用于评估的模型列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'result': {
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

# 获取在线数据集
evaluation_online_data_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取在线数据集',
    'description': '获取可用的在线评估数据集列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'result': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '在线数据集列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}


# ==================== 报告相关接口 ====================

# 获取评估总结
evaluation_summary_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '获取评估总结',
    'description': '获取指定任务的评估总结信息，包括各维度的统计信息，需要登录',
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
                    'result': EVALUATION_SUMMARY_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 下载评估报告
download_report_excel_spec: Dict[str, Any] = {
    'tags': ['模型评测'],
    'summary': '下载评估报告',
    'description': '下载评估任务的Excel报告文件，可通过token参数进行认证，不需要登录（通过token认证）',
    'parameters': download_report_excel_params(),
    'responses': {
        **standard_error_responses(include_403=True, include_404=True),
        '200': {
            'description': '下载成功',
            'schema': {
                'type': 'file',
            },
        },
    },
}
