from typing import Protocol

class QueueProtocol(Protocol):
    def put_nowait(self, item: Any) -> None:
        ...  # pragma: no cover
