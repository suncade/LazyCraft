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

"""工具模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']
TOOL_TYPE_ENUM = ['官方内置', '自定义']
TOOL_MODE_ENUM = ['API', 'IDE']
PUBLISH_TYPE_ENUM = ['预发布', '正式发布']

# ==================== Schema 定义 ====================

TOOL_FIELD_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '字段ID'},
        'name': {'type': 'string', 'description': '字段名称'},
        'description': {'type': 'string', 'description': '字段描述'},
        'field_type': {'type': 'string', 'description': '字段类型'},
        'field_format': {'type': 'string', 'description': '字段格式'},
        'field_use_model': {'type': 'string', 'description': '带入方法'},
        'required': {'type': 'boolean', 'description': '是否必填'},
        'default_value': {'type': 'string', 'description': '默认值'},
        'visible': {'type': 'boolean', 'description': '是否可见'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'user_id': {'type': 'string', 'description': '用户ID'},
    },
}

TOOL_DETAIL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '工具ID'},
        'name': {'type': 'string', 'description': '工具名称'},
        'description': {'type': 'string', 'description': '工具描述'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'publish_at': {'type': 'string', 'format': 'date-time', 'description': '发布时间'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'publish': {'type': 'boolean', 'description': '是否发布'},
        'publish_type': {'type': 'string', 'description': '发布类型'},
        'enable': {'type': 'boolean', 'description': '是否启用'},
        'tool_type': {'type': 'string', 'description': '工具类型'},
        'tool_kind': {'type': 'string', 'description': '工具类别'},
        'tool_mode': {'type': 'string', 'description': '工具模式'},
        'tool_ide_code': {'type': 'string', 'description': '工具IDE代码'},
        'tool_ide_code_type': {'type': 'string', 'description': '工具IDE代码类型'},
        'tool_field_input_ids': {'type': 'array', 'items': {'type': 'integer'}, 'description': '工具字段输入ID列表'},
        'tool_field_output_ids': {'type': 'array', 'items': {'type': 'integer'}, 'description': '工具字段输出ID列表'},
        'tool_api_id': {'type': 'string', 'description': '工具API ID'},
        'icon': {'type': 'string', 'description': '工具图标'},
        'tags': {'type': 'array', 'items': {'type': 'string'}, 'description': '标签列表'},
        'share': {'type': 'boolean', 'description': '共享状态'},
        'need_share': {'type': 'boolean', 'description': '是否展示共享按钮'},
        'auth': {'type': 'integer', 'description': '是否授权 0-默认值 1-授权 2-未授权 3已过期'},
        'user_name': {'type': 'string', 'description': '用户名'},
        'test_state': {'type': 'string', 'description': '测试状态'},
        'ref_status': {'type': 'boolean', 'description': '引用状态'},
    },
}

TOOL_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': TOOL_DETAIL_SCHEMA,
            'description': '工具列表'
        },
    },
}

TOOL_API_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': 'API ID'},
        'url': {'type': 'string', 'description': 'URL'},
        'header': {'type': 'object', 'description': '请求头'},
        'auth_method': {'type': 'string', 'description': '认证方法'},
        'api_key': {'type': 'string', 'description': 'API密钥'},
        'request_type': {'type': 'string', 'description': '请求类型'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'grant_type': {'type': 'string', 'description': '授权类型'},
        'endpoint_url': {'type': 'string', 'description': '端点URL'},
        'audience': {'type': 'string', 'description': '受众'},
        'scope': {'type': 'string', 'description': '作用域'},
        'client_id': {'type': 'string', 'description': '客户端ID'},
        'client_secret': {'type': 'string', 'description': '客户端密钥'},
        'client_url': {'type': 'string', 'description': '客户端URL'},
        'authorization_url': {'type': 'string', 'description': '授权URL'},
        'authorization_content_type': {'type': 'string', 'description': '授权内容类型'},
        'location': {'type': 'string', 'description': '位置'},
        'param_name': {'type': 'string', 'description': '参数名'},
    },
}

APP_REF_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '应用ID'},
        'name': {'type': 'string', 'description': '应用名称'},
        'is_public': {'type': 'boolean', 'description': '是否公开'},
    },
}

# ==================== 请求 Schema 定义 ====================

TOOL_LIST_REQUEST_SCHEMA = {
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
            'default': 20,
            'description': '每页大小'
        },
        'tool_type': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '工具类型'
        },
        'published': {
            'type': 'array',
            'items': {'type': 'boolean'},
            'required': False,
            'description': '发布状态列表'
        },
        'enabled': {
            'type': 'array',
            'items': {'type': 'boolean'},
            'required': False,
            'description': '启用状态列表'
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
        'tool_mode': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '工具模式列表'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '用户ID列表'
        },
        'is_draft': {
            'type': 'boolean',
            'required': False,
            'default': True,
            'description': '是否为草稿'
        },
    },
}

TOOL_CREATE_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': False,
            'description': '工具ID，如果提供则进行更新'
        },
        'name': {
            'type': 'string',
            'required': True,
            'description': '工具名称（必需）'
        },
        'description': {
            'type': 'string',
            'required': False,
            'description': '工具描述'
        },
        'icon': {
            'type': 'string',
            'required': False,
            'description': '工具图标'
        },
        'tool_type': {
            'type': 'string',
            'required': False,
            'enum': TOOL_TYPE_ENUM,
            'description': '工具类型'
        },
        'tool_kind': {
            'type': 'string',
            'required': False,
            'description': '工具类别'
        },
        'tool_mode': {
            'type': 'string',
            'required': False,
            'enum': TOOL_MODE_ENUM,
            'description': '工具模式：API 或 IDE'
        },
        'tool_ide_code': {
            'type': 'string',
            'required': False,
            'description': '工具IDE代码'
        },
        'tool_ide_code_type': {
            'type': 'string',
            'required': False,
            'description': '工具IDE代码类型'
        },
    },
    'required': ['name'],
}

TOOL_API_CREATE_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': False,
            'description': 'API ID，如果提供则进行更新'
        },
        'tool_id': {
            'type': 'string',
            'required': False,
            'description': '工具ID'
        },
        'url': {
            'type': 'string',
            'required': False,
            'description': 'URL'
        },
        'header': {
            'type': 'object',
            'required': False,
            'description': '请求头'
        },
        'auth_method': {
            'type': 'string',
            'required': False,
            'description': '认证方法'
        },
        'api_key': {
            'type': 'string',
            'required': False,
            'description': 'API密钥'
        },
        'request_type': {
            'type': 'string',
            'required': False,
            'description': '请求类型'
        },
    },
}

TOOL_PUBLISH_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
        'publish_type': {
            'type': 'string',
            'required': False,
            'default': '正式发布',
            'enum': PUBLISH_TYPE_ENUM,
            'description': '发布类型：预发布 或 正式发布'
        },
    },
    'required': ['id'],
}

TOOL_ENABLE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
        'enable': {
            'type': 'boolean',
            'required': True,
            'description': '是否启用工具'
        },
    },
    'required': ['id', 'enable'],
}

TOOL_TEST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
        'input': {
            'type': 'object',
            'required': False,
            'default': {},
            'description': '输入参数'
        },
        'vars_for_code': {
            'type': 'object',
            'required': False,
            'default': {},
            'description': '代码变量'
        },
    },
    'required': ['id'],
}

TOOL_AUTH_SHARE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tool_id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
        'share_status': {
            'type': 'boolean',
            'required': True,
            'description': '分享状态'
        },
    },
    'required': ['tool_id', 'share_status'],
}

CHECK_NAME_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'required': True,
            'description': '要检查的工具名称'
        },
    },
    'required': ['name'],
}

TOOL_AUTH_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tool_id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
    },
    'required': ['tool_id'],
}

TOOL_FIELD_CREATE_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'fields': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'description': '字段ID，如果提供则进行更新'},
                    'tool_id': {'type': 'string', 'description': '工具ID'},
                    'name': {'type': 'string', 'description': '字段名称'},
                    'description': {'type': 'string', 'description': '字段描述'},
                    'field_type': {'type': 'string', 'description': '字段类型'},
                    'field_format': {'type': 'string', 'description': '字段格式'},
                    'field_use_model': {'type': 'string', 'description': '带入方法'},
                    'required': {'type': 'boolean', 'description': '是否必填'},
                    'default_value': {'type': 'string', 'description': '默认值'},
                    'visible': {'type': 'boolean', 'description': '是否可见'},
                },
            },
            'required': True,
            'description': '工具字段列表'
        },
    },
    'required': ['fields'],
}

TOOL_FIELDS_DETAIL_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'fields': {
            'type': 'array',
            'items': {'type': 'integer'},
            'required': False,
            'default': [],
            'description': '字段ID列表'
        },
    },
}

TOOL_ID_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': True,
            'description': '工具ID'
        },
    },
    'required': ['id'],
}

# ==================== 参数定义函数 ====================

def tool_list_params() -> List[Dict[str, Any]]:
    """获取工具列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': TOOL_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def tool_id_query_param() -> Dict[str, Any]:
    """工具ID查询参数定义"""
    return {
        'name': 'tool_id',
        'in': 'query',
        'type': 'string',
        'required': True,
        'description': '工具ID'
    }


def check_name_params() -> List[Dict[str, Any]]:
    """检查名称的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': CHECK_NAME_REQUEST_SCHEMA,
            'description': '检查参数'
        },
    ]


def tool_create_update_params() -> List[Dict[str, Any]]:
    """创建或更新工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_CREATE_UPDATE_REQUEST_SCHEMA,
            'description': '工具数据'
        },
    ]


def tool_id_body_param() -> List[Dict[str, Any]]:
    """工具ID body参数定义（使用 schema）"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_ID_REQUEST_SCHEMA,
            'description': '工具ID'
        },
    ]


def tool_field_create_update_params() -> List[Dict[str, Any]]:
    """创建或更新工具字段的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_FIELD_CREATE_UPDATE_REQUEST_SCHEMA,
            'description': '工具字段数据'
        },
    ]


def tool_fields_detail_params() -> List[Dict[str, Any]]:
    """获取工具字段详情的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': TOOL_FIELDS_DETAIL_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def tool_api_create_update_params() -> List[Dict[str, Any]]:
    """创建或更新工具API的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_API_CREATE_UPDATE_REQUEST_SCHEMA,
            'description': 'API数据'
        },
    ]


def api_id_query_param() -> Dict[str, Any]:
    """API ID查询参数定义"""
    return {
        'name': 'api_id',
        'in': 'query',
        'type': 'integer',
        'required': False,
        'default': 0,
        'description': 'API ID'
    }


def tool_publish_params() -> List[Dict[str, Any]]:
    """发布工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_PUBLISH_REQUEST_SCHEMA,
            'description': '发布参数'
        },
    ]


def tool_enable_params() -> List[Dict[str, Any]]:
    """启用或禁用工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_ENABLE_REQUEST_SCHEMA,
            'description': '启用参数'
        },
    ]


def tool_test_params() -> List[Dict[str, Any]]:
    """测试工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_TEST_REQUEST_SCHEMA,
            'description': '测试参数'
        },
    ]


def tool_auth_params() -> List[Dict[str, Any]]:
    """工具授权的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_AUTH_REQUEST_SCHEMA,
            'description': '授权参数'
        },
    ]


def tool_auth_share_params() -> List[Dict[str, Any]]:
    """工具授权分享的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TOOL_AUTH_SHARE_REQUEST_SCHEMA,
            'description': '分享参数'
        },
    ]


def tool_export_params() -> List[Dict[str, Any]]:
    """导出工具的参数定义"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '工具ID'
        },
        {
            'name': 'format',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '导出格式：json 或 file'
        },
    ]


def tool_reference_result_params() -> List[Dict[str, Any]]:
    """获取工具引用结果的参数定义"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '工具ID'
        },
    ]


def auth_callback_params() -> List[Dict[str, Any]]:
    """授权回调的参数定义"""
    return [
        {
            'name': 'code',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '授权码'
        },
        {
            'name': 'state',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '状态'
        },
    ]
