from flask import Flask, request, jsonify
from agent.manager import AgentManager
from ui.handler import RequestHandler  # 导入 RequestHandler
import os

def create_app():
    app = Flask(__name__)

    # 配置文件路径
    config_file = os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml')

    # 创建 AgentManager 实例
    agent_manager = AgentManager(config_file)

    # 创建 RequestHandler 实例
    request_handler = RequestHandler(agent_manager)  # 使用 RequestHandler

    @app.route('/process', methods=['POST'])
    def process_text():
        try:
            data = request.get_json()
            text = data.get('text')
            agent_names = data.get('agents')

            # 使用 RequestHandler 处理请求
            result = request_handler.handle_request(text, agent_names)

            return jsonify({'result': result})

        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except Exception as e:
            return jsonify({'error': f"服务器内部错误: {str(e)}"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)