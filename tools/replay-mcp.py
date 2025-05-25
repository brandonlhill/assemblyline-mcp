from fastmcp import FastMCP
from assemblyline_client import get_client
from typing import Any, Dict, List, Optional

mcp = FastMCP("Assemblyline Replay Subserver")
al_client = get_client("https://your-assemblyline-instance", auth=('username', 'password'))

@mcp.tool()
def get_replay_checkpoint(m_type: str) -> Any:
    """
    Get the checkpoint of a given type for processing in a worker.
    :param m_type: Message type (badlist, safelist, workflow)
    :return: The checkpoint object.
    """
    return al_client.replay.get_checkpoint(m_type)

@mcp.tool()
def get_replay_message(m_type: str) -> Any:
    """
    Get the next message of a given type for processing in a worker.
    :param m_type: Message type (alert, submission, file)
    :return: The message object.
    """
    return al_client.replay.get_message(m_type)

@mcp.tool()
def put_replay_checkpoint(m_type: str, checkpoint: str) -> Any:
    """
    Set checkpoint for message type in the Replay for processing in a worker.
    :param m_type: Message type (badlist, safelist, workflow)
    :param checkpoint: Date string or "*" to set checkpoint value
    :return: The result of the operation.
    """
    return al_client.replay.put_checkpoint(m_type, checkpoint)

@mcp.tool()
def put_replay_message(m_type: str, message: Dict[str, Any]) -> Any:
    """
    Put a message in the replay queues for processing in a worker.
    :param m_type: Message type (alert, submission, file)
    :param message: The message to be queued.
    :return: The result of the operation.
    """
    return al_client.replay.put_message(m_type, message)

@mcp.tool()
def replay_request(index: str, doc_id: str) -> Any:
    """
    Request an alert or a submission to be transferred to another system.
    :param index: Document type (alert or submission)
    :param doc_id: Document ID
    :return: The requested document.
    """
    return al_client.replay.request(index, doc_id)

@mcp.tool()
def set_replay_complete(index: str, doc_id: str) -> Any:
    """
    Mark an alert or submission as successfully transferred to another system.
    :param index: Document type (alert or submission)
    :param doc_id: Document ID
    :return: The result of the operation.
    """
    return al_client.replay.set_complete(index, doc_id)

@mcp.tool()
def set_replay_bulk_pending(
    index: str,
    query: str,
    filter_queries: List[str],
    max_docs: int
) -> Any:
    """
    Set the replay pending state on alerts or submissions matching the queries.
    :param index: Document type (alert or submission)
    :param query: Main query string
    :param filter_queries: Additional filter query strings
    :param max_docs: Maximum number of documents to modify
    :return: The result of the bulk pending operation.
    """
    return al_client.replay.set_bulk_pending(index, query, filter_queries, max_docs)
