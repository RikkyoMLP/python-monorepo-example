# Python Monorepo Example

This is a monorepo example for Python using [uv](https://docs.astral.sh/uv/).

## Usage

### Install uv

```bash
# Install via pip
pip install uv
# Or via curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone the repository

```bash
git clone --recursive https://github.com/RikkyoMLP/python-monorepo-example.git
cd python-monorepo-example
```

### Install dependencies

```bash
uv sync
```

## Run example

```bash
uv run example_monorepo_usage.py
```

This will create a plot in current project directory.
