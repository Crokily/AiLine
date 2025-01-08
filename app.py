# app.py

from flask import Flask, request, jsonify
from agent.manager import AgentManager
from workflow.workflow import Workflow
import os

def create_app():
    app = Flask(__name__)

    # 配置文件路径
    config_file = os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml')

    # 创建 AgentManager 实例
    agent_manager = AgentManager(config_file)

    @app.route('/process', methods=['POST'])
    def process_text():
        try:
            data = request.get_json()
            text = data.get('text')
            agent_names = data.get('agents')  # 接受要使用的代理列表

            if not text:
                return jsonify({'error': '请提供输入文本'}), 400
            if not agent_names:
                return jsonify({'error': '请提供要使用的代理名称列表'}), 400

            # 检查代理是否存在
            selected_agents = []
            for name in agent_names:
                agent = agent_manager.get_agent(name.strip())
                if not agent:
                    return jsonify({'error': f'代理 "{name}" 不存在'}), 400
                selected_agents.append(agent)

            # 创建工作流并运行
            workflow = Workflow(selected_agents)
            result = workflow.run(text)

            return jsonify({'result': result})

        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400
        except Exception as e:
            return jsonify({'error': f"服务器内部错误: {str(e)}"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)