from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List, Union

mcp = FastMCP("Assemblyline System Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def clear_system_message() -> Any:
    """
    Clear the current system message.
    """
    return al_client.system.clear_system_message()

@mcp.resource("system://system_message")
def get_system_message() -> Dict[str, Any]:
    """
    Get the current system message.
    """
    return al_client.system.get_system_message()

@mcp.tool()
def set_system_message(message_object: Dict[str, Any]) -> Any:
    """
    Set the current system message.
    Example: {"title": "...", "severity": "info", "message": "..."}
    """
    return al_client.system.set_system_message(message_object)

@mcp.resource("system://tag_safelist")
def get_tag_safelist() -> Any:
    """
    Get the current tag_safelist.yml file.
    """
    return al_client.system.get_tag_safelist()

@mcp.tool()
def set_tag_safelist(yaml_file: Union[str, Dict[str, Any]]) -> Any:
    """
    Set the current tag_safelist.yml file.
    """
    return al_client.system.set_tag_safelist(yaml_file)

@mcp.resource("system://classification_aliases")
def get_classification_aliases() -> Dict[str, Any]:
    """
    Get the current display aliases for the classification engine.
    """
    return al_client.system.get_classification_aliases()

@mcp.tool()
def set_classification_aliases(aliases: Dict[str, Any]) -> Any:
    """
    Save display aliases for the classification engine.
    Example: {"ORG_000000": {"name": "...", "short_name": "..."}, ...}
    """
    return al_client.system.set_classification_aliases(aliases)

@mcp.resource("system://metadata_suggestions")
def get_metadata_suggestions(key: Optional[str] = None) -> Any:
    """
    Get the current metadata suggestions. Optionally filter by key.
    """
    return al_client.system.get_metadata_suggestions(key)

@mcp.tool()
def set_metadata_suggestions(suggestions: Union[Dict[str, List[str]], List[str]], key: Optional[str] = None) -> Any:
    """
    Set the metadata suggestions.
    Can be a dict of lists per key, or a list of suggestions for a single key.
    """
    return al_client.system.set_metadata_suggestions(suggestions, key)
