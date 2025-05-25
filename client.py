from smolagents import ToolCollection
from langchain_mcp_adapters.tools import load_mcp_tools

from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp import ClientSession

import asyncio

server_parameters = StdioServerParameters(
        command="uv",
        args=["run", "server.py"]
    )

def run_smolagents_tools():
    with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tools:
        print("SmolAgents tools:")
        print("\n".join(f"{tool.name}: {tool.description}" for tool in tools.tools), "\n")

async def run_langchain_tools():
    async with stdio_client(server_parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            print("Langchain tools:")
            print("\n".join(f"{tool.name}: {tool.description}" for tool in tools), "\n")


if __name__ == "__main__":
    
    print("Starting SmoleAgent tools...")
    run_smolagents_tools()

    print("Starting Langchain tools...")
    asyncio.run(run_langchain_tools())