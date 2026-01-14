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

"""全局共用 Swagger 定义。

包含所有模块共用的定义，如认证、通用错误响应、分页参数等。
"""

from copy import deepcopy
from typing import Dict, Any, List, Optional

# ==================== 认证相关 ====================

AUTH_BEARER = {'Bearer': []}
"""Bearer Token 认证定义"""

AUTH_SECURITY = [AUTH_BEARER]
"""标准安全认证列表"""

# ==================== 通用错误响应 ====================

ERROR_401 = {'description': '未授权'}
ERROR_403 = {'description': '无权限'}
ERROR_400 = {'description': '参数错误'}
ERROR_404 = {'description': '资源不存在'}
ERROR_500 = {'description': '服务器错误'}

# ==================== 通用响应组合函数 ====================

def standard_error_responses(
    include_400: bool = True,
    include_403: bool = True,
    include_404: bool = False,
    include_500: bool = False
) -> Dict[int, Dict[str, str]]:
    """生成标准错误响应字典。

    Args:
        include_400: 是否包含 400 错误
        include_403: 是否包含 403 错误
        include_404: 是否包含 404 错误
        include_500: 是否包含 500 错误

    Returns:
        包含标准错误响应的字典
    """
    responses = {
        200: {'description': '成功'},
        401: deepcopy(ERROR_401),
    }
    if include_400:
        responses[400] = deepcopy(ERROR_400)
    if include_403:
        responses[403] = deepcopy(ERROR_403)
    if include_404:
        responses[404] = deepcopy(ERROR_404)
    if include_500:
        responses[500] = deepcopy(ERROR_500)
    return responses

# ==================== 分页参数 ====================

PAGINATION_PARAMS = [
    {
        'name': 'page',
        'in': 'query',
        'type': 'integer',
        'required': False,
        'default': 1,
        'minimum': 1,
        'maximum': 99999,
        'description': '页码，从 1 开始'
    },
    {
        'name': 'limit',
        'in': 'query',
        'type': 'integer',
        'required': False,
        'default': 20,
        'minimum': 1,
        'maximum': 100,
        'description': '每页数量'
    }
]
"""标准分页参数定义"""

# ==================== UUID 路径参数 ====================

def uuid_path_param(name: str, description: str = '资源ID') -> Dict[str, Any]:
    """生成 UUID 路径参数定义。

    Args:
        name: 参数名称（如 'app_id', 'tag_id'）
        description: 参数描述

    Returns:
        路径参数定义字典
    """
    return {
        'name': name,
        'in': 'path',
        'type': 'string',
        'required': True,
        'format': 'uuid',
        'description': description
    }
