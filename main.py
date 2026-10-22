"""Replace a local artifact atomically; temporary file shares the target filesystem."""
import os
from pathlib import Path
import tempfile


def atomic_write(path, data):
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'report.txt'
        atomic_write(path, b'synthetic report v1')
        print(path.read_text())
