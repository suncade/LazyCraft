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

"""MCP工具模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']
TRANSPORT_TYPE_ENUM = ['stdio', 'http']
PUBLISH_TYPE_ENUM = ['group', 'builtin']
TEST_STATE_ENUM = ['success', 'error', 'pending']

# ==================== Schema 定义 ====================

MCP_SERVER_DETAIL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '服务器ID'},
        'name': {'type': 'string', 'description': '服务器名称'},
        'description': {'type': 'string', 'description': '服务器描述'},
        'icon': {'type': 'string', 'description': '服务器图标'},
        'transport_type': {'type': 'string', 'enum': TRANSPORT_TYPE_ENUM, 'description': '传输类型'},
        'timeout': {'type': 'integer', 'description': '超时时间'},
        'stdio_command': {'type': 'string', 'description': 'STDIO命令'},
        'stdio_arguments': {'type': 'string', 'description': 'STDIO参数'},
        'stdio_env': {'type': 'object', 'description': 'STDIO环境变量'},
        'http_url': {'type': 'string', 'description': 'HTTP URL'},
        'headers': {'type': 'object', 'description': 'HTTP头'},
        'sync_tools_at': {'type': 'string', 'format': 'date-time', 'description': '同步工具时间'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'publish_at': {'type': 'string', 'format': 'date-time', 'description': '发布时间'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'user_name': {'type': 'string', 'description': '用户名'},
        'tenant_id': {'type': 'string', 'description': '租户ID'},
        'publish': {'type': 'boolean', 'description': '是否发布'},
        'publish_type': {'type': 'string', 'enum': PUBLISH_TYPE_ENUM, 'description': '发布类型'},
        'enable': {'type': 'boolean', 'description': '是否启用'},
        'test_state': {'type': 'string', 'enum': TEST_STATE_ENUM, 'description': '测试状态'},
        'tags': {'type': 'array', 'items': {'type': 'string'}, 'description': '标签列表'},
        'ref_status': {'type': 'boolean', 'description': '引用状态'},
    },
}

MCP_SERVER_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': MCP_SERVER_DETAIL_SCHEMA,
            'description': 'MCP服务器列表'
        },
    },
}

MCP_TOOL_DETAIL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '工具ID'},
        'mcp_server_id': {'type': 'integer', 'description': 'MCP服务器ID'},
        'name': {'type': 'string', 'description': '工具名称'},
        'description': {'type': 'string', 'description': '工具描述'},
        'input_schema': {'type': 'object', 'description': '输入schema'},
        'additional_properties': {'type': 'object', 'description': '附加属性'},
        'annotations': {'type': 'object', 'description': '注解'},
        'schema': {'type': 'string', 'description': 'Schema'},
        'status': {'type': 'string', 'description': '状态'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
    },
}

MCP_TOOL_LIST_SCHEMA = {
    'type': 'object',
    'properties': {
        'data': {
            'type': 'array',
            'items': MCP_TOOL_DETAIL_SCHEMA,
            'description': 'MCP工具列表'
        },
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

MCP_SERVER_LIST_REQUEST_SCHEMA = {
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
        'publish': {
            'type': 'array',
            'items': {'type': 'boolean'},
            'required': False,
            'description': '发布状态列表'
        },
        'enable': {
            'type': 'boolean',
            'required': False,
            'description': '启用状态'
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
            'description': '搜索标签列表'
        },
        'search_name': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '搜索名称'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '用户ID列表'
        },
    },
}

MCP_SERVER_CREATE_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'integer',
            'required': False,
            'description': '服务器ID，如果提供则进行更新'
        },
        'name': {
            'type': 'string',
            'required': True,
            'description': '服务器名称'
        },
        'description': {
            'type': 'string',
            'required': False,
            'description': '服务器描述'
        },
        'icon': {
            'type': 'string',
            'required': False,
            'description': '服务器图标'
        },
        'transport_type': {
            'type': 'string',
            'required': True,
            'enum': TRANSPORT_TYPE_ENUM,
            'description': '传输类型：stdio 或 http'
        },
        'timeout': {
            'type': 'integer',
            'required': False,
            'description': '超时时间'
        },
        'stdio_command': {
            'type': 'string',
            'required': False,
            'description': 'STDIO命令'
        },
        'stdio_arguments': {
            'type': 'string',
            'required': False,
            'description': 'STDIO参数'
        },
        'stdio_env': {
            'type': 'object',
            'required': False,
            'description': 'STDIO环境变量'
        },
        'http_url': {
            'type': 'string',
            'required': False,
            'description': 'HTTP URL'
        },
        'headers': {
            'type': 'object',
            'required': False,
            'description': 'HTTP头'
        },
    },
    'required': ['name', 'transport_type'],
}

MCP_SERVER_PUBLISH_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'required': True,
            'description': '服务器ID'
        },
        'publish_type': {
            'type': 'string',
            'required': True,
            'enum': PUBLISH_TYPE_ENUM,
            'description': '发布类型：group(组) 或 builtin(内置)'
        },
    },
    'required': ['id', 'publish_type'],
}

MCP_SERVER_ENABLE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'integer',
            'required': True,
            'description': '服务器ID'
        },
        'enable': {
            'type': 'boolean',
            'required': True,
            'description': '是否启用服务器'
        },
    },
    'required': ['id', 'enable'],
}

MCP_TOOL_TEST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'mcp_server_id': {
            'type': 'integer',
            'required': True,
            'description': 'MCP服务器ID'
        },
        'tool_id': {
            'type': 'integer',
            'required': True,
            'description': '工具ID'
        },
        'param': {
            'type': 'object',
            'required': False,
            'description': '测试参数'
        },
    },
    'required': ['mcp_server_id', 'tool_id'],
}

MCP_CHECK_NAME_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'required': True,
            'description': '要检查的服务器名称'
        },
    },
    'required': ['name'],
}

MCP_TOOL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'mcp_server_id': {
            'type': 'integer',
            'required': True,
            'description': 'MCP服务器ID'
        },
    },
    'required': ['mcp_server_id'],
}

MCP_SERVER_ID_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'integer',
            'required': True,
            'description': 'MCP服务器ID'
        },
    },
    'required': ['id'],
}

# ==================== 参数定义函数 ====================

def server_list_params() -> List[Dict[str, Any]]:
    """获取MCP服务器列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': MCP_SERVER_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def server_id_query_param() -> Dict[str, Any]:
    """MCP服务器ID查询参数定义"""
    return {
        'name': 'mcp_server_id',
        'in': 'query',
        'type': 'integer',
        'required': True,
        'description': 'MCP服务器ID'
    }


def check_name_params() -> List[Dict[str, Any]]:
    """检查名称的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_CHECK_NAME_REQUEST_SCHEMA,
            'description': '检查参数'
        },
    ]


def server_create_update_params() -> List[Dict[str, Any]]:
    """创建或更新MCP服务器的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_SERVER_CREATE_UPDATE_REQUEST_SCHEMA,
            'description': '服务器数据'
        },
    ]


def server_id_body_param() -> List[Dict[str, Any]]:
    """MCP服务器ID body参数定义（使用 schema）"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_SERVER_ID_REQUEST_SCHEMA,
            'description': 'MCP服务器ID'
        },
    ]


def server_publish_params() -> List[Dict[str, Any]]:
    """发布MCP服务器的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_SERVER_PUBLISH_REQUEST_SCHEMA,
            'description': '发布参数'
        },
    ]


def server_enable_params() -> List[Dict[str, Any]]:
    """启用或禁用MCP服务器的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_SERVER_ENABLE_REQUEST_SCHEMA,
            'description': '启用参数'
        },
    ]


def tool_list_params() -> List[Dict[str, Any]]:
    """获取MCP工具列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_TOOL_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def tool_id_query_param() -> Dict[str, Any]:
    """MCP工具ID查询参数定义"""
    return {
        'name': 'tool_id',
        'in': 'query',
        'type': 'integer',
        'required': True,
        'description': '工具ID'
    }


def tool_test_params() -> List[Dict[str, Any]]:
    """测试MCP工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MCP_TOOL_TEST_REQUEST_SCHEMA,
            'description': '测试参数'
        },
    ]


def reference_result_params() -> List[Dict[str, Any]]:
    """获取MCP工具引用结果的参数定义"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'MCP工具ID'
        },
    ]
