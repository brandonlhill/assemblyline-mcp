from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

# Initialize the FastMCP server
mcp = FastMCP("Assemblyline Badlist Subserver")

# Initialize the Assemblyline client
# Replace 'https://your-assemblyline-instance' with your actual Assemblyline URL
# and provide appropriate authentication credentials.
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_badlist_entry(badlist_type: str, value: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve a specific badlist entry by type and value.

    :param badlist_type: The type of the badlist entry (e.g., 'ip', 'domain', 'url').
    :param value: The value of the badlist entry to retrieve.
    :return: The badlist entry if found, otherwise None.
    """
    try:
        return al_client.badlist.get(badlist_type, value)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def add_badlist_entry(badlist_type: str, value: str, score: int, source: str, classification: str) -> Dict[str, Any]:
    """
    Add a new entry to the badlist.

    :param badlist_type: The type of the badlist entry (e.g., 'ip', 'domain', 'url').
    :param value: The value to add to the badlist.
    :param score: The score associated with the badlist entry.
    :param source: The source of the badlist entry.
    :param classification: The classification level of the badlist entry.
    :return: The result of the add operation.
    """
    try:
        return al_client.badlist.add(badlist_type, value, score, source, classification)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def delete_badlist_entry(badlist_type: str, value: str) -> Dict[str, Any]:
    """
    Delete a specific badlist entry by type and value.

    :param badlist_type: The type of the badlist entry (e.g., 'ip', 'domain', 'url').
    :param value: The value of the badlist entry to delete.
    :return: The result of the delete operation.
    """
    try:
        return al_client.badlist.delete(badlist_type, value)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def list_badlist_entries(badlist_type: str) -> List[str]:
    """
    List all badlist entries of a specific type.

    :param badlist_type: The type of badlist entries to list (e.g., 'ip', 'domain', 'url').
    :return: A list of badlist entry values.
    """
    try:
        return al_client.badlist.list(badlist_type)
    except Exception as e:
        return {"error": str(e)}
