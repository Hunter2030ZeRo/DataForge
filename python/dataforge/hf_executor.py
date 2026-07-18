from __future__ import annotations
from datasets import Dataset, DatasetDict
from .operation import FilterOperation, MapOperation, Operation


class HuggingFaceExecutor:
    def __init__(self, *, mode: str = "auto") -> None:
        if mode not in {"auto", "safe", "debug", "fast"}:
            raise ValueError(f"Unkown execution mode: {mode}")

        self.mode = mode

    def execute(
        self,
        dataset: Dataset | DatasetDict,
        operations: tuple[Operation, ...],
    ) -> Dataset | DatasetDict:
        current = dataset

        for operation in operations:
            if isinstance(operation, MapOperation):
                current = current.map(
                    operation.function,
                    batched=operation.batched or False,
                    batch_size=operation.batch_size,
                    num_proc=operation.num_workers,
                )
            elif isinstance(operation, FilterOperation):
                current = current.filter(
                    operation.function,
                    batched=operation.batched or False,
                    batch_size=operation.batch_size,
                    num_proc=operation.num_workers,
                )

        return current
