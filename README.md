# zeppos_core
Python library with miscellaneous functionality.

# Purpose
Any python functionality that really is too small to fit in its own library is contained with in this package.

The idea is; when a functionality becomes too large for the library,
it will be split-off into its own library. But until then, it lives here.

## Setup Instructions
### pip
```
pip install zeppos-core
```
### pipenv
```
pipenv install zeppos-core
```

## Usage

- Timer
```
from zeppos_core.timer import Timer

def main():
    timer = Timer()
    timer.start_timer()
    timer.pause(time_in_seconds=2)
    timer.stop_timer()

    print(f"Time Elapsed In Seconds: {timer.time_elapsed_in_seconds}")


if __name__ == '__main__':
    main()
```
 