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

"""对话模块的 Swagger 规范定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import standard_error_responses
from .definitions import (
    AUTH_SECURITY,
    CONVERSATION_MESSAGE_SCHEMA,
    SESSION_SCHEMA,
    INIT_RESPONSE_SCHEMA,
    app_id_path_param,
    speak_history_query_params,
    speak_to_app_body_schema,
    speak_feedback_body_schema,
)


# ==================== 对话接口 ====================

# 初始化对话
speak_init_spec: Dict[str, Any] = {
    'tags': ['conversation'],
    'summary': '初始化对话',
    'description': '初始化用户身份并获取认证令牌，用于后续对话接口的认证',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'TempToken',
            'in': 'header',
            'type': 'string',
            'required': False,
            'description': '临时令牌（可选）'
        },
        {
            'name': '_token',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '认证令牌（可选）'
        }
    ],
    'responses': {
        200: {
            'description': '初始化成功，返回认证令牌',
            'schema': deepcopy(INIT_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False, include_404=False)
    },
    'security': []
}

# 获取会话列表
speak_sessions_spec: Dict[str, Any] = {
    'tags': ['conversation'],
    'summary': '获取会话列表',
    'description': '获取当前用户的所有对话会话列表',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': '认证令牌，格式: Bearer <token> 或直接 <token>'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回会话列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': deepcopy(SESSION_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    },
    'security': []
}

# 获取会话历史
speak_history_spec: Dict[str, Any] = {
    'tags': ['conversation'],
    'summary': '获取会话历史',
    'description': '获取指定会话的历史对话记录',
    'parameters': [
        app_id_path_param(),
        *speak_history_query_params(),
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': '认证令牌，格式: Bearer <token> 或直接 <token>'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回历史记录',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': deepcopy(CONVERSATION_MESSAGE_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    },
    'security': []
}

# 与应用对话（SSE流式响应）
speak_to_app_spec: Dict[str, Any] = {
    'tags': ['conversation'],
    'summary': '与应用对话',
    'description': '向应用发送消息并获取流式响应（SSE格式）',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(speak_to_app_body_schema())
        },
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': '认证令牌，格式: Bearer <token> 或直接 <token>'
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应，返回对话结果',
            'schema': {
                'type': 'string',
                'format': 'text/event-stream'
            }
        },
        **standard_error_responses(include_403=False)
    },
    'security': []
}

# 对话反馈
speak_feedback_spec: Dict[str, Any] = {
    'tags': ['conversation'],
    'summary': '对话反馈',
    'description': '对对话结果进行用户反馈',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(speak_feedback_body_schema())
        },
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'description': '认证令牌，格式: Bearer <token> 或直接 <token>'
        }
    ],
    'responses': {
        200: {
            'description': '反馈成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    },
    'security': []
}
