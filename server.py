from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP(name="MCP-Server-Hello-World")

# Add simple tools, resources, and custom prompts
@mcp.tool()
def weather_tool(location: str) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Get the weather resource for a given location."""
    return f"Weather resource for {location}: sunny"

@mcp.prompt()
def weather_prompt(location: str) -> str:
    """Get a weather prompt for a given location."""
    return f"""You are a weather reporter. Weather report for {location}?"""

if __name__ == "__main__":
    # Start the server
    mcp.run()
