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

"""文档管理模块的 Swagger 文档定义"""

from .specs import (
    doc_list_spec,
    doc_detail_get_spec,
    doc_create_spec,
    doc_update_spec,
    doc_delete_spec,
    doc_publish_spec,
    doc_unpublish_spec,
    doc_upload_image_spec,
    doc_image_spec,
    doc_view_spec,
)

__all__ = [
    'doc_list_spec',
    'doc_detail_get_spec',
    'doc_create_spec',
    'doc_update_spec',
    'doc_delete_spec',
    'doc_publish_spec',
    'doc_unpublish_spec',
    'doc_upload_image_spec',
    'doc_image_spec',
    'doc_view_spec',
]
