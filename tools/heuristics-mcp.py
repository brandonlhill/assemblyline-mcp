from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Dict, Any

mcp = FastMCP("Assemblyline Heuristics Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_heuristic(heuristic_id: str) -> Dict[str, Any]:
    """
    Get a specific heuristic's details from the system.

    :param heuristic_id: ID of the heuristic.
    :return: The details of the heuristic as a dictionary.
    """
    return al_client.heuristics(heuristic_id)

@mcp.resource("heuristics://stats")
def heuristic_stats() -> Dict[str, Any]:
    """
    Gather statistics about all the heuristics in the system.

    :return: A dictionary containing statistics for all heuristics.
    """
    return al_client.heuristics.stats()
