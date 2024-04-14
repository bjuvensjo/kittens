Some kittens for Kitty terminal

## Setup

Install [uv](https://github.com/astral-sh/uv), e.g.

    pipx install uv

Create virtual environment and activate it

    uv venv -p 3.12

    # On macOS and Linux.
    source .venv/bin/activate

    # On Windows.
    .venv\Scripts\activate  
    
Export dependencies to requirements.txt

    uv pip compile pyproject.toml -o requirements.txt --extra dev --extra test

Install exported requirements in virtual environment

    uv pip install -r requirements.txt

Below are the setup commands for easy copy paste into a terminal:

```bash
uv venv -p 3.12
source .venv/bin/activate
uv pip compile pyproject.toml -o requirements.txt --extra dev --extra test
uv pip install -r requirements.txt
pytest
```

