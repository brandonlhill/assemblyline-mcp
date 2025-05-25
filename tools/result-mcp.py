from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import List, Optional, Dict, Any

mcp = FastMCP("Assemblyline Result Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_result(key: str) -> Dict[str, Any]:
    """
    Return the result with the given key.
    :param key: Result key.
    :return: The result object.
    """
    return al_client.result(key)

@mcp.tool()
def get_result_error(key: str) -> Dict[str, Any]:
    """
    Return the error object with the given key.
    :param key: Error key.
    :return: The error object.
    """
    return al_client.result.error(key)

@mcp.tool()
def get_multiple_results(
    result: Optional[List[str]] = None,
    error: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Get multiple result and error objects at the same time.
    :param result: List of result keys.
    :param error: List of error keys.
    :return: A dictionary with found results and errors.
    """
    result = result if result is not None else []
    error = error if error is not None else []
    return al_client.result.multiple(result=result, error=error)
