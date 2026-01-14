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

"""模型管理模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    MODEL_SCHEMA,
    MODEL_PAGINATION_SCHEMA,
    FINETUNE_PAGINATION_SCHEMA,
    model_list_params,
    model_create_params,
    model_id_path_param,
    finetune_model_id_path_param,
    model_id_body_param,
    online_model_list_params,
    delete_online_model_list_params,
    update_apikey_params,
    delete_apikey_params,
    model_update_params,
    model_delete_params,
    check_model_name_params,
    models_tree_params,
    model_info_params,
    create_finetune_params,
    finetune_model_list_params,
    update_online_model_list_params,
    upload_file_chunk_params,
    merge_file_params,
    delete_uploaded_file_params,
)


# ==================== 模型管理相关接口 ====================

# 查询模型翻页列表
model_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '查询模型翻页列表',
    'description': '根据传入的查询条件获取模型的分页列表，支持按模型类型、状态、标签、名称等条件进行筛选，需要登录',
    'parameters': model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': MODEL_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 创建新模型
model_create_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '创建新模型',
    'description': '创建新的模型，支持本地模型和在线模型，需要登录和写入权限',
    'parameters': model_create_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': MODEL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 保存在线模型列表
online_model_list_create_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '保存在线模型列表',
    'description': '保存指定基础模型的在线模型列表，需要登录和写入权限',
    'parameters': online_model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '保存成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除在线模型列表中的指定模型
online_model_list_delete_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '删除在线模型列表',
    'description': '删除在线模型列表中的指定模型，需要登录和管理员权限',
    'parameters': delete_online_model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 新增或更新 api_key
update_apikey_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '新增或更新API密钥',
    'description': '根据 model_brand 和 api_key 新增或更新 LazyModelConfigInfo 中的 api_key，需要登录和写入权限',
    'parameters': update_apikey_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'example': 'success'},
                    'result': {'type': 'object'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 清除 api_key
delete_apikey_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '清除API密钥',
    'description': '清除数据库中的 api_key，需要登录和写入权限',
    'parameters': delete_apikey_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '清除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'example': 'success'},
                    'result': {'type': 'object'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 重试下载模型
retry_download_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '重试下载模型',
    'description': '重试下载指定的模型，只支持从hf、ms导入的本地模型，需要登录',
    'parameters': [model_id_path_param()],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'boolean',
                'example': True,
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 重试下载微调模型
finetune_retry_download_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '重试下载微调模型',
    'description': '重试下载指定的微调模型，只支持本地模型，需要登录和写入权限',
    'parameters': [model_id_path_param(), finetune_model_id_path_param()],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '操作成功',
            'schema': {
                'type': 'boolean',
                'example': True,
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取模型树结构
models_tree_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取模型树结构',
    'description': '获取模型的树形结构数据，支持按模型类型、模型种类筛选，需要登录',
    'parameters': models_tree_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'description': '模型树结构数据'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新模型配置
model_update_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '更新模型配置',
    'description': '更新模型的配置信息，主要是API密钥，需要登录和写入权限',
    'parameters': model_update_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '更新成功',
            'schema': MODEL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 删除模型
model_delete_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '删除模型',
    'description': '删除指定的模型，删除前会检查模型是否被引用，需要登录和管理员权限',
    'parameters': model_delete_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 上传模型图标文件
icon_upload_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '上传模型图标',
    'description': '上传模型图标文件，支持jpg、jpeg、png、gif、bmp格式，需要登录和写入权限',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '图标文件'
        },
    ],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': '文件路径'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 上传本地模型文件分片
upload_file_chunk_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '上传文件分片',
    'description': '上传本地模型文件的分片，支持大文件分片上传，需要登录和写入权限',
    'parameters': upload_file_chunk_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': '当前分片 1/10 上传成功'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 合并本地模型文件分片
merge_file_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '合并文件分片',
    'description': '合并上传的本地模型文件分片，需要登录和写入权限',
    'parameters': merge_file_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '合并成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'description': '文件ID'},
                    'name': {'type': 'string', 'description': '文件名'},
                    'path': {'type': 'string', 'description': '文件路径'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除上传但未被引用的模型文件
delete_uploaded_file_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '删除上传文件',
    'description': '删除上传但未被引用的模型文件或分片临时目录，需要登录和写入权限',
    'parameters': delete_uploaded_file_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 检查模型名称
check_model_name_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '检查模型名称',
    'description': '检查模型名称是否合法，验证名称是否已存在，需要登录',
    'parameters': check_model_name_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '名称可用',
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

# 获取模型详细信息
model_info_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取模型信息',
    'description': '获取指定模型的详细信息，需要登录',
    'parameters': [model_id_path_param()] + model_info_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'description': '模型详细信息'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建微调模型
create_finetune_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '创建微调模型',
    'description': '创建微调模型，基于指定的基础模型，需要登录和写入权限',
    'parameters': create_finetune_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '创建成功',
            'schema': MODEL_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 删除微调模型
delete_finetune_model_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '删除微调模型',
    'description': '删除指定的微调模型，需要登录和管理员权限',
    'parameters': [model_id_path_param(), finetune_model_id_path_param()],
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取微调模型分页列表
finetune_model_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取微调模型列表',
    'description': '获取微调模型的分页列表，支持按模型ID筛选，需要登录',
    'parameters': finetune_model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': FINETUNE_PAGINATION_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}

# 获取支持的在线模型列表
online_model_support_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取在线模型支持列表',
    'description': '获取系统支持的在线模型列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'description': '在线模型信息'
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 更新在线模型列表
update_online_model_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '更新在线模型列表',
    'description': '更新指定基础模型的在线模型列表，需要登录和写入权限',
    'parameters': update_online_model_list_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'description': '更新操作的结果'
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取已存在的第三方模型列表
exist_model_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取已存在模型列表',
    'description': '获取已存在的第三方模型列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'description': '已存在的模型信息'
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取默认图标列表
default_icon_list_spec: Dict[str, Any] = {
    'tags': ['模型仓库'],
    'summary': '获取默认图标列表',
    'description': '获取系统默认的图标列表，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'string',
                    'description': '图标路径'
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}
