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

"""文档管理模块的 Swagger 定义"""

# ==================== Schema 定义 ====================

ACCOUNT_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'avatar': {'type': 'string'},
    },
}

DOC_DETAIL_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer', 'description': '文档ID'},
        'title': {'type': 'string', 'description': '文档标题'},
        'doc_content': {'type': 'string', 'description': '文档内容（Markdown格式）'},
        'index': {'type': 'string', 'description': '文档索引'},
        'status': {'type': 'string', 'description': '文档状态'},
        'status_label': {'type': 'string', 'description': '文档状态标签'},
        'created_by': {'type': 'string', 'description': '创建者ID'},
        'created_by_account': ACCOUNT_SCHEMA,
        'created_at': {'type': 'string', 'format': 'date-time'},
        'updated_at': {'type': 'string', 'format': 'date-time'},
    },
}

DOC_PAGINATION_SCHEMA = {
    'type': 'object',
    'properties': {
        'page': {'type': 'integer', 'description': '当前页码'},
        'limit': {'type': 'integer', 'description': '每页数量'},
        'total': {'type': 'integer', 'description': '总记录数'},
        'has_more': {'type': 'boolean', 'description': '是否有更多数据'},
        'data': {
            'type': 'array',
            'items': DOC_DETAIL_SCHEMA,
            'description': '文档列表'
        },
    },
}

DOC_UPLOAD_IMAGE_RESPONSE_SCHEMA = {
    'type': 'object',
    'properties': {
        'url': {'type': 'string', 'description': '图片访问URL'},
    },
}

# ==================== 参数定义 ====================

def doc_list_params():
    """文档列表查询参数"""
    return [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'default': 1,
            'minimum': 1,
            'maximum': 99999,
            'description': '页码，从1开始'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'default': 20,
            'minimum': 1,
            'maximum': 100,
            'description': '每页数量'
        },
        {
            'name': 'search_name',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '文档名称搜索关键词'
        },
    ]

def doc_detail_get_params():
    """获取文档详情参数"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '文档ID'
        },
    ]

def doc_create_params():
    """创建文档参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {
                        'type': 'string',
                        'required': True,
                        'description': '文档标题'
                    },
                    'doc_content': {
                        'type': 'string',
                        'required': True,
                        'description': '文档内容（Markdown格式）'
                    },
                    'index': {
                        'type': 'string',
                        'required': False,
                        'description': '文档索引'
                    },
                },
                'required': ['title', 'doc_content']
            },
        },
    ]

def doc_update_params():
    """更新文档参数"""
    return [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'required': True,
                        'description': '文档ID'
                    },
                    'title': {
                        'type': 'string',
                        'required': True,
                        'description': '文档标题'
                    },
                    'doc_content': {
                        'type': 'string',
                        'required': True,
                        'description': '文档内容（Markdown格式）'
                    },
                    'index': {
                        'type': 'string',
                        'required': False,
                        'description': '文档索引'
                    },
                },
                'required': ['id', 'title', 'doc_content']
            },
        },
    ]

def doc_delete_params():
    """删除文档参数"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '文档ID'
        },
    ]

def doc_publish_params():
    """发布文档参数"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '文档ID'
        },
    ]

def doc_unpublish_params():
    """下架文档参数"""
    return [
        {
            'name': 'id',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': '文档ID'
        },
    ]

def doc_upload_image_params():
    """上传文档图片参数"""
    return [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '要上传的图片文件'
        },
        {
            'name': 'file_name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': '文件名'
        },
    ]

def doc_image_path_param():
    """文档图片路径参数"""
    return {
        'name': 'subpath',
        'in': 'path',
        'type': 'string',
        'required': True,
        'description': '图片文件路径'
    }

def doc_view_path_param():
    """文档视图路径参数"""
    return {
        'name': 'subpath',
        'in': 'path',
        'type': 'string',
        'required': False,
        'description': '文档视图子路径，用于访问具体的文档或资源'
    }
