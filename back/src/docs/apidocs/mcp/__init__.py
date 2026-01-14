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

"""MCP工具模块的 Swagger 定义导出"""

from .specs import (
    server_list_spec,
    server_detail_spec,
    server_check_name_spec,
    server_create_update_spec,
    server_delete_spec,
    server_publish_spec,
    server_enable_spec,
    server_sync_tools_spec,
    tool_list_spec,
    tool_detail_spec,
    tool_test_spec,
    tool_reference_result_spec,
)

__all__ = [
    'server_list_spec',
    'server_detail_spec',
    'server_check_name_spec',
    'server_create_update_spec',
    'server_delete_spec',
    'server_publish_spec',
    'server_enable_spec',
    'server_sync_tools_spec',
    'tool_list_spec',
    'tool_detail_spec',
    'tool_test_spec',
    'tool_reference_result_spec',
]
