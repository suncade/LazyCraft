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

"""知识库模块的 Swagger 定义"""

# ==================== 枚举定义 ====================

QTYPE_ENUM = ['mine', 'group', 'builtin', 'already']

# ==================== Schema 定义 ====================

KNOWLEDGE_BASE_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'format': 'uuid'},
        'name': {'type': 'string', 'description': '知识库名称'},
        'description': {'type': 'string', 'description': '知识库描述'},
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
        'path': {'type': 'string', 'description': '知识库路径'},
        'user_name': {'type': 'string', 'description': '创建者用户名'},
        'user_id': {'type': 'string', 'description': '创建者用户ID'},
        'tags': {
            'type': 'array',
            'items': {'type': 'string'},
            'description': '标签列表'
        },
        'ref_status': {'type': 'boolean', 'description': '是否被引用'},
    },
}

KNOWLEDGE_BASE_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': KNOWLEDGE_BASE_SCHEMA,
            'description': '知识库列表'
        },
    },
}

FILE_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'format': 'uuid'},
        'name': {'type': 'string', 'description': '文件名'},
        'size': {'type': 'integer', 'description': '文件大小（字节）'},
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
        'file_type': {'type': 'string', 'description': '文件类型'},
        'file_path': {'type': 'string', 'description': '文件路径'},
        'file_md5': {'type': 'string', 'description': '文件MD5值'},
        'user_id': {'type': 'string', 'description': '用户ID'},
        'storage_type': {'type': 'string', 'description': '存储类型'},
        'knowledge_base_id': {'type': 'string', 'format': 'uuid', 'description': '所属知识库ID'},
        'used': {'type': 'boolean', 'description': '是否已使用'},
    },
}

FILE_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'page_size': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': FILE_SCHEMA,
            'description': '文件列表'
        },
        'knowledge_base_info': {
            'type': 'object',
            'description': '知识库信息',
            'properties': KNOWLEDGE_BASE_SCHEMA['properties'],
        },
    },
}

FILE_LIST_SCHEMA = {
    'type': 'object',
    'properties': {
        'files': {
            'type': 'array',
            'items': FILE_SCHEMA,
            'description': '文件列表'
        },
    },
}

APP_REF_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'format': 'uuid'},
        'name': {'type': 'string', 'description': '应用名称'},
        'is_public': {'type': 'boolean', 'description': '是否公开'},
    },
}

APP_REF_LIST_SCHEMA = {
    'type': 'array',
    'items': APP_REF_SCHEMA,
    'description': '引用该知识库的应用列表'
}

# ==================== 参数定义 ====================

def knowledge_base_list_params():
    """知识库列表查询参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {
                        'type': 'integer',
                        'default': 1,
                        'description': '页码，从1开始'
                    },
                    'page_size': {
                        'type': 'integer',
                        'default': 20,
                        'description': '每页数量'
                    },
                    'qtype': {
                        'type': 'string',
                        'enum': QTYPE_ENUM,
                        'default': 'already',
                        'description': '查询类型：mine（我的）/group（组内）/builtin（内置）/already（已访问）'
                    },
                    'search_tags': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'default': [],
                        'description': '标签筛选列表'
                    },
                    'search_name': {
                        'type': 'string',
                        'default': '',
                        'description': '知识库名称搜索关键词'
                    },
                    'user_id': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'default': [],
                        'description': '用户ID筛选列表'
                    },
                },
                'required': []
            },
        },
    ]

def knowledge_base_create_params():
    """创建知识库参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'required': True,
                        'description': '知识库名称'
                    },
                    'description': {
                        'type': 'string',
                        'required': True,
                        'description': '知识库描述'
                    },
                },
                'required': ['name', 'description']
            },
        },
    ]

def knowledge_base_update_params():
    """更新知识库参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'string',
                        'format': 'uuid',
                        'required': True,
                        'description': '知识库ID'
                    },
                    'name': {
                        'type': 'string',
                        'required': True,
                        'description': '知识库名称'
                    },
                    'description': {
                        'type': 'string',
                        'required': True,
                        'description': '知识库描述'
                    },
                },
                'required': ['id', 'name', 'description']
            },
        },
    ]

def knowledge_base_delete_params():
    """删除知识库参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'string',
                        'format': 'uuid',
                        'required': True,
                        'description': '知识库ID'
                    },
                },
                'required': ['id']
            },
        },
    ]

def file_upload_params():
    """文件上传参数"""
    return [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '要上传的文件，支持格式：.xls, .xlsx, .doc, .docx, .zip, .csv, .json, .txt, .pdf, .html, .tex, .md, .ppt, .pptx, .xml。单个文件最大50MB，zip文件最大500MB'
        },
    ]

def file_get_params():
    """获取文件详情参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'file_id': {
                        'type': 'string',
                        'format': 'uuid',
                        'required': True,
                        'description': '文件ID'
                    },
                },
                'required': ['file_id']
            },
        },
    ]

def file_download_params():
    """文件下载参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'file_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'required': True,
                        'description': '文件ID列表，单个文件直接下载，多个文件打包为zip下载'
                    },
                },
                'required': ['file_ids']
            },
        },
    ]

def knowledge_base_add_file_params():
    """添加文件到知识库参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'knowledge_base_id': {
                        'type': 'string',
                        'format': 'uuid',
                        'required': True,
                        'description': '知识库ID'
                    },
                    'file_ids': {
                        'type': 'array',
                        'items': {'type': 'string', 'format': 'uuid'},
                        'required': True,
                        'description': '文件ID列表'
                    },
                },
                'required': ['knowledge_base_id', 'file_ids']
            },
        },
    ]

def knowledge_base_file_list_params():
    """知识库文件列表查询参数"""
    return [
        {
            'name': 'knowledge_base_id',
            'in': 'query',
            'type': 'string',
            'format': 'uuid',
            'required': True,
            'description': '知识库ID'
        },
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'default': 1,
            'description': '页码，从1开始'
        },
        {
            'name': 'page_size',
            'in': 'query',
            'type': 'integer',
            'default': 20,
            'description': '每页数量'
        },
        {
            'name': 'file_name',
            'in': 'query',
            'type': 'string',
            'default': '',
            'description': '文件名搜索关键词'
        },
    ]

def knowledge_base_file_delete_params():
    """删除文件参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'file_ids': {
                        'type': 'array',
                        'items': {'type': 'string', 'format': 'uuid'},
                        'required': True,
                        'description': '要删除的文件ID列表'
                    },
                },
                'required': ['file_ids']
            },
        },
    ]

def knowledge_base_reference_result_params():
    """获取知识库引用结果参数"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'string',
            'format': 'uuid',
            'required': True,
            'description': '知识库ID'
        },
    ]
