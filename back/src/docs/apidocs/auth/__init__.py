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

"""认证模块的 Swagger 文档定义"""

from .specs import (
    # 登录注册
    register_spec,
    login_spec,
    login_sms_spec,
    logout_spec,
    # 用户管理
    add_user_spec,
    account_profile_spec,
    account_password_spec,
    account_update_spec,
    # 短信验证
    sendsms_spec,
    validate_exist_spec,
    # 密钥交换
    key_exchange_spec,
    # OAuth
    oauth_login_spec,
    oauth_authorize_get_spec,
    oauth_authorize_post_spec,
    # 忘记密码
    forgot_password_send_email_spec,
    forgot_password_check_spec,
    forgot_password_reset_spec,
    forgot_password_admin_reset_spec,
)

__all__ = [
    'register_spec',
    'login_spec',
    'login_sms_spec',
    'logout_spec',
    'add_user_spec',
    'account_profile_spec',
    'account_password_spec',
    'account_update_spec',
    'sendsms_spec',
    'validate_exist_spec',
    'key_exchange_spec',
    'oauth_login_spec',
    'oauth_authorize_get_spec',
    'oauth_authorize_post_spec',
    'forgot_password_send_email_spec',
    'forgot_password_check_spec',
    'forgot_password_reset_spec',
    'forgot_password_admin_reset_spec',
]
