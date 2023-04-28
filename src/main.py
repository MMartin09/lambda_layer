import json
import os.path
import shutil
import subprocess
import sys
from functools import reduce
from typing import Dict

import boto3

from src.models.layer_config import LayerConfig


def camel_to_snake_case(val: str) -> str:
    """Convert a given string from Camel Case to Snake Case."""
    return reduce(lambda x, y: x + ("_" if y.isupper() else "") + y, val).lower()


def load_layer_config() -> Dict:
    with open("../example/layer_config.json", "r") as config_file:
        layer_config = json.load(config_file)

    return layer_config


def install_requirements(requirements_file: str, archive_file: str) -> None:
    archive_file = os.path.join(archive_file, "python")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            requirements_file,
            "-t",
            archive_file,
        ]
    )


def compress_archive(archive_name: str, archive_source: str) -> None:
    pathname, _ = os.path.splitext(archive_name)

    shutil.make_archive(base_name=pathname, format="zip", root_dir=archive_source)


def upload_layer(client, config: LayerConfig, archive_name: str) -> None:
    layer_content = open(archive_name, "rb").read()

    response = client.publish_layer_version(
        LayerName=config.name,
        Description=config.description,
        Content={"ZipFile": layer_content},
        CompatibleRuntimes=config.compatible_runtimes,
        CompatibleArchitectures=config.compatible_architectures,
    )
    print(response)


def main():
    requirements_directory = "../example/requirements/"
    lambda_client = boto3.client("lambda")

    layer_config = load_layer_config()
    for layer in layer_config["layers"]:
        layer_obj = LayerConfig(**layer)

        requirements_file = os.path.join(
            requirements_directory, layer_obj.requirements_file
        )
        requirements_dir = "../example/requirements_dir/"
        requirements_archive = os.path.join(
            "../example", camel_to_snake_case(layer_obj.name) + ".zip"
        )

        install_requirements(requirements_file, requirements_dir)
        compress_archive(requirements_archive, requirements_dir)
        upload_layer(lambda_client, layer_obj, requirements_archive)

        shutil.rmtree(requirements_dir)
        os.remove(requirements_archive)


if __name__ == "__main__":
    main()
