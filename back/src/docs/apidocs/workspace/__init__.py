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

"""工作空间模块的 Swagger 定义导出"""

from .specs import (
    all_user_list_spec,
    select_user_list_spec,
    tenant_user_list_spec,
    all_tenant_list_spec,
    account_tenant_list_spec,
    current_tenant_list_spec,
    current_tenant_id_spec,
    switch_tenant_spec,
    add_tenant_spec,
    detail_tenant_spec,
    update_roles_spec,
    move_assets_spec,
    delete_tenant_spec,
    exit_tenant_spec,
    delete_role_spec,
    delete_account_spec,
    coop_status_spec,
    coop_open_spec,
    coop_close_spec,
    coop_join_list_spec,
    storage_check_spec,
    personal_space_get_spec,
    personal_space_post_spec,
    quota_request_list_spec,
    quota_request_spec,
    quota_request_detail_spec,
    quota_request_action_spec,
    ai_tool_set_spec,
    ai_tool_list_spec,
    tenant_enable_ai_spec,
)

__all__ = [
    'all_user_list_spec',
    'select_user_list_spec',
    'tenant_user_list_spec',
    'all_tenant_list_spec',
    'account_tenant_list_spec',
    'current_tenant_list_spec',
    'current_tenant_id_spec',
    'switch_tenant_spec',
    'add_tenant_spec',
    'detail_tenant_spec',
    'update_roles_spec',
    'move_assets_spec',
    'delete_tenant_spec',
    'exit_tenant_spec',
    'delete_role_spec',
    'delete_account_spec',
    'coop_status_spec',
    'coop_open_spec',
    'coop_close_spec',
    'coop_join_list_spec',
    'storage_check_spec',
    'personal_space_get_spec',
    'personal_space_post_spec',
    'quota_request_list_spec',
    'quota_request_spec',
    'quota_request_detail_spec',
    'quota_request_action_spec',
    'ai_tool_set_spec',
    'ai_tool_list_spec',
    'tenant_enable_ai_spec',
]
