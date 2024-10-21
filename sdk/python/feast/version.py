from importlib.metadata import PackageNotFoundError, version


def get_version():
    """Returns version information of the Feast Python Package."""
    try:
        sdk_version = "0.40.1"
    except PackageNotFoundError:
        sdk_version = "unknown"
    return sdk_version
