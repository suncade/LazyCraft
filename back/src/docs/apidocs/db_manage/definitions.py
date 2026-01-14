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

from docs.apidocs.common_definitions import AUTH_SECURITY

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']

# ==================== Schema 定义 ====================

ACCOUNT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
    },
}

DATABASE_INFO_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'tenant_id': {'type': 'string'},
        'created_by': {'type': 'string'},
        'name': {'type': 'string'},
        'database_name': {'type': 'string'},
        'comment': {'type': 'string'},
        'url': {'type': 'string', 'x-nullable': True},
        'type': {'type': 'string'},
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
        'created_by_account': ACCOUNT_SCHEMA,
        'table_count': {'type': 'integer'},
        'user_name': {'type': 'string'},
    },
}

TABLE_INFO_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'tenant_id': {'type': 'string'},
        'created_by': {'type': 'string'},
        'name': {'type': 'string'},
        'comment': {'type': 'string'},
        'row_count': {'type': 'integer'},
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
        'created_by_account': ACCOUNT_SCHEMA,
    },
}

PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer'},
        'limit': {'type': 'integer'},
        'total': {'type': 'integer'},
        'has_more': {'type': 'boolean'},
        'data': {
            'type': 'array',
            'items': DATABASE_INFO_SCHEMA,
        },
    },
}

TABLE_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer'},
        'limit': {'type': 'integer'},
        'total': {'type': 'integer'},
        'has_more': {'type': 'boolean'},
        'data': {
            'type': 'array',
            'items': TABLE_INFO_SCHEMA,
        },
    },
}

TABLE_STRUCTURE_SCHEMA = {
    'type': 'object',
    'properties': {
        'table_id': {'type': 'integer'},
        'table_name': {'type': 'string'},
        'comment': {'type': 'string'},
        'columns': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'type': {'type': 'string'},
                    'comment': {'type': 'string'},
                    'nullable': {'type': 'boolean'},
                    'default': {'type': 'string', 'x-nullable': True},
                },
            },
        },
    },
}

COLUMN_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'type': {'type': 'string'},
        'comment': {'type': 'string'},
        'nullable': {'type': 'boolean'},
        'default': {'type': 'string', 'x-nullable': True},
    },
    'required': ['name', 'type'],
}

DATA_IMPORT_PREVIEW_SCHEMA = {
    'type': 'object',
    'properties': {
        'total_rows': {'type': 'integer'},
        'columns': {
            'type': 'array',
            'items': COLUMN_SCHEMA,
        },
        'data': {
            'type': 'array',
            'items': {'type': 'object'},
        },
    },
}

TABLE_DATA_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer'},
        'limit': {'type': 'integer'},
        'total': {'type': 'integer'},
        'has_more': {'type': 'boolean'},
        'data': {
            'type': 'array',
            'items': {'type': 'object'},
        },
    },
}

# ==================== 请求 Schema 定义 ====================

DATABASE_CREATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'db_name': {
            'type': 'string',
            'required': True,
            'description': '数据库名称（以字母开头，只能包含字母、数字和下划线，长度不超过20）'
        },
        'comment': {
            'type': 'string',
            'required': True,
            'description': '数据库注释'
        },
    },
    'required': ['db_name', 'comment'],
}

DATABASE_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {
            'type': 'integer',
            'default': 1,
            'description': '页码'
        },
        'limit': {
            'type': 'integer',
            'default': 10,
            'description': '每页数量'
        },
        'db_name': {
            'type': 'string',
            'default': '',
            'description': '数据库名称筛选'
        },
        'qtype': {
            'type': 'string',
            'enum': QTYPE_ENUM,
            'default': 'already',
            'description': '查询类型：mine（我的）/group（组内）/builtin（内置）/already（已访问）'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'default': [],
            'description': '用户ID列表筛选'
        },
    },
}

DATABASE_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'db_name': {
            'type': 'string',
            'required': True,
            'description': '新的数据库名称'
        },
        'comment': {
            'type': 'string',
            'required': True,
            'description': '新的数据库注释'
        },
    },
    'required': ['db_name', 'comment'],
}

TABLE_CREATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'table_name': {
            'type': 'string',
            'required': True,
            'description': '表名'
        },
        'comment': {
            'type': 'string',
            'required': True,
            'description': '表注释'
        },
        'columns': {
            'type': 'array',
            'items': COLUMN_SCHEMA,
            'required': True,
            'description': '列定义列表'
        },
    },
    'required': ['table_name', 'comment', 'columns'],
}

DATA_IMPORT_EXECUTE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'action': {
            'type': 'string',
            'enum': ['preview', 'import'],
            'required': True,
            'description': '操作类型：preview（预览）/import（导入）'
        },
        'data': {
            'type': 'array',
            'items': {'type': 'object'},
            'required': False,
            'description': '要导入的数据列表（当action为import时必填）'
        },
    },
    'required': ['action'],
}

TABLE_DATA_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'add_items': {
            'type': 'array',
            'items': {'type': 'object'},
            'description': '要添加的数据项列表'
        },
        'update_items': {
            'type': 'array',
            'items': {'type': 'object'},
            'description': '要更新的数据项列表'
        },
        'delete_items': {
            'type': 'array',
            'items': {'type': 'object'},
            'description': '要删除的数据项列表'
        },
        'table_name': {
            'type': 'string',
            'description': '表名'
        },
    },
}

TABLE_DATA_DELETE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'data_items': {
            'type': 'array',
            'items': {'type': 'object'},
            'required': True,
            'description': '要删除的数据项列表'
        },
        'table_name': {
            'type': 'string',
            'description': '表名'
        },
    },
    'required': ['data_items'],
}

# ==================== 参数定义 ====================

def database_id_path_param():
    return {
        'name': 'database_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '数据库ID',
    }

def table_id_path_param():
    return {
        'name': 'table_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '表ID',
    }

def table_name_path_param():
    return {
        'name': 'table_name',
        'in': 'path',
        'type': 'string',
        'required': True,
        'description': '表名',
    }

def pagination_params():
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'default': 1,
            'description': '页码',
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'default': 10,
            'description': '每页数量',
        },
    ]

def pagination_body_params():
    return [
        {
            'name': 'page',
            'in': 'body',
            'type': 'integer',
            'default': 1,
            'description': '页码',
        },
        {
            'name': 'limit',
            'in': 'body',
            'type': 'integer',
            'default': 10,
            'description': '每页数量',
        },
    ]

def database_create_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DATABASE_CREATE_REQUEST_SCHEMA,
            'description': '数据库创建参数'
        },
    ]

def database_list_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': DATABASE_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]

def database_update_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DATABASE_UPDATE_REQUEST_SCHEMA,
            'description': '数据库更新参数'
        },
    ]

def table_list_params():
    return pagination_params() + [
        {
            'name': 'table_name',
            'in': 'query',
            'type': 'string',
            'default': '',
            'description': '表名筛选',
        },
    ]

def table_create_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TABLE_CREATE_REQUEST_SCHEMA,
            'description': '表创建参数'
        },
    ]

def table_update_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TABLE_CREATE_REQUEST_SCHEMA,
            'description': '表更新参数'
        },
    ]

def data_import_execute_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DATA_IMPORT_EXECUTE_REQUEST_SCHEMA,
            'description': '数据导入参数'
        },
    ]

def table_data_update_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TABLE_DATA_UPDATE_REQUEST_SCHEMA,
            'description': '表数据更新参数'
        },
    ]

def table_data_delete_params():
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': TABLE_DATA_DELETE_REQUEST_SCHEMA,
            'description': '表数据删除参数'
        },
    ]
