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

"""数据库管理模块的 Swagger 规范定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    PAGINATION_SCHEMA,
    TABLE_PAGINATION_SCHEMA,
    TABLE_STRUCTURE_SCHEMA,
    DATA_IMPORT_PREVIEW_SCHEMA,
    TABLE_DATA_PAGINATION_SCHEMA,
    database_id_path_param,
    table_id_path_param,
    table_name_path_param,
    pagination_params,
    pagination_body_params,
    database_create_params,
    database_list_params,
    database_update_params,
    table_list_params,
    table_create_params,
    table_update_params,
    data_import_execute_params,
    table_data_update_params,
    table_data_delete_params,
)


# ==================== 数据库相关接口 ====================

# 创建数据库
database_create_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '创建数据库',
    'description': '创建新数据库，要求数据库名称以字母开头，只能包含字母、数字和下划线，且长度不超过20',
    'parameters': database_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                    'data': {'type': 'object'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取数据库列表
database_list_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '获取数据库列表',
    'description': '分页获取用户可访问的数据库列表，支持按数据库名称、查询类型、用户ID等条件筛选',
    'parameters': database_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 更新数据库信息
database_update_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '更新数据库信息',
    'description': '更新指定数据库的名称和注释信息',
    'parameters': [
        database_id_path_param(),
    ] + database_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                    'data': {'type': 'object'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除数据库
database_delete_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '删除数据库',
    'description': '删除指定的数据库，需要管理员权限',
    'parameters': [
        database_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
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


# ==================== 表相关接口 ====================

# 获取表列表
table_list_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '获取表列表',
    'description': '分页获取指定数据库中的所有表，支持按表名筛选',
    'parameters': [
        database_id_path_param(),
    ] + table_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': TABLE_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 根据表名获取表结构
table_get_by_name_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '根据表名获取表结构',
    'description': '获取指定数据库中指定表名的表结构信息',
    'parameters': [
        database_id_path_param(),
        table_name_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': TABLE_STRUCTURE_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 根据表ID获取表结构
table_get_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '根据表ID获取表结构',
    'description': '获取指定数据库中指定表ID的表结构信息',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': TABLE_STRUCTURE_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 编辑表结构
table_update_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '编辑表结构',
    'description': '修改指定表的结构，包括表名、注释和列定义，需要写入权限',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ] + table_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '修改成功',
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

# 删除表
table_delete_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '删除表',
    'description': '删除指定数据库中的指定表，需要管理员权限',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ],
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

# 创建表
table_create_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '创建表',
    'description': '在指定数据库中创建新表，包括表名、注释和列定义，需要写入权限',
    'parameters': [
        database_id_path_param(),
    ] + table_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
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


# ==================== 数据导入相关接口 ====================

# 下载数据导入模板
data_import_template_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '下载数据导入模板',
    'description': '生成并下载指定表的Excel导入模板文件，包含表的所有列',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '下载成功',
            'schema': {
                'type': 'file',
            },
        },
    },
}

# 上传并预览导入数据
data_import_preview_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '上传并预览导入数据',
    'description': '上传Excel文件并预览要导入的数据，包括数据验证和格式转换',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '要上传的Excel文件',
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '预览成功',
            'schema': DATA_IMPORT_PREVIEW_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 执行数据导入
data_import_execute_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '执行数据导入',
    'description': '根据预览的数据执行实际的数据导入操作',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ] + data_import_execute_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '导入成功',
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


# ==================== 表数据相关接口 ====================

# 获取表数据（分页）
table_data_list_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '获取表数据',
    'description': '分页获取指定表中的数据记录',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ] + pagination_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': TABLE_DATA_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 批量更新表数据
table_data_update_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '批量更新表数据',
    'description': '批量执行表数据的增加、更新和删除操作',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ] + table_data_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
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

# 删除表数据
table_data_delete_spec: Dict[str, Any] = {
    'tags': ['数据库管理'],
    'summary': '删除表数据',
    'description': '删除指定表中的数据记录',
    'parameters': [
        database_id_path_param(),
        table_id_path_param(),
    ] + table_data_delete_params(),
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
