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

"""推理服务模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']
STATUS_ENUM = ['Ready', 'Pending', 'Running', 'Stopped', 'Error']

# ==================== Schema 定义 ====================

SERVICE_ITEM_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '服务ID'},
        'name': {'type': 'string', 'description': '服务名称'},
        'group_id': {'type': 'integer', 'description': '服务组ID'},
        'model_id': {'type': 'integer', 'description': '模型ID'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_type': {'type': 'string', 'description': '模型类型'},
        'status': {'type': 'string', 'description': '服务状态'},
        'job_id': {'type': 'string', 'description': '任务ID'},
        'gid': {'type': 'string', 'description': '组ID'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'created_time': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_time': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'tenant_id': {'type': 'string', 'description': '租户ID'},
    },
}

SERVICE_LIST_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'total': {'type': 'integer', 'description': '总记录数'},
        'pages': {'type': 'integer', 'description': '总页数'},
        'current_page': {'type': 'integer', 'description': '当前页码'},
        'next_page': {'type': 'integer', 'description': '下一页页码'},
        'prev_page': {'type': 'integer', 'description': '上一页页码'},
        'result': {
            'type': 'array',
            'items': SERVICE_ITEM_SCHEMA,
            'description': '服务列表'
        },
    },
}

MODEL_ITEM_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '模型ID'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'need_confirm': {'type': 'boolean', 'description': '是否需要确认'},
    },
}

SERVICE_GROUP_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '服务组ID'},
        'model_id': {'type': 'integer', 'description': '模型ID'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_type': {'type': 'string', 'description': '模型类型'},
        'tenant_id': {'type': 'string', 'description': '租户ID'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'created_time': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
    },
}

SERVICE_CONFIG_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'description': '服务名称'},
        'num_gpus': {'type': 'integer', 'description': 'GPU数量', 'default': 1},
    },
    'required': ['name'],
}

CLOUD_SERVICE_STATUS_SCHEMA = {
    'type': 'object',
    'properties': {
        'enabled': {'type': 'boolean', 'description': '是否启用'},
        'message': {'type': 'string', 'description': '状态消息'},
    },
}

# ==================== 请求 Schema 定义 ====================

SERVICE_LIST_REQUEST_SCHEMA = {
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
        'search_name': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '搜索名称'
        },
        'status': {
            'type': 'array',
            'items': {'type': 'string', 'enum': STATUS_ENUM},
            'required': False,
            'default': [],
            'description': '状态筛选'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'default': [],
            'description': '用户ID筛选'
        },
        'tenant': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '租户筛选'
        },
    },
}

CREATE_SERVICE_GROUP_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_type': {
            'type': 'string',
            'required': True,
            'description': '模型类型'
        },
        'model_id': {
            'type': 'integer',
            'required': True,
            'description': '模型ID'
        },
        'services': {
            'type': 'array',
            'items': SERVICE_CONFIG_SCHEMA,
            'required': True,
            'description': '服务配置列表'
        },
    },
    'required': ['model_type', 'model_id', 'services'],
}

CREATE_SERVICE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'group_id': {
            'type': 'integer',
            'required': True,
            'description': '服务组ID'
        },
        'services': {
            'type': 'array',
            'items': SERVICE_CONFIG_SCHEMA,
            'required': True,
            'description': '服务配置列表'
        },
    },
    'required': ['group_id', 'services'],
}

GROUP_ID_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'group_id': {
            'type': 'integer',
            'required': True,
            'description': '服务组ID'
        },
    },
    'required': ['group_id'],
}

SERVICE_ID_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'service_id': {
            'type': 'integer',
            'required': True,
            'description': '服务ID'
        },
    },
    'required': ['service_id'],
}

# ==================== 参数定义函数 ====================

def service_list_params() -> List[Dict[str, Any]]:
    """获取推理服务列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': SERVICE_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def model_list_params() -> List[Dict[str, Any]]:
    """获取模型列表的参数定义"""
    return [
        {
            'name': 'model_type',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'local',
            'description': '模型类型'
        },
        {
            'name': 'model_kind',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型种类'
        },
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '查询类型'
        },
    ]


def create_service_group_params() -> List[Dict[str, Any]]:
    """创建服务组的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': CREATE_SERVICE_GROUP_REQUEST_SCHEMA,
            'description': '服务组数据'
        },
    ]


def create_service_params() -> List[Dict[str, Any]]:
    """创建服务的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': CREATE_SERVICE_REQUEST_SCHEMA,
            'description': '服务数据'
        },
    ]


def service_id_param() -> List[Dict[str, Any]]:
    """服务ID参数定义（使用 schema）"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': SERVICE_ID_REQUEST_SCHEMA,
            'description': '服务ID'
        },
    ]


def group_id_param() -> List[Dict[str, Any]]:
    """服务组ID参数定义（使用 schema）"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': GROUP_ID_REQUEST_SCHEMA,
            'description': '服务组ID'
        },
    ]


def draw_service_list_params() -> List[Dict[str, Any]]:
    """获取绘图服务列表的参数定义"""
    return [
        {
            'name': 'model_kind',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型种类'
        },
    ]


def ams_model_list_params() -> List[Dict[str, Any]]:
    """获取AMS模型列表的参数定义"""
    return [
        {
            'name': 'model_type',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型类型'
        },
    ]
