# ui/cli.py

from workflow.workflow import Workflow

class CLI:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager

    def run(self):
        # 列出可用的代理
        print("可用的代理:")
        for name in self.agent_manager.list_agents():
            print(f"- {name}")

        # 用户选择代理
        agent_names = input("请输入要使用的代理名称（多个用逗号分隔）: ").split(',')
        agent_names = [name.strip() for name in agent_names]

        selected_agents = []
        for name in agent_names:
            agent = self.agent_manager.get_agent(name)
            if not agent:
                print(f'代理 "{name}" 不存在')
                return
            selected_agents.append(agent)

        # 获取用户输入的文本
        text = input("请输入要处理的文本: ")

        # 创建工作流并运行
        workflow = Workflow(selected_agents)
        result = workflow.run(text)

        # 输出结果
        print("处理结果:")
        print(result)