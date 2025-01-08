# main.py

import os
from agent.manager import AgentManager
from ui.cli import CLI

def main():
    # 配置文件路径
    config_file = os.path.join(os.path.dirname(__file__), 'config', 'agents.yaml')

    # 创建 AgentManager 实例
    agent_manager = AgentManager(config_file)

    # 创建 CLI 实例并运行
    cli = CLI(agent_manager)
    cli.run()

if __name__ == '__main__':
    main()