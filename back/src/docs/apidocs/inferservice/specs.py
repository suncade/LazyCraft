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

"""推理服务模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    SERVICE_LIST_PAGINATION_SCHEMA,
    MODEL_ITEM_SCHEMA,
    CLOUD_SERVICE_STATUS_SCHEMA,
    service_list_params,
    model_list_params,
    create_service_group_params,
    create_service_params,
    service_id_param,
    group_id_param,
    draw_service_list_params,
    ams_model_list_params,
)


# ==================== 推理服务管理相关接口 ====================

# 获取推理服务列表
service_list_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '获取推理服务列表',
    'description': '分页获取推理服务列表，支持按名称、状态、用户ID、租户等条件筛选，需要登录',
    'parameters': service_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': SERVICE_LIST_PAGINATION_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取模型列表
model_list_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '获取模型列表',
    'description': '获取可用于创建推理服务的模型列表，支持按模型类型、模型种类筛选，需要登录',
    'parameters': model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': MODEL_ITEM_SCHEMA,
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建服务组
create_service_group_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '创建服务组',
    'description': '创建推理服务组，需要登录和写入权限，需要启用推理服务功能',
    'parameters': create_service_group_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Group created successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 创建服务
create_service_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '创建服务',
    'description': '在指定服务组中创建推理服务，需要登录和写入权限，需要启用推理服务功能',
    'parameters': create_service_params(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service created successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 启动服务组
start_service_group_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '启动服务组',
    'description': '启动指定服务组中的所有服务，需要登录和写入权限，需要启用推理服务功能',
    'parameters': group_id_param(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '启动成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service started successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 关闭服务组
close_service_group_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '关闭服务组',
    'description': '关闭指定服务组中的所有服务，需要登录和写入权限',
    'parameters': group_id_param(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '关闭成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service deleted successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 启动服务
start_service_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '启动服务',
    'description': '启动指定的推理服务，需要登录和写入权限，需要启用推理服务功能',
    'parameters': service_id_param(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '启动成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service started successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 停止服务
stop_service_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '停止服务',
    'description': '停止指定的推理服务，需要登录和写入权限',
    'parameters': service_id_param(),
    'responses': {
        **standard_error_responses(include_404=True),
        '200': {
            'description': '停止成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service stopped successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 删除服务
delete_service_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '删除服务',
    'description': '删除指定的推理服务，需要登录和写入权限',
    'parameters': service_id_param(),
    'responses': {
        **standard_error_responses(include_404=True, include_500=True),
        '200': {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Service deleted successfully'},
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取画布服务列表
draw_service_list_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '获取画布服务列表',
    'description': '获取可用于画布的在线推理服务列表，支持按模型种类筛选，需要登录',
    'parameters': draw_service_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': {
                        'type': 'object',
                        'properties': {
                            'result': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': '服务ID'},
                                        'name': {'type': 'string', 'description': '服务名称'},
                                        'model_name': {'type': 'string', 'description': '模型名称'},
                                        'status': {'type': 'string', 'description': '服务状态'},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取AMS模型列表
ams_model_list_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '获取AMS模型列表',
    'description': '获取AMS支持的本地模型列表，包括微调模型，需要登录',
    'parameters': ams_model_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'array',
                'items': MODEL_ITEM_SCHEMA,
            },
        },
    },
    'security': AUTH_SECURITY,
}

# 获取云服务状态
cloud_service_status_spec: Dict[str, Any] = {
    'tags': ['推理服务'],
    'summary': '获取云服务状态',
    'description': '查询cloud-service的启用状态，需要登录',
    'parameters': [],
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': CLOUD_SERVICE_STATUS_SCHEMA,
        },
    },
    'security': AUTH_SECURITY,
}
