import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import install
from build import portable_text
from validate import validate


class PackageTests(unittest.TestCase):
    def test_package(self):
        self.assertEqual(validate(), (ROOT / 'VERSION').read_text().strip())

    def test_portable_prompt_current(self):
        self.assertEqual((ROOT / 'prompts/human-writing-pro.md').read_text(encoding='utf-8'), portable_text())

    def test_user_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            for agent, folder in [('codex', '.agents'), ('claude', '.claude'), ('copilot', '.copilot')]:
                self.assertEqual(install.destination_for(agent, 'user', home=temp),
                                 Path(temp) / folder / 'skills/human-writing-pro')

    def test_project_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(install.destination_for('copilot', 'project', temp),
                             Path(temp).resolve() / '.github/skills/human-writing-pro')
            for agent, folder in [('codex', '.agents'), ('claude', '.claude')]:
                self.assertEqual(install.destination_for(agent, 'project', temp),
                                 Path(temp).resolve() / folder / 'skills/human-writing-pro')

    def test_copy_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory(prefix='writing skill ') as temp:
            target = Path(temp) / 'human-writing-pro'
            install.install(target)
            for file in install.SOURCE.rglob('*'):
                if file.is_file():
                    self.assertEqual(file.read_bytes(), (target/file.relative_to(install.SOURCE)).read_bytes())
            marker = target / 'user-note.txt'
            marker.write_text('keep')
            with self.assertRaises(FileExistsError):
                install.install(target)
            self.assertEqual(marker.read_text(), 'keep')

    def test_dry_run_no_files(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'new-parent' / 'human-writing-pro'
            install.install(target, dry_run=True)
            self.assertFalse(target.parent.exists())

    def test_wrong_name(self):
        with self.assertRaises(ValueError):
            install.install(Path('wrong-name'), dry_run=True)

    def test_missing_project(self):
        with self.assertRaises(ValueError):
            install.destination_for('codex', 'project')

    def test_recursive_destination(self):
        with self.assertRaises(ValueError):
            install.install(install.SOURCE / 'nested' / 'human-writing-pro', dry_run=True)


if __name__ == '__main__':
    unittest.main()
