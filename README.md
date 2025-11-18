# **Project Template**
This is an example README.md template for a Spekboom project. 

## Setup
Set up `uv` & sync
```bash
source bash/uv_setup.sh
```
Run tests with pytest
```bash
uv run pytest -rAP tests/test_module.py
```
Create a `launch.json` in `.vscode`
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: debug.py",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/debug/debug.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            },
            "justMyCode": true
        }
    ]
}
```

## Subheading: Some More Things to Think About
- more things
- something more

