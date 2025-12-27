# Directory Structure

```bash
east-side-server/
├── after-work/
├── assignments/
├── docs/
├── orchids/
├── uploads/          # Temporary staging only
├── images/
├── index.html
├── server.py
├── success.png
└── venv/
```

## Logging
> All uploads and routing actions are logged using Python’s logging module.
> Each successful upload produces a log entry confirming:
- Upload completion
- Filename evaluated
- Routing destination

This allows easy verification and troubleshooting without additional tooling.
