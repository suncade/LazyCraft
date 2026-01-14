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

"""模型管理模块的 Swagger 定义"""

from typing import Dict, Any, List

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']
MODEL_TYPE_ENUM = ['local', 'online']
MODEL_FROM_ENUM = ['localModel', 'existModel', 'hf', 'ms']

# ==================== Schema 定义 ====================

MODEL_NAME_SCHEMA = {
    'type': 'object',
    'properties': {
        'is_finetune_model': {'type': 'boolean', 'description': '是否为微调模型'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_key': {'type': 'string', 'description': '模型密钥'},
    },
}

MODEL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '模型ID'},
        'description': {'type': 'string', 'description': '模型描述'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'model_icon': {'type': 'string', 'description': '模型图标'},
        'model_type': {'type': 'string', 'description': '模型类型'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_path': {'type': 'string', 'description': '模型路径'},
        'model_from': {'type': 'string', 'description': '模型来源'},
        'model_kind': {'type': 'string', 'description': '模型种类'},
        'model_kind_display': {'type': 'string', 'description': '模型种类显示'},
        'model_key': {'type': 'string', 'description': '模型密钥'},
        'model_status': {'type': 'string', 'description': '模型状态'},
        'prompt_keys': {'type': 'string', 'description': '提示词密钥'},
        'model_brand': {'type': 'string', 'description': '模型品牌'},
        'model_url': {'type': 'string', 'description': '模型URL'},
        'model_list': {
            'type': 'array',
            'items': MODEL_NAME_SCHEMA,
            'description': '模型列表'
        },
        'user_id': {'type': 'string', 'description': '用户ID'},
        'model_dir': {'type': 'string', 'description': '模型目录'},
        'api_key': {'type': 'string', 'description': 'API密钥'},
        'download_message': {'type': 'string', 'description': '下载消息'},
        'tags': {'type': 'array', 'items': {'type': 'string'}, 'description': '标签列表'},
        'user_name': {'type': 'string', 'description': '用户名'},
    },
}

MODEL_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': MODEL_SCHEMA,
            'description': '模型列表'
        },
    },
}

ONLINE_MODEL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': 'ID'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_key': {'type': 'string', 'description': '模型密钥'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'parent_id': {'type': 'string', 'description': '父模型ID'},
        'source_info': {'type': 'string', 'description': '来源信息'},
        'model_id': {'type': 'string', 'description': '模型ID'},
        'finetune_task_id': {'type': 'integer', 'description': '微调任务ID'},
        'can_finetune': {'type': 'boolean', 'description': '是否可微调'},
    },
}

FINETUNE_MODEL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '模型ID'},
        'description': {'type': 'string', 'description': '模型描述'},
        'created_at': {'type': 'string', 'format': 'date-time', 'description': '创建时间'},
        'updated_at': {'type': 'string', 'format': 'date-time', 'description': '更新时间'},
        'model_name': {'type': 'string', 'description': '模型名称'},
        'model_key': {'type': 'string', 'description': '模型密钥'},
        'source_info': {'type': 'string', 'description': '来源信息'},
        'finetune_task_id': {'type': 'integer', 'description': '微调任务ID'},
        'model_status': {'type': 'string', 'description': '模型状态'},
    },
}

FINETUNE_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': FINETUNE_MODEL_SCHEMA,
            'description': '微调模型列表'
        },
    },
}

# ==================== 请求 Schema 定义 ====================

MODEL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_type': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型类型筛选条件'
        },
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
            'description': '模型名称搜索条件'
        },
        'available': {
            'type': 'integer',
            'required': False,
            'description': '可用性筛选条件'
        },
        'status': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '状态筛选条件'
        },
        'model_kind': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型种类筛选条件'
        },
        'model_brand': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型品牌筛选条件'
        },
        'tenant': {
            'type': 'string',
            'required': False,
            'default': '',
            'description': '租户筛选条件'
        },
    },
}

MODEL_CREATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_type': {
            'type': 'string',
            'required': True,
            'enum': MODEL_TYPE_ENUM,
            'description': '模型类型（必需）'
        },
        'model_icon': {
            'type': 'string',
            'required': False,
            'description': '模型图标路径'
        },
        'model_name': {
            'type': 'string',
            'required': False,
            'description': '模型名称'
        },
        'description': {
            'type': 'string',
            'required': False,
            'description': '模型描述'
        },
        'model_from': {
            'type': 'string',
            'required': False,
            'enum': MODEL_FROM_ENUM,
            'description': '模型来源'
        },
        'model_kind': {
            'type': 'string',
            'required': False,
            'description': '模型种类'
        },
        'model_key': {
            'type': 'string',
            'required': False,
            'description': '模型密钥'
        },
        'access_tokens': {
            'type': 'string',
            'required': False,
            'description': '访问令牌'
        },
        'prompt_keys': {
            'type': 'string',
            'required': False,
            'description': '提示词密钥'
        },
        'model_brand': {
            'type': 'string',
            'required': False,
            'description': '模型品牌'
        },
        'model_url': {
            'type': 'string',
            'required': False,
            'description': '模型URL'
        },
        'proxy_url': {
            'type': 'string',
            'required': False,
            'description': '代理URL'
        },
        'model_list': {
            'type': 'string',
            'required': False,
            'description': '模型列表'
        },
        'model_dir': {
            'type': 'string',
            'required': False,
            'description': '模型目录'
        },
        'tag_names': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': False,
            'description': '标签名称列表'
        },
    },
    'required': ['model_type'],
}

ONLINE_MODEL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_id': {
            'type': 'integer',
            'required': True,
            'description': '基础模型ID'
        },
        'model_list': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'model_key': {'type': 'string', 'description': '模型密钥'},
                    'can_finetune': {'type': 'boolean', 'description': '是否可微调'},
                },
            },
            'required': True,
            'description': '在线模型列表'
        },
    },
    'required': ['model_id', 'model_list'],
}

DELETE_ONLINE_MODEL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_id': {
            'type': 'integer',
            'required': True,
            'description': '基础模型ID'
        },
        'model_keys': {
            'type': 'array',
            'items': {'type': 'string'},
            'required': True,
            'description': '要删除的模型密钥列表'
        },
    },
    'required': ['model_id', 'model_keys'],
}

UPDATE_APIKEY_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_brand': {
            'type': 'string',
            'required': True,
            'description': '模型品牌（必需）'
        },
        'api_key': {
            'type': 'string',
            'required': False,
            'description': 'API密钥'
        },
        'proxy_url': {
            'type': 'string',
            'required': False,
            'description': '代理URL'
        },
        'proxy_auth_info': {
            'type': 'object',
            'required': False,
            'description': '代理认证信息'
        },
    },
    'required': ['model_brand'],
}

MODEL_UPDATE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_id': {
            'type': 'string',
            'required': True,
            'description': '模型ID（必需）'
        },
        'api_key': {
            'type': 'string',
            'required': True,
            'description': 'API密钥（必需）'
        },
    },
    'required': ['model_id', 'api_key'],
}

CHECK_MODEL_NAME_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_name': {
            'type': 'string',
            'required': True,
            'description': '模型名称（必需）'
        },
        'model_from': {
            'type': 'string',
            'required': False,
            'description': '模型来源'
        },
    },
    'required': ['model_name'],
}

CREATE_FINETUNE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'base_model_id': {
            'type': 'integer',
            'required': True,
            'description': '基础模型ID（必需）'
        },
        'model_from': {
            'type': 'string',
            'required': True,
            'description': '模型来源（必需）'
        },
        'model_key': {
            'type': 'string',
            'required': False,
            'description': '模型密钥'
        },
        'access_tokens': {
            'type': 'string',
            'required': False,
            'description': '访问令牌'
        },
        'prompt_keys': {
            'type': 'string',
            'required': False,
            'description': '提示词密钥'
        },
        'model_type': {
            'type': 'string',
            'required': False,
            'description': '模型类型'
        },
        'model_dir': {
            'type': 'string',
            'required': False,
            'description': '模型目录'
        },
        'model_name': {
            'type': 'string',
            'required': False,
            'description': '模型名称'
        },
    },
    'required': ['base_model_id', 'model_from'],
}

FINETUNE_MODEL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_id': {
            'type': 'string',
            'required': False,
            'default': '0',
            'description': '模型ID筛选条件'
        },
        'online_model_id': {
            'type': 'string',
            'required': False,
            'default': '0',
            'description': '在线模型ID筛选条件'
        },
        'page': {
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': '页码'
        },
        'page_size': {
            'type': 'integer',
            'required': False,
            'default': 20,
            'description': '每页大小'
        },
        'qtype': {
            'type': 'string',
            'required': False,
            'default': 'already',
            'enum': QTYPE_ENUM,
            'description': '查询类型'
        },
    },
}

MERGE_FILE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'filename': {
            'type': 'string',
            'required': True,
            'description': '文件名（必需）'
        },
        'file_dir': {
            'type': 'string',
            'required': True,
            'description': '文件目录（必需）'
        },
    },
    'required': ['filename', 'file_dir'],
}

DELETE_UPLOADED_FILE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'filename': {
            'type': 'string',
            'required': True,
            'description': '文件名（必需）'
        },
        'file_dir': {
            'type': 'string',
            'required': True,
            'description': '文件目录（必需）'
        },
    },
    'required': ['filename', 'file_dir'],
}

DELETE_APIKEY_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_brand': {
            'type': 'string',
            'required': True,
            'description': '模型品牌（必需）'
        },
    },
    'required': ['model_brand'],
}

MODEL_DELETE_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'model_id': {
            'type': 'string',
            'required': True,
            'description': '模型ID（必需）'
        },
    },
    'required': ['model_id'],
}

UPDATE_ONLINE_MODEL_LIST_REQUEST_SCHEMA = {
    'type': 'object',
    'properties': {
        'base_model_id': {
            'type': 'integer',
            'required': True,
            'description': '基础模型ID'
        },
    },
    'required': ['base_model_id'],
}

# ==================== 参数定义函数 ====================

def model_list_params() -> List[Dict[str, Any]]:
    """获取模型列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': MODEL_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def model_create_params() -> List[Dict[str, Any]]:
    """创建模型的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MODEL_CREATE_REQUEST_SCHEMA,
            'description': '模型数据'
        },
    ]


def model_id_path_param() -> Dict[str, Any]:
    """模型ID路径参数定义"""
    return {
        'name': 'model_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '模型ID'
    }


def finetune_model_id_path_param() -> Dict[str, Any]:
    """微调模型ID路径参数定义"""
    return {
        'name': 'finetune_model_id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': '微调模型ID'
    }


def model_id_body_param() -> Dict[str, Any]:
    """模型ID body参数定义"""
    return {
        'name': 'model_id',
        'in': 'body',
        'type': 'string',
        'required': True,
        'description': '模型ID'
    }


def online_model_list_params() -> List[Dict[str, Any]]:
    """保存在线模型列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': ONLINE_MODEL_LIST_REQUEST_SCHEMA,
            'description': '在线模型列表数据'
        },
    ]


def delete_online_model_list_params() -> List[Dict[str, Any]]:
    """删除在线模型列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_ONLINE_MODEL_LIST_REQUEST_SCHEMA,
            'description': '删除参数'
        },
    ]


def update_apikey_params() -> List[Dict[str, Any]]:
    """更新API密钥的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': UPDATE_APIKEY_REQUEST_SCHEMA,
            'description': 'API密钥数据'
        },
    ]


def delete_apikey_params() -> List[Dict[str, Any]]:
    """删除API密钥的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_APIKEY_REQUEST_SCHEMA,
            'description': '删除参数'
        },
    ]


def model_update_params() -> List[Dict[str, Any]]:
    """更新模型的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MODEL_UPDATE_REQUEST_SCHEMA,
            'description': '更新数据'
        },
    ]


def model_delete_params() -> List[Dict[str, Any]]:
    """删除模型的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MODEL_DELETE_REQUEST_SCHEMA,
            'description': '删除参数'
        },
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'mine',
            'description': '查询类型'
        },
    ]


def check_model_name_params() -> List[Dict[str, Any]]:
    """检查模型名称的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': CHECK_MODEL_NAME_REQUEST_SCHEMA,
            'description': '检查参数'
        },
    ]


def models_tree_params() -> List[Dict[str, Any]]:
    """获取模型树结构的参数定义"""
    return [
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': True,
            'default': 'already',
            'enum': QTYPE_ENUM,
            'description': '查询类型'
        },
        {
            'name': 'model_type',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型类型筛选条件'
        },
        {
            'name': 'model_kind',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': '',
            'description': '模型种类筛选条件'
        },
    ]


def model_info_params() -> List[Dict[str, Any]]:
    """获取模型信息的参数定义"""
    return [
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'mine',
            'description': '查询类型'
        },
        {
            'name': 'namespace',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'already',
            'description': '命名空间'
        },
    ]


def create_finetune_params() -> List[Dict[str, Any]]:
    """创建微调模型的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': CREATE_FINETUNE_REQUEST_SCHEMA,
            'description': '微调模型数据'
        },
    ]


def finetune_model_list_params() -> List[Dict[str, Any]]:
    """获取微调模型列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': False,
            'schema': FINETUNE_MODEL_LIST_REQUEST_SCHEMA,
            'description': '查询参数'
        },
    ]


def update_online_model_list_params() -> List[Dict[str, Any]]:
    """更新在线模型列表的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': UPDATE_ONLINE_MODEL_LIST_REQUEST_SCHEMA,
            'description': '更新参数'
        },
        {
            'name': 'qtype',
            'in': 'query',
            'type': 'string',
            'required': False,
            'default': 'already',
            'description': '查询类型'
        },
    ]


def upload_file_chunk_params() -> List[Dict[str, Any]]:
    """上传文件分片的参数定义"""
    return [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '上传的文件分片'
        },
        {
            'name': 'chunk_number',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': '分片编号'
        },
        {
            'name': 'total_chunks',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': '总分片数'
        },
        {
            'name': 'file_name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': '文件名'
        },
        {
            'name': 'file_dir',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': '文件目录'
        },
    ]


def merge_file_params() -> List[Dict[str, Any]]:
    """合并文件分片的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MERGE_FILE_REQUEST_SCHEMA,
            'description': '合并参数'
        },
    ]


def delete_uploaded_file_params() -> List[Dict[str, Any]]:
    """删除上传文件的参数定义"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': DELETE_UPLOADED_FILE_REQUEST_SCHEMA,
            'description': '删除参数'
        },
    ]
