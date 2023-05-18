import boto3

from src.models.layer_config import LayerConfig


class LambdaFunctionManager:
    """Manager for Lambda functions."""

    def __init__(self) -> None:
        self.client = boto3.client("lambda")

    def upload_layer(self, config: LayerConfig, archive_name: str) -> None:
        """Create or update a Lambda layer.
        If the layer already exists a new version is created.

        Args:
            config: Lambda Layer configuration object.
            archive_name: Name of the .zip file to use for the layer.

        """

        layer_content = open(archive_name, "rb").read()

        data = {
            "LayerName": config.name,
            "Content": {"ZipFile": layer_content},
            "CompatibleRuntimes": config.compatible_runtimes,
            "CompatibleArchitectures": config.compatible_architectures,
        }

        if config.description:
            data["Description"] = config.description

        response = self.client.publish_layer_version(**data)  # type: ignore[arg-type]
        if response["ResponseMetadata"]["HTTPStatusCode"] != 201:
            raise Exception
