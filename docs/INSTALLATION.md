# Installation

Install the complete `skills/human-writing-pro` folder, including its `references`, `agents`, and `LICENSE` files. Copying only `SKILL.md` leaves its supporting references unavailable.

## Optional installer

From the repository root, with Python 3.10 or later:

```sh
python3 scripts/install.py --agent codex
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent copilot
```

Choose the command for your host; you do not need all three. Windows users can replace `python3` with `py`. The installer copies local files only: it makes no network requests, changes no host configuration, and refuses an existing destination. It prints the path it uses. Inspect `scripts/install.py` before running it if desired.

For one project:

```sh
python3 scripts/install.py --agent codex --scope project --project /path/to/project
```

Windows example:

```powershell
py scripts/install.py --agent claude --scope project --project 'C:\Projects\My Project'
```

For another compatible host, use the exact destination skill folder from its documentation:

```sh
python3 scripts/install.py --destination /path/to/skills/human-writing-pro
```

The destination must end in `human-writing-pro`. Do not pass the parent skills directory. `--destination` cannot be combined with host or scope options. Preview a destination without writing files by adding `--dry-run`.

## Manual installation: no Python needed

Copy the repository's `skills/human-writing-pro` folder into the parent directory below. Create the parent directory if necessary.

| Host | Personal parent directory | Project parent directory |
|---|---|---|
| Codex | `~/.agents/skills/` | `<project>/.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `<project>/.claude/skills/` |
| Copilot in VS Code | `~/.copilot/skills/` | `<project>/.github/skills/` |

Here `~` means your home directory. On Windows, a typical personal path is `C:\Users\YOUR_NAME\.agents\skills\human-writing-pro\SKILL.md`. `YOUR_NAME` is an example placeholder, not a literal folder to create.

Verify that the resulting path ends with `human-writing-pro/SKILL.md`, with only one `human-writing-pro` directory. Native discovery paths are documented by [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), and [VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills). Paths and product behavior can change; checked 10 November 2026.

## Use it

- Codex: `Use $human-writing-pro to revise this article: ...`
- Claude Code: `/human-writing-pro Rewrite this description in a calm, direct voice: ...`
- Copilot: ask `Use the Human Writing Pro skill to write ...`, or select it through the host's skill UI if available.

If discovery fails, reload or restart the application, verify its active workspace and skill settings, and check whether organizational policy disables personal skills. Avoid duplicate installations under multiple discovery paths.

## Assistants without native skills

Paste the entire contents of `prompts/human-writing-pro.md`, followed by your task. If the product supports instruction files or knowledge attachments, you can supply it there instead. The portable prompt includes every reference inline. If the product has a smaller context limit, provide `SKILL.md` and the relevant format reference manually. Do not assume an assistant can open relative links unless it has access to the files.

## Updating and uninstalling

An installation is a copy; `git pull` does not update it. Back up your installed folder outside the host's skill discovery directories, remove only the old `human-writing-pro` folder after checking its path, and install the new version. Keep your own voice samples outside the installed folder so updates cannot replace them.

To uninstall, remove only that installed skill folder and reload the host. The installer has no auto-update service or uninstall hook. It cannot grant filesystem permissions: use a location your account can write to, or ask your system administrator when managed settings restrict it.
