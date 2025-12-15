from typing import Any, Protocol  # noqa: A005


class QueueProtocol(Protocol):
    def put_nowait(self, item: Any) -> None:
        ...  # pragma: no cover

    def qsize(self) -> int:
        ...  # pragma: no cover

    def get(self) -> Any:
        ...  # pragma: no cover

    def task_done(self) -> None:
        ...  # pragma: no cover
