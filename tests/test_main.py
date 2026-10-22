import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'report'
            m.atomic_write(path,b'old')
            m.atomic_write(path,b'new')
            self.assertEqual(path.read_bytes(),b'new')
            self.assertEqual(len(list(Path(directory).iterdir())),1)
