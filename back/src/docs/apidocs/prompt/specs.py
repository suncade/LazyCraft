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

"""Prompt模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    PROMPT_SCHEMA,
    PROMPT_PAGINATION_SCHEMA,
    prompt_create_params,
    prompt_id_path_param,
    prompt_update_params,
    prompt_list_params,
)


# ==================== Prompt管理相关接口 ====================

# 创建提示信息
prompt_create_spec: Dict[str, Any] = {
    'tags': ['Prompt'],
    'summary': '创建提示信息',
    'description': '创建新的提示信息，支持包含名称、描述、内容和分类的提示信息，需要登录和写入权限',
    'parameters': prompt_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'description': '创建的提示信息ID'},
                        },
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取提示信息
prompt_get_spec: Dict[str, Any] = {
    'tags': ['Prompt'],
    'summary': '获取提示信息',
    'description': '根据提示信息ID获取其详细信息，包括名称、描述、内容、分类和时间戳等，需要登录',
    'parameters': [prompt_id_path_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': PROMPT_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新提示信息
prompt_update_spec: Dict[str, Any] = {
    'tags': ['Prompt'],
    'summary': '更新提示信息',
    'description': '根据提示信息ID和用户提交的数据更新提示信息，内置提示信息需要超级管理员权限，需要登录和写入权限',
    'parameters': [prompt_id_path_param()] + prompt_update_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '修改成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除提示信息
prompt_delete_spec: Dict[str, Any] = {
    'tags': ['Prompt'],
    'summary': '删除提示信息',
    'description': '根据提示信息ID删除提示信息，内置提示信息需要超级管理员权限，需要登录和管理员权限',
    'parameters': [prompt_id_path_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': '删除成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取提示信息列表
prompt_list_spec: Dict[str, Any] = {
    'tags': ['Prompt'],
    'summary': '获取提示信息列表',
    'description': '分页获取所有提示信息的列表，支持按查询类型、标签、名称、用户ID等条件筛选，需要登录',
    'parameters': prompt_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': PROMPT_PAGINATION_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}
