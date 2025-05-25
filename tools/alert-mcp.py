from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import List, Dict, Any, Optional

# Initialize FastMCP instance
mcp = FastMCP("AssemblylineAlertTools")

# Initialize the Assemblyline client
# Replace 'https://your-assemblyline-instance' with your actual Assemblyline URL
# and provide appropriate authentication credentials.
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_alert(alert_id: str) -> Dict[str, Any]:
    """
    Retrieve a single alert by its alert ID.
    """
    return al_client.alert.get(alert_id)


@mcp.tool()
def search_alerts(query: str, rows: int = 25, offset: int = 0) -> List[Dict[str, Any]]:
    """
    Search for alerts matching a query string.
    """
    return list(al_client.alert.search(query, rows=rows, offset=offset))


@mcp.tool()
def add_alert_label(alert_id: str, labels: List[str]) -> Dict[str, Any]:
    """
    Add one or more labels to a given alert.
    """
    return al_client.alert.add_label(alert_id, labels)


@mcp.tool()
def get_alert_labels(query: Optional[str] = None) -> List[str]:
    """
    Retrieve all alert labels or filter by query.
    """
    return al_client.alert.labels(query) if query else al_client.alert.labels()


@mcp.tool()
def get_alert_statistics(query: Optional[str] = None) -> Dict[str, Any]:
    """
    Get statistics for alerts matching a query.
    """
    return al_client.alert.statistics(query)


@mcp.tool()
def get_alert_priorities(query: Optional[str] = None) -> Dict[str, int]:
    """
    Get priority breakdown for alerts matching a query.
    """
    return al_client.alert.priorities(query)


@mcp.tool()
def get_alert_timeline(alert_id: str) -> List[Dict[str, Any]]:
    """
    Get the timeline events for a specific alert.
    """
    return al_client.alert.timeline(alert_id)


@mcp.tool()
def archive_alert(alert_id: str) -> Dict[str, Any]:
    """
    Archive a specific alert.
    """
    return al_client.alert.archive(alert_id)


@mcp.tool()
def escalate_alert(alert_id: str) -> Dict[str, Any]:
    """
    Escalate a specific alert.
    """
    return al_client.alert.escalate(alert_id)


@mcp.tool()
def get_alert_file(alert_id: str) -> str:
    """
    Get the SHA256 hash for the file linked to the alert.
    """
    return al_client.alert.file(alert_id)

