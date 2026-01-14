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

"""文档管理模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    DOC_PAGINATION_SCHEMA,
    DOC_DETAIL_SCHEMA,
    DOC_UPLOAD_IMAGE_RESPONSE_SCHEMA,
    doc_list_params,
    doc_detail_get_params,
    doc_create_params,
    doc_update_params,
    doc_delete_params,
    doc_publish_params,
    doc_unpublish_params,
    doc_upload_image_params,
    doc_image_path_param,
    doc_view_path_param,
)


# ==================== 文档管理相关接口 ====================

# 获取文档列表
doc_list_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '获取文档列表',
    'description': '分页获取文档列表，支持按文档名称搜索，不需要登录',
    'parameters': doc_list_params(),
    'responses': {
        **standard_error_responses(include_403=False),
        '200': {
            'description': '获取成功',
            'schema': DOC_PAGINATION_SCHEMA,
        },
    },
}

# 获取文档详情
doc_detail_get_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '获取文档详情',
    'description': '根据文档ID获取文档的详细信息，需要登录',
    'parameters': doc_detail_get_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': DOC_DETAIL_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建文档
doc_create_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '创建文档',
    'description': '创建新文档，需要登录和管理员权限',
    'parameters': doc_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': DOC_DETAIL_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新文档
doc_update_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '更新文档',
    'description': '更新指定文档的信息，需要登录和管理员权限',
    'parameters': doc_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': DOC_DETAIL_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除文档
doc_delete_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '删除文档',
    'description': '删除指定文档，需要登录和管理员权限',
    'parameters': doc_delete_params(),
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

# 发布文档
doc_publish_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '发布文档',
    'description': '发布指定文档，使其对外可见，需要登录',
    'parameters': doc_publish_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '发布成功',
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

# 下架文档
doc_unpublish_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '下架文档',
    'description': '下架指定文档，使其不再对外可见，需要登录',
    'parameters': doc_unpublish_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '下架成功',
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

# 上传文档图片
doc_upload_image_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '上传文档图片',
    'description': '上传文档中使用的图片文件，需要登录',
    'parameters': doc_upload_image_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '上传成功',
            'schema': DOC_UPLOAD_IMAGE_RESPONSE_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取文档图片
doc_image_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '获取文档图片',
    'description': '根据图片路径获取文档图片，不需要登录',
    'parameters': [
        doc_image_path_param(),
    ],
    'responses': {
        **standard_error_responses(include_403=False, include_404=True),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'file',
            },
        },
    },
}

# 文档视图
doc_view_spec: Dict[str, Any] = {
    'tags': ['文档管理'],
    'summary': '文档视图',
    'description': '访问文档的Web视图，支持Markdown文档渲染，不需要登录',
    'parameters': [
        doc_view_path_param(),
    ],
    'responses': {
        **standard_error_responses(include_403=False, include_404=True, include_500=True),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'string',
                'description': 'HTML页面或Markdown内容'
            },
        },
    },
}
