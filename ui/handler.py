from workflow.workflow import Workflow

class RequestHandler:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager

    def handle_request(self, text, agent_names):
        """
        处理请求的核心逻辑

        Args:
            text: 用户输入的文本
            agent_names: 用户选择的代理名称列表

        Returns:
            处理结果
        """

        if not text:
            raise ValueError("请提供输入文本")
        if not agent_names:
            raise ValueError("请提供要使用的代理名称列表")

        # 检查代理是否存在
        selected_agents = []
        for name in agent_names:
            agent = self.agent_manager.get_agent(name.strip())
            if not agent:
                raise ValueError(f'代理 "{name}" 不存在')
            selected_agents.append(agent)

        # 创建工作流并运行
        workflow = Workflow(selected_agents)
        result = workflow.run(text)

        return result