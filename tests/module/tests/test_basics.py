import os

from sync_env import SyncEnv
import pytest

os.environ["NONE"] = "のん"


class Env(SyncEnv):

    TEST = "test"
    VALUE = None
    NONE: str = None


@pytest.fixture
def env():
    env = Env()
    return env


def test_(env: Env):
    assert env.TEST == "test"
    assert env.VALUE == None
    assert env.NONE == "のん"


if __name__ == "__main__":
    print(Env().__dict__)
