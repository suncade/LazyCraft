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

"""标签管理模块共用 Swagger 定义。

包含标签模块内共用的定义，如标签类型枚举、标签对象 schema 等。
"""

from copy import deepcopy
from typing import Dict, Any

from ..helpers import create_query_param

# ==================== 标签类型枚举 ====================

TAG_TYPES = ['knowledgebase', 'app', 'model', 'tool', 'prompt', 'dataset', 'script', 'mcp']
"""标签类型枚举值"""

BRAND_TYPES = ['llm', 'embedding', 'reranker']
"""产商类型枚举值"""

# ==================== Schema 定义 ====================

TAG_OBJECT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '标签ID'},
        'name': {'type': 'string', 'description': '标签名称'},
        'type': {'type': 'string', 'description': '标签类型'}
    }
}
"""标签对象 schema"""

BRAND_OBJECT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '产商ID'},
        'name': {'type': 'string', 'description': '产商名称'},
        'type': {'type': 'string', 'description': '产商类型'}
    }
}
"""产商对象 schema"""

# ==================== 参数定义函数 ====================

def tag_type_param(required: bool = True) -> Dict[str, Any]:
    """生成标签类型参数定义。

    Args:
        required: 是否必填

    Returns:
        标签类型查询参数定义
    """
    return create_query_param(
        name='type',
        param_type='string',
        required=required,
        enum=TAG_TYPES,
        description='标签类型' + ('，必填' if required else '，可选')
    )


def brand_type_param(required: bool = True) -> Dict[str, Any]:
    """生成产商类型参数定义。

    Args:
        required: 是否必填

    Returns:
        产商类型查询参数定义
    """
    return create_query_param(
        name='type',
        param_type='string',
        required=required,
        enum=BRAND_TYPES,
        description='产商类型' + ('，必填' if required else '，可选')
    )


def keyword_param() -> Dict[str, Any]:
    """生成关键词搜索参数定义。

    Returns:
        关键词查询参数定义
    """
    return create_query_param(
        name='keyword',
        param_type='string',
        required=False,
        default='',
        description='搜索关键词，可选'
    )


def tag_create_body_schema() -> Dict[str, Any]:
    """生成创建标签的请求体 schema。

    Returns:
        创建标签请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '标签名称'},
            'type': {
                'type': 'string',
                'enum': TAG_TYPES,
                'description': '标签类型'
            }
        },
        'required': ['name', 'type']
    }


def brand_create_body_schema() -> Dict[str, Any]:
    """生成创建产商的请求体 schema。

    Returns:
        创建产商请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '产商名称'},
            'type': {
                'type': 'string',
                'enum': BRAND_TYPES,
                'description': '产商类型'
            }
        },
        'required': ['name', 'type']
    }


def tag_binding_update_body_schema() -> Dict[str, Any]:
    """生成更新标签绑定关系的请求体 schema。

    Returns:
        更新标签绑定关系请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'type': {
                'type': 'string',
                'enum': TAG_TYPES,
                'description': '标签类型'
            },
            'target_id': {'type': 'string', 'description': '目标对象ID'},
            'tag_names': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '标签名称列表'
            }
        },
        'required': ['type', 'target_id', 'tag_names']
    }
