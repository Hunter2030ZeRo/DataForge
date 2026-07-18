from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Literal

Transform = Callable[..., dict[str, Any]]
Predicate = Callable[..., bool]

ExecutionMode = Literal["auto", "safe", "debug", "fast"]

@dataclass(frozen=True, slots=True)
class MapOperation:
    function: Transform
    batched: bool | None = None
    batch_size: int | None = None
    num_workers: int | None = None
    remove_columns: tuple[str, ...] = ()

@dataclass(frozen=True, slots=True)
class FilterOperation:
    function: Predicate
    batched: bool | None = None
    batch_size: int | None = None
    num_workers: int | None = None

Operation = MapOperation | FilterOperation
