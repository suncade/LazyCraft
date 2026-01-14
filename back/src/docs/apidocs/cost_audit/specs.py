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

"""成本审计模块的 Swagger 规范定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import standard_error_responses
from .definitions import (
    AUTH_SECURITY,
    APP_COST_AUDIT_SCHEMA,
    STAT_COST_AUDIT_SCHEMA,
    APP_STATISTICS_SCHEMA,
    app_id_path_param,
    tenant_id_query_param,
    app_statistics_body_schema,
    calc_and_save_app_statistics_body_schema,
    daily_app_statistics_body_schema,
    cache_app_statistics_for_periods_body_schema,
    get_app_statistics_by_period_body_schema,
    query_app_statistics_body_schema,
    query_conversations_body_schema,
)


# ==================== 成本审计接口 ====================

# 查询应用成本审计
app_cost_audit_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '查询应用成本审计',
    'description': '查询指定应用的成本审计信息，包括调试和发布模式的调用次数和Token使用数',
    'parameters': [app_id_path_param()],
    'responses': {
        200: {
            'description': '成功返回应用成本审计信息',
            'schema': deepcopy(APP_COST_AUDIT_SCHEMA)
        },
        **standard_error_responses(include_404=True)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 查询费用统计
stat_cost_audit_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '查询费用统计',
    'description': '查询费用统计数据，支持按租户统计。如果有租户ID，查询该租户下所有用户的费用统计数据，否则查询当前用户的费用统计数据',
    'parameters': [tenant_id_query_param()],
    'responses': {
        200: {
            'description': '成功返回费用统计数据',
            'schema': deepcopy(STAT_COST_AUDIT_SCHEMA)
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}


# ==================== 应用统计接口 ====================

# 获取应用统计指标
app_statistics_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '获取应用统计指标',
    'description': '获取指定app_id的统计指标，优先从redis缓存读取',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(app_statistics_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '成功返回统计指标',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': deepcopy(APP_STATISTICS_SCHEMA)
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 统计并保存应用统计数据
calc_and_save_app_statistics_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '统计并保存应用统计数据',
    'description': '统计指定app_id下的各类指标，并存入AppStatistics表',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(calc_and_save_app_statistics_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '统计成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'object', 'description': '统计结果'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 每日应用统计
daily_app_statistics_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '每日应用统计',
    'description': '遍历所有app_id，统计指定日期的数据并存入AppStatistics表',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(daily_app_statistics_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '统计完成',
            'schema': {
                'type': 'object',
                'properties': {
                    'msg': {'type': 'string', 'example': '统计完成'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 缓存应用统计数据
cache_app_statistics_for_periods_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '缓存应用统计数据',
    'description': '遍历所有app_id，统计近7天、近30天的数据并缓存到redis',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(cache_app_statistics_for_periods_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '缓存完成',
            'schema': {
                'type': 'object',
                'properties': {
                    'msg': {'type': 'string', 'example': '缓存完成'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 按时间区间获取应用统计
get_app_statistics_by_period_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '按时间区间获取应用统计',
    'description': '获取指定app_id和时间区间的统计数据，优先从redis获取，未命中则实时统计',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(get_app_statistics_by_period_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '成功返回统计数据',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'object', 'description': '统计数据'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 查询应用统计
query_app_statistics_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '查询应用统计',
    'description': '查询AppStatistics表，支持按app_id、时间区间、call_type过滤',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(query_app_statistics_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '成功返回查询结果',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'array', 'description': '查询结果列表'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 查询对话记录
query_conversations_spec: Dict[str, Any] = {
    'tags': ['cost_audit'],
    'summary': '查询对话记录',
    'description': '查询Conversation表，支持按app_id、时间区间、from_who过滤',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(query_conversations_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '成功返回查询结果',
            'schema': {
                'type': 'object',
                'properties': {
                    'data': {'type': 'array', 'description': '对话记录列表'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}
