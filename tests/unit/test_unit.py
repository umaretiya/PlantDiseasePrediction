import pytest
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError
from PlantDisease.utils.common import read_yaml


class Test_read_yaml:
    yaml_file = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml",
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_file[0]))

    def test_read_yaml_return_type(self):
        respons = read_yaml(Path(self.yaml_file[-1]))
        assert isinstance(respons, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", yaml_file)
    def test_read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)
