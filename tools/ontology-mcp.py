from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import List, Union, Optional, Dict, Any

mcp = FastMCP("Assemblyline Ontology Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_ontology_alert(
    alert_id: str,
    sha256s: Optional[Union[List[str], str]] = None,
    services: Optional[Union[List[str], str]] = None
) -> List[Dict[str, Any]]:
    """
    Get all ontology records for a given alert.

    :param alert_id: Alert ID to get ontology records for.
    :param sha256s: Single or list of sha256 to get ontology records for (default: all).
    :param services: Single or list of services to get ontology records for (default: all).
    :return: List of ontology records as dictionaries.
    """
    sha256s = sha256s if sha256s is not None else []
    services = services if services is not None else []
    return al_client.ontology.alert(alert_id, sha256s=sha256s, services=services)

@mcp.tool()
def get_ontology_file(
    sha256: str,
    services: Optional[Union[List[str], str]] = None,
    all_versions: bool = False
) -> List[Dict[str, Any]]:
    """
    Get all ontology records for a given file.

    :param sha256: SHA256 hash to get ontology records for.
    :param services: Single or list of services to get ontology records for (default: all).
    :param all_versions: Get all versions of ontology records if True.
    :return: List of ontology records as dictionaries.
    """
    services = services if services is not None else []
    return al_client.ontology.file(sha256, services=services, all=all_versions)

@mcp.tool()
def get_ontology_submission(
    sid: str,
    sha256s: Optional[Union[List[str], str]] = None,
    services: Optional[Union[List[str], str]] = None
) -> List[Dict[str, Any]]:
    """
    Get all ontology records for a given submission.

    :param sid: Submission ID to get ontology records for.
    :param sha256s: Single or list of sha256 to get ontology records for (default: all).
    :param services: Single or list of services to get ontology records for (default: all).
    :return: List of ontology records as dictionaries.
    """
    sha256s = sha256s if sha256s is not None else []
    services = services if services is not None else []
    return al_client.ontology.submission(sid, sha256s=sha256s, services=services)
