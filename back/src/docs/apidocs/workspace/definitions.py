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

"""工作空间模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QUOTA_REQUEST_TYPE_ENUM = ['storage', 'gpu']
QUOTA_STATUS_ENUM = ['pending', 'approved', 'rejected']
TARGET_TYPE_ENUM = ['app', 'dataset', 'knowledge_base', 'doc']

# ==================== Schema 定义 ====================

ACCOUNT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '账户ID'},
        'name': {'type': 'string', 'description': '账户名称'},
        'avatar': {'type': 'string', 'description': '头像'},
        'email': {'type': 'string', 'description': '邮箱'},
        'phone': {'type': 'string', 'description': '电话'},
        'last_login_at': {'type': 'integer', 'description': '最后登录时间'},
        'last_active_at': {'type': 'integer', 'description': '最后活跃时间'},
        'created_at': {'type': 'integer', 'description': '创建时间'},
        'status': {'type': 'string', 'description': '状态'},
        'role': {'type': 'string', 'description': '角色'},
    },
}

ACCOUNT_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'limit': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': ACCOUNT_SCHEMA,
            'description': '账户列表'
        },
    },
}

TENANT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '租户ID'},
        'name': {'type': 'string', 'description': '租户名称'},
        'status': {'type': 'string', 'description': '状态'},
        'created_at': {'type': 'integer', 'description': '创建时间'},
        'current': {'type': 'boolean', 'description': '是否为当前租户'},
        'role': {'type': 'string', 'description': '角色'},
        'storage_quota': {'type': 'integer', 'description': '存储配额'},
        'storage_used': {'type': 'number', 'description': '已使用存储'},
        'gpu_quota': {'type': 'integer', 'description': 'GPU配额'},
        'gpu_used': {'type': 'integer', 'description': '已使用GPU'},
        'enable_ai': {'type': 'boolean', 'description': '是否启用AI'},
        'has_assets': {'type': 'boolean', 'description': '是否有资产'},
    },
}

TENANT_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'limit': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': TENANT_SCHEMA,
            'description': '租户列表'
        },
        'user_id': {'type': 'string', 'description': '用户ID'},
    },
}

COOPERATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'target_type': {'type': 'string', 'description': '目标类型'},
        'target_id': {'type': 'string', 'description': '目标ID'},
        'enable': {'type': 'boolean', 'description': '是否启用'},
        'tenant_id': {'type': 'string', 'description': '租户ID'},
        'created_by': {'type': 'string', 'description': '创建者'},
        'accounts': {'type': 'array', 'items': {'type': 'string'}, 'description': '账户列表'},
    },
}

QUOTA_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '申请ID'},
        'request_type': {'type': 'string', 'description': '申请类型'},
        'requested_amount': {'type': 'integer', 'description': '申请数量'},
        'approved_amount': {'type': 'integer', 'description': '批准数量'},
        'reason': {'type': 'string', 'description': '申请原因'},
        'tenant_name': {'type': 'string', 'description': '租户名称'},
        'tenant_id': {'type': 'string', 'description': '租户ID'},
        'account_id': {'type': 'string', 'description': '账户ID'},
        'account_name': {'type': 'string', 'description': '账户名称'},
        'reject_reason': {'type': 'string', 'description': '拒绝原因'},
        'status': {'type': 'string', 'description': '状态'},
        'processed_at': {'type': 'string', 'format': 'date-time', 'description': '处理时间'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
    },
}

QUOTA_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'pages': {'type': 'integer', 'description': '总页数'},
        'has_prev': {'type': 'boolean', 'description': '是否有上一页'},
        'has_next': {'type': 'boolean', 'description': '是否有下一页'},
        'data': {
            'type': 'array',
            'items': QUOTA_REQUEST_SCHEMA,
            'description': '配额申请列表'
        },
    },
}

# ==================== 请求 Schema 定义 ====================

UPDATE_ROLES_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
        'tenant_name': {
            'type': 'string',
            'required': False,
            'description': '租户名称'
        },
        'data_list': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'account_id': {'type': 'string'},
                    'name': {'type': 'string'},
                    'role': {'type': 'string'},
                },
            },
            'required': False,
            'description': '用户角色列表'
        },
        'storage_quota': {
            'type': 'integer',
            'required': True,
            'default': 0,
            'description': '存储配额（GB）'
        },
        'gpu_quota': {
            'type': 'integer',
            'required': False,
            'description': 'GPU配额'
        },
    },
    'required': ['tenant_id', 'storage_quota'],
}

MOVE_ASSETS_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
        'source_account_id': {
            'type': 'string',
            'required': True,
            'description': '源账户ID'
        },
        'target_account_id': {
            'type': 'string',
            'required': True,
            'description': '目标账户ID'
        },
    },
    'required': ['tenant_id', 'source_account_id', 'target_account_id'],
}

COOPERATION_BODY_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'target_type': {
            'type': 'string',
            'required': True,
            'enum': TARGET_TYPE_ENUM,
            'description': '目标类型'
        },
        'target_id': {
            'type': 'string',
            'required': True,
            'description': '目标ID'
        },
        'accounts': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': True,
            'description': '账户ID列表'
        },
    },
    'required': ['target_type', 'target_id', 'accounts'],
}

PERSONAL_SPACE_POST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'gpu_quota': {
            'type': 'integer',
            'required': True,
            'description': 'GPU配额'
        },
        'storage_quota': {
            'type': 'integer',
            'required': True,
            'description': '存储配额（GB）'
        },
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['gpu_quota', 'storage_quota', 'tenant_id'],
}

QUOTA_REQUEST_LIST_REQUEST_SCHEMA = {
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
            'description': '每页数量'
        },
        'request_type': {
            'type': 'string',
            'required': False,
            'default': '',
            'enum': QUOTA_REQUEST_TYPE_ENUM,
            'description': '申请类型'
        },
        'tenant_name': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '租户名称'
        },
        'account_name': {
            'type': 'string',
            'required': False,
            'description': '账户名称'
        },
        'status': {
            'type': 'string',
            'required': False,
            'enum': QUOTA_STATUS_ENUM,
            'description': '状态'
        },
    },
}

QUOTA_REQUEST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'type': {
            'type': 'string',
            'required': True,
            'enum': QUOTA_REQUEST_TYPE_ENUM,
            'description': '申请类型：storage 或 gpu'
        },
        'amount': {
            'type': 'integer',
            'required': True,
            'description': '申请数量'
        },
        'reason': {
            'type': 'string',
            'required': True,
            'description': '申请原因'
        },
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['type', 'amount', 'reason', 'tenant_id'],
}

QUOTA_REQUEST_ACTION_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'request_id': {
            'type': 'string',
            'required': True,
            'description': '申请ID'
        },
        'action': {
            'type': 'string',
            'required': True,
            'enum': ['approve', 'reject'],
            'description': '操作类型：approve 或 reject'
        },
        'amount': {
            'type': 'integer',
            'required': False,
            'description': '批准数量（仅当 action 为 approve 时必需）'
        },
        'reason': {
            'type': 'string',
            'required': False,
            'description': '拒绝原因（仅当 action 为 reject 时必需）'
        },
    },
    'required': ['request_id', 'action'],
}

AI_TOOL_SET_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'data': {
            'type': 'array',
            'items': {'type': 'object'},
            'required': True,
            'description': 'AI工具配置数据列表'
        },
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['data', 'tenant_id'],
}

TENANT_ENABLE_AI_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'enable': {
            'type': 'boolean',
            'required': True,
            'description': '是否启用AI'
        },
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['enable', 'tenant_id'],
}

SWITCH_TENANT_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['tenant_id'],
}

ADD_TENANT_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'required': True,
            'description': '租户名称'
        },
    },
    'required': ['name'],
}

DELETE_ROLE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
        'account_id': {
            'type': 'string',
            'required': True,
            'description': '账户ID'
        },
    },
    'required': ['tenant_id', 'account_id'],
}

DELETE_TENANT_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['tenant_id'],
}

EXIT_TENANT_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'tenant_id': {
            'type': 'string',
            'required': True,
            'description': '租户ID'
        },
    },
    'required': ['tenant_id'],
}

DELETE_ACCOUNT_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'account_id': {
            'type': 'string',
            'required': True,
            'description': '账户ID'
        },
    },
    'required': ['account_id'],
}

COOP_CLOSE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'target_type': {
            'type': 'string',
            'required': True,
            'enum': TARGET_TYPE_ENUM,
            'description': '目标类型'
        },
        'target_id': {
            'type': 'string',
            'required': True,
            'description': '目标ID'
        },
    },
    'required': ['target_type', 'target_id'],
}

# ==================== 参数定义函数 ====================

def user_list_params() -> List[Dict[str, Any]]:
    """用户列表查询参数定义"""
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': '页码，从 1 开始'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 20,
            'description': '每页数量'
        },
        {
            'name': 'search_name',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '名称搜索'
        },
        {
            'name': 'search_phone',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '电话搜索'
        },
        {
            'name': 'search_email',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '邮箱搜索'
        },
    ]


def select_user_list_params() -> List[Dict[str, Any]]:
    """选择用户列表查询参数定义"""
    params = user_list_params()
    params.append({
        'name': 'tenant_id',
        'in': 'query',
        'type': 'string',
        'required': False,
        'description': '租户ID'
    })
    return params


def tenant_list_params() -> List[Dict[str, Any]]:
    """租户列表查询参数定义"""
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': '页码，从 1 开始'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 20,
            'description': '每页数量'
        },
        {
            'name': 'search_name',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '名称搜索'
        },
        {
            'name': 'search_user',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '用户搜索'
        },
    ]


def account_id_query_param() -> Dict[str, Any]:
    """账户ID查询参数定义"""
    return {
        'name': 'account_id',
        'in': 'query',
        'type': 'string',
        'required': True,
        'description': '账户ID'
    }


def tenant_id_query_param() -> Dict[str, Any]:
    """租户ID查询参数定义"""
    return {
        'name': 'tenant_id',
        'in': 'query',
        'type': 'string',
        'required': True,
        'description': '租户ID'
    }


def tenant_id_body_param() -> Dict[str, Any]:
    """租户ID body参数定义"""
    return {
        'name': 'tenant_id',
        'in': 'body',
        'type': 'string',
        'required': True,
        'description': '租户ID'
    }


def switch_tenant_params() -> List[Dict[str, Any]]:
    """切换租户的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': SWITCH_TENANT_REQUEST_SCHEMA,
            'description': '切换参数'
        },
    ]


def add_tenant_params() -> List[Dict[str, Any]]:
    """添加租户的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': ADD_TENANT_REQUEST_SCHEMA,
            'description': '租户数据'
        },
    ]


def update_roles_params() -> List[Dict[str, Any]]:
    """更新角色的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': UPDATE_ROLES_REQUEST_SCHEMA,
            'description': '角色数据'
        },
    ]


def move_assets_params() -> List[Dict[str, Any]]:
    """迁移资产的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MOVE_ASSETS_REQUEST_SCHEMA,
            'description': '迁移参数'
        },
    ]


def delete_role_params() -> List[Dict[str, Any]]:
    """删除角色的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_ROLE_REQUEST_SCHEMA,
            'description': '删除参数'
        },
    ]


def account_id_body_param() -> List[Dict[str, Any]]:
    """账户ID body参数定义（使用 schema）"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_ACCOUNT_REQUEST_SCHEMA,
            'description': '账户ID'
        },
    ]


def cooperation_params() -> List[Dict[str, Any]]:
    """协作的参数定义"""
    return [
        {
            'name': 'target_type',
            'in': 'query',
            'type': 'string',
            'required': True,
            'enum': TARGET_TYPE_ENUM,
            'description': '目标类型'
        },
        {
            'name': 'target_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '目标ID'
        },
    ]


def cooperation_body_params() -> List[Dict[str, Any]]:
    """协作的body参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': COOPERATION_BODY_REQUEST_SCHEMA,
            'description': '协作参数'
        },
    ]


def personal_space_get_params() -> List[Dict[str, Any]]:
    """获取个人空间资源的参数定义"""
    return [account_id_query_param()]


def personal_space_post_params() -> List[Dict[str, Any]]:
    """修改个人空间资源的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': PERSONAL_SPACE_POST_REQUEST_SCHEMA,
            'description': '个人空间数据'
        },
    ]


def quota_request_list_params() -> List[Dict[str, Any]]:
    """配额申请列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': QUOTA_REQUEST_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def quota_request_params() -> List[Dict[str, Any]]:
    """配额申请的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': QUOTA_REQUEST_REQUEST_SCHEMA,
            'description': '申请数据'
        },
    ]


def quota_request_detail_params() -> List[Dict[str, Any]]:
    """配额申请详情的参数定义"""
    return [
        {
            'name': 'request_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '申请ID'
        },
    ]


def quota_request_action_params() -> List[Dict[str, Any]]:
    """配额申请处理的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': QUOTA_REQUEST_ACTION_REQUEST_SCHEMA,
            'description': '处理参数'
        },
    ]


def ai_tool_set_params() -> List[Dict[str, Any]]:
    """设置AI工具的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': AI_TOOL_SET_REQUEST_SCHEMA,
            'description': 'AI工具配置数据'
        },
    ]


def ai_tool_list_params() -> List[Dict[str, Any]]:
    """AI工具列表的参数定义"""
    return [
        {
            'name': 'tenant_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '租户ID，为空则使用当前租户'
        },
    ]


def tenant_enable_ai_params() -> List[Dict[str, Any]]:
    """设置租户启用AI的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TENANT_ENABLE_AI_REQUEST_SCHEMA,
            'description': '启用参数'
        },
    ]
