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

"""Prompt模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']

# ==================== Schema 定义 ====================

PROMPT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '提示信息ID'},
        'name': {'type': 'string', 'description': '提示信息名称'},
        'describe': {'type': 'string', 'description': '提示信息描述'},
        'content': {'type': 'string', 'description': '提示信息内容'},
        'category': {'type': 'string', 'description': '提示信息分类'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
    },
}

PROMPT_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'total': {'type': 'integer', 'description': '总记录数'},
        'pages': {'type': 'integer', 'description': '总页数'},
        'current_page': {'type': 'integer', 'description': '当前页码'},
        'next_page': {'type': 'integer', 'description': '下一页页码'},
        'prev_page': {'type': 'integer', 'description': '上一页页码'},
        'prompts': {
            'type': 'array',
            'items': PROMPT_SCHEMA,
            'description': '提示信息列表'
        },
    },
}

# ==================== 请求 Schema 定义 ====================

PROMPT_CREATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'required': True,
            'description': '提示信息的名称（必需）'
        },
        'describe': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '提示信息的描述'
        },
        'content': {
            'type': 'string',
            'required': True,
            'description': '提示信息的内容（必需）'
        },
        'category': {
            'type': 'string',
            'required': False,
            'default': None,
            'description': '提示信息的分类'
        },
    },
    'required': ['name', 'content'],
}

PROMPT_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'required': False,
            'description': '提示信息的名称'
        },
        'describe': {
            'type': 'string',
            'required': False,
            'description': '提示信息的描述'
        },
        'content': {
            'type': 'string',
            'required': False,
            'description': '提示信息的内容'
        },
        'template_id': {
            'type': 'integer',
            'required': False,
            'description': '模板ID'
        },
        'category': {
            'type': 'string',
            'required': False,
            'description': '提示信息的分类'
        },
    },
}

PROMPT_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': '页码，从 1 开始'
        },
        'per_page': {
            'type': 'integer',
            'required': False,
            'default': 10,
            'description': '每页数量'
        },
        'qtype': {
            'type': 'string',
            'required': False,
            'default': 'already',
            'enum': QTYPE_ENUM,
            'description': '查询类型：mine(我的)、group(组)、builtin(内置)、already(已有)'
        },
        'search_tags': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '标签搜索条件'
        },
        'search_name': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '名称搜索条件'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '用户ID筛选'
        },
    },
}

# ==================== 参数定义函数 ====================

def prompt_create_params() -> List[Dict[str, Any]]:
    """创建提示信息的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': PROMPT_CREATE_REQUEST_SCHEMA,
            'description': '提示信息数据'
        },
    ]


def prompt_id_path_param() -> Dict[str, Any]:
    """提示信息ID路径参数定义"""
    return {
        'name': 'id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '提示信息ID'
    }


def prompt_update_params() -> List[Dict[str, Any]]:
    """更新提示信息的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': PROMPT_UPDATE_REQUEST_SCHEMA,
            'description': '提示信息数据'
        },
    ]


def prompt_list_params() -> List[Dict[str, Any]]:
    """获取提示信息列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': PROMPT_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]
