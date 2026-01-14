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

"""数据集模块的 Swagger 定义和参数"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses


# ==================== 枚举定义 ====================

# 数据类型
DATA_TYPE_ENUM = ['doc', 'pic']

# 上传类型
UPLOAD_TYPE_ENUM = ['local', 'url']

# 版本类型
VERSION_TYPE_ENUM = ['branch', 'tag']

# 脚本类型（常见）
SCRIPT_TYPE_ENUM = ['数据过滤', '数据增强', '数据去噪', '数据标注', '智能处理']

# 脚本代理类型
SCRIPT_AGENT_ENUM = ['script']


# ==================== Schema 定义 ====================

# 分页响应 Schema（通用）
PAGINATION_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页大小'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {'type': 'array', 'description': '数据列表'}
    }
}

# 脚本字段 Schema
SCRIPT_FIELD_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '脚本ID'},
        'name': {'type': 'string', 'description': '脚本名称'},
        'description': {'type': 'string', 'description': '脚本描述'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'updated_at': {'type': 'integer', 'description': '更新时间戳'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'user_name': {'type': 'string', 'description': '用户名'},
        'script_url': {'type': 'string', 'description': '脚本URL'},
        'script_type': {'type': 'string', 'description': '脚本类型'},
        'upload_status': {'type': 'string', 'description': '上传状态'},
        'data_type': {'type': 'string', 'description': '数据类型'}
    }
}

# 数据集字段 Schema
DATA_SET_FIELD_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '数据集ID'},
        'name': {'type': 'string', 'description': '数据集名称'},
        'description': {'type': 'string', 'description': '数据集描述'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'updated_at': {'type': 'integer', 'description': '更新时间戳'},
        'last_sync_at': {'type': 'integer', 'description': '最后同步时间戳'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'user_name': {'type': 'string', 'description': '用户名'},
        'data_set_url': {'type': 'string', 'description': '数据集URL'},
        'label': {'type': 'array', 'items': {'type': 'string'}, 'description': '标签列表'},
        'tags': {'type': 'array', 'items': {'type': 'string'}, 'description': '标签列表'},
        'data_type': {'type': 'string', 'description': '数据类型'},
        'data_format': {'type': 'string', 'description': '数据格式'},
        'upload_type': {'type': 'string', 'description': '上传类型'},
        'from_type': {'type': 'string', 'description': '来源类型'},
        'file_urls': {'type': 'array', 'items': {'type': 'string'}, 'description': '文件URL列表'},
        'file_paths': {'type': 'array', 'items': {'type': 'string'}, 'description': '文件路径列表'},
        'data_set_file_ids': {'type': 'array', 'items': {'type': 'integer'}, 'description': '数据集文件ID列表'},
        'tags_num': {'type': 'integer', 'description': '标签数量'},
        'branches_num': {'type': 'integer', 'description': '分支数量'},
        'reflux_type': {'type': 'string', 'description': '回流类型'}
    }
}

# 数据集版本字段 Schema
DATA_SET_VERSION_FIELD_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '版本ID'},
        'name': {'type': 'string', 'description': '版本名称'},
        'version': {'type': 'string', 'description': '版本号'},
        'data_set_id': {'type': 'integer', 'description': '数据集ID'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'updated_at': {'type': 'integer', 'description': '更新时间戳'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'status': {'type': 'string', 'description': '状态'},
        'is_original': {'type': 'string', 'description': '是否原始版本'},
        'data_set_file_ids': {'type': 'array', 'items': {'type': 'integer'}, 'description': '数据集文件ID列表'},
        'version_type': {'type': 'string', 'description': '版本类型'},
        'is_published': {'type': 'boolean', 'description': '是否已发布'},
        'version_path': {'type': 'string', 'description': '版本路径'},
        'previous_version_id': {'type': 'integer', 'description': '上一个版本ID'}
    }
}

# 数据集文件字段 Schema
DATA_SET_FILE_FIELD_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '文件ID'},
        'name': {'type': 'string', 'description': '文件名'},
        'path': {'type': 'string', 'description': '文件路径'},
        'download_url': {'type': 'string', 'description': '下载URL'},
        'status': {'type': 'string', 'description': '文件状态'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'updated_at': {'type': 'integer', 'description': '更新时间戳'},
        'data_set_id': {'type': 'integer', 'description': '数据集ID'},
        'data_set_version_id': {'type': 'integer', 'description': '数据集版本ID'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'operation': {'type': 'string', 'description': '操作类型'},
        'finished_at': {'type': 'integer', 'description': '完成时间戳'},
        'file_type': {'type': 'string', 'description': '文件类型'},
        'error_msg': {'type': 'string', 'description': '错误信息'}
    }
}

# 回流数据字段 Schema
REFLUX_DATA_FIELD_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '回流数据ID'},
        'data_set_id': {'type': 'integer', 'description': '数据集ID'},
        'data_set_version_id': {'type': 'integer', 'description': '数据集版本ID'},
        'app_id': {'type': 'string', 'description': '应用ID'},
        'app_name': {'type': 'string', 'description': '应用名称'},
        'module_id': {'type': 'string', 'description': '模块ID'},
        'module_name': {'type': 'string', 'description': '模块名称'},
        'module_type': {'type': 'string', 'description': '模块类型'},
        'output_time': {'type': 'integer', 'description': '输出时间戳'},
        'module_input': {'type': 'string', 'description': '模块输入'},
        'module_output': {'type': 'string', 'description': '模块输出'},
        'conversation_id': {'type': 'string', 'description': '会话ID'},
        'turn_number': {'type': 'string', 'description': '轮次编号'},
        'is_satisfied': {'type': 'string', 'description': '是否满意'},
        'user_feedback': {'type': 'string', 'description': '用户反馈'},
        'status': {'type': 'string', 'description': '状态'},
        'operation': {'type': 'string', 'description': '操作类型'},
        'finished_at': {'type': 'string', 'description': '完成时间'},
        'error_msg': {'type': 'string', 'description': '错误信息'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'updated_at': {'type': 'integer', 'description': '更新时间戳'}
    }
}


# ==================== 参数定义函数 ====================

def pagination_params() -> list:
    """分页参数"""
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'minimum': 1,
            'description': '页码，从1开始'
        },
        {
            'name': 'page_size',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 20,
            'minimum': 1,
            'maximum': 100,
            'description': '每页大小'
        }
    ]


# ==================== 请求 Schema 定义 ====================

PAGINATION_BODY_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {
            'type': 'integer',
            'required': False,
            'default': 1,
            'minimum': 1,
            'description': '页码，从1开始'
        },
        'page_size': {
            'type': 'integer',
            'required': False,
            'default': 20,
            'minimum': 1,
            'maximum': 100,
            'description': '每页大小'
        },
    },
}

COMMON_QUERY_BODY_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'qtype': {
            'type': 'string',
            'required': False,
            'default': 'already',
            'description': '查询类型'
        },
        'search_tags': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'description': '搜索标签列表'
        },
        'search_name': {
            'type': 'string',
            'required': False,
            'description': '搜索名称'
        },
        'user_id': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'description': '用户ID列表'
        },
    },
}

# ==================== 参数定义函数 ====================

def pagination_body_params() -> list:
    """分页请求体参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': PAGINATION_BODY_REQUEST_SCHEMA,
            'description': '分页参数'
        },
    ]


def common_query_params() -> list:
    """通用查询参数"""
    return [
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'already',
            'description': '查询类型'
        },
        {
            'name': 'search_tags',
            'in': 'query',
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'description': '搜索标签列表'
        },
        {
            'name': 'search_name',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '搜索名称'
        },
        {
            'name': 'user_id',
            'in': 'query',
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'description': '用户ID列表'
        }
    ]


def common_query_body_params() -> list:
    """通用查询请求体参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': COMMON_QUERY_BODY_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]
