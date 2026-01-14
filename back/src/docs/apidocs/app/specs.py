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

"""应用管理模块所有接口的 Swagger 定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from ..helpers import create_list_spec, create_detail_spec, create_create_spec, create_query_param
from .definitions import (
    APP_OBJECT_SCHEMA,
    APP_PAGINATION_SCHEMA,
    WORKFLOW_OBJECT_SCHEMA,
    app_id_path_param,
    mode_path_param,
    app_list_query_params,
    app_list_page_body_schema,
    app_create_body_schema,
)

# ==================== 应用基础管理接口 ====================

# 获取应用列表
app_list_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取应用列表',
    'description': '根据查询参数获取应用的分页列表，支持按名称、标签、发布状态等条件筛选',
    'parameters': app_list_query_params(),
    'responses': {
        200: {
            'description': '成功返回应用列表',
            'schema': deepcopy(APP_PAGINATION_SCHEMA)
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取应用列表（分页版本）
app_list_page_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取应用列表（分页）',
    'description': '使用POST方式获取应用的分页列表，支持更复杂的查询参数',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': app_list_page_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功返回应用列表',
            'schema': deepcopy(APP_PAGINATION_SCHEMA)
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建应用
app_create_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '创建应用',
    'description': '创建空白的应用',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': app_create_body_schema()
        }
    ],
    'responses': {
        201: {
            'description': '成功创建应用',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取应用详情
app_detail_get_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取应用详情',
    'description': '根据应用ID获取应用详细信息',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回应用详情',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新应用信息
app_detail_put_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '更新应用信息',
    'description': '更新应用的基本信息',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': app_create_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功更新应用',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除应用
app_detail_delete_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '删除应用',
    'description': '删除指定的应用',
    'parameters': [app_id_path_param()],
    'responses': {
        204: {'description': '成功删除'},
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 应用功能接口 ====================

# 启用/禁用应用服务
app_enable_api_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '启用/禁用应用服务',
    'description': '启用或禁用应用的API服务，返回SSE流式响应',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'enable_api': {'type': 'boolean', 'description': '是否启用API服务'}
                },
                'required': ['enable_api']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 启用/禁用数据回流
app_enable_backflow_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '启用/禁用数据回流',
    'description': '启用或禁用应用的数据回流功能',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'enable_backflow': {'type': 'boolean', 'description': '是否启用回流功能'}
                },
                'required': ['enable_backflow']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功更新',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 启用/禁用API调用
app_enable_api_call_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '启用/禁用API调用',
    'description': '启用或禁用应用的API调用功能',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'enable_api_call': {'type': 'string', 'description': 'API调用开关：0或1'}
                },
                'required': ['enable_api_call']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功更新',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导出应用
app_export_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '导出应用',
    'description': '导出应用为文件',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回导出文件',
            'schema': {'type': 'file'}
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导入应用
app_import_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '导入应用',
    'description': '从文件导入应用',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '应用文件'
        }
    ],
    'responses': {
        200: {
            'description': '成功导入应用',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 转换为模板
app_convert_to_template_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '转换为模板',
    'description': '将应用转换为模板',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'}
                },
                'required': ['app_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功转换',
            'schema': {'type': 'object'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 模板管理接口 ====================

# 获取模板列表
template_list_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取模板列表',
    'description': '获取应用模板列表',
    'parameters': [
        *app_list_query_params()
    ],
    'responses': {
        200: {
            'description': '成功返回模板列表',
            'schema': deepcopy(APP_PAGINATION_SCHEMA)
        },
        **standard_error_responses(include_400=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取模板详情
template_detail_get_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取模板详情',
    'description': '根据模板ID获取模板详细信息',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回模板详情',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新模板信息
template_detail_put_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '更新模板信息',
    'description': '更新模板的基本信息',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': app_create_body_schema()
        }
    ],
    'responses': {
        200: {
            'description': '成功更新模板',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除模板
template_detail_delete_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '删除模板',
    'description': '删除指定的模板',
    'parameters': [app_id_path_param()],
    'responses': {
        204: {'description': '成功删除'},
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 兼容旧名称
template_detail_spec = template_detail_get_spec

# 模板转换为应用
template_convert_to_app_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '模板转换为应用',
    'description': '将模板转换为应用',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '模板ID'}
                },
                'required': ['app_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功转换',
            'schema': deepcopy(APP_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 工作流相关接口 ====================

# 获取草稿工作流
draft_workflow_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取草稿工作流',
    'description': '获取应用的草稿工作流',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回工作流',
            'schema': deepcopy(WORKFLOW_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 同步草稿工作流
draft_workflow_post_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '同步草稿工作流',
    'description': '同步草稿工作流的配置',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'graph': {'type': 'object', 'description': '工作流图配置'},
                    'hash': {'type': 'string', 'description': '工作流哈希值'}
                },
                'required': ['graph']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功同步',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string'},
                    'hash': {'type': 'string'},
                    'updated_at': {'type': 'string', 'format': 'date-time'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取草稿工作流状态
draft_workflow_status_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取草稿工作流状态',
    'description': '查询草稿调试的状态',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回状态',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'description': '状态：running/stop'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 开始草稿调试
draft_workflow_start_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '开始草稿调试',
    'description': '开始草稿调试，返回SSE流式响应',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 运行草稿工作流
draft_workflow_run_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '运行草稿工作流',
    'description': '运行草稿工作流进行预览',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'inputs': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '输入内容列表'
                    },
                    'files': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '文件列表'
                    }
                },
                'required': ['inputs']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 停止草稿工作流
draft_workflow_stop_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '停止草稿工作流',
    'description': '停止草稿调试',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 重置草稿会话
draft_workflow_reset_session_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '重置草稿会话',
    'description': '重置草稿工作流的会话',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {'description': '成功重置', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取发布工作流
published_workflow_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取发布工作流',
    'description': '获取已发布的工作流',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回工作流',
            'schema': deepcopy(WORKFLOW_OBJECT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 发布工作流
published_workflow_post_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '发布工作流',
    'description': '发布草稿工作流为正式版本',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'version': {'type': 'string', 'description': '版本号'},
                    'description': {'type': 'string', 'description': '版本描述'}
                },
                'required': ['version', 'description']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功发布',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string'},
                    'publish_at': {'type': 'string', 'format': 'date-time'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 取消发布
cancel_publish_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '取消发布',
    'description': '取消已发布的工作流',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {'description': '成功取消发布', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 调试相关接口 ====================

# 获取调试详情
draft_debug_detail_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取调试详情',
    'description': '获取应用的调试详情',
    'parameters': [
        app_id_path_param(),
        mode_path_param()
    ],
    'responses': {
        200: {
            'description': '成功返回调试详情',
            'schema': {'type': 'object'}
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 调试详情流式响应
draft_debug_detail_stream_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '调试详情流式响应',
    'description': '获取调试详情的SSE流式响应',
    'parameters': [
        app_id_path_param(),
        mode_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'inputs': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '输入内容列表'
                    },
                    'files': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '文件列表'
                    }
                },
                'required': ['inputs']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取调试历史
draft_debug_detail_history_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取调试历史',
    'description': '获取调试历史记录',
    'parameters': [
        app_id_path_param(),
        mode_path_param()
    ],
    'responses': {
        200: {
            'description': '成功返回历史记录',
            'schema': {
                'type': 'array',
                'items': {'type': 'object'}
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除调试历史
draft_debug_detail_history_delete_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '删除调试历史',
    'description': '删除指定的调试历史记录',
    'parameters': [
        app_id_path_param(),
        mode_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'history_id': {'type': 'string', 'description': '历史记录ID'}
                },
                'required': ['history_id']
            }
        }
    ],
    'responses': {
        200: {'description': '成功删除', 'schema': {'type': 'object'}},
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 停止调试流
draft_debug_detail_stream_stop_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '停止调试流',
    'description': '停止调试的流式响应',
    'parameters': [
        app_id_path_param(),
        mode_path_param()
    ],
    'responses': {
        200: {'description': '成功停止', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取调试流状态
draft_debug_detail_stream_status_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取调试流状态',
    'description': '获取调试流的运行状态',
    'parameters': [
        app_id_path_param(),
        mode_path_param()
    ],
    'responses': {
        200: {
            'description': '成功返回状态',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'description': '状态'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# ==================== 其他接口 ====================

# 应用报告
app_report_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '应用报告',
    'description': '获取应用的使用报告',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'},
                    'start_date': {'type': 'string', 'format': 'date', 'description': '开始日期'},
                    'end_date': {'type': 'string', 'format': 'date', 'description': '结束日期'}
                },
                'required': ['app_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回报告',
            'schema': {'type': 'object'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 应用版本
app_version_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取应用版本',
    'description': '获取应用的版本列表',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回版本列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string'},
                                'version': {'type': 'string'},
                                'description': {'type': 'string'},
                                'release_time': {'type': 'string', 'format': 'date-time'}
                            }
                        }
                    }
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 恢复应用版本
app_restore_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '恢复应用版本',
    'description': '恢复到指定的应用版本',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'version_id': {'type': 'string', 'description': '版本ID'}
                },
                'required': ['version_id']
            }
        }
    ],
    'responses': {
        200: {'description': '成功恢复', 'schema': {'type': 'object'}},
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 检查版本数量
check_versions_count_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '检查版本数量',
    'description': '检查应用的版本数量',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回版本数量',
            'schema': {
                'type': 'object',
                'properties': {
                    'count': {'type': 'integer', 'description': '版本数量'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 引用结果
reference_result_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '获取引用结果',
    'description': '获取应用的引用结果',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回引用结果',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'string'},
                        'name': {'type': 'string'},
                        'is_public': {'type': 'boolean'}
                    }
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 从文件导入草稿
draft_import_from_file_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '从文件导入草稿',
    'description': '从文件导入草稿工作流',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '工作流文件'
        }
    ],
    'responses': {
        200: {'description': '成功导入', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 节点运行流
node_run_stream_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '节点运行流',
    'description': '运行指定节点的流式响应',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'node_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '节点ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'inputs': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '输入内容列表'
                    }
                },
                'required': ['inputs']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应',
            'schema': {'type': 'string', 'format': 'text/event-stream'}
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 从空创建工作流
new_workflow_from_empty_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '从空创建工作流',
    'description': '从空白创建新的工作流',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'}
                },
                'required': ['app_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建',
            'schema': deepcopy(WORKFLOW_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 从应用创建工作流
new_workflow_from_app_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '从应用创建工作流',
    'description': '从应用创建新的工作流',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'},
                    'target_app_id': {'type': 'string', 'format': 'uuid', 'description': '目标应用ID'}
                },
                'required': ['app_id', 'target_app_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建',
            'schema': deepcopy(WORKFLOW_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 从模板创建工作流
new_workflow_from_template_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '从模板创建工作流',
    'description': '从模板创建新的工作流',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'},
                    'template_id': {'type': 'string', 'format': 'uuid', 'description': '模板ID'}
                },
                'required': ['app_id', 'template_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建',
            'schema': deepcopy(WORKFLOW_OBJECT_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 添加工作流日志
workflow_add_log_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '添加工作流日志',
    'description': '添加工作流执行日志',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'},
                    'node_id': {'type': 'string', 'description': '节点ID'},
                    'log': {'type': 'string', 'description': '日志内容'}
                },
                'required': ['app_id', 'node_id', 'log']
            }
        }
    ],
    'responses': {
        200: {'description': '成功添加', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 批量添加工作流日志
workflow_batch_log_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '批量添加工作流日志',
    'description': '批量添加工作流执行日志',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_id': {'type': 'string', 'format': 'uuid', 'description': '应用ID'},
                    'logs': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'node_id': {'type': 'string'},
                                'log': {'type': 'string'}
                            }
                        },
                        'description': '日志列表'
                    }
                },
                'required': ['app_id', 'logs']
            }
        }
    ],
    'responses': {
        200: {'description': '成功添加', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 文档解析
doc_parse_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '文档解析',
    'description': '解析文档节点',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'doc_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '文档ID'
        }
    ],
    'responses': {
        200: {'description': '成功开始解析', 'schema': {'type': 'object'}},
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 文档解析状态
doc_parse_status_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': '文档解析状态',
    'description': '获取文档解析状态',
    'parameters': [
        app_id_path_param(),
        {
            'name': 'doc_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '文档ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回状态',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'description': '解析状态'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# AI代码助手
ai_code_assistant_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': 'AI代码助手',
    'description': '使用AI代码助手生成代码',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'prompt': {'type': 'string', 'description': '提示词'},
                    'code': {'type': 'string', 'description': '现有代码'},
                    'language': {'type': 'string', 'description': '编程语言'}
                },
                'required': ['prompt']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回代码',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'string', 'description': '生成的代码'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# AI提示词助手
ai_prompt_assistant_spec: Dict[str, Any] = {
    'tags': ['应用商店'],
    'summary': 'AI提示词助手',
    'description': '使用AI提示词助手优化提示词',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'prompt': {'type': 'string', 'description': '原始提示词'},
                    'session': {'type': 'string', 'description': '会话ID'}
                },
                'required': ['prompt']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回优化后的提示词',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'description': '优化后的提示词'},
                    'session': {'type': 'string', 'description': '会话ID'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}
