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

"""工作空间模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    ACCOUNT_PAGINATION_SCHEMA,
    TENANT_PAGINATION_SCHEMA,
    TENANT_SCHEMA,
    COOPERATION_SCHEMA,
    QUOTA_PAGINATION_SCHEMA,
    QUOTA_REQUEST_SCHEMA,
    DELETE_TENANT_REQUEST_SCHEMA,
    EXIT_TENANT_REQUEST_SCHEMA,
    DELETE_ACCOUNT_REQUEST_SCHEMA,
    COOP_CLOSE_REQUEST_SCHEMA,
    user_list_params,
    select_user_list_params,
    tenant_list_params,
    account_id_query_param,
    tenant_id_query_param,
    switch_tenant_params,
    add_tenant_params,
    update_roles_params,
    move_assets_params,
    delete_role_params,
    account_id_body_param,
    cooperation_params,
    cooperation_body_params,
    personal_space_get_params,
    personal_space_post_params,
    quota_request_list_params,
    quota_request_params,
    quota_request_detail_params,
    quota_request_action_params,
    ai_tool_set_params,
    ai_tool_list_params,
    tenant_enable_ai_params,
)


# ==================== 用户管理相关接口 ====================

# 获取所有用户列表
all_user_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取所有用户列表',
    'description': '查看所有的用户，支持分页和搜索，需要登录',
    'parameters': user_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': ACCOUNT_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取选择用户列表
select_user_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取选择用户列表',
    'description': '查看所有的用户（仅在选择用户列表中使用），支持分页和搜索，需要登录',
    'parameters': select_user_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': ACCOUNT_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取租户用户列表
tenant_user_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取租户用户列表',
    'description': '查询当前租户下全部用户列表，需要登录',
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': {'type': 'object'},
                'description': '用户列表'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# ==================== 租户管理相关接口 ====================

# 获取所有租户列表
all_tenant_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取所有租户列表',
    'description': '查看所有的租户，支持分页和搜索，需要登录',
    'parameters': tenant_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': TENANT_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取账户租户列表
account_tenant_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取账户租户列表',
    'description': '查看用户加入的租户，需要登录',
    'parameters': [account_id_query_param()],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'tenants': {
                        'type': 'array',
                        'items': TENANT_SCHEMA,
                        'description': '租户列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取当前租户列表
current_tenant_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取当前租户列表',
    'description': '查看当前用户加入的租户，需要登录',
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'tenants': {
                        'type': 'array',
                        'items': TENANT_SCHEMA,
                        'description': '租户列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取当前租户ID
current_tenant_id_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取当前租户ID',
    'description': '查看当前租户ID，需要登录',
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'tenant_id': {'type': 'string', 'description': '当前租户ID'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 切换租户
switch_tenant_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '切换租户',
    'description': '切换当前用户的租户，需要登录',
    'parameters': switch_tenant_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '切换成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 添加租户
add_tenant_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '添加租户',
    'description': '创建新的租户，需要登录和写入权限',
    'parameters': add_tenant_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': TENANT_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取租户详情
detail_tenant_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取租户详情',
    'description': '查看租户详细信息和用户列表，需要登录和写入权限',
    'parameters': [tenant_id_query_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    **TENANT_SCHEMA['properties'],
                    'accounts': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '账户列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新角色
update_roles_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '更新角色',
    'description': '修改租户内的用户身份和配额，需要登录和管理员权限',
    'parameters': update_roles_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 迁移资产
move_assets_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '迁移资产',
    'description': '在租户内迁移用户资产，需要登录和超级管理员权限',
    'parameters': move_assets_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '迁移成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除租户
delete_tenant_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '删除租户',
    'description': '删除指定的租户，需要登录和超级管理员或创建者权限',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_TENANT_REQUEST_SCHEMA,
            'description': '删除参数'
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 退出租户
exit_tenant_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '退出租户',
    'description': '退出指定的租户，超管和创建者不能退出，需要登录',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': EXIT_TENANT_REQUEST_SCHEMA,
            'description': '退出参数'
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '退出成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除角色
delete_role_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '删除角色',
    'description': '从租户中删除用户，需要登录和管理员权限',
    'parameters': delete_role_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除账户
delete_account_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '删除账户',
    'description': '删除指定的账户，需要登录和超级管理员权限',
    'parameters': account_id_body_param(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# ==================== 协作相关接口 ====================

# 获取协作状态
coop_status_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取协作状态',
    'description': '查询协作的设置详情，需要登录',
    'parameters': cooperation_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': COOPERATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 打开协作
coop_open_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '打开协作',
    'description': '打开指定目标的协作功能，需要登录和写入权限',
    'parameters': cooperation_body_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': COOPERATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 关闭协作
coop_close_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '关闭协作',
    'description': '关闭指定目标的协作功能，需要登录和写入权限',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': COOP_CLOSE_REQUEST_SCHEMA,
            'description': '关闭参数'
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': COOPERATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取协作加入列表
coop_join_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取协作加入列表',
    'description': '查看自己被加入协作的列表，需要登录',
    'parameters': [
        {
            'name': 'target_type',
            'in': 'query',
            'type': 'string',
            'required': True,
            'enum': ['app', 'dataset', 'knowledge_base', 'doc'],
            'description': '目标类型'
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'ID列表'
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# ==================== 资源管理相关接口 ====================

# 存储空间检查
storage_check_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '存储空间检查',
    'description': '查看当前工作组的存储空间使用情况，需要登录',
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'boolean', 'description': '是否有可用空间'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取个人空间资源
personal_space_get_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取个人空间资源',
    'description': '获取个人空间资源配置信息，需要登录',
    'parameters': personal_space_get_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'description': '资源配置信息'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 修改个人空间资源
personal_space_post_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '修改个人空间资源',
    'description': '修改个人空间GPU配额，需要登录和超级管理员权限',
    'parameters': personal_space_post_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '修改成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# ==================== 配额申请相关接口 ====================

# 获取配额申请列表
quota_request_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取配额申请列表',
    'description': '获取工作空间配额申请列表，需要登录和超级管理员权限',
    'parameters': quota_request_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': QUOTA_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 提交配额申请
quota_request_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '提交配额申请',
    'description': '提交配额申请（存储或GPU），需要登录和管理员权限',
    'parameters': quota_request_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '提交成功',
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

# 获取配额申请详情
quota_request_detail_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取配额申请详情',
    'description': '获取配额申请详情，需要登录和超级管理员权限',
    'parameters': quota_request_detail_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': QUOTA_REQUEST_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 处理配额申请
quota_request_action_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '处理配额申请',
    'description': '管理员处理配额申请（批准或拒绝），需要登录和超级管理员权限',
    'parameters': quota_request_action_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '处理成功',
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

# ==================== AI工具相关接口 ====================

# 设置AI工具
ai_tool_set_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '设置AI工具',
    'description': '设置租户的AI能力配置，需要登录和超级管理员权限',
    'parameters': ai_tool_set_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '设置成功',
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

# 获取AI工具列表
ai_tool_list_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '获取AI工具列表',
    'description': '获取租户的AI能力配置，需要登录',
    'parameters': ai_tool_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                    'data': {'type': 'string', 'description': 'JSON格式的配置数据'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 设置租户启用AI
tenant_enable_ai_spec: Dict[str, Any] = {
    'tags': ['工作空间'],
    'summary': '设置租户启用AI',
    'description': '设置是否开启租户的AI能力，需要登录和超级管理员权限',
    'parameters': tenant_enable_ai_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '设置成功',
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
