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

"""标签管理模块的 Swagger 文档定义"""

from .specs import (
    tag_list_spec,
    tag_create_spec,
    tag_delete_spec,
    tag_binding_update_spec,
    brand_list_spec,
    brand_create_spec,
    brand_delete_spec,
)

__all__ = [
    'tag_list_spec',
    'tag_create_spec',
    'tag_delete_spec',
    'tag_binding_update_spec',
    'brand_list_spec',
    'brand_create_spec',
    'brand_delete_spec',
]
