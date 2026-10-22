# Atomic Artifacts

Atomic local artifact replacement using same-filesystem temporary files.

Writes are flushed and fsynced before atomic replacement. Temporary files share the destination filesystem and are cleaned up on failure.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
