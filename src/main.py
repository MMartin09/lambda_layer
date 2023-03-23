import json
import os.path
import subprocess
import sys
from typing import Optional

from pydantic import BaseModel


class LayerConfig(BaseModel):
    name: str
    description: Optional[str]
    requirements_file: str


def install_requirements() -> None:
    ...


def main():
    requirements_directory = "../example/requirements/"

    with open("../example/layer_config.json", "r") as config_file:
        layer_config = json.load(config_file)

    for layer in layer_config["layers"]:
        layer_obj = LayerConfig(**layer)

        requirements_file = os.path.join(requirements_directory, layer_obj.requirements_file)
        archive_file = "../example/my_archive/python/"

        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file, "-t", archive_file])


if __name__ == "__main__":
    main()
