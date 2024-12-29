from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Present data in a tabular format"],
    show_tool_calls=True,
    markdown=True
)

agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent.print_response("Should I buy the Nvidia Stock?")
# response = agent.run("What is going on with Border Gavaskar Tropy 2024-25")
# result = response.get_content_as_string()
# print(f"Response: {result}")