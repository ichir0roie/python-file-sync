# python-file-sync
easy load environment methods for python

# basic

## environment

```batch
NONE=のん
```

## python file
```python
class Env(SyncEnv):

    TEST = "test"
    VALUE = None
    NONE: str = None

env = Env()
```

## output

```python
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

TODO