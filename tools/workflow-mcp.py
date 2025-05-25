from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Dict, Any, List

mcp = FastMCP("Assemblyline Workflow Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.resource("workflow://{workflow_id}")
def get_workflow(workflow_id: str) -> Dict[str, Any]:
    """
    Get the details for a workflow.

    Args:
        workflow_id (str): ID of the workflow to retrieve.

    Returns:
        Dict[str, Any]: Workflow details as a dictionary.
    """
    return al_client.workflow(workflow_id)

@mcp.tool()
def add_workflow(workflow: Dict[str, Any]) -> Any:
    """
    Add a workflow to the system.

    Args:
        workflow (Dict[str, Any]): Data describing the workflow.

    Returns:
        Any: API response from the server.
    """
    return al_client.workflow.add(workflow)

@mcp.tool()
def delete_workflow(workflow_id: str) -> Any:
    """
    Remove the specified workflow.

    Args:
        workflow_id (str): ID of the workflow to delete.

    Returns:
        Any: API response from the server.
    """
    return al_client.workflow.delete(workflow_id)

@mcp.resource("workflow://labels")
def get_workflow_labels() -> List[str]:
    """
    Return the list of potential labels for workflows.

    Returns:
        List[str]: List of workflow label strings.
    """
    return al_client.workflow.labels()

@mcp.resource("workflow://list")
def list_workflows(query: str = "*:*", rows: int = 10, offset: int = 0) -> List[Dict[str, Any]]:
    """
    List the potential workflows (paginated).

    Args:
        query (str): Query string to filter workflows.
        rows (int): Number of workflows to return.
        offset (int): Offset for pagination.

    Returns:
        List[Dict[str, Any]]: List of workflow dictionaries.
    """
    return al_client.workflow.list(query=query, rows=rows, offset=offset)

@mcp.tool()
def update_workflow(workflow_id: str, workflow: Dict[str, Any]) -> Any:
    """
    Update a workflow.

    Args:
        workflow_id (str): ID of the workflow to update.
        workflow (Dict[str, Any]): New workflow data.

    Returns:
        Any: API response from the server.
    """
    return al_client.workflow.update(workflow_id, workflow)
