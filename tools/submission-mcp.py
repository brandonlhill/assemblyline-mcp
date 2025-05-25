from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Optional, Dict, Any, List

mcp = FastMCP("Assemblyline Submission Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

# ========== SUBMISSION ==========

@mcp.resource("submission://{sid}")
def get_submission(sid: str) -> Dict[str, Any]:
    """
    Retrieve the submission record for the given submission ID.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: Submission record as a dictionary.
    """
    return al_client.submission(sid)

@mcp.tool()
def delete_submission(sid: str) -> Any:
    """
    Delete the submission and all related records.

    Args:
        sid (str): Submission ID.

    Returns:
        Any: API response from the server.
    """
    return al_client.submission.delete(sid)

@mcp.tool()
def submission_file(
    sid: str, sha256: str,
    results: Optional[List[str]] = None,
    errors: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Get errors and results for a file within a specific submission.

    Args:
        sid (str): Submission ID.
        sha256 (str): File key (SHA256).
        results (Optional[List[str]]): List of extra result keys to include.
        errors (Optional[List[str]]): List of extra error keys to include.

    Returns:
        Dict[str, Any]: Submission file information.
    """
    return al_client.submission.file(sid, sha256, results=results, errors=errors)

@mcp.resource("submission://full/{sid}")
def get_submission_full(sid: str) -> Dict[str, Any]:
    """
    Retrieve the full result for a given submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: Full submission results.
    """
    return al_client.submission.full(sid)

@mcp.resource("submission://completed/{sid}")
def is_submission_completed(sid: str) -> bool:
    """
    Check if a submission is completed.

    Args:
        sid (str): Submission ID.

    Returns:
        bool: True if completed, False otherwise.
    """
    return al_client.submission.is_completed(sid)

@mcp.resource("submission://list")
def list_submissions(
    user: Optional[str] = None,
    group: Optional[str] = None,
    fq: Optional[str] = None,
    rows: int = 10,
    offset: int = 0,
    use_archive: bool = False,
    track_total_hits: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    List all submissions of a given user or group.

    Args:
        user (Optional[str]): Username to filter submissions.
        group (Optional[str]): Group name to filter submissions.
        fq (Optional[str]): Query to further filter the submission list.
        rows (int): Number of submissions to return.
        offset (int): Offset at which to start listing.
        use_archive (bool): Whether to also query the archive.
        track_total_hits (Optional[int]): Number of hits to track.

    Returns:
        List[Dict[str, Any]]: List of submission summaries.
    """
    return al_client.submission.list(
        user=user, group=group, fq=fq, rows=rows, offset=offset,
        use_archive=use_archive, track_total_hits=track_total_hits
    )

@mcp.resource("submission://report/{sid}")
def get_submission_report(sid: str) -> Dict[str, Any]:
    """
    Create a report for a submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: Submission report data.
    """
    return al_client.submission.report(sid)

@mcp.tool()
def set_submission_verdict(sid: str, verdict: str) -> Any:
    """
    Set the verdict of a submission.

    Args:
        sid (str): Submission ID.
        verdict (str): Verdict value ('malicious', 'non_malicious').

    Returns:
        Any: API response from the server.
    """
    return al_client.submission.set_verdict(sid, verdict)

@mcp.resource("submission://summary/{sid}")
def get_submission_summary(sid: str) -> Dict[str, Any]:
    """
    Retrieve the executive summary for a submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: Summary information.
    """
    return al_client.submission.summary(sid)

@mcp.resource("submission://tree/{sid}")
def get_submission_tree(sid: str) -> Dict[str, Any]:
    """
    Return the file hierarchy for a submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: File hierarchy/tree.
    """
    return al_client.submission.tree(sid)

# ========== LIVE (WATCH QUEUES) ==========

@mcp.resource("submission://live/message/{wq}")
def get_live_message(wq: str) -> Dict[str, Any]:
    """
    Get a message from the given watch queue.

    Args:
        wq (str): Watch queue name.

    Returns:
        Dict[str, Any]: Message data.
    """
    return al_client.live.get_message(wq)

@mcp.resource("submission://live/message_list/{wq}")
def get_live_message_list(wq: str) -> List[Dict[str, Any]]:
    """
    Get all current messages from the given watch queue.

    Args:
        wq (str): Watch queue name.

    Returns:
        List[Dict[str, Any]]: List of messages.
    """
    return al_client.live.get_message_list(wq)

@mcp.resource("submission://live/outstanding_services/{sid}")
def get_outstanding_services(sid: str) -> Dict[str, Any]:
    """
    List outstanding services and file counts for a submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Dict[str, Any]: Outstanding services and their file counts.
    """
    return al_client.live.outstanding_services(sid)

@mcp.tool()
def setup_watch_queue(sid: str) -> Any:
    """
    Set up a watch queue for a given submission.

    Args:
        sid (str): Submission ID.

    Returns:
        Any: API response from the server.
    """
    return al_client.live.setup_watch_queue(sid)
