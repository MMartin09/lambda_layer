import os.path
import pathlib
import tempfile

import typer

from src.managers.lambda_function import LambdaFunctionManager
from src.models.layer_config import LayerConfig
from src.utils import (
    camel_to_snake_case,
    compress_archive,
    install_requirements,
    load_layer_config,
)

app = typer.Typer()


@app.command()
def main(config_file: str):
    layer_config = load_layer_config(config_file)
    for layer in layer_config["layers"]:
        requirements_file = pathlib.Path(
            os.path.join(os.path.dirname(config_file), layer["requirements"])
        )

        layer_obj = LayerConfig(name=layer["name"], **layer["config"])

        temp_install_dir = tempfile.TemporaryDirectory()

        requirements_archive = os.path.join(
            temp_install_dir.name, camel_to_snake_case(layer_obj.name) + ".zip"
        )

        install_requirements(str(requirements_file), temp_install_dir.name)
        compress_archive(requirements_archive, temp_install_dir.name)

        lambda_function_manager = LambdaFunctionManager()
        lambda_function_manager.upload_layer(layer_obj, requirements_archive)

        temp_install_dir.cleanup()


if __name__ == "__main__":
    app()
