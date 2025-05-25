from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

mcp = FastMCP("Assemblyline Signature Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))


@mcp.resource("signature://{signature_id}")
def get_signature(signature_id: str) -> Dict[str, Any]:
    """
    Return the signature with the given ID.
    """
    return al_client.signature(signature_id)

@mcp.tool()
def add_update_signature(data: Dict[str, Any], dedup_name: bool = True) -> Dict[str, Any]:
    """
    Add or update a signature.
    :param data: Dict with signature details.
    :param dedup_name: Deduplicate by name before insert (default: True).
    """
    return al_client.signature.add_update(data, dedup_name=dedup_name)

@mcp.tool()
def add_update_signatures(
    source: str, sig_type: str, data: List[Dict[str, Any]], dedup_name: bool = True
) -> Dict[str, Any]:
    """
    Add or update multiple signatures.
    :param source: Source of the signature.
    :param sig_type: Type of signature.
    :param data: List of signature dicts.
    :param dedup_name: Deduplicate by name before insert (default: True).
    """
    return al_client.signature.add_update_many(source, sig_type, data, dedup_name=dedup_name)

@mcp.tool()
def change_signature_status(signature_id: str, status: str) -> Dict[str, Any]:
    """
    Change the status of a signature (e.g. DEPLOYED, NOISY, DISABLED, TESTING, STAGING).
    """
    return al_client.signature.change_status(signature_id, status)

@mcp.tool()
def clear_signature_status(signature_id: str) -> Dict[str, Any]:
    """
    Clear the user's status change for a signature.
    """
    return al_client.signature.clear_status(signature_id)

@mcp.tool()
def delete_signature(signature_id: str) -> Dict[str, Any]:
    """
    Delete a signature by ID.
    """
    return al_client.signature.delete(signature_id)

@mcp.tool()
def download_signatures(query: Optional[str] = None) -> str:
    """
    Download signatures, optionally filtered by a Lucene query. Returns text data.
    """
    return al_client.signature.download(query=query)

@mcp.resource("signature://stats")
def signature_stats() -> Dict[str, Any]:
    """
    Gather statistics about all the signatures in the system.
    """
    return al_client.signature.stats()

@mcp.tool()
def signatures_update_available(since: str = '', sig_type: str = '*') -> Dict[str, Any]:
    """
    Check if updated signatures are available since a certain date, optionally filtered by type.
    """
    return al_client.signature.update_available(since=since, sig_type=sig_type)

# =============== SIGNATURE SOURCES ===============

@mcp.resource("signature://sources")
def get_signature_sources() -> List[Dict[str, Any]]:
    """
    Get all signature sources.
    """
    return al_client.signature.sources()

@mcp.tool()
def add_signature_source(service: str, new_source: Dict[str, Any]) -> Any:
    """
    Add a signature source for a given service.
    """
    return al_client.signature.sources.add(service, new_source)

@mcp.tool()
def delete_signature_source(service: str, name: str) -> Any:
    """
    Delete a signature source by name for a given service.
    """
    return al_client.signature.sources.delete(service, name)

@mcp.tool()
def update_signature_source(service: str, name: str, source_data: Dict[str, Any]) -> Any:
    """
    Update a signature source by name for a given service.
    """
    return al_client.signature.sources.update(service, name, source_data)
