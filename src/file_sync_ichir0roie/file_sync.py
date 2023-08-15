import os


class SyncEnvFile:

    def __init__(self) -> None:
        for key in dir(self):
            value = getattr(self, key)
            if key[0] == "_":
                continue
            env_value = os.getenv(key)
            setattr(self, key, env_value if env_value else value)
