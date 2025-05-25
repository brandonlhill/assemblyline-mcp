from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import List, Optional, Dict, Any, Union

mcp = FastMCP("Assemblyline HashSearch Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def hash_search(
    h: str,
    db: Optional[List[str]] = None,
    max_timeout: Optional[float] = None
) -> Dict[str, Any]:
    """
    Perform a hash search for the given md5, sha1, or sha256.

    :param h: The hash to search for (md5, sha1, or sha256).
    :param db: Optional list of data sources to query.
    :param max_timeout: Optional max time to wait for a response, in seconds.
    :return: Search result as a dict.
    """
    return al_client.hash_search(h, db=db, max_timeout=max_timeout)

@mcp.resource("hashsearch://data_sources")
def list_hashsearch_data_sources() -> List[str]:
    """
    Return the available hash search data sources.
    """
    return al_client.hash_search.list_data_sources()
