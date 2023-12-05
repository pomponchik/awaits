from typing import Any

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


class QueueProtocol(Protocol):
    def put_nowait(self, item: Any) -> None:
        ...  # pragma: no cover

    def qsize(self) -> int:
        ...  # pragma: no cover
