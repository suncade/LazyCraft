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

"""文件管理模块的 Swagger 规范定义"""

from typing import Dict, Any

from ..common_definitions import standard_error_responses
from .definitions import (
    FILE_UPLOAD_RESPONSE_SCHEMA,
    file_upload_params,
)


# ==================== 文件上传相关接口 ====================

# 上传文件
file_upload_spec: Dict[str, Any] = {
    'tags': ['文件管理'],
    'summary': '上传文件',
    'description': '上传本地文件供大模型使用。此端点允许在不需要身份验证的情况下上传文件，因为访客也可以访问。上传的文件会保存到工作流目录中，并使用随机生成的文件名',
    'parameters': file_upload_params(),
    'responses': {
        **standard_error_responses(include_403=False, include_400=True),
        '200': {
            'description': '上传成功',
            'schema': FILE_UPLOAD_RESPONSE_SCHEMA,
        },
    },
}
