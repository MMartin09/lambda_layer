import json
import os
import shutil
import subprocess
import sys
from functools import reduce
from typing import Any, Dict


def camel_to_snake_case(val: str) -> str:
    """Convert a given string from Camel Case to Snake Case."""
    return reduce(lambda x, y: x + ("_" if y.isupper() else "") + y, val).lower()


def compress_archive(archive_name: str, archive_source: str) -> None:
    """Compress an archive in a .zip file.

    Args:
        archive_name: The name of the archive file.
        archive_source: Directory to compress.

    """

    pathname, _ = os.path.splitext(archive_name)
    shutil.make_archive(base_name=pathname, format="zip", root_dir=archive_source)


def load_layer_config(file_path: str) -> Dict[str, Any]:
    """Load a layer config file.

    Args:
        file_path: Path to the config file.

    Returns:
        Layer configuration as dictionary.

    """

    with open(file_path) as config_file:
        layer_config = json.load(config_file)

    return layer_config


def install_requirements(requirements_file: str, target_dir: str) -> None:
    """Install python packages defined in a requirements file.

    Args:
        requirements_file: Path to the requirements file.
        target_dir: Directory where to install the packages.

    """

    target_dir = os.path.join(target_dir, "python")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            requirements_file,
            "-t",
            target_dir,
        ]
    )
