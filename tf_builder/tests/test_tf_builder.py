"""
Unit and regression test for the tf_builder package.
"""

# Import package, test suite, and other packages as needed
import tf_builder
import pytest
import sys

def test_tf_builder_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "tf_builder" in sys.modules
