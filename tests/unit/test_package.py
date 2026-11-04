"""Unit tests for the imu_lab package metadata."""

from importlib.metadata import version

import imu_lab


def test_version_matches_installed_metadata():
    """__version__ matches the installed package metadata."""
    assert imu_lab.__version__ == version("imu_lab")
