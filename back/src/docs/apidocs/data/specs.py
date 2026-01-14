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

"""数据集模块的 Swagger 规范定义（分批生成）"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import standard_error_responses
from .definitions import (
    AUTH_SECURITY,
    PAGINATION_SCHEMA,
    SCRIPT_FIELD_SCHEMA,
    DATA_SET_FIELD_SCHEMA,
    DATA_SET_VERSION_FIELD_SCHEMA,
    DATA_SET_FILE_FIELD_SCHEMA,
    REFLUX_DATA_FIELD_SCHEMA,
    pagination_params,
    PAGINATION_BODY_REQUEST_SCHEMA,
    COMMON_QUERY_BODY_REQUEST_SCHEMA,
    common_query_params,
    DATA_TYPE_ENUM,
    UPLOAD_TYPE_ENUM,
    VERSION_TYPE_ENUM,
    SCRIPT_TYPE_ENUM,
    SCRIPT_AGENT_ENUM,
)


# ==================== 脚本相关接口 ====================

# 脚本列表
script_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取脚本列表',
    'description': '获取脚本分页列表，支持按脚本类型、名称、标签等条件筛选',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    **deepcopy(PAGINATION_BODY_REQUEST_SCHEMA['properties']),
                    'script_type': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '脚本类型列表'
                    },
                    'name': {'type': 'string', 'description': '脚本名称'},
                    **deepcopy(COMMON_QUERY_BODY_REQUEST_SCHEMA['properties']),
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回脚本分页列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {'type': 'integer'},
                    'page_size': {'type': 'integer'},
                    'total': {'type': 'integer'},
                    'has_more': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': deepcopy(SCRIPT_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建脚本
script_create_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '创建脚本',
    'description': '创建新的脚本',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': '脚本名称'},
                    'description': {'type': 'string', 'description': '脚本描述'},
                    'icon': {'type': 'string', 'description': '脚本图标'},
                    'script_url': {'type': 'string', 'description': '脚本URL'},
                    'script_type': {'type': 'string', 'description': '脚本类型'},
                    'data_type': {'type': 'string', 'enum': DATA_TYPE_ENUM, 'description': '数据类型'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建脚本',
            'schema': deepcopy(SCRIPT_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除脚本
script_delete_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '删除脚本',
    'description': '删除指定的脚本',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'script_id': {'type': 'integer', 'description': '脚本ID'}
                },
                'required': ['script_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 上传脚本
script_upload_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '上传脚本文件',
    'description': '上传脚本文件（.py格式），文件大小不能超过1MB',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '脚本文件（.py格式）'
        }
    ],
    'responses': {
        200: {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': '文件路径'},
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新脚本
script_update_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '更新脚本',
    'description': '更新指定脚本的信息',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'script_id': {'type': 'integer', 'description': '脚本ID'},
                    'name': {'type': 'string', 'description': '脚本名称'},
                    'description': {'type': 'string', 'description': '脚本描述'},
                    'icon': {'type': 'string', 'description': '脚本图标'},
                    'script_url': {'type': 'string', 'description': '脚本URL'},
                    'script_type': {'type': 'string', 'description': '脚本类型'},
                    'data_type': {'type': 'string', 'enum': DATA_TYPE_ENUM, 'description': '数据类型'}
                },
                'required': ['script_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '更新成功',
            'schema': deepcopy(SCRIPT_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 按类型获取脚本列表
script_list_by_type_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '按类型获取脚本列表',
    'description': '根据脚本类型获取脚本列表',
    'parameters': [
        {
            'name': 'script_type',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '脚本类型'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回脚本列表',
            'schema': {
                'type': 'array',
                'items': deepcopy(SCRIPT_FIELD_SCHEMA)
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}


# ==================== 数据集相关接口（第一批） ====================

# 数据集列表
data_set_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集列表',
    'description': '获取数据集分页列表，支持按名称、数据类型、标签等条件筛选',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    **deepcopy(PAGINATION_BODY_REQUEST_SCHEMA['properties']),
                    'name': {'type': 'string', 'description': '数据集名称'},
                    'data_type': {
                        'type': 'array',
                        'items': {'type': 'string', 'enum': DATA_TYPE_ENUM},
                        'description': '数据类型列表'
                    },
                    **deepcopy(COMMON_QUERY_BODY_REQUEST_SCHEMA['properties']),
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集分页列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {'type': 'integer'},
                    'page_size': {'type': 'integer'},
                    'total': {'type': 'integer'},
                    'has_more': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': deepcopy(DATA_SET_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建数据集
data_set_create_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '创建数据集',
    'description': '创建新的数据集，支持本地上传或URL上传',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': '数据集名称'},
                    'description': {'type': 'string', 'description': '数据集描述'},
                    'data_type': {'type': 'string', 'enum': DATA_TYPE_ENUM, 'description': '数据类型（doc或pic）'},
                    'upload_type': {'type': 'string', 'enum': UPLOAD_TYPE_ENUM, 'description': '上传类型（local或url）'},
                    'file_paths': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '本地文件路径列表（upload_type为local时必填）'
                    },
                    'file_urls': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '文件URL列表（upload_type为url时必填）'
                    },
                    'data_format': {'type': 'string', 'description': '数据格式'},
                    'from_type': {'type': 'string', 'description': '来源类型'}
                },
                'required': ['name', 'data_type', 'upload_type']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建数据集',
            'schema': deepcopy(DATA_SET_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 上传数据集文件
upload_data_set_file_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '上传数据集文件',
    'description': '上传数据集文件，支持图片和文档类型，支持压缩包',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': '上传的文件'
        },
        {
            'name': 'file_type',
            'in': 'formData',
            'type': 'string',
            'enum': DATA_TYPE_ENUM,
            'required': True,
            'description': '文件类型（pic或doc）'
        }
    ],
    'responses': {
        200: {
            'description': '上传成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': '文件路径'},
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据集版本列表
data_set_version_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集版本列表',
    'description': '获取指定数据集的版本分页列表',
    'parameters': [
        *pagination_params(),
        {
            'name': 'version_type',
            'in': 'query',
            'type': 'string',
            'enum': VERSION_TYPE_ENUM,
            'required': False,
            'description': '版本类型'
        },
        {
            'name': 'data_set_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '数据集ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集版本分页列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {'type': 'integer'},
                    'page_size': {'type': 'integer'},
                    'total': {'type': 'integer'},
                    'has_more': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据集文件列表
data_set_file_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集文件列表',
    'description': '获取指定数据集版本下的文件分页列表',
    'parameters': [
        *pagination_params(),
        {
            'name': 'data_set_version_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '数据集版本ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集文件分页列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {'type': 'integer'},
                    'page_size': {'type': 'integer'},
                    'total': {'type': 'integer'},
                    'has_more': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': deepcopy(DATA_SET_FILE_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据集标签列表
data_set_tag_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集标签列表',
    'description': '获取数据集的标签版本列表',
    'parameters': [
        {
            'name': 'data_set_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '数据集ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集标签列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 根据标签创建数据集版本
create_data_set_version_by_tag_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '根据标签创建数据集版本',
    'description': '基于标签版本创建新的分支版本',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'},
                    'name': {'type': 'string', 'description': '新版本名称'}
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功创建数据集版本',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 发布数据集版本
data_set_version_publish_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '发布数据集版本',
    'description': '发布数据集版本为标签版本',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'}
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功发布数据集版本',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取数据集文件内容
data_set_file_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集文件内容',
    'description': '获取JSON文件内容并返回给前端，支持分页读取',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_file_id': {'type': 'string', 'description': '数据集文件ID'},
                    'start': {'type': 'integer', 'description': '起始行号'},
                    'end': {'type': 'integer', 'description': '结束行号'}
                },
                'required': ['data_set_file_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '成功返回文件内容',
            'schema': {
                'type': 'object',
                'description': '文件内容'
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新数据集文件
data_set_file_update_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '更新数据集文件',
    'description': '修改数据集文件内容',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_file_id': {'type': 'string', 'description': '数据集文件ID'},
                    'content': {'type': 'string', 'description': '新的文件内容'},
                    'data_set_file_name': {'type': 'string', 'description': '新的文件名'},
                    'start': {'type': 'integer', 'description': '起始行号'},
                    'end': {'type': 'integer', 'description': '结束行号'}
                },
                'required': ['data_set_file_id', 'content']
            }
        }
    ],
    'responses': {
        200: {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                    'data': {
                        'type': 'object',
                        'properties': {
                            'total': {'type': 'integer', 'description': '新的总行数'}
                        }
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取数据集详情
data_set_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集详情',
    'description': '获取指定数据集的详细信息',
    'parameters': [
        {
            'name': 'data_set_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '数据集ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集详情',
            'schema': deepcopy(DATA_SET_FIELD_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取数据集版本详情
data_set_version_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据集版本详情',
    'description': '获取指定数据集版本的详细信息',
    'parameters': [
        {
            'name': 'data_set_version_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '数据集版本ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回数据集版本详情',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除数据集
data_set_delete_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '删除数据集',
    'description': '删除指定的数据集',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_id': {'type': 'string', 'description': '数据集ID'}
                },
                'required': ['data_set_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除数据集版本
data_set_version_delete_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '删除数据集版本',
    'description': '删除指定的数据集版本',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'}
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200},
                    'count': {'type': 'integer', 'description': '剩余版本数量'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除数据集文件
data_set_file_delete_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '删除数据集文件',
    'description': '删除指定的数据集文件',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_file_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': '数据集文件ID列表'
                    }
                },
                'required': ['data_set_file_ids']
            }
        }
    ],
    'responses': {
        200: {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据集版本添加文件
data_set_version_add_file_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '数据集版本添加文件',
    'description': '向数据集版本添加新文件',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'},
                    'name': {'type': 'string', 'description': '版本名称'},
                    'version': {'type': 'string', 'description': '版本号'},
                    'file_paths': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '本地文件路径列表'
                    },
                    'file_urls': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '文件URL列表'
                    }
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '添加成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导出数据集版本
data_set_version_export_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '导出数据集版本',
    'description': '导出一个或多个数据集版本，返回压缩文件',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_ids': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '数据集版本ID列表'
                    }
                },
                'required': ['data_set_version_ids']
            }
        }
    ],
    'responses': {
        200: {
            'description': '导出成功，返回压缩文件',
            'schema': {
                'type': 'file',
                'description': '压缩文件下载'
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导出数据集版本（微调专用）
data_set_version_export_ft_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '导出数据集版本（微调专用）',
    'description': '导出数据集版本文件，用于微调',
    'parameters': [
        {
            'name': 'filename',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '文件路径'
        },
        {
            'name': 'filefrom',
            'in': 'query',
            'type': 'string',
            'enum': ['upload', 'return'],
            'required': True,
            'description': '文件来源（upload或return）'
        }
    ],
    'responses': {
        200: {
            'description': '导出成功，返回文件下载',
            'schema': {
                'type': 'file',
                'description': '文件下载'
            }
        },
        **standard_error_responses()
    },
    'security': []
}

# 测试数据集版本状态
test_data_set_version_status_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '测试数据集版本状态',
    'description': '测试数据集版本状态变更功能',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'}
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '状态变更成功',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据集版本清洗或增强
clean_or_augment_data_set_version_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '数据集版本清洗或增强',
    'description': '对数据集版本进行数据清洗或增强处理',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'},
                    'data_set_script_id': {'type': 'string', 'description': '数据集脚本ID'},
                    'script_agent': {'type': 'string', 'enum': SCRIPT_AGENT_ENUM, 'default': 'script', 'description': '脚本代理类型'},
                    'script_type': {'type': 'string', 'enum': SCRIPT_TYPE_ENUM, 'description': '脚本类型'},
                    'data_set_version_name': {'type': 'string', 'description': '数据集版本名称'}
                },
                'required': ['data_set_version_id', 'data_set_script_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '处理成功',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 异步数据集版本清洗或增强
clean_or_augment_data_set_version_async_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '异步数据集版本清洗或增强',
    'description': '异步启动数据集版本的数据清洗或增强处理',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'},
                    'data_set_script_id': {'type': 'string', 'description': '数据集脚本ID'},
                    'script_agent': {'type': 'string', 'enum': SCRIPT_AGENT_ENUM, 'default': 'script', 'description': '脚本代理类型'},
                    'script_type': {'type': 'string', 'enum': SCRIPT_TYPE_ENUM, 'description': '脚本类型'},
                    'data_set_version_name': {'type': 'string', 'description': '数据集版本名称'}
                },
                'required': ['data_set_version_id', 'data_set_script_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '任务启动成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'task_id': {'type': 'string', 'description': '任务ID'},
                    'message': {'type': 'string', 'description': '提示信息'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 异步数据集版本清洗或增强（基于数据条数）
clean_or_augment_data_set_version_async_with_item_count_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '异步数据集版本清洗或增强（基于数据条数）',
    'description': '异步启动数据集版本的数据清洗或增强处理，并统计数据条数',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'},
                    'data_set_script_id': {'type': 'string', 'description': '数据集脚本ID'},
                    'script_agent': {'type': 'string', 'enum': SCRIPT_AGENT_ENUM, 'default': 'script', 'description': '脚本代理类型'},
                    'script_type': {'type': 'string', 'enum': SCRIPT_TYPE_ENUM, 'description': '脚本类型'},
                    'data_set_version_name': {'type': 'string', 'description': '数据集版本名称'}
                },
                'required': ['data_set_version_id', 'data_set_script_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '任务启动成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'task_id': {'type': 'string', 'description': '任务ID'},
                    'message': {'type': 'string', 'description': '提示信息'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据处理任务进度
data_processing_task_progress_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据处理任务进度',
    'description': '获取指定数据处理任务的进度信息',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '任务ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回任务进度',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'description': '任务状态'},
                    'progress': {'type': 'number', 'description': '进度百分比'},
                    'message': {'type': 'string', 'description': '进度信息'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 取消数据处理任务
data_processing_task_cancel_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '取消数据处理任务',
    'description': '取消指定的数据处理任务',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '任务ID'
        }
    ],
    'responses': {
        200: {
            'description': '取消成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'message': {'type': 'string', 'example': '任务已取消'}
                }
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据处理任务列表
data_processing_task_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取数据处理任务列表',
    'description': '获取所有数据处理任务的列表',
    'parameters': [],
    'responses': {
        200: {
            'description': '成功返回任务列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'tasks': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '任务列表'
                    },
                    'total': {'type': 'integer', 'description': '任务总数'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 数据处理任务流式进度
data_processing_task_stream_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '数据处理任务流式进度',
    'description': '通过SSE实时推送任务进度',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': '任务ID'
        }
    ],
    'responses': {
        200: {
            'description': 'SSE流式响应，实时推送任务进度',
            'schema': {
                'type': 'string',
                'format': 'text/event-stream'
            }
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}


# ==================== 回流数据相关接口 ====================

# 应用发布回流
reflux_app_publish_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '应用发布回流',
    'description': '处理应用发布时的数据回流',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'app_msg': {'type': 'object', 'description': '应用消息数据'},
                    'node_msgs': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': '节点消息数据列表'
                    }
                },
                'required': ['app_msg', 'node_msgs']
            }
        }
    ],
    'responses': {
        200: {
            'description': '回流成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 创建回流数据
reflux_data_create_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '创建回流数据',
    'description': '创建回流数据',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'object', 'description': '回流数据'}
                },
                'required': ['data']
            }
        }
    ],
    'responses': {
        200: {
            'description': '创建成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新回流数据反馈
reflux_data_update_feedback_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '更新回流数据反馈',
    'description': '更新回流数据的反馈信息',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'object', 'description': '反馈数据'}
                },
                'required': ['data']
            }
        }
    ],
    'responses': {
        200: {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses()
    },
    'security': []
}

# 数据集版本发布回流
reflux_data_set_version_publish_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '数据集版本发布回流',
    'description': '发布数据集版本回流数据',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_id': {'type': 'string', 'description': '数据集版本ID'}
                },
                'required': ['data_set_version_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '发布成功',
            'schema': deepcopy(DATA_SET_VERSION_FIELD_SCHEMA)
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 回流数据列表
reflux_data_list_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取回流数据列表',
    'description': '获取回流数据分页列表',
    'parameters': [
        *pagination_params(),
        {
            'name': 'data_set_version_id',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': '数据集版本ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回回流数据分页列表',
            'schema': {
                'type': 'object',
                'properties': {
                    'page': {'type': 'integer'},
                    'page_size': {'type': 'integer'},
                    'total': {'type': 'integer'},
                    'has_more': {'type': 'boolean'},
                    'data': {
                        'type': 'array',
                        'items': deepcopy(REFLUX_DATA_FIELD_SCHEMA)
                    }
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 回流数据详情
reflux_data_detail_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '获取回流数据详情',
    'description': '获取回流数据的详细信息',
    'parameters': [
        {
            'name': 'reflux_data_id',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '回流数据ID'
        }
    ],
    'responses': {
        200: {
            'description': '成功返回回流数据详情',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'object',
                        'properties': {
                            'content': {'type': 'object', 'description': '回流数据内容'},
                            'id': {'type': 'string', 'description': '回流数据ID'}
                        }
                    },
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 删除回流数据
reflux_data_delete_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '删除回流数据',
    'description': '删除指定的回流数据',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'reflux_data_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': '要删除的回流数据ID列表'
                    }
                },
                'required': ['reflux_data_ids']
            }
        }
    ],
    'responses': {
        200: {
            'description': '删除成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新回流数据
reflux_data_update_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '更新回流数据',
    'description': '修改回流数据内容',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'reflux_data_id': {'type': 'string', 'description': '回流数据ID'},
                    'content': {'type': 'string', 'description': '更新内容'}
                },
                'required': ['reflux_data_id', 'content']
            }
        }
    ],
    'responses': {
        200: {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'success'},
                    'code': {'type': 'integer', 'example': 200}
                }
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导出数据集版本（回流）
reflux_data_set_version_export_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '导出数据集版本（回流）',
    'description': '导出数据集版本，返回压缩文件',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'data_set_version_ids': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': '数据集版本ID列表'
                    }
                },
                'required': ['data_set_version_ids']
            }
        }
    ],
    'responses': {
        200: {
            'description': '导出成功，返回压缩文件',
            'schema': {
                'type': 'file',
                'description': '压缩文件下载'
            }
        },
        **standard_error_responses()
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 导出数据集版本（回流，微调专用）
reflux_data_set_version_export_for_ft_spec: Dict[str, Any] = {
    'tags': ['数据集'],
    'summary': '导出数据集版本（回流，微调专用）',
    'description': '导出数据集版本文件，用于微调',
    'parameters': [
        {
            'name': 'filename',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': '数据集文件名'
        }
    ],
    'responses': {
        200: {
            'description': '导出成功，返回文件下载',
            'schema': {
                'type': 'file',
                'description': '文件下载'
            }
        },
        **standard_error_responses()
    },
    'security': []
}
