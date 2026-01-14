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

"""系统消息模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== Schema 定义 ====================

NOTIFICATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '通知ID'},
        'module': {'type': 'string', 'description': '消息所属模块'},
        'source_id': {'type': 'string', 'description': '来源ID'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'user_body': {'type': 'string', 'description': '用户回执消息体'},
        'user_read': {'type': 'boolean', 'description': '用户是否已读回执消息'},
        'user_read_time': {'type': 'string', 'description': '用户已读回执时间'},
        'notify_user1_id': {'type': 'string', 'description': '通知人1的ID'},
        'notify_user1_body': {'type': 'string', 'description': '通知人1消息体'},
        'notify_user1_read': {'type': 'boolean', 'description': '通知人1是否已读'},
        'notify_user1_read_time': {'type': 'string', 'description': '通知人1已读时间'},
        'notify_user2_id': {'type': 'string', 'description': '通知人2的ID'},
        'notify_user2_body': {'type': 'string', 'description': '通知人2消息体'},
        'notify_user2_read': {'type': 'boolean', 'description': '通知人2是否已读'},
        'notify_user2_read_time': {'type': 'string', 'description': '通知人2已读时间'},
        'created_at': {'type': 'string', 'description': '创建时间'},
    },
}

NOTIFICATION_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'items': {
            'type': 'array',
            'items': NOTIFICATION_SCHEMA,
            'description': '通知列表'
        },
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'pages': {'type': 'integer', 'description': '总页数'},
    },
}

# ==================== 请求 Schema 定义 ====================

NOTIFICATION_CREATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'module': {
            'type': 'string',
            'required': True,
            'description': '模块名称，如"quota_request"'
        },
        'source_id': {
            'type': 'string',
            'required': True,
            'description': '源对象ID'
        },
        'user_id': {
            'type': 'string',
            'required': True,
            'description': '用户ID'
        },
        'user_body': {
            'type': 'string',
            'required': True,
            'description': '用户通知内容'
        },
        'user_read': {
            'type': 'boolean',
            'required': False,
            'default': False,
            'description': '用户是否已读'
        },
        'user_read_time': {
            'type': 'string',
            'required': False,
            'description': '用户阅读时间'
        },
        'notify_user1_id': {
            'type': 'string',
            'required': True,
            'description': '通知用户1的ID'
        },
        'notify_user1_body': {
            'type': 'string',
            'required': True,
            'description': '通知用户1的内容'
        },
        'notify_user1_read': {
            'type': 'boolean',
            'required': False,
            'default': False,
            'description': '通知用户1是否已读'
        },
        'notify_user1_read_time': {
            'type': 'string',
            'required': False,
            'description': '通知用户1的阅读时间'
        },
        'notify_user2_id': {
            'type': 'string',
            'required': False,
            'description': '通知用户2的ID'
        },
        'notify_user2_body': {
            'type': 'string',
            'required': False,
            'description': '通知用户2的内容'
        },
        'notify_user2_read': {
            'type': 'boolean',
            'required': False,
            'default': False,
            'description': '通知用户2是否已读'
        },
        'notify_user2_read_time': {
            'type': 'string',
            'required': False,
            'description': '通知用户2的阅读时间'
        },
        'created_at': {
            'type': 'string',
            'required': False,
            'description': '创建时间'
        },
    },
    'required': ['module', 'source_id', 'user_id', 'user_body', 'notify_user1_id', 'notify_user1_body'],
}

NOTIFICATION_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': '页码，从 1 开始'
        },
        'page_size': {
            'type': 'integer',
            'required': False,
            'default': 100,
            'description': '每页数量'
        },
        'created_at_start': {
            'type': 'string',
            'required': False,
            'description': '创建时间开始'
        },
        'created_at_end': {
            'type': 'string',
            'required': False,
            'description': '创建时间结束'
        },
        'user_read': {
            'type': 'boolean',
            'required': False,
            'default': False,
            'description': '用户是否已读过滤'
        },
        'module': {
            'type': 'string',
            'required': False,
            'description': '模块名称过滤'
        },
        'source_id': {
            'type': 'string',
            'required': False,
            'description': '来源ID过滤'
        },
    },
}

NOTIFICATION_READ_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'notification_id': {
            'type': 'string',
            'required': True,
            'description': '通知ID'
        },
    },
    'required': ['notification_id'],
}

# ==================== 参数定义函数 ====================

def notification_create_params() -> List[Dict[str, Any]]:
    """创建通知的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': NOTIFICATION_CREATE_REQUEST_SCHEMA,
            'description': '通知数据'
        },
    ]


def notification_list_params() -> List[Dict[str, Any]]:
    """获取通知列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': NOTIFICATION_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def notification_read_params() -> List[Dict[str, Any]]:
    """标记通知为已读的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': NOTIFICATION_READ_REQUEST_SCHEMA,
            'description': '标记参数'
        },
    ]


def notification_id_query_param() -> Dict[str, Any]:
    """通知ID查询参数定义"""
    return {
        'name': 'notification_id',
        'in': 'query',
        'type': 'string',
        'required': True,
        'description': '通知ID'
    }
