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

"""Swagger 文档辅助函数库。

提供快速创建常用 Swagger 定义的辅助函数。
"""

from copy import deepcopy
from typing import Dict, Any, List, Optional, Union

from .common_definitions import AUTH_SECURITY, standard_error_responses


def create_list_spec(
    tag: str,
    summary: str,
    description: str,
    item_schema: Dict[str, Any],
    params: Optional[List[Dict[str, Any]]] = None,
    include_pagination: bool = False,
    custom_responses: Optional[Dict[int, Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """快速创建列表接口 spec。

    Args:
        tag: API 标签
        summary: API 摘要
        description: API 详细描述
        item_schema: 列表项 schema
        params: 额外查询参数
        include_pagination: 是否包含分页参数
        custom_responses: 自定义响应（会合并到标准响应中）

    Returns:
        完整的 Swagger spec 字典
    """
    from .common_definitions import PAGINATION_PARAMS

    parameters = []
    if include_pagination:
        parameters.extend(deepcopy(PAGINATION_PARAMS))
    if params:
        parameters.extend(deepcopy(params))

    responses = {
        200: {
            'description': '成功返回列表',
            'schema': {
                'type': 'array',
                'items': deepcopy(item_schema)
            }
        },
        **standard_error_responses(include_400=False)
    }
    if custom_responses:
        responses.update(custom_responses)

    return {
        'tags': [tag],
        'summary': summary,
        'description': description,
        'parameters': parameters,
        'responses': responses,
        'security': deepcopy(AUTH_SECURITY)
    }


def create_detail_spec(
    tag: str,
    summary: str,
    description: str,
    path_param: Dict[str, Any],
    response_schema: Dict[str, Any],
    method: str = 'GET',
    custom_responses: Optional[Dict[int, Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """快速创建详情接口 spec。

    Args:
        tag: API 标签
        summary: API 摘要
        description: API 详细描述
        path_param: 路径参数定义
        response_schema: 响应 schema
        method: HTTP 方法
        custom_responses: 自定义响应

    Returns:
        完整的 Swagger spec 字典
    """
    responses = {
        200: {
            'description': '成功返回详情',
            'schema': deepcopy(response_schema)
        },
        **standard_error_responses(include_400=False, include_404=True)
    }
    if custom_responses:
        responses.update(custom_responses)

    return {
        'tags': [tag],
        'summary': summary,
        'description': description,
        'parameters': [deepcopy(path_param)],
        'responses': responses,
        'security': deepcopy(AUTH_SECURITY)
    }


def create_create_spec(
    tag: str,
    summary: str,
    description: str,
    body_schema: Dict[str, Any],
    response_schema: Optional[Dict[str, Any]] = None,
    custom_responses: Optional[Dict[int, Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """快速创建创建接口 spec。

    Args:
        tag: API 标签
        summary: API 摘要
        description: API 详细描述
        body_schema: 请求体 schema
        response_schema: 响应 schema（默认与 body_schema 相同）
        custom_responses: 自定义响应

    Returns:
        完整的 Swagger spec 字典
    """
    if response_schema is None:
        response_schema = deepcopy(body_schema)

    responses = {
        200: {
            'description': '成功创建',
            'schema': deepcopy(response_schema)
        },
        **standard_error_responses()
    }
    if custom_responses:
        responses.update(custom_responses)

    return {
        'tags': [tag],
        'summary': summary,
        'description': description,
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': deepcopy(body_schema)
            }
        ],
        'responses': responses,
        'security': deepcopy(AUTH_SECURITY)
    }


def create_update_spec(
    tag: str,
    summary: str,
    description: str,
    path_param: Dict[str, Any],
    body_schema: Dict[str, Any],
    response_schema: Optional[Dict[str, Any]] = None,
    custom_responses: Optional[Dict[int, Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """快速创建更新接口 spec。

    Args:
        tag: API 标签
        summary: API 摘要
        description: API 详细描述
        path_param: 路径参数定义
        body_schema: 请求体 schema
        response_schema: 响应 schema（默认与 body_schema 相同）
        custom_responses: 自定义响应

    Returns:
        完整的 Swagger spec 字典
    """
    if response_schema is None:
        response_schema = deepcopy(body_schema)

    responses = {
        200: {
            'description': '成功更新',
            'schema': deepcopy(response_schema)
        },
        **standard_error_responses(include_404=True)
    }
    if custom_responses:
        responses.update(custom_responses)

    return {
        'tags': [tag],
        'summary': summary,
        'description': description,
        'parameters': [
            deepcopy(path_param),
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': deepcopy(body_schema)
            }
        ],
        'responses': responses,
        'security': deepcopy(AUTH_SECURITY)
    }


def create_delete_spec(
    tag: str,
    summary: str,
    description: str,
    path_param: Dict[str, Any],
    custom_responses: Optional[Dict[int, Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """快速创建删除接口 spec。

    Args:
        tag: API 标签
        summary: API 摘要
        description: API 详细描述
        path_param: 路径参数定义
        custom_responses: 自定义响应

    Returns:
        完整的 Swagger spec 字典
    """
    responses = {
        200: {
            'description': '成功删除',
            'schema': {'type': 'object'}
        },
        **standard_error_responses(include_404=True)
    }
    if custom_responses:
        responses.update(custom_responses)

    return {
        'tags': [tag],
        'summary': summary,
        'description': description,
        'parameters': [deepcopy(path_param)],
        'responses': responses,
        'security': deepcopy(AUTH_SECURITY)
    }


def create_query_param(
    name: str,
    param_type: str = 'string',
    required: bool = False,
    description: str = '',
    enum: Optional[List[str]] = None,
    default: Optional[Union[str, int, bool]] = None,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None
) -> Dict[str, Any]:
    """创建查询参数定义。

    Args:
        name: 参数名称
        param_type: 参数类型（string, integer, boolean 等）
        required: 是否必填
        description: 参数描述
        enum: 枚举值列表
        default: 默认值
        minimum: 最小值（用于 integer）
        maximum: 最大值（用于 integer）

    Returns:
        查询参数定义字典
    """
    param = {
        'name': name,
        'in': 'query',
        'type': param_type,
        'required': required,
        'description': description
    }
    if enum is not None:
        param['enum'] = enum
    if default is not None:
        param['default'] = default
    if minimum is not None:
        param['minimum'] = minimum
    if maximum is not None:
        param['maximum'] = maximum
    return param
