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

"""MCP工具模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    MCP_SERVER_DETAIL_SCHEMA,
    MCP_SERVER_PAGINATION_SCHEMA,
    MCP_TOOL_DETAIL_SCHEMA,
    MCP_TOOL_LIST_SCHEMA,
    APP_REF_SCHEMA,
    server_list_params,
    server_id_query_param,
    check_name_params,
    server_create_update_params,
    server_id_body_param,
    server_publish_params,
    server_enable_params,
    tool_list_params,
    tool_id_query_param,
    tool_test_params,
    reference_result_params,
)


# ==================== MCP服务器管理相关接口 ====================

# 获取MCP服务器分页列表
server_list_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '获取MCP服务器列表',
    'description': '根据传入的查询条件获取MCP服务器的分页列表，支持按发布状态、启用状态、标签、名称等条件进行筛选，需要登录',
    'parameters': server_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': MCP_SERVER_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取MCP服务器详细信息
server_detail_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '获取MCP服务器详细信息',
    'description': '根据MCP服务器ID获取服务器的详细信息，需要登录',
    'parameters': [server_id_query_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': MCP_SERVER_DETAIL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 检查MCP服务器名称是否已存在
server_check_name_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '检查MCP服务器名称',
    'description': '验证指定的服务器名称是否已经被使用，需要登录',
    'parameters': check_name_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '名称可用',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建或更新MCP服务器
server_create_update_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '创建或更新MCP服务器',
    'description': '根据传入的数据创建新的MCP服务器或更新已存在的服务器。如果数据中包含id字段则进行更新，否则创建新服务器，需要登录和写入权限',
    'parameters': server_create_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建或更新成功',
            'schema': MCP_SERVER_DETAIL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 删除MCP服务器
server_delete_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '删除MCP服务器',
    'description': '删除指定的MCP服务器，删除前会检查服务器是否被引用，需要登录和管理员权限',
    'parameters': server_id_body_param(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 发布MCP服务器
server_publish_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '发布MCP服务器',
    'description': '将MCP服务器发布为可用状态，支持不同的发布类型，需要登录和写入权限',
    'parameters': server_publish_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '发布成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 启用或禁用MCP服务器
server_enable_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '启用或禁用MCP服务器',
    'description': '设置MCP服务器的启用状态，需要登录和写入权限',
    'parameters': server_enable_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 同步MCP服务器的工具
server_sync_tools_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '同步MCP服务器工具',
    'description': '从指定的MCP服务器同步工具，使用服务器端发送事件方式返回进度，需要登录和写入权限',
    'parameters': server_id_body_param(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '同步成功（服务器端发送事件流）',
            'schema': {
                'type': 'string',
                'description': 'text/event-stream 格式的事件流'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# ==================== MCP工具管理相关接口 ====================

# 获取MCP工具列表
tool_list_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '获取MCP工具列表',
    'description': '根据MCP服务器ID获取对应的工具列表，需要登录',
    'parameters': tool_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': MCP_TOOL_LIST_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取MCP工具详细信息
tool_detail_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '获取MCP工具详细信息',
    'description': '根据工具ID获取MCP工具的详细信息，需要登录',
    'parameters': [tool_id_query_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': MCP_TOOL_DETAIL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 测试MCP工具
tool_test_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '测试MCP工具',
    'description': '使用指定的参数测试MCP工具的功能，并更新服务器的测试状态，需要登录和写入权限',
    'parameters': tool_test_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '测试成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'description': '测试结果消息'},
                    'status': {'type': 'integer', 'example': 200},
                },
            },
        },
        '400': {
            'description': '测试失败',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'description': '错误消息'},
                    'status': {'type': 'integer', 'example': 400},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取MCP工具引用结果
tool_reference_result_spec: Dict[str, Any] = {
    'tags': ['MCP工具'],
    'summary': '获取MCP工具引用结果',
    'description': '获取引用指定MCP工具的应用列表，需要登录',
    'parameters': reference_result_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': APP_REF_SCHEMA,
            },
        },
    },
    'security': AUTH_SECURITY,
}
