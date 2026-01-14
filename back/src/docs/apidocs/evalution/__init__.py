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

"""模型评测模块的 Swagger 文档定义"""

from .specs import (
    upload_dataset_spec,
    create_task_spec,
    evaluation_dimension_spec,
    evaluate_spec,
    task_info_spec,
    task_list_spec,
    delete_task_spec,
    evaluation_data_paginator_spec,
    evaluation_model_spec,
    evaluation_online_data_spec,
    evaluation_summary_spec,
    download_report_excel_spec,
    download_dataset_tpl_spec,
)

__all__ = [
    'upload_dataset_spec',
    'create_task_spec',
    'evaluation_dimension_spec',
    'evaluate_spec',
    'task_info_spec',
    'task_list_spec',
    'delete_task_spec',
    'evaluation_data_paginator_spec',
    'evaluation_model_spec',
    'evaluation_online_data_spec',
    'evaluation_summary_spec',
    'download_report_excel_spec',
    'download_dataset_tpl_spec',
]
