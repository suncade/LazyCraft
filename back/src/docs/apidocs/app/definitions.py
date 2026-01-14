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

"""应用管理模块共用 Swagger 定义"""

from typing import Dict, Any

from ..common_definitions import PAGINATION_PARAMS, uuid_path_param
from ..helpers import create_query_param

# ==================== 查询类型枚举 ====================

QTYPE_OPTIONS = ['mine', 'group', 'builtin', 'already']
"""查询类型枚举值：mine（我的）/group（团队）/builtin（内置）/already（全部）"""

WORKFLOW_MODE_OPTIONS = ['draft', 'publish']
"""工作流模式枚举值"""

# ==================== Schema 定义 ====================

APP_OBJECT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '应用ID'},
        'name': {'type': 'string', 'description': '应用名称'},
        'description': {'type': 'string', 'description': '应用描述'},
        'icon': {'type': 'string', 'description': '应用图标'},
        'icon_background': {'type': 'string', 'description': '图标背景色'},
        'workflow_id': {'type': 'string', 'description': '工作流ID'},
        'status': {'type': 'string', 'description': '状态'},
        'categories': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': '应用分类'
        },
        'enable_site': {'type': 'boolean', 'description': '是否启用站点'},
        'enable_api': {'type': 'boolean', 'description': '是否启用API'},
        'enable_backflow': {'type': 'boolean', 'description': '是否启用回流'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'workflow_updated_at': {'type': 'string', 'format': 'date-time', 'description': '工作流更新时间'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'enable_api_call': {'type': 'string', 'description': 'API调用开关'},
        'ref_status': {'type': 'boolean', 'description': '引用状态'},
        'mode': {'type': 'string', 'description': '模式'},
        'model_config': {'type': 'object', 'description': '模型配置'},
        'tracing': {'type': 'object', 'description': '追踪配置'},
        'tags': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': '标签列表'
        },
        'publish_status': {'type': 'string', 'description': '发布状态'},
        'engine_status': {'type': 'string', 'description': '引擎状态'}
    }
}
"""应用对象 schema"""

APP_PAGINATION_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '页码'},
        'limit': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总数量'},
        'has_more': {'type': 'boolean', 'description': '是否有更多'},
        'data': {
            'type': 'array',
            'items': APP_OBJECT_SCHEMA,
            'description': '应用列表'
        }
    }
}
"""应用分页响应 schema"""

WORKFLOW_OBJECT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '工作流ID'},
        'graph': {'type': 'object', 'description': '工作流图'},
        'hash': {'type': 'string', 'description': '唯一哈希'},
        'refer_model_count': {'type': 'integer', 'description': '引用模型数量'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_by': {'type': 'string', 'description': '更新者ID'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'}
    }
}
"""工作流对象 schema"""

# ==================== 参数定义函数 ====================

def app_id_path_param() -> Dict[str, Any]:
    """生成应用ID路径参数定义。

    Returns:
        应用ID路径参数定义
    """
    return uuid_path_param('app_id', '应用ID')


def mode_path_param() -> Dict[str, Any]:
    """生成工作流模式路径参数定义。

    Returns:
        工作流模式路径参数定义
    """
    return {
        'name': 'mode',
        'in': 'path',
        'type': 'string',
        'required': True,
        'enum': WORKFLOW_MODE_OPTIONS,
        'description': '工作流模式：draft（草稿）或 publish（发布）'
    }


def app_list_query_params() -> list:
    """生成应用列表查询参数。

    Returns:
        查询参数列表
    """
    return [
        *PAGINATION_PARAMS,
        create_query_param('search_name', 'string', False, '搜索应用名称'),
        create_query_param('search_tags', 'string', False, '搜索标签名称'),
        create_query_param('qtype', 'string', False, '查询类型：mine/group/builtin/already', enum=QTYPE_OPTIONS, default='mine'),
        create_query_param('is_published', 'boolean', False, '是否已发布')
    ]


def app_list_page_body_schema() -> Dict[str, Any]:
    """生成应用列表分页请求体 schema。

    Returns:
        应用列表分页请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'page': {'type': 'integer', 'minimum': 1, 'maximum': 99999, 'default': 1, 'description': '页码'},
            'limit': {'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20, 'description': '每页数量'},
            'search_name': {'type': 'string', 'description': '搜索应用名称'},
            'search_tags': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '搜索标签列表'
            },
            'qtype': {
                'type': 'string',
                'enum': QTYPE_OPTIONS,
                'default': 'mine',
                'description': '查询类型：mine/group/builtin/already'
            },
            'is_published': {'type': 'boolean', 'description': '是否已发布'},
            'enable_api': {'type': 'boolean', 'description': '是否启用API'}
        }
    }


def app_create_body_schema() -> Dict[str, Any]:
    """生成创建应用的请求体 schema。

    Returns:
        创建应用请求体 schema
    """
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '应用名称'},
            'description': {'type': 'string', 'description': '应用描述'},
            'icon': {'type': 'string', 'description': '应用图标'},
            'icon_background': {'type': 'string', 'description': '图标背景色'},
            'categories': {
                'type': 'array',
                'items': {'type': 'string'},
                'description': '应用分类'
            }
        },
        'required': ['name']
    }
