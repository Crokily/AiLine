class Workflow:
    def __init__(self, agents):
        """
        agents: 一个由 Agent 实例组成的列表，定义了工作流中 Agent 的执行顺序。
        """
        self.agents = agents

    def run(self, input_text):
        text = input_text
        for agent in self.agents:
            text = agent.process(text)
        return text