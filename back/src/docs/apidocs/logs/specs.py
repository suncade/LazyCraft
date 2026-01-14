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

"""操作日志模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses
from .definitions import (
    LOG_LIST_PAGINATION_SCHEMA,
    log_list_params,
)


# ==================== 操作日志管理相关接口 ====================

# 获取操作日志列表
log_list_spec: Dict[str, Any] = {
    'tags': ['操作日志'],
    'summary': '获取操作日志列表',
    'description': '查询用户的操作日志，支持按日期、用户、模块、动作等条件筛选。所有时间参数均为北京时间（Asia/Shanghai），系统会自动转换为 UTC 进行查询。只有管理员才有权查看其他用户的操作日志，普通用户只能查看自己的日志，需要登录',
    'parameters': log_list_params(),
    'responses': {
        **standard_error_responses(),
        '200': {
            'description': '获取成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'code': {'type': 'integer', 'example': 200},
                    'data': LOG_LIST_PAGINATION_SCHEMA,
                },
            },
        },
    },
    'security': AUTH_SECURITY,
}
