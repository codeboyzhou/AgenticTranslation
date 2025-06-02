from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("mcp_server_translation")


@mcp.prompt()
def translate(text: str, language: str) -> str:
    """Translate text to a given language"""
    return f"Translation of '{text}' to '{language}' is '{text}'"


if __name__ == "__main__":
    mcp.run()
