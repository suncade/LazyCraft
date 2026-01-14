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

"""成本审计模块的 Swagger 定义和参数"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses


# ==================== 枚举定义 ====================

# 调用类型
CALL_TYPE_ENUM = ['debug', 'release']


# ==================== Schema 定义 ====================

# 应用成本审计响应 Schema
APP_COST_AUDIT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'run_call_num': {'type': 'integer', 'description': '调试模式调用次数'},
        'run_token_num': {'type': 'integer', 'description': '调试模式Token使用数'},
        'release_call_num': {'type': 'integer', 'description': '发布模式调用次数'},
        'release_token_num': {'type': 'integer', 'description': '发布模式Token使用数'}
    }
}

# 费用统计分类 Schema
COST_CATEGORY_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'category': {'type': 'string', 'description': '分类名称'},
        'count': {'type': 'integer', 'description': '数量'},
        'token_usage_times': {'type': 'integer', 'description': 'Token使用次数'},
        'token_consumption': {'type': 'integer', 'description': 'Token消耗量'},
        'gpu_consumption': {'type': 'integer', 'description': 'GPU消耗量'}
    }
}

# 费用统计总计 Schema
COST_TOTAL_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'count': {'type': 'integer', 'description': '总数量'},
        'token_usage_times': {'type': 'integer', 'description': '总Token使用次数'},
        'token_consumption': {'type': 'integer', 'description': '总Token消耗量'},
        'gpu_consumption': {'type': 'integer', 'description': '总GPU消耗量'}
    }
}

# 费用统计响应 Schema
STAT_COST_AUDIT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'categories': {
            'type': 'array',
            'items': deepcopy(COST_CATEGORY_SCHEMA)
        },
        'total': deepcopy(COST_TOTAL_SCHEMA)
    }
}

# 应用统计指标 Schema
APP_STATISTICS_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'description': '应用统计指标，包含累计token消费、用户数、会话数、互动数等'
}


# ==================== 参数定义函数 ====================

def app_id_path_param() -> Dict[str, Any]:
    """应用ID路径参数（UUID格式）"""
    return {
        'name': 'app_id',
        'in': 'path',
        'type': 'string',
        'format': 'uuid',
        'required': True,
        'description': '应用ID'
    }


def tenant_id_query_param() -> Dict[str, Any]:
    """租户ID查询参数"""
    return {
        'name': 'tenant_id',
        'in': 'query',
        'type': 'string',
        'required': False,
        'description': '租户ID，如果提供则查询该租户下所有用户的费用统计数据'
    }


def app_statistics_body_schema() -> Dict[str, Any]:
    """获取应用统计指标请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'app_id': {
                'type': 'string',
                'format': 'uuid',
                'description': '应用ID'
            }
        },
        'required': ['app_id']
    }


def calc_and_save_app_statistics_body_schema() -> Dict[str, Any]:
    """统计并保存应用统计数据请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'app_id': {
                'type': 'string',
                'format': 'uuid',
                'description': '应用ID'
            },
            'call_type': {
                'type': 'string',
                'enum': CALL_TYPE_ENUM,
                'default': 'release',
                'description': '调用类型'
            },
            'stat_date': {
                'type': 'string',
                'format': 'date',
                'description': '统计日期，格式为YYYY-MM-DD'
            },
            'stat_date_start': {
                'type': 'string',
                'format': 'date',
                'description': '统计开始日期，格式为YYYY-MM-DD'
            },
            'stat_date_end': {
                'type': 'string',
                'format': 'date',
                'description': '统计结束日期，格式为YYYY-MM-DD'
            },
            'need_save_db': {
                'type': 'boolean',
                'default': False,
                'description': '是否需要保存到数据库'
            }
        }
    }


def daily_app_statistics_body_schema() -> Dict[str, Any]:
    """每日应用统计请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'stat_date': {
                'type': 'string',
                'format': 'date',
                'description': '统计日期，格式为YYYY-MM-DD。如果不提供，则统计昨天的数据'
            }
        }
    }


def cache_app_statistics_for_periods_body_schema() -> Dict[str, Any]:
    """缓存应用统计数据请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'stat_date': {
                'type': 'string',
                'format': 'date',
                'description': '统计基准日期，格式为YYYY-MM-DD。如果不提供，则使用今天作为基准日期'
            }
        }
    }


def get_app_statistics_by_period_body_schema() -> Dict[str, Any]:
    """按时间区间获取应用统计请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'app_id': {
                'type': 'string',
                'format': 'uuid',
                'description': '应用ID'
            },
            'start_date': {
                'type': 'string',
                'format': 'date',
                'description': '起始日期，格式为YYYY-MM-DD'
            },
            'end_date': {
                'type': 'string',
                'format': 'date',
                'description': '结束日期，格式为YYYY-MM-DD'
            }
        },
        'required': ['app_id', 'start_date', 'end_date']
    }


def query_app_statistics_body_schema() -> Dict[str, Any]:
    """查询应用统计请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'app_id': {
                'type': 'string',
                'format': 'uuid',
                'description': '应用ID'
            },
            'start_date': {
                'type': 'string',
                'format': 'date',
                'description': '起始日期，格式为YYYY-MM-DD'
            },
            'end_date': {
                'type': 'string',
                'format': 'date',
                'description': '结束日期，格式为YYYY-MM-DD'
            },
            'call_type': {
                'type': 'string',
                'enum': CALL_TYPE_ENUM,
                'description': '调用类型，用于过滤数据'
            }
        }
    }


def query_conversations_body_schema() -> Dict[str, Any]:
    """查询对话记录请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'app_id': {
                'type': 'string',
                'format': 'uuid',
                'description': '应用ID（可选）'
            },
            'start_time': {
                'type': 'string',
                'format': 'date-time',
                'description': '起始时间，格式为YYYY-MM-DD HH:MM:SS'
            },
            'end_time': {
                'type': 'string',
                'format': 'date-time',
                'description': '结束时间，格式为YYYY-MM-DD HH:MM:SS'
            },
            'from_who': {
                'type': 'string',
                'description': '用户ID，用于过滤特定用户的对话'
            }
        }
    }
