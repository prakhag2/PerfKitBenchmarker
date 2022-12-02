"""Errors for messaging_service_scripts."""


class EndToEnd:
  """Errors for end-to-end benchmark code."""

  class ReceivedUnexpectedObjectError(Exception):
    """Got an unexpected object from another process."""

  class SubprocessTimeoutError(Exception):
    """Subprocess output timed out."""

  class SubprocessFailedOperationError(Exception):
    """Subprocess reported a failure while performing an operation."""

  class PublisherFailedOperationError(SubprocessFailedOperationError):
    """Publisher subprocess reported a failure while performing an operation."""

  class ReceiverFailedOperationError(SubprocessFailedOperationError):
    """Receiver subprocess reported a failure while performing an operation."""

  class PullTimeoutOnReceiverError(Exception):
    """Signals a pull timeout in the receiver process."""
