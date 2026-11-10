"""Copy the local skill to an explicit, non-existing destination. No network."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skills' / 'human-writing-pro'
PATHS = {
    'codex': ('.agents/skills', '.agents/skills'),
    'claude': ('.claude/skills', '.claude/skills'),
    'copilot': ('.copilot/skills', '.github/skills'),
}


def destination_for(agent, scope, project=None, home=None):
    base = Path(home) if home is not None else Path.home()
    if scope == 'project':
        if project is None:
            raise ValueError('--project is required for project scope')
        base = Path(project).expanduser().resolve()
        if not base.is_dir():
            raise ValueError('Project directory must already exist')
    return base / PATHS[agent][scope == 'project'] / 'human-writing-pro'


def install(destination, dry_run=False):
    destination = Path(destination).expanduser().absolute()
    if destination.name != 'human-writing-pro':
        raise ValueError('Destination must end in human-writing-pro')
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f'Destination already exists; no files changed: {destination}')
    resolved = destination.resolve()
    if resolved.is_relative_to(SOURCE.resolve()):
        raise ValueError('Destination must be outside the source skill')
    if not (SOURCE / 'SKILL.md').is_file():
        raise ValueError('Run from a complete repository download')
    if dry_run:
        return resolved
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination, dirs_exist_ok=False)
    return resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=PATHS)
    parser.add_argument('--scope', choices=['user', 'project'])
    parser.add_argument('--project', type=Path)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if args.destination is not None and any([args.agent, args.scope, args.project]):
        parser.error('--destination cannot be combined with --agent, --scope, or --project')
    if args.destination is None and args.agent is None:
        parser.error('Choose --agent or --destination')
    if args.project is not None and args.scope != 'project':
        parser.error('--project requires --scope project')
    try:
        destination = args.destination or destination_for(args.agent, args.scope or 'user', args.project)
        result = install(destination, args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Installation stopped: {exc}\n')
    print(f'{"Would install to" if args.dry_run else "Installed to"}: {result}')


if __name__ == '__main__':
    main()
