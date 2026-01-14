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

"""认证模块的 Swagger 规范定义"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import standard_error_responses
from .definitions import (
    AUTH_SECURITY,
    ACCOUNT_SCHEMA,
    LOGIN_RESPONSE_SCHEMA,
    KEY_EXCHANGE_RESPONSE_SCHEMA,
    encrypted_data_param,
    register_body_schema,
    login_body_schema,
    login_sms_body_schema,
    add_user_body_schema,
    sendsms_body_schema,
    validate_exist_body_schema,
    account_password_body_schema,
    account_update_body_schema,
    oauth_provider_path_param,
    oauth_bind_body_schema,
    forgot_password_email_body_schema,
    forgot_password_check_body_schema,
    forgot_password_reset_body_schema,
    forgot_password_admin_reset_body_schema,
)


# ==================== 登录注册接口 ====================

# 注册
register_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '用户注册',
    'description': '注册新用户账号，需要提供加密后的用户信息和短信验证码',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'encrypted_data': {
                        'type': 'string',
                        'description': '加密后的注册数据（Base64编码）'
                    },
                    'session_id': {
                        'type': 'string',
                        'format': 'uuid',
                        'description': '会话ID（从密钥交换接口获取）'
                    }
                },
                'required': ['encrypted_data', 'session_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '注册成功，返回登录令牌',
            'schema': deepcopy(LOGIN_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False)
    }
}

# 密码登录
login_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '密码登录',
    'description': '使用用户名/邮箱/手机号和密码进行登录',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'encrypted_data': {
                        'type': 'string',
                        'description': '加密后的登录数据（Base64编码）'
                    },
                    'session_id': {
                        'type': 'string',
                        'format': 'uuid',
                        'description': '会话ID（从密钥交换接口获取）'
                    }
                },
                'required': ['encrypted_data', 'session_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '登录成功，返回访问令牌',
            'schema': deepcopy(LOGIN_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False)
    }
}

# 短信验证码登录
login_sms_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '短信验证码登录',
    'description': '使用手机号和短信验证码进行登录',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'encrypted_data': {
                        'type': 'string',
                        'description': '加密后的登录数据（Base64编码）'
                    },
                    'session_id': {
                        'type': 'string',
                        'format': 'uuid',
                        'description': '会话ID（从密钥交换接口获取）'
                    }
                },
                'required': ['encrypted_data', 'session_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': '登录成功，返回访问令牌',
            'schema': deepcopy(LOGIN_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False)
    }
}

# 退出登录
logout_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '退出登录',
    'description': '注销当前用户会话',
    'responses': {
        200: {
            'description': '退出成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_400=False, include_403=False, include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}


# ==================== 用户管理接口 ====================

# 管理员添加用户
add_user_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '管理员添加用户',
    'description': '管理员创建新用户账号，不需要短信验证码',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(add_user_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '添加成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'id': {'type': 'string', 'description': '用户ID'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 获取用户资料
account_profile_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '获取用户资料',
    'description': '获取当前登录用户的详细信息和租户信息',
    'responses': {
        200: {
            'description': '成功返回用户资料',
            'schema': deepcopy(ACCOUNT_SCHEMA)
        },
        **standard_error_responses(include_400=False, include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 修改密码
account_password_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '修改密码',
    'description': '修改当前用户的登录密码',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(account_password_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '密码修改成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}

# 更新用户信息
account_update_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '更新用户信息',
    'description': '更新当前用户的基本信息（姓名、邮箱、手机号）',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(account_update_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '更新成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'message': {'type': 'string', 'example': '用户信息更新成功'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}


# ==================== 短信验证接口 ====================

# 发送短信验证码
sendsms_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '发送短信验证码',
    'description': '向指定手机号发送短信验证码',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(sendsms_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '发送成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}

# 校验用户信息唯一性
validate_exist_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '校验用户信息唯一性',
    'description': '验证用户名、手机号或邮箱是否已被使用',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(validate_exist_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '验证结果',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {
                        'type': 'string',
                        'enum': ['success', 'failed'],
                        'description': 'success表示可用，failed表示已存在'
                    },
                    'message': {'type': 'string', 'description': '错误信息（当result为failed时）'}
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}


# ==================== 密钥交换接口 ====================

# ECDH 密钥交换
key_exchange_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': 'ECDH 密钥交换',
    'description': '进行 ECDH 密钥交换，获取会话密钥用于数据加密',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'frontend_public_key': {
                        'type': 'string',
                        'description': '前端公钥（Base64编码）'
                    }
                },
                'required': ['frontend_public_key']
            }
        }
    ],
    'responses': {
        200: {
            'description': '密钥交换成功',
            'schema': deepcopy(KEY_EXCHANGE_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}


# ==================== OAuth 接口 ====================

# OAuth 登录
oauth_login_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': 'OAuth 登录',
    'description': '启动 OAuth 登录流程，重定向到 OAuth 提供商授权页面',
    'security': [],
    'parameters': [oauth_provider_path_param()],
    'responses': {
        302: {'description': '重定向到 OAuth 授权页面'},
        **standard_error_responses(include_403=False, include_404=False)
    }
}

# OAuth 回调处理（GET）
oauth_authorize_get_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': 'OAuth 回调处理',
    'description': '处理 OAuth 授权完成后的回调请求',
    'security': [],
    'parameters': [
        oauth_provider_path_param(),
        {
            'name': 'code',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'OAuth 授权码'
        }
    ],
    'responses': {
        302: {'description': '重定向到绑定页面或登录成功页面'},
        400: {'description': 'OAuth 授权失败'},
        **standard_error_responses(include_403=False, include_404=False)
    }
}

# OAuth 绑定（POST）
oauth_authorize_post_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': 'OAuth 账号绑定',
    'description': '完成 OAuth 账号与手机号的绑定',
    'security': [],
    'parameters': [
        oauth_provider_path_param(),
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(oauth_bind_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '绑定成功，返回登录令牌',
            'schema': deepcopy(LOGIN_RESPONSE_SCHEMA)
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}


# ==================== 忘记密码接口 ====================

# 发送密码重置邮件
forgot_password_send_email_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '发送密码重置邮件',
    'description': '向用户注册邮箱发送包含重置链接的邮件',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(forgot_password_email_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '邮件发送成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'},
                    'token': {
                        'type': 'string',
                        'description': '重置令牌（仅在调试模式下返回）'
                    }
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}

# 验证重置令牌
forgot_password_check_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '验证密码重置令牌',
    'description': '验证密码重置令牌的有效性',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(forgot_password_check_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '验证结果',
            'schema': {
                'type': 'object',
                'properties': {
                    'is_valid': {'type': 'boolean', 'description': '令牌是否有效'},
                    'email': {'type': 'string', 'format': 'email', 'description': '关联的邮箱地址'}
                }
            }
        },
        **standard_error_responses(include_403=False, include_404=False)
    }
}

# 重置密码
forgot_password_reset_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '重置密码',
    'description': '使用有效的重置令牌更新用户密码',
    'security': [],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(forgot_password_reset_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '密码重置成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    }
}

# 管理员重置密码
forgot_password_admin_reset_spec: Dict[str, Any] = {
    'tags': ['auth'],
    'summary': '管理员重置密码',
    'description': '管理员强制重置指定用户的密码',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': deepcopy(forgot_password_admin_reset_body_schema())
        }
    ],
    'responses': {
        200: {
            'description': '密码重置成功',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'string', 'example': 'success'}
                }
            }
        },
        **standard_error_responses(include_404=False)
    },
    'security': deepcopy(AUTH_SECURITY)
}
