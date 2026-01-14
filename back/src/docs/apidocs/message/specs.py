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

"""系统消息模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    NOTIFICATION_SCHEMA,
    NOTIFICATION_PAGINATION_SCHEMA,
    notification_create_params,
    notification_list_params,
    notification_read_params,
    notification_id_query_param,
)


# ==================== 系统消息管理相关接口 ====================

# 创建通知
notification_create_spec: Dict[str, Any] = {
    'tags': ['系统消息'],
    'summary': '创建通知',
    'description': '创建新的通知，支持多用户通知场景，创建包含用户通知和审批人通知的完整通知记录，需要登录',
    'parameters': notification_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': NOTIFICATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取通知列表
notification_list_spec: Dict[str, Any] = {
    'tags': ['系统消息'],
    'summary': '获取通知列表',
    'description': '支持分页、所有字段过滤、时间区间过滤的消息列表查询，需要登录',
    'parameters': notification_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': NOTIFICATION_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 标记通知为已读
notification_read_spec: Dict[str, Any] = {
    'tags': ['系统消息'],
    'summary': '标记通知为已读',
    'description': '通过通知ID和用户ID将通知标记为已读，需要登录',
    'parameters': notification_read_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '标记成功',
            'schema': NOTIFICATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取通知详情
notification_detail_spec: Dict[str, Any] = {
    'tags': ['系统消息'],
    'summary': '获取通知详情',
    'description': '获取指定通知的详细信息，只有管理员或通知所属用户才能查看，需要登录',
    'parameters': [notification_id_query_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': NOTIFICATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}
