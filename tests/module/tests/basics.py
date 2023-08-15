import os

from sync_env.sync_env import SyncEnv


class Env(SyncEnv):

    TEST = "test"
    VALUE = None
    NONE: str = None


env = Env()

if __name__ == "__main__":
    print(env.__dict__)
