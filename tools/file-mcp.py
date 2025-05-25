from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List, Union

mcp = FastMCP("Assemblyline File Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.resource("file://{sha256}/ascii")
def file_ascii(sha256: str) -> str:
    """
    Returns an ASCII representation of the file content for the given SHA256.
    Throws a Client exception if the file does not exist.
    """
    return al_client.file.ascii(sha256)

@mcp.resource("file://{sha256}/hex")
def file_hex(sha256: str, bytes_only: Optional[bool] = False, length: Optional[int] = None) -> str:
    """
    Returns a hexadecimal representation of the file for the given SHA256.
    Optionally, only the bytes or a specific length can be returned.
    Throws a Client exception if the file does not exist.
    """
    return al_client.file.hex(sha256, bytes_only=bytes_only, length=length)

@mcp.resource("file://{sha256}/info")
def file_info(sha256: str) -> Dict[str, Any]:
    """
    Returns information about the file with the given SHA256.
    """
    return al_client.file.info(sha256)

@mcp.tool()
def download_file(sha256: str, encoding: Optional[str] = None, sid: Optional[str] = None, password: Optional[str] = None) -> bytes:
    """
    Downloads the file with the given SHA256 and returns the content as bytes.
    """
    return al_client.file.download(sha256, encoding=encoding, sid=sid, password=password)

@mcp.resource("file://{sha256}/children")
def file_children(sha256: str) -> List[str]:
    """
    Returns the list of children for the file with the given SHA256.
    """
    return al_client.file.children(sha256)

@mcp.resource("file://{sha256}/result")
def file_result(sha256: str, service: Optional[str] = None) -> Any:
    """
    Returns all the results for the file, optionally filtered by service name.
    """
    return al_client.file.result(sha256, service=service)

@mcp.resource("file://{sha256}/score")
def file_score(sha256: str) -> int:
    """
    Returns the latest score for the file with the given SHA256.
    """
    return al_client.file.score(sha256)

@mcp.resource("file://{sha256}/strings")
def file_strings(sha256: str) -> List[str]:
    """
    Returns all strings found in the file with the given SHA256.
    """
    return al_client.file.strings(sha256)

@mcp.tool()
def delete_from_filestore(sha256: str) -> Dict[str, Any]:
    """
    Deletes the file from the filestore without deleting the file record.
    """
    return al_client.file.delete_from_filestore(sha256)
