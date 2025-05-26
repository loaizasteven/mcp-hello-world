# Basic example of how to use the MCP client with SmolAgents and Langchain tools

from smolagents import ToolCollection, InferenceClientModel, CodeAgent
from langchain_mcp_adapters.tools import load_mcp_tools

from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp import ClientSession

import asyncio

server_parameters = StdioServerParameters(
        command="uv",
        args=["run", "server.py"]
    )

def run_smolagents_tools(location: str = "Tokyo") -> str:
    with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tools:
        print("SmolAgents tools:")
        print("\n".join(f"{tool.name}: {tool.description}" for tool in tools.tools), "\n")
        response = weather_agent(tool_collection= tools, location=location)
        return response
    
def weather_agent(tool_collection:ToolCollection, location: str, model_id:str = "Qwen/Qwen2.5-Coder-32B-Instruct") -> str:
    """Create a CodeAgent instance with the model and tools from the MCP server."""
    model = InferenceClientModel(model_id=model_id)
    agent = CodeAgent(tools=tool_collection.tools, model=model)

    return agent.run(f"What's the weather in {location}?")

async def run_langchain_tools():
    async with stdio_client(server_parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            print("Langchain tools:")
            print("\n".join(f"{tool.name}: {tool.description}" for tool in tools), "\n")


if __name__ == "__main__":

    print("Starting SmoleAgent tools...")
    location = "Tokyo"
    run_smolagents_tools(location=location)

    print("Starting Langchain tools...")
    asyncio.run(run_langchain_tools())
