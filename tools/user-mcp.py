from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

mcp = FastMCP("Assemblyline User Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

# ===== USER PROFILE =====

@mcp.resource("user://{username}")
def get_user_profile(username: str) -> Dict[str, Any]:
    """
    Retrieve a user profile.

    Args:
        username (str): The username to retrieve the profile for.

    Returns:
        Dict[str, Any]: The user profile data as a dictionary.
    """
    return al_client.user(username)

@mcp.tool()
def add_user(username: str, user_data: Dict[str, Any]) -> Any:
    """
    Add a new user to the system.

    Args:
        username (str): The username to add.
        user_data (dict): The profile data for the user.

    Returns:
        Any: API response from the server.
    """
    return al_client.user.add(username, user_data)

@mcp.tool()
def delete_user(username: str) -> Any:
    """
    Delete a user from the system.

    Args:
        username (str): The username to remove.

    Returns:
        Any: API response from the server.
    """
    return al_client.user.delete(username)

@mcp.resource("user://all")
def list_users(query: str = "*:*", rows: int = 10, offset: int = 0, sort: str = "uname asc") -> List[Dict[str, Any]]:
    """
    List users in the system.

    Args:
        query (str): Query string for filtering users.
        rows (int): Number of users to return.
        offset (int): Index to start listing from.
        sort (str): Sorting order.

    Returns:
        List[Dict[str, Any]]: A list of user profile dictionaries.
    """
    return al_client.user.list(query=query, rows=rows, offset=offset, sort=sort)

@mcp.resource("user://submission_params/{username}")
def get_submission_params(username: str, profile: str = "default") -> Dict[str, Any]:
    """
    Get submission parameters for a user.

    Args:
        username (str): The user key.
        profile (str): Submission profile name.

    Returns:
        Dict[str, Any]: Submission parameters.
    """
    return al_client.user.submission_params(username, profile)

@mcp.tool()
def update_user(username: str, user_data: Dict[str, Any]) -> Any:
    """
    Update a user profile in the system.

    Args:
        username (str): Name of the user to update.
        user_data (dict): Updated profile data.

    Returns:
        Any: API response from the server.
    """
    return al_client.user.update(username, user_data)

@mcp.resource("user://whoami")
def whoami() -> Dict[str, Any]:
    """
    Return the currently logged in user and system configuration.

    Returns:
        Dict[str, Any]: Info about the current user and system.
    """
    return al_client.user.whoami()

@mcp.tool()
def user_tos(username: str) -> Any:
    """
    Agree to Terms of Service as a user.

    Args:
        username (str): Username agreeing to the terms.

    Returns:
        Any: API response from the server.
    """
    return al_client.user.tos(username)

# ===== AVATAR =====

@mcp.resource("user://avatar/{username}")
def get_user_avatar(username: str) -> Any:
    """
    Load a user's avatar.

    Args:
        username (str): User key.

    Returns:
        Any: Avatar data or metadata.
    """
    return al_client.user.avatar(username)

@mcp.tool()
def update_user_avatar(username: str, avatar: Any) -> Any:
    """
    Update a user's avatar.

    Args:
        username (str): User key.
        avatar (Any): New avatar content or metadata.

    Returns:
        Any: API response.
    """
    return al_client.user.avatar.update(username, avatar)

# ===== FAVORITES =====

@mcp.resource("user://favorites/{username}")
def get_user_favorites(username: str) -> Any:
    """
    Load the user's favorites.

    Args:
        username (str): User key.

    Returns:
        Any: Favorites data.
    """
    return al_client.user.favorites(username)

@mcp.tool()
def add_user_favorite(username: str, fav_type: str, fav_data: Dict[str, Any]) -> Any:
    """
    Add a favorite to a user's favorites.

    Args:
        username (str): User key.
        fav_type (str): Type of favorite.
        fav_data (dict): Data block of the favorite.

    Returns:
        Any: API response.
    """
    return al_client.user.favorites.add(username, fav_type, fav_data)

@mcp.tool()
def delete_user_favorite(username: str, fav_type: str, name: str) -> Any:
    """
    Remove a favorite from a user's favorites.

    Args:
        username (str): User key.
        fav_type (str): Type of favorite.
        name (str): Name of favorite.

    Returns:
        Any: API response.
    """
    return al_client.user.favorites.delete(username, fav_type, name)

@mcp.tool()
def update_user_favorites(username: str, favorites: Any) -> Any:
    """
    Update a user's favorite queries.

    Args:
        username (str): User key.
        favorites (Any): New favorites data.

    Returns:
        Any: API response.
    """
    return al_client.user.favorites.update(username, favorites)

# ===== QUOTAS =====

@mcp.resource("user://quotas/{username}")
def get_user_quotas(username: str) -> Any:
    """
    Get the current user's quotas.

    Args:
        username (str): User key.

    Returns:
        Any: Quota information.
    """
    return al_client.user.quotas(username)

# ===== SETTINGS =====

@mcp.resource("user://settings/{username}")
def get_user_settings(username: str) -> Any:
    """
    Get the current user's settings.

    Args:
        username (str): User key.

    Returns:
        Any: User settings.
    """
    return al_client.user.settings(username)

@mcp.tool()
def update_user_settings(username: str, settings: Dict[str, Any]) -> Any:
    """
    Update the user's settings.

    Args:
        username (str): User key.
        settings (dict): New settings data.

    Returns:
        Any: API response.
    """
    return al_client.user.setti_
