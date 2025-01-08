# ui/cli.py

from ui.handler import RequestHandler

class CLI:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager
        self.request_handler = RequestHandler(agent_manager)  # 使用 RequestHandler

    def run(self):
        # 列出可用的代理
        print("可用的代理:")
        for name in self.agent_manager.list_agents():
            print(f"- {name}")

        # 用户选择代理
        agent_names = input("请输入要使用的代理名称（多个用逗号分隔）: ").split(',')
        agent_names = [name.strip() for name in agent_names]

        # 获取用户输入的文本
        text = input("请输入要处理的文本: ")

        # 使用 RequestHandler 处理请求
        try:
            result = self.request_handler.handle_request(text, agent_names)
            print("处理结果:")
            print(result)
        except ValueError as e:
            print(e)