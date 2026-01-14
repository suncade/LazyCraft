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

"""认证模块的 Swagger 定义和参数"""

from copy import deepcopy
from typing import Dict, Any

from ..common_definitions import AUTH_SECURITY, standard_error_responses


# ==================== 枚举定义 ====================

# 短信操作类型
SMS_OPERATION_ENUM = ['login', 'register', 'reset', 'relate']

# OAuth 提供商
OAUTH_PROVIDER_ENUM = ['github']


# ==================== Schema 定义 ====================

# 账户信息 Schema
ACCOUNT_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string', 'description': '用户ID'},
        'name': {'type': 'string', 'description': '用户名'},
        'avatar': {'type': 'string', 'description': '头像URL'},
        'email': {'type': 'string', 'format': 'email', 'description': '邮箱'},
        'interface_language': {'type': 'string', 'description': '界面语言'},
        'interface_theme': {'type': 'string', 'description': '界面主题'},
        'timezone': {'type': 'string', 'description': '时区'},
        'last_login_at': {'type': 'integer', 'description': '最后登录时间戳'},
        'last_login_ip': {'type': 'string', 'description': '最后登录IP'},
        'created_at': {'type': 'integer', 'description': '创建时间戳'},
        'tenant': {
            'type': 'object',
            'properties': {
                'id': {'type': 'string', 'description': '租户ID'},
                'name': {'type': 'string', 'description': '租户名称'},
                'status': {'type': 'string', 'description': '租户状态'},
                'role': {'type': 'string', 'description': '用户角色', 'enum': ['administrator', 'super', 'owner', 'member', None]},
            }
        }
    }
}

# 登录响应 Schema
LOGIN_RESPONSE_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'result': {'type': 'string', 'description': '操作结果', 'example': 'success'},
        'data': {'type': 'string', 'description': '访问令牌'}
    }
}

# 密钥交换响应 Schema
KEY_EXCHANGE_RESPONSE_SCHEMA: Dict[str, Any] = {
    'type': 'object',
    'properties': {
        'backend_public_key': {'type': 'string', 'description': '后端公钥（Base64编码）'},
        'session_id': {'type': 'string', 'format': 'uuid', 'description': '会话ID'},
        'expires_in': {'type': 'integer', 'description': '过期时间（秒）', 'example': 300},
        'algorithm': {'type': 'string', 'description': '加密算法', 'example': 'ECDH-P256 + AES-256-GCM'},
        'curve': {'type': 'string', 'description': '椭圆曲线', 'example': 'secp256r1'},
        'key_size': {'type': 'integer', 'description': '密钥长度', 'example': 256}
    }
}


# ==================== 参数定义函数 ====================

def encrypted_data_param() -> Dict[str, Any]:
    """加密数据参数"""
    return {
        'name': 'encrypted_data',
        'in': 'body',
        'type': 'object',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'encrypted_data': {
                    'type': 'string',
                    'description': '加密后的数据（Base64编码）'
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


def register_body_schema() -> Dict[str, Any]:
    """注册请求体 Schema（解密后的数据）"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '用户名'},
            'email': {'type': 'string', 'format': 'email', 'description': '邮箱'},
            'phone': {'type': 'string', 'description': '手机号'},
            'password': {'type': 'string', 'description': '密码'},
            'confirm_password': {'type': 'string', 'description': '确认密码'},
            'verify_code': {'type': 'string', 'description': '短信验证码'}
        },
        'required': ['name', 'email', 'phone', 'password', 'confirm_password', 'verify_code']
    }


def login_body_schema() -> Dict[str, Any]:
    """登录请求体 Schema（解密后的数据）"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '用户名（可选）'},
            'email': {'type': 'string', 'format': 'email', 'description': '邮箱（可选）'},
            'phone': {'type': 'string', 'description': '手机号（可选）'},
            'password': {'type': 'string', 'description': '密码'},
            'remember_me': {'type': 'boolean', 'description': '记住我', 'default': False}
        },
        'required': ['password'],
        'anyOf': [
            {'required': ['name']},
            {'required': ['email']},
            {'required': ['phone']}
        ]
    }


def login_sms_body_schema() -> Dict[str, Any]:
    """短信登录请求体 Schema（解密后的数据）"""
    return {
        'type': 'object',
        'properties': {
            'phone': {'type': 'string', 'description': '手机号'},
            'verify_code': {'type': 'string', 'description': '短信验证码'}
        },
        'required': ['phone', 'verify_code']
    }


def add_user_body_schema() -> Dict[str, Any]:
    """添加用户请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '用户名'},
            'email': {'type': 'string', 'format': 'email', 'description': '邮箱（可选）'},
            'phone': {'type': 'string', 'description': '手机号（可选）'},
            'password': {'type': 'string', 'description': '密码'},
            'confirm_password': {'type': 'string', 'description': '确认密码'}
        },
        'required': ['name', 'password', 'confirm_password']
    }


def sendsms_body_schema() -> Dict[str, Any]:
    """发送短信请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'phone': {'type': 'string', 'description': '手机号'},
            'operation': {
                'type': 'string',
                'enum': SMS_OPERATION_ENUM,
                'description': '操作类型'
            }
        },
        'required': ['phone', 'operation']
    }


def validate_exist_body_schema() -> Dict[str, Any]:
    """校验用户信息唯一性请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '用户名（可选）'},
            'email': {'type': 'string', 'format': 'email', 'description': '邮箱（可选）'},
            'phone': {'type': 'string', 'description': '手机号（可选）'}
        }
    }


def account_password_body_schema() -> Dict[str, Any]:
    """修改密码请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'password': {'type': 'string', 'description': '当前密码（可选）'},
            'new_password': {'type': 'string', 'description': '新密码'},
            'repeat_new_password': {'type': 'string', 'description': '确认新密码'}
        },
        'required': ['new_password', 'repeat_new_password']
    }


def account_update_body_schema() -> Dict[str, Any]:
    """更新用户信息请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '用户名（可选）'},
            'email': {'type': 'string', 'format': 'email', 'description': '邮箱（可选）'},
            'phone': {'type': 'string', 'description': '手机号（可选）'}
        }
    }


def oauth_provider_path_param() -> Dict[str, Any]:
    """OAuth 提供商路径参数"""
    return {
        'name': 'provider',
        'in': 'path',
        'type': 'string',
        'required': True,
        'enum': OAUTH_PROVIDER_ENUM,
        'description': 'OAuth 提供商名称'
    }


def oauth_bind_body_schema() -> Dict[str, Any]:
    """OAuth 绑定请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'openid': {'type': 'string', 'description': 'OAuth 用户ID'},
            'phone': {'type': 'string', 'description': '手机号'},
            'verify_code': {'type': 'string', 'description': '短信验证码'}
        },
        'required': ['openid', 'phone', 'verify_code']
    }


def forgot_password_email_body_schema() -> Dict[str, Any]:
    """忘记密码发送邮件请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'email': {'type': 'string', 'format': 'email', 'description': '用户邮箱'}
        },
        'required': ['email']
    }


def forgot_password_check_body_schema() -> Dict[str, Any]:
    """验证重置令牌请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'token': {'type': 'string', 'description': '密码重置令牌'}
        },
        'required': ['token']
    }


def forgot_password_reset_body_schema() -> Dict[str, Any]:
    """重置密码请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'token': {'type': 'string', 'description': '密码重置令牌'},
            'new_password': {'type': 'string', 'description': '新密码'},
            'password_confirm': {'type': 'string', 'description': '确认新密码'}
        },
        'required': ['token', 'new_password', 'password_confirm']
    }


def forgot_password_admin_reset_body_schema() -> Dict[str, Any]:
    """管理员重置密码请求体 Schema"""
    return {
        'type': 'object',
        'properties': {
            'name': {'type': 'string', 'description': '目标用户名'},
            'new_password': {'type': 'string', 'description': '新密码'},
            'password_confirm': {'type': 'string', 'description': '确认新密码'}
        },
        'required': ['name', 'new_password', 'password_confirm']
    }
