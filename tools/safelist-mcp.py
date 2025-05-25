from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Dict, Any, List

mcp = FastMCP("Assemblyline Safelist Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def safelist_check(qhash: str) -> Dict[str, Any]:
    """
    Check if a hash exists in the safelist.
    :param qhash: Hash to check in the safelist.
    :return: Safelist object if present, otherwise empty.
    """
    return al_client.safelist(qhash)

@mcp.tool()
def safelist_add_update(safelist_object: Dict[str, Any]) -> Any:
    """
    Add a hash to the safelist, or update its sources if it exists.
    :param safelist_object: A dictionary with safelist details.
    :return: API response.
    """
    return al_client.safelist.add_update(safelist_object)

@mcp.tool()
def safelist_add_update_many(list_of_safelist_object: List[Dict[str, Any]]) -> Any:
    """
    Add or update a list of safelist objects.
    :param list_of_safelist_object: List of safelist dictionaries.
    :return: API response.
    """
    return al_client.safelist.add_update_many(list_of_safelist_object)

@mcp.tool()
def safelist_delete(safelist_id: str) -> Any:
    """
    Delete a safelist object by its ID.
    :param safelist_id: ID of the safelist object (hash or tag hash).
    :return: API response.
    """
    return al_client.safelist.delete(safelist_id)

@mcp.tool()
def safelist_set_enabled(safelist_id: str, enabled: bool) -> Any:
    """
    Set the enabled status of a safelist object by its ID.
    :param safelist_id: ID of the safelist object.
    :param enabled: True to enable, False to disable.
    :return: API response.
    """
    return al_client.safelist.set_enabled(safelist_id, enabled)
