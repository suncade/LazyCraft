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

"""工具模块的 Swagger 定义导出"""

from .specs import (
    tool_list_spec,
    tool_detail_spec,
    tool_check_name_spec,
    tool_create_update_spec,
    tool_delete_spec,
    tool_field_create_update_spec,
    tool_fields_detail_spec,
    tool_api_create_update_spec,
    tool_api_detail_spec,
    tool_publish_spec,
    tool_cancel_publish_spec,
    tool_enable_spec,
    tool_copy_spec,
    tool_test_spec,
    tool_test_log_spec,
    tool_auth_return_url_spec,
    tool_auth_callback_spec,
    tool_auth_share_spec,
    tool_auth_delete_spec,
    tool_export_spec,
    tool_reference_result_spec,
)

__all__ = [
    'tool_list_spec',
    'tool_detail_spec',
    'tool_check_name_spec',
    'tool_create_update_spec',
    'tool_delete_spec',
    'tool_field_create_update_spec',
    'tool_fields_detail_spec',
    'tool_api_create_update_spec',
    'tool_api_detail_spec',
    'tool_publish_spec',
    'tool_cancel_publish_spec',
    'tool_enable_spec',
    'tool_copy_spec',
    'tool_test_spec',
    'tool_test_log_spec',
    'tool_auth_return_url_spec',
    'tool_auth_callback_spec',
    'tool_auth_share_spec',
    'tool_auth_delete_spec',
    'tool_export_spec',
    'tool_reference_result_spec',
]
