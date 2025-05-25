from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

mcp = FastMCP("Assemblyline Service Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.resource("service://{service_name}")
def get_service_config(service_name: str, version: Optional[str] = None) -> Dict[str, Any]:
    """
    Load the configuration for a given service, optionally for a specific version.
    """
    return al_client.service(service_name, version=version)

@mcp.tool()
def add_service(service_manifest_yaml: str) -> Any:
    """
    Add a new service using its YAML manifest.
    """
    return al_client.service.add(service_manifest_yaml)

@mcp.tool()
def backup_services() -> str:
    """
    Create a backup of the current system configuration (returns the backup as string).
    """
    return al_client.service.backup()

@mcp.resource("service://constants")
def get_service_constants() -> Dict[str, Any]:
    """
    Get global service constants.
    """
    return al_client.service.constants()

@mcp.tool()
def delete_service(service_name: str) -> Any:
    """
    Remove a service from the system.
    """
    return al_client.service.delete(service_name)

@mcp.resource("service://all")
def list_services() -> List[Dict[str, Any]]:
    """
    List all service configurations of the system.
    """
    return al_client.service.list()

@mcp.tool()
def restore_services(backup_yaml: str) -> Any:
    """
    Restore an old backup of the system configuration.
    """
    return al_client.service.restore(backup_yaml)

@mcp.tool()
def set_service(service_name: str, service_data: Dict[str, Any]) -> Any:
    """
    Calculate and apply the configuration delta for a service.
    """
    return al_client.service.set(service_name, service_data)

@mcp.resource("service://stats/{service_name}")
def get_service_stats(service_name: str, version: Optional[str] = None) -> Dict[str, Any]:
    """
    Get statistics for a given service, optionally for a specific version.
    """
    return al_client.service.stats(service_name, version=version)

@mcp.tool()
def update_service(
    name: str,
    image: str,
    tag: str,
    username: Optional[str] = None,
    password: Optional[str] = None
) -> Any:
    """
    Update a given service with a new container image and tag. Supports optional docker registry credentials.
    """
    return al_client.service.update(name, image, tag, username=username, password=password)

@mcp.resource("service://updates")
def check_service_updates() -> Dict[str, Any]:
    """
    Check for potential updates for services.
    """
    return al_client.service.updates()

@mcp.resource("service://versions/{service_name}")
def list_service_versions(service_name: str) -> List[str]:
    """
    List the different versions of a given service.
    """
    return al_client.service.versions(service_name)
