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

"""API Key 管理模块共用 Swagger 定义"""

from typing import Dict, Any

from ..helpers import create_query_param

# ==================== API Key 状态枚举 ====================

APIKEY_STATUSES = ['active', 'disabled', 'deleted', 'expired']
"""API Key 状态枚举值"""

# ==================== Schema 定义 ====================

APIKEY_OBJECT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': 'API Key ID'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'user_name': {'type': 'string', 'description': '用户名'},
        'tenant_list': {'type': 'string', 'description': '空间列表（逗号分隔）'},
        'api_key': {'type': 'string', 'description': 'API Key'},
        'description': {'type': 'string', 'description': '描述'},
        'status': {'type': 'string', 'description': '状态'},
        'expire_date': {'type': 'string', 'format': 'date', 'description': '过期日期'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'}
    }
}
"""API Key 对象 schema"""

# ==================== 参数定义函数 ====================

def apikey_create_body_schema() -> Dict[str, Any]:
    """生成创建 API Key 的请求体 schema。

    Returns:
        创建 API Key 请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'description': {'type': 'string', 'description': 'API Key 描述'},
            'expire_date': {'type': 'string', 'format': 'date', 'description': '过期日期，格式：YYYY-MM-DD'},
            'tenant_id': {'type': 'string', 'description': '空间ID，多个空间ID用逗号分隔'}
        },
        'required': ['tenant_id']
    }


def apikey_update_body_schema() -> Dict[str, Any]:
    """生成更新 API Key 状态的请求体 schema。

    Returns:
        更新 API Key 状态请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer', 'description': 'API Key ID'},
            'status': {
                'type': 'string',
                'enum': APIKEY_STATUSES,
                'description': '状态：active, disabled, deleted, expired'
            }
        },
        'required': ['id', 'status']
    }


def apikey_delete_body_schema() -> Dict[str, Any]:
    """生成删除 API Key 的请求体 schema。

    Returns:
        删除 API Key 请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer', 'description': 'API Key ID'}
        },
        'required': ['id']
    }


def apikey_chat_body_schema() -> Dict[str, Any]:
    """生成 API Key 对话的请求体 schema。

    Returns:
        API Key 对话请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'inputs': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '输入内容列表',
                'minItems': 1
            },
            'mode': {
                'type': 'string',
                'default': 'publish',
                'description': '运行模式，默认为 publish'
            },
            'files': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '文件列表，可为空'
            }
        },
        'required': ['inputs']
    }
