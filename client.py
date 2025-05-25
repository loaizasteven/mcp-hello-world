from smolagents import ToolCollection
from mcp.client.stdio import StdioServerParameters

server_parameters = StdioServerParameters(
    command="uv",
    args=["run", "server.py"]
)

# Create a collection of tools with smolagents
with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tools:
    print("\n".join(f"{tool.name}: {tool.description}" for tool in tools.tools))
    