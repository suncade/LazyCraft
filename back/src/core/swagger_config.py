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

import os

from flasgger import Swagger


def init_swagger(app):
    """初始化 Swagger 文档生成。

    Args:
        app: Flask 应用实例
    """
    swagger_enabled = os.getenv('SWAGGER_ENABLED', 'true').lower() == 'true'
    if not swagger_enabled:
        app.logger.info('Swagger UI 已禁用（SWAGGER_ENABLED=false）')
        return

    swagger_config = {
        'headers': [],
        'specs': [
            {
                'endpoint': 'apispec',
                'route': '/apispec.json',
                'rule_filter': lambda rule: True,
                'model_filter': lambda tag: True,
            }
        ],
        'static_url_path': '/flasgger_static',
        'swagger_ui': True,
        'specs_route': '/api-docs',
        'ui_params': {
            # 核心1：关闭 所有接口列表 的默认展开 → 只显示模块名，接口折叠
            'docExpansion': 'none',  
            # 核心2：关闭 swagger自带的Models模型模块的展开（侧边栏）
            'defaultModelsExpandDepth': -1,
            # 核心3：关闭 单个Model模型的字段展开
            'defaultModelExpandDepth': -1,
            # 接口排序规则，按字母正序排列，模块内接口更整齐
            'operationsSorter': 'alpha'
        },
    }

    swagger_template = {
        'swagger': '2.0',
        'info': {
            'title': 'LazyCraft API',
            'description': 'LazyCraft 平台 API 文档',
            'version': '1.0.0',
            'contact': {
                'name': 'LazyLLM Team',
            },
        },
        'host': os.getenv('SWAGGER_HOST', 'localhost:30382'),
        'basePath': '/console/api',
        'schemes': ['http', 'https'],
        'securityDefinitions': {
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT Token 认证，格式: Bearer <token>',
            }
        },
        'security': [
            {
                'Bearer': []
            }
        ],
        'tags': [
            {
                'name': '应用商店',
                'description': '应用商店相关的 API'
            },
            {
                'name': '数据库管理',
                'description': '资源库-数据库管理相关的 API（数据库、表、数据管理等）'
            },
            {
                'name': '知识库管理',
                'description': '资源库-知识库管理相关的 API（知识库、文件管理等）'
            },
            {
                'name': '文档管理',
                'description': '资源库-知识库-文档管理相关的 API（文档CRUD、发布、图片上传等）'
            },
            {
                'name': 'Prompt',
                'description': 'Prompt相关的 API'
            },
            {
                'name': '模型仓库',
                'description': '模型仓库-模型管理相关的 API（模型管理、创建、更新、删除、上传、微调模型管理等）'
            },
            {
                'name': '模型评测',
                'description': '模型仓库-模型评测相关的 API（评估任务管理、数据集上传、评估执行、报告下载等）'
            },
            {
                'name': '推理服务',
                'description': '推理服务相关的 API'
            },
            {
                'name': '模型微调',
                'description': '模型微调相关的 API'
            },
            {
                'name': '工具',
                'description': '工具相关的 API'
            },
            {
                'name': 'MCP工具',
                'description': '工具-MCP工具相关的 API（MCP服务器管理、工具管理等）'
            },
            {
                'name': '数据集',
                'description': '数据集相关的 API（数据集管理、脚本管理、数据回流等）'
            },
            {
                'name': '标签管理',
                'description': '标签相关的 API'
            },
            {
                'name': 'API Key',
                'description': 'API Key 管理相关的 API'
            },
            {
                'name': 'auth',
                'description': '认证相关的 API（登录、注册、OAuth等）'
            },
            {
                'name': 'conversation',
                'description': '对话相关的 API（会话管理、对话交互等）'
            },
            {
                'name': 'cost_audit',
                'description': '成本审计相关的 API（token统计、应用统计等）'
            },
            {
                'name': '操作日志',
                'description': '操作日志相关的 API（日志查询等）'
            },
            {
                'name': '系统消息',
                'description': '系统消息相关的 API（通知创建、查询、已读标记等）'
            },
            {
                'name': '文件管理',
                'description': '文件管理相关的 API（文件上传等）'
            },
            {
                'name': '工作空间',
                'description': '工作空间相关的 API（租户管理、用户管理、协作、配额管理等）'
            },
        ],
    }

    Swagger(app, config=swagger_config, template=swagger_template)
