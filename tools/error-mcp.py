from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

# Initialize the FastMCP server
mcp = FastMCP("Assemblyline Error Subserver")

# Initialize the Assemblyline client
# Replace 'https://your-assemblyline-instance' with your actual Assemblyline URL
# and provide appropriate authentication credentials.
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_error(sha256: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve a specific error entry by its SHA256 hash.

    :param sha256: The SHA256 hash of the file associated with the error.
    :return: The error entry if found, otherwise None.
    """
    try:
        return al_client.error.get(sha256)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def delete_error(sha256: str) -> Dict[str, Any]:
    """
    Delete a specific error entry by its SHA256 hash.

    :param sha256: The SHA256 hash of the file associated with the error.
    :return: The result of the delete operation.
    """
    try:
        return al_client.error.delete(sha256)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def list_errors() -> List[str]:
    """
    List all error entries.

    :return: A list of SHA256 hashes for all error entries.
    """
    try:
        return al_client.error.list()
    except Exception as e:
        return {"error": str(e)}
