from typing import Protocol, Any


class QueueProtocol(Protocol):
    def put_nowait(self, item: Any) -> None:
        ...  # pragma: no cover

    def qsize(self) -> int:
        ...  # pragma: no cover
