from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class StorageFile(BaseModel):
    name: str
    kind: str
    owner: bool
    link: str
    file: List[Optional[str]]
