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

"""API Key 管理模块所有接口的 Swagger 定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    APIKEY_OBJECT_SCHEMA,
    apikey_create_body_schema,
    apikey_update_body_schema,
    apikey_delete_body_schema,
    apikey_chat_body_schema,
)

# ==================== API Key 管理接口 ====================

# 获取 API Key 列表
apikey_list_spec: Dict[str, Any] = {
    'tags': ['API Key'],
    'summary': '获取 API Key 列表',
    'description': '获取当前用户的所有 API Key 列表',
    'parameters': [],
    'responses': {
        200: {
            'description': '成功返回 API Key 列表',
            'schema': {
                'type': 'array',
                'items': deepcopy(APIKEY_OBJECT_SCHEMA)
            }
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建 API Key
apikey_create_spec: Dict[str, Any] = {
    'tags': ['API Key'],
    'summary': '创建 API Key',
    'description': '创建新的 API Key',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': apikey_create_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功创建 API Key',
            'schema': deepcopy(APIKEY_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除 API Key
apikey_delete_spec: Dict[str, Any] = {
    'tags': ['API Key'],
    'summary': '删除 API Key',
    'description': '删除指定的 API Key',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': apikey_delete_body_schema()
        }
    ],
    'responses': {
        204: {
            'description': '成功删除'
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新 API Key 状态
apikey_update_spec: Dict[str, Any] = {
    'tags': ['API Key'],
    'summary': '更新 API Key 状态',
    'description': '更新 API Key 的状态（active, disabled, deleted, expired）',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': apikey_update_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功更新',
            'schema': deepcopy(APIKEY_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# API Key 对话
apikey_chat_spec: Dict[str, Any] = {
    'tags': ['API Key'],
    'summary': 'API Key 对话',
    'description': '使用 API Key 与指定应用进行对话',
    'parameters': [
        {
            'name': 'app_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '应用ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': apikey_chat_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功返回对话结果',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'object', 'description': '对话结果数据'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': [{'Bearer': []}]
}
