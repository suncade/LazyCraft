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

"""工具模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    TOOL_DETAIL_SCHEMA,
    TOOL_PAGINATION_SCHEMA,
    TOOL_API_SCHEMA,
    APP_REF_SCHEMA,
    tool_list_params,
    tool_id_query_param,
    check_name_params,
    tool_create_update_params,
    tool_id_body_param,
    tool_field_create_update_params,
    tool_fields_detail_params,
    tool_api_create_update_params,
    api_id_query_param,
    tool_publish_params,
    tool_enable_params,
    tool_test_params,
    tool_auth_params,
    tool_auth_share_params,
    tool_export_params,
    tool_reference_result_params,
    auth_callback_params,
)


# ==================== 工具管理相关接口 ====================

# 获取工具分页列表
tool_list_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '获取工具列表',
    'description': '根据传入的查询条件获取工具的分页列表，支持按工具类型、发布状态、启用状态、标签、名称等条件进行筛选，需要登录',
    'parameters': tool_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': TOOL_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取工具详情
tool_detail_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '获取工具详情',
    'description': '根据工具ID获取工具的详细信息，需要登录',
    'parameters': [tool_id_query_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': TOOL_DETAIL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 检查工具名称
tool_check_name_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '检查工具名称',
    'description': '验证指定的工具名称是否已经被使用，需要登录',
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

# 创建或更新工具
tool_create_update_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '创建或更新工具',
    'description': '根据传入的数据创建新的工具或更新已存在的工具。如果数据中包含id字段则进行更新，否则创建新工具，需要登录和写入权限',
    'parameters': tool_create_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建或更新成功',
            'schema': TOOL_DETAIL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 删除工具
tool_delete_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '删除工具',
    'description': '删除指定的工具，需要登录和管理员权限',
    'parameters': tool_id_body_param(),
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

# 创建或更新工具字段
tool_field_create_update_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '创建或更新工具字段',
    'description': '创建或更新工具的字段（API+IDE两种模式都有），每次都是新增数据，需要登录和写入权限',
    'parameters': tool_field_create_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'save_success_field': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '成功保存的字段列表'
                    },
                    'update_success_field': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '成功更新的字段列表'
                    },
                    'save_error': {'type': 'string', 'description': '保存错误'},
                    'update_error': {'type': 'string', 'description': '更新错误'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取工具字段详情
tool_fields_detail_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '获取工具字段详情',
    'description': '获取工具字段的数据详情（API+IDE两种模式都有），需要登录和写入权限',
    'parameters': tool_fields_detail_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '工具字段列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建或更新工具API
tool_api_create_update_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '创建或更新工具API',
    'description': '创建或更新工具的HTTP API配置，需要登录和写入权限',
    'parameters': tool_api_create_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': TOOL_API_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取工具API详情
tool_api_detail_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '获取工具API详情',
    'description': '获取工具的HTTP API配置详情，需要登录',
    'parameters': [api_id_query_param()],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': TOOL_API_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 发布工具
tool_publish_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '发布工具',
    'description': '将工具发布为可用状态，支持不同的发布类型，需要登录和写入权限',
    'parameters': tool_publish_params(),
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

# 取消发布工具
tool_cancel_publish_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '取消发布工具',
    'description': '取消工具的发布状态，需要登录和写入权限',
    'parameters': tool_id_body_param(),
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

# 启用或禁用工具
tool_enable_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '启用或禁用工具',
    'description': '设置工具的启用状态，需要登录和写入权限',
    'parameters': tool_enable_params(),
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

# 复制工具
tool_copy_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '复制工具',
    'description': '复制一份新的工具，需要登录和读取权限',
    'parameters': tool_id_body_param(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '复制成功',
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

# 测试工具
tool_test_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '测试工具',
    'description': '使用指定的参数测试工具的功能，需要登录和写入权限，需要启用工具运行功能',
    'parameters': tool_test_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '测试成功',
            'schema': {
                'type': 'object',
                'description': '测试结果'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 测试（日志）
tool_test_log_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '测试工具日志',
    'description': '测试工具日志功能，需要登录和写入权限',
    'parameters': tool_id_body_param(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'object',
                'description': '日志信息'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 生成授权URL
tool_auth_return_url_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '生成授权URL',
    'description': '生成对应的授权URL，需要登录和写入权限',
    'parameters': tool_auth_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '生成成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'url': {'type': 'string', 'description': '授权URL'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 授权回调
tool_auth_callback_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '授权回调',
    'description': '处理OAuth授权回调，不需要登录',
    'parameters': auth_callback_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '授权成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': [],
}

# 授权分享
tool_auth_share_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '授权分享',
    'description': '设置工具的授权分享状态，需要登录和写入权限',
    'parameters': tool_auth_share_params(),
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

# 删除授权
tool_auth_delete_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '删除授权',
    'description': '删除工具的用户授权，需要登录和写入权限',
    'parameters': tool_auth_params(),
    'responses': {
        **standard_error_responses(),
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

# 导出工具
tool_export_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '导出工具',
    'description': '导出工具为JSON格式，支持直接返回JSON或下载文件，需要登录和读取权限',
    'parameters': tool_export_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '导出成功',
            'schema': {
                'type': 'object',
                'description': '工具JSON数据或文件下载'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取工具引用结果
tool_reference_result_spec: Dict[str, Any] = {
    'tags': ['工具'],
    'summary': '获取工具引用结果',
    'description': '获取引用指定工具的应用列表，不需要登录',
    'parameters': tool_reference_result_params(),
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
    'security': [],
}
