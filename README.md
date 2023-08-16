# python-sync-env
easy load environment methods for python

## 2023/08/16

似たライブラリがあった…
<https://pypi.org/project/myenv/>
<https://blog.utgw.net/entry/2021/07/03/115713>

# basic usage

## environment

```batch
NONE=のん
```

## python file
```python
from sync_env import SyncEnv

class Env(SyncEnv):

    TEST = "test"
    VALUE = None
    NONE = None

env = Env()
```

## any file


```python

from any.file import env

assert env.NONE == "なん"

```

## output

```python

# ~~

if __name__ == "__main__":
    print(env.TEST)
    print(env.VALUE)
    print(env.NONE)
```

```log
test
None
のん
```

# generate

## generate script

```python
from sync_env import SyncEnv, GenerateEnv


class EnvA(SyncEnv):
    one = None
    two = None


class EnvB(SyncEnv):
    two = None
    three = None


ge = GenerateEnv([
    EnvA,
    EnvB
])

ge.generate()

```


## output

.env

```bat
one=
two=
three=

```
