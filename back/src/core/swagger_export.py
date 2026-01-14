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

import json
import os

from flask import Flask


def export_swagger_json(app: Flask, output_path: str = None):
    """导出 Swagger JSON 文件。

    Args:
        app: Flask 应用实例
        output_path: 输出文件路径，默认为 back/src/docs/swagger.json
    """
    if output_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        docs_dir = os.path.join(os.path.dirname(current_dir), 'docs')
        output_path = os.path.join(docs_dir, 'swagger.json')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with app.app_context():
        with app.test_client() as client:
            response = client.get('/apispec.json')
            if response.status_code == 200:
                swagger_data = response.get_json()
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(swagger_data, f, indent=2, ensure_ascii=False)
                print(f'✅ Swagger JSON 导出成功: {output_path}')
                return True
            else:
                print(f'❌ 导出失败: HTTP {response.status_code}')
                print(f'   响应内容: {response.get_data(as_text=True)}')
                return False
