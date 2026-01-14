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

"""知识库模块的 Swagger 文档定义"""

from .specs import (
    knowledge_base_list_spec,
    knowledge_base_create_spec,
    knowledge_base_update_spec,
    knowledge_base_delete_spec,
    file_upload_spec,
    file_get_spec,
    file_download_spec,
    knowledge_base_add_file_spec,
    knowledge_base_file_list_spec,
    knowledge_base_file_delete_spec,
    knowledge_base_reference_result_spec,
)

__all__ = [
    'knowledge_base_list_spec',
    'knowledge_base_create_spec',
    'knowledge_base_update_spec',
    'knowledge_base_delete_spec',
    'file_upload_spec',
    'file_get_spec',
    'file_download_spec',
    'knowledge_base_add_file_spec',
    'knowledge_base_file_list_spec',
    'knowledge_base_file_delete_spec',
    'knowledge_base_reference_result_spec',
]
