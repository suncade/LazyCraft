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

"""模型管理模块的 Swagger 定义导出"""

from .specs import (
    model_list_spec,
    model_create_spec,
    online_model_list_create_spec,
    online_model_list_delete_spec,
    update_apikey_spec,
    delete_apikey_spec,
    retry_download_spec,
    finetune_retry_download_spec,
    models_tree_spec,
    model_update_spec,
    model_delete_spec,
    icon_upload_spec,
    upload_file_chunk_spec,
    merge_file_spec,
    delete_uploaded_file_spec,
    check_model_name_spec,
    model_info_spec,
    create_finetune_spec,
    delete_finetune_model_spec,
    finetune_model_list_spec,
    online_model_support_list_spec,
    update_online_model_list_spec,
    exist_model_list_spec,
    default_icon_list_spec,
)

__all__ = [
    'model_list_spec',
    'model_create_spec',
    'online_model_list_create_spec',
    'online_model_list_delete_spec',
    'update_apikey_spec',
    'delete_apikey_spec',
    'retry_download_spec',
    'finetune_retry_download_spec',
    'models_tree_spec',
    'model_update_spec',
    'model_delete_spec',
    'icon_upload_spec',
    'upload_file_chunk_spec',
    'merge_file_spec',
    'delete_uploaded_file_spec',
    'check_model_name_spec',
    'model_info_spec',
    'create_finetune_spec',
    'delete_finetune_model_spec',
    'finetune_model_list_spec',
    'online_model_support_list_spec',
    'update_online_model_list_spec',
    'exist_model_list_spec',
    'default_icon_list_spec',
]
