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

"""对话模块的 Swagger 定义和参数"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses


# ==================== Schema 定义 ====================

# 对话消息 Schema
CONVERSATION_MESSAGE_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '消息ID'},
        'from_who': {'type': 'string', 'description': '发送者ID'},
        'content': {'type': 'string', 'description': '消息内容'},
        'turn_number': {'type': 'integer', 'description': '轮次编号'},
        'files': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': '文件URL列表'
        },
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'is_satisfied': {'type': 'boolean', 'description': '是否满意'},
        'user_feedback': {'type': 'string', 'description': '用户反馈'}
    }
}

# 会话信息 Schema
SESSION_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'sessionid': {'type': 'string', 'description': '会话ID'},
        'title': {'type': 'string', 'description': '会话标题'},
        'order': {'type': 'integer', 'description': '排序序号'}
    }
}

# 初始化响应 Schema
INIT_RESPONSE_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'token': {'type': 'string', 'description': '认证令牌'}
    }
}


# ==================== 参数定义函数 ====================

def app_id_path_param() -> Dict[str, Any]:
    """应用ID路径参数"""
    return {
        'name': 'app_id',
        'in': 'path',
        'type': 'string',
        'required': True,
        'description': '应用ID'
    }


def speak_history_query_params() -> list:
    """会话历史查询参数"""
    return [
        {
            'name': 'sessionid',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '会话ID'
        },
        {
            'name': 'start_id',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': '起始消息ID，用于分页'
        }
    ]


def speak_to_app_body_schema() -> Dict[str, Any]:
    """与应用对话请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'sessionid': {
                'type': 'string',
                'description': '会话ID'
            },
            'inputs': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '输入内容列表'
            },
            'files': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '文件列表（可选）'
            },
            'mode': {
                'type': 'string',
                'enum': ['publish', 'draft'],
                'default': 'publish',
                'description': '运行模式，publish为发布模式，draft为草稿模式'
            }
        },
        'required': ['sessionid', 'inputs']
    }


def speak_feedback_body_schema() -> Dict[str, Any]:
    """对话反馈请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'sessionid': {
                'type': 'string',
                'description': '会话ID'
            },
            'speak_id': {
                'type': 'integer',
                'description': '对话消息ID'
            },
            'is_satisfied': {
                'type': 'boolean',
                'description': '是否满意'
            },
            'user_feedback': {
                'type': 'string',
                'description': '用户反馈内容'
            }
        },
        'required': ['sessionid', 'speak_id', 'is_satisfied', 'user_feedback']
    }
