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

"""标签管理模块所有接口的 Swagger 定义。

包含标签管理相关的所有 API 接口的完整 Swagger spec。
"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from ..helpers import create_list_spec, create_create_spec
from .definitions import (
    TAG_OBJECT_SCHEMA,
    BRAND_OBJECT_SCHEMA,
    tag_type_param,
    brand_type_param,
    keyword_param,
    tag_create_body_schema,
    brand_create_body_schema,
    tag_binding_update_body_schema,
)

# ==================== 标签管理接口 ====================

# 获取标签列表
tag_list_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '获取标签列表',
    'description': '根据标签类型和关键词查询标签列表',
    'parameters': [
        tag_type_param(required=True),
        keyword_param()
    ],
    'responses': {
        200: {
            'description': '成功返回标签列表',
            'schema': {
                'type': 'array',
                'items': deepcopy(TAG_OBJECT_SCHEMA)
            }
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建内置标签
tag_create_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '创建内置标签',
    'description': '创建一个新的内置标签，只有超级用户可以执行此操作',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': tag_create_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功创建标签',
            'schema': deepcopy(TAG_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除标签
tag_delete_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '删除标签',
    'description': '删除指定的标签',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': '标签名称'},
                    'type': {
                        'type': 'string',
                        'enum': ['knowledgebase', 'app', 'model', 'tool', 'prompt', 'dataset', 'script', 'mcp'],
                        'description': '标签类型'
                    }
                },
                'required': ['name', 'type']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功删除标签',
            'schema': {'type': 'object'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新标签绑定关系
tag_binding_update_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '更新标签绑定关系',
    'description': '更新目标对象与标签的绑定关系',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': tag_binding_update_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功更新绑定关系',
            'schema': {'type': 'object'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 产商管理接口 ====================

# 获取产商列表
brand_list_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '获取产商列表',
    'description': '根据产商类型查询产商列表',
    'parameters': [
        brand_type_param(required=True)
    ],
    'responses': {
        200: {
            'description': '成功返回产商列表',
            'schema': {
                'type': 'array',
                'items': deepcopy(BRAND_OBJECT_SCHEMA)
            }
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建产商标签
brand_create_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '创建产商标签',
    'description': '创建一个新的产商标签，只有超级用户可以执行此操作',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': brand_create_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功创建产商标签',
            'schema': deepcopy(BRAND_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除产商
brand_delete_spec: Dict[str, Any] = {
    'tags': ['标签管理'],
    'summary': '删除产商',
    'description': '删除指定的产商标签',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': '产商名称'},
                    'type': {
                        'type': 'string',
                        'enum': ['llm', 'embedding', 'reranker'],
                        'description': '产商类型'
                    }
                },
                'required': ['name', 'type']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功删除产商',
            'schema': {'type': 'object'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}
