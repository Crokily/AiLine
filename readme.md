# AiLine

[English Version](#english-version)

一个轻量级的 AI Agent 工作流框架，支持配置和管理多个 AI Agent，并将它们组合成工作流进行串行处理。

## 特性

- 支持多个 AI Agent 的配置和管理
- 支持将多个 Agent 组合成工作流
- 提供本地调用和 API 两种使用方式
- 基于配置文件的 Agent 定义
- 轻量级设计，易于理解和扩展

## 项目结构

```
project/
│
├── main.py           # 本地直接调用的主程序
├── app.py            # Flask API 程序
├── config/
│   └── agents.yaml   # 代理配置文件
├── agent/
│   ├── __init__.py
│   ├── agent.py      # Agent 类
│   └── manager.py    # AgentManager 类
├── workflow/
│   ├── __init__.py
│   └── workflow.py   # Workflow 类
├── ui/
│   ├── __init__.py
│   └── cli.py        # CLI 类
│   └── handler.py        # 处理请求业务逻辑
```

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 配置 Agent

在 `config/agents.yaml` 中定义 Agent：

```yaml
agents:
  - name: translator
    model_name: "gemini-1.5-flash-8b"
    system_instruction: |
      你是一个中译英的常用英语表达翻译器...
    history:
      - role: user
        parts:
          - "我是一个资深的后端开发专家，精通使用python flask开发后端"
      - role: model
        parts:
          - "1.  I'm a **senior backend developer**,...
```

### 2. 本地使用

```bash
python main.py
```

### 3. API 调用

启动服务器：
```bash
python app.py
```

发送请求：
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "text": "我想去图书馆学习",
  "agents": ["translator"]
}' http://localhost:5000/process
```

## 技术栈

- Python 3.8+
- Flask
- Google Generative AI
- PyYAML

## 开发难点与解决方案

### 1. Agent 的封装与管理

**难点**：需要灵活管理多个不同配置的 Agent

**解决方案**：使用工厂模式和配置文件

```python
class AgentManager:
    def __init__(self, config_file):
        self.agents = self.load_agents(config_file)

    def load_agents(self, config_file):
        agents = {}
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        for agent_config in config.get('agents', []):
            name = agent_config.get('name')
            agents[name] = Agent(**agent_config)
        return agents
```

### 2. 工作流的实现

**难点**：需要支持多个 Agent 的串行处理

**解决方案**：使用责任链模式

```python
class Workflow:
    def __init__(self, agents):
        self.agents = agents

    def run(self, input_text):
        text = input_text
        for agent in self.agents:
            text = agent.process(text)
        return text
```

## 涉及的设计模式

- 工厂模式：Agent 的创建和管理
- 责任链模式：工作流的实现
- 策略模式：不同 Agent 的行为封装
- 单例模式：AgentManager 的实现

---

# English Version

A lightweight AI Agent workflow framework that supports configuring and managing multiple AI Agents and combining them into sequential workflows.

## Features

- Support for multiple AI Agent configuration and management
- Support for combining multiple Agents into workflows
- Provides both local and API usage
- Configuration file-based Agent definition
- Lightweight design, easy to understand and extend

## Project Structure

```
project/
│
├── main.py           # Local execution program
├── app.py            # Flask API program
├── config/
│   └── agents.yaml   # Agent configuration file
├── agent/
│   ├── __init__.py
│   ├── agent.py      # Agent class
│   └── manager.py    # AgentManager class
├── workflow/
│   ├── __init__.py
│   └── workflow.py   # Workflow class
├── ui/
│   ├── __init__.py
│   └── cli.py        # CLI class
│   └── handler.py        # Handling the request logic
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Configure Agent

Define Agents in `config/agents.yaml`:

```yaml
agents:
  - name: translator
    model_name: "gemini-1.5-flash-8b"
    system_instruction: |
      You are a Chinese to English translator...
    history:
      - role: user
        parts:
          - "我是一个资深的后端开发专家，精通使用python flask开发后端"
      - role: model
        parts:
          - "1.  I'm a **senior backend developer**,...
```

### 2. Local Usage

```bash
python main.py
```

### 3. API Usage

Start server:
```bash
python app.py
```

Send request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "text": "I want to study in the library",
  "agents": ["translator"]
}' http://localhost:5000/process
```

## Tech Stack

- Python 3.8+
- Flask
- Google Generative AI
- PyYAML

## Development Challenges and Solutions

### 1. Agent Encapsulation and Management

**Challenge**: Need to flexibly manage multiple Agents with different configurations

**Solution**: Use Factory Pattern and configuration file

```python
class AgentManager:
    def __init__(self, config_file):
        self.agents = self.load_agents(config_file)

    def load_agents(self, config_file):
        agents = {}
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        for agent_config in config.get('agents', []):
            name = agent_config.get('name')
            agents[name] = Agent(**agent_config)
        return agents
```

### 2. Workflow Implementation

**Challenge**: Need to support sequential processing of multiple Agents

**Solution**: Use Chain of Responsibility Pattern

```python
class Workflow:
    def __init__(self, agents):
        self.agents = agents

    def run(self, input_text):
        text = input_text
        for agent in self.agents:
            text = agent.process(text)
        return text
```

## Design Patterns Used

- Factory Pattern: Agent creation and management
- Chain of Responsibility Pattern: Workflow implementation
- Strategy Pattern: Agent behavior encapsulation
- Singleton Pattern: AgentManager implementation

## License

[MIT License](LICENSE)