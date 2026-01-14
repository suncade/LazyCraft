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

"""数据集模块的 Swagger 文档定义"""

# 脚本相关接口
from .specs import (
    script_list_spec,
    script_create_spec,
    script_delete_spec,
    script_upload_spec,
    script_update_spec,
    script_list_by_type_spec,
)

# 数据集相关接口
from .specs import (
    data_set_list_spec,
    data_set_create_spec,
    upload_data_set_file_spec,
    data_set_version_list_spec,
    data_set_file_list_spec,
    data_set_tag_list_spec,
    create_data_set_version_by_tag_spec,
    data_set_version_publish_spec,
    data_set_file_spec,
    data_set_file_update_spec,
    data_set_spec,
    data_set_version_spec,
    data_set_delete_spec,
    data_set_version_delete_spec,
    data_set_file_delete_spec,
    data_set_version_add_file_spec,
    data_set_version_export_spec,
    data_set_version_export_ft_spec,
    test_data_set_version_status_spec,
    clean_or_augment_data_set_version_spec,
    clean_or_augment_data_set_version_async_spec,
    clean_or_augment_data_set_version_async_with_item_count_spec,
    data_processing_task_progress_spec,
    data_processing_task_cancel_spec,
    data_processing_task_list_spec,
    data_processing_task_stream_spec,
)

# 回流数据相关接口
from .specs import (
    reflux_app_publish_spec,
    reflux_data_create_spec,
    reflux_data_update_feedback_spec,
    reflux_data_set_version_publish_spec,
    reflux_data_list_spec,
    reflux_data_detail_spec,
    reflux_data_delete_spec,
    reflux_data_update_spec,
    reflux_data_set_version_export_spec,
    reflux_data_set_version_export_for_ft_spec,
)

__all__ = [
    # 脚本相关
    'script_list_spec',
    'script_create_spec',
    'script_delete_spec',
    'script_upload_spec',
    'script_update_spec',
    'script_list_by_type_spec',
    # 数据集相关
    'data_set_list_spec',
    'data_set_create_spec',
    'upload_data_set_file_spec',
    'data_set_version_list_spec',
    'data_set_file_list_spec',
    'data_set_tag_list_spec',
    'create_data_set_version_by_tag_spec',
    'data_set_version_publish_spec',
    'data_set_file_spec',
    'data_set_file_update_spec',
    'data_set_spec',
    'data_set_version_spec',
    'data_set_delete_spec',
    'data_set_version_delete_spec',
    'data_set_file_delete_spec',
    'data_set_version_add_file_spec',
    'data_set_version_export_spec',
    'data_set_version_export_ft_spec',
    'test_data_set_version_status_spec',
    'clean_or_augment_data_set_version_spec',
    'clean_or_augment_data_set_version_async_spec',
    'clean_or_augment_data_set_version_async_with_item_count_spec',
    'data_processing_task_progress_spec',
    'data_processing_task_cancel_spec',
    'data_processing_task_list_spec',
    'data_processing_task_stream_spec',
    # 回流数据相关
    'reflux_app_publish_spec',
    'reflux_data_create_spec',
    'reflux_data_update_feedback_spec',
    'reflux_data_set_version_publish_spec',
    'reflux_data_list_spec',
    'reflux_data_detail_spec',
    'reflux_data_delete_spec',
    'reflux_data_update_spec',
    'reflux_data_set_version_export_spec',
    'reflux_data_set_version_export_for_ft_spec',
]
