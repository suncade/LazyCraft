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

"""应用管理模块的 Swagger 文档定义"""

# 由于接口较多，分批次导入
from .specs import (
    # 应用基础管理
    app_list_spec,
    app_list_page_spec,
    app_detail_get_spec,
    app_detail_put_spec,
    app_detail_delete_spec,
    app_create_spec,
    # 应用功能
    app_enable_api_spec,
    app_enable_backflow_spec,
    app_enable_api_call_spec,
    app_export_spec,
    app_import_spec,
    app_convert_to_template_spec,
    # 模板管理
    template_list_spec,
    template_detail_spec,
    template_detail_get_spec,
    template_detail_put_spec,
    template_detail_delete_spec,
    template_convert_to_app_spec,
    # 工作流相关
    draft_workflow_spec,
    draft_workflow_post_spec,
    draft_workflow_status_spec,
    draft_workflow_start_spec,
    draft_workflow_run_spec,
    draft_workflow_stop_spec,
    draft_workflow_reset_session_spec,
    published_workflow_spec,
    published_workflow_post_spec,
    cancel_publish_spec,
    # 调试相关
    draft_debug_detail_spec,
    draft_debug_detail_stream_spec,
    draft_debug_detail_history_spec,
    draft_debug_detail_history_delete_spec,
    draft_debug_detail_stream_stop_spec,
    draft_debug_detail_stream_status_spec,
    # 其他
    app_report_spec,
    app_version_spec,
    app_restore_spec,
    check_versions_count_spec,
    reference_result_spec,
    draft_import_from_file_spec,
    node_run_stream_spec,
    new_workflow_from_empty_spec,
    new_workflow_from_app_spec,
    new_workflow_from_template_spec,
    workflow_add_log_spec,
    workflow_batch_log_spec,
    doc_parse_spec,
    doc_parse_status_spec,
    ai_code_assistant_spec,
    ai_prompt_assistant_spec,
)

__all__ = [
    'app_list_spec',
    'app_list_page_spec',
    'app_detail_get_spec',
    'app_detail_put_spec',
    'app_detail_delete_spec',
    'app_create_spec',
    'app_enable_api_spec',
    'app_enable_backflow_spec',
    'app_enable_api_call_spec',
    'app_export_spec',
    'app_import_spec',
    'app_convert_to_template_spec',
    'template_list_spec',
    'template_detail_spec',
    'template_detail_get_spec',
    'template_detail_put_spec',
    'template_detail_delete_spec',
    'template_convert_to_app_spec',
    'draft_workflow_spec',
    'draft_workflow_post_spec',
    'draft_workflow_status_spec',
    'draft_workflow_start_spec',
    'draft_workflow_run_spec',
    'draft_workflow_stop_spec',
    'draft_workflow_reset_session_spec',
    'published_workflow_spec',
    'published_workflow_post_spec',
    'cancel_publish_spec',
    'draft_debug_detail_spec',
    'draft_debug_detail_stream_spec',
    'draft_debug_detail_history_spec',
    'draft_debug_detail_history_delete_spec',
    'draft_debug_detail_stream_stop_spec',
    'draft_debug_detail_stream_status_spec',
    'app_report_spec',
    'app_version_spec',
    'app_restore_spec',
    'check_versions_count_spec',
    'reference_result_spec',
    'draft_import_from_file_spec',
    'node_run_stream_spec',
    'new_workflow_from_empty_spec',
    'new_workflow_from_app_spec',
    'new_workflow_from_template_spec',
    'workflow_add_log_spec',
    'workflow_batch_log_spec',
    'doc_parse_spec',
    'doc_parse_status_spec',
    'ai_code_assistant_spec',
    'ai_prompt_assistant_spec',
]
