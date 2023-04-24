from typing import List, Optional

from pydantic import BaseModel


class LayerConfig(BaseModel):
    name: str
    description: Optional[str]
    requirements_file: str
    compatible_runtimes: List[str]
    compatible_architectures: List[str]
