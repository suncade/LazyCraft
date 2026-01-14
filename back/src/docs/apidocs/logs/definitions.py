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

"""操作日志模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== Schema 定义 ====================

LOG_ITEM_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '日志ID'},
        'username': {'type': 'string', 'description': '用户名'},
        'module': {'type': 'string', 'description': '操作模块名称'},
        'action': {'type': 'string', 'description': '操作动作名称'},
        'details': {'type': 'string', 'description': '操作详细信息'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
    },
}

LOG_LIST_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'data': {
            'type': 'array',
            'items': LOG_ITEM_SCHEMA,
            'description': '日志列表'
        },
        'total': {'type': 'integer', 'description': '总记录数'},
        'page': {'type': 'integer', 'description': '当前页码'},
        'per_page': {'type': 'integer', 'description': '每页数量'},
    },
}

# ==================== 参数定义函数 ====================

def log_list_params() -> List[Dict[str, Any]]:
    """获取操作日志列表的参数定义"""
    return [
        {
            'name': 'start_date',
            'in': 'query',
            'type': 'string',
            'format': 'date',
            'required': False,
            'description': '开始日期，格式为 YYYY-MM-DD，默认为今天。所有时间参数均为北京时间（Asia/Shanghai）'
        },
        {
            'name': 'end_date',
            'in': 'query',
            'type': 'string',
            'format': 'date',
            'required': False,
            'description': '结束日期，格式为 YYYY-MM-DD，默认为今天。所有时间参数均为北京时间（Asia/Shanghai）'
        },
        {
            'name': 'details',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '操作的详细信息，支持模糊匹配'
        },
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'minimum': 1,
            'description': '分页页码，从 1 开始'
        },
        {
            'name': 'per_page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 10,
            'minimum': 1,
            'maximum': 100,
            'description': '每页记录数'
        },
        {
            'name': 'organization_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '组织的唯一标识符。如果有组织ID，查询该组织下所有用户的操作日志（当前日志中并未记录日志所属的工作空间信息，故该参数无效）'
        },
        {
            'name': 'account_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '用户账户ID。只有管理员才有权查看其他用户的操作日志，普通用户只能查看自己的日志'
        },
        {
            'name': 'user_name',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '用户名称，支持模糊匹配'
        },
        {
            'name': 'module',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '操作模块名称，支持模糊匹配'
        },
        {
            'name': 'action',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '操作动作名称，支持模糊匹配'
        },
    ]
