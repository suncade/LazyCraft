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

"""知识库模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    KNOWLEDGE_BASE_PAGINATION_SCHEMA,
    KNOWLEDGE_BASE_SCHEMA,
    FILE_SCHEMA,
    FILE_PAGINATION_SCHEMA,
    FILE_LIST_SCHEMA,
    APP_REF_LIST_SCHEMA,
    knowledge_base_list_params,
    knowledge_base_create_params,
    knowledge_base_update_params,
    knowledge_base_delete_params,
    file_upload_params,
    file_get_params,
    file_download_params,
    knowledge_base_add_file_params,
    knowledge_base_file_list_params,
    knowledge_base_file_delete_params,
    knowledge_base_reference_result_params,
)


# ==================== 知识库相关接口 ====================

# 获取知识库列表
knowledge_base_list_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '获取知识库列表',
    'description': '分页获取用户可访问的知识库列表，支持按知识库名称、查询类型、标签、用户ID等条件筛选',
    'parameters': knowledge_base_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': KNOWLEDGE_BASE_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 创建知识库
knowledge_base_create_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '创建知识库',
    'description': '创建新的空知识库，需要写入权限',
    'parameters': knowledge_base_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': KNOWLEDGE_BASE_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新知识库
knowledge_base_update_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '更新知识库',
    'description': '更新指定知识库的名称和描述信息，需要写入权限',
    'parameters': knowledge_base_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': KNOWLEDGE_BASE_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除知识库
knowledge_base_delete_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '删除知识库',
    'description': '删除指定的知识库，需要管理员权限',
    'parameters': knowledge_base_delete_params(),
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


# ==================== 文件相关接口 ====================

# 上传文件
file_upload_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '上传文件',
    'description': '上传单个文件到系统，支持格式：.xls, .xlsx, .doc, .docx, .zip, .csv, .json, .txt, .pdf, .html, .tex, .md, .ppt, .pptx, .xml。单个文件最大50MB，zip文件最大500MB。需要写入权限',
    'parameters': file_upload_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': FILE_LIST_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取文件详情
file_get_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '获取文件详情',
    'description': '根据文件ID获取文件的详细信息',
    'parameters': file_get_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': FILE_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 下载文件
file_download_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '下载文件',
    'description': '下载单个或多个文件。单个文件直接下载，多个文件打包为zip下载',
    'parameters': file_download_params(),
    'responses': {
        **standard_error_responses(include_403=False),
        '200': {
            'description': '下载成功',
            'schema': {
                'type': 'file',
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 添加文件到知识库
knowledge_base_add_file_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '添加文件到知识库',
    'description': '将已上传的文件添加到指定的知识库中，需要对该知识库有写入权限',
    'parameters': knowledge_base_add_file_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '添加成功',
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

# 获取知识库文件列表
knowledge_base_file_list_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '获取知识库文件列表',
    'description': '分页获取指定知识库中的文件列表，同时返回知识库的基本信息，需要对该知识库有读取权限',
    'parameters': knowledge_base_file_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': FILE_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 删除文件
knowledge_base_file_delete_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '删除文件',
    'description': '批量删除知识库中的文件，需要对该知识库有管理员权限',
    'parameters': knowledge_base_file_delete_params(),
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

# 获取知识库引用结果
knowledge_base_reference_result_spec: Dict[str, Any] = {
    'tags': ['知识库管理'],
    'summary': '获取知识库引用结果',
    'description': '获取引用指定知识库的应用列表，需要对该知识库有读取权限',
    'parameters': knowledge_base_reference_result_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': APP_REF_LIST_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}
