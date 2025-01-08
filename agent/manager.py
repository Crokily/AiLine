# agent/manager.py

import os
import yaml
from agent.agent import Agent

class AgentManager:
    def __init__(self, config_file):
        self.agents = self.load_agents(config_file)

    def load_agents(self, config_file):
        agents = {}
        with open(config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        for agent_config in config.get('agents', []):
            name = agent_config.get('name')
            agents[name] = Agent(
                name=name,
                model_name=agent_config.get('model_name'),
                generation_config=agent_config.get('generation_config'),
                system_instruction=agent_config.get('system_instruction'),
                history=agent_config.get('history'),
            )
        return agents

    def get_agent(self, name):
        return self.agents.get(name)

    def list_agents(self):
        return list(self.agents.keys())