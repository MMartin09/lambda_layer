import json
import os.path
import shutil
import subprocess
import sys
from typing import Dict

from src.managers.lambda_function import LambdaFunctionManager
from src.models.layer_config import LayerConfig
from src.utils import camel_to_snake_case


def load_layer_config(file_path: str) -> Dict:
    with open(file_path) as config_file:
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


def main():
    requirements_directory = "../example/requirements/"

    layer_config = load_layer_config("../example/layer_config.json")
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

        lambda_function_manager = LambdaFunctionManager()
        lambda_function_manager.upload_layer(layer_obj, requirements_archive)

        shutil.rmtree(requirements_dir)
        os.remove(requirements_archive)


if __name__ == "__main__":
    main()
