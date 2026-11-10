# Human Writing Pro

Write useful articles, titles, descriptions, and everyday copy in a natural voice.

Human Writing Pro is an open-source, instruction-only **Agent Skill**. It helps an assistant choose a clear angle, adapt to its reader, preserve facts, and edit repetitive or generic prose. Supply your own writing samples for closer voice matching.

**No API key, paid service, or runtime dependency is required by the skill itself.** You need an assistant that can follow the instructions. Optional installation and packaging tools use Python 3.10+ and its standard library.

## What it helps with

- Articles and blog posts with a useful angle and clear structure.
- Titles and descriptions that accurately represent the content.
- Website copy, product descriptions, newsletters, and social posts.
- Rewriting that preserves facts, qualifications, and the author's stance.
- Voice matching based on examples, with room for personal and cultural differences.

It checks for vague claims, unnecessary repetition, stock openings, mechanical structure, and invented personal experience. It is evidence-informed editorial guidance, not a guarantee of human authorship or a tool that promises to pass AI detectors.

## Quick start

Download this repository with **Code → Download ZIP**, extract it, and open a terminal in the extracted folder. Or clone it using your repository's GitHub URL.

For a personal Codex installation:

```sh
python3 scripts/install.py --agent codex
```

On Windows, use `py` in place of `python3` if you installed Python with the Windows launcher:

```powershell
py scripts/install.py --agent codex
```

Then ask Codex:

```text
Use $human-writing-pro to write a 700-word article about organizing a small
workspace for people working from home. Include a title and description.
Use a warm, practical voice. Avoid unsupported productivity claims.
```

For Claude Code, use `--agent claude`; invoke it with `/human-writing-pro`. For Copilot in VS Code, use `--agent copilot` and ask it to use Human Writing Pro. Restart or reload the host if the skill does not appear. See the [installation guide](docs/INSTALLATION.md) for project installs and manual copying.

**Other assistants:** open [the portable prompt](prompts/human-writing-pro.md), paste its contents into the conversation or the assistant's supported instruction field, and add your writing brief. This is prompt-based use; it does not create persistent skill support in a product that lacks it.

## A small example

Supplied facts: a notebook has 160 numbered pages and lies flat.

Before:

> Unlock boundless creativity with a revolutionary notebook designed to elevate every idea.

After:

> Keep notes and sketches across 160 numbered pages. The notebook lies flat while you write.

The revision uses available facts without inventing benefits. See the [sample article](examples/small-desk-article.txt), [prompt examples](docs/USAGE.md), and [editorial review cases](skills/human-writing-pro/references/editorial-review.md).

## Compatibility

| Host | Integration | Verification status |
|---|---|---|
| Codex, local sessions | Agent Skills directory and optional OpenAI UI metadata | Local installation previously exercised; no broad model benchmark |
| Claude Code, local sessions | Agent Skills directory | Path and invocation documented by vendor; not tested in a live Claude session |
| GitHub Copilot in VS Code | Agent Skills directory | Paths documented by vendor; not tested in a live Copilot session |
| Other Agent Skills hosts | Copy the complete skill folder into their documented location | Host-specific support must be checked |
| Other text assistants | Paste the portable prompt | Depends on context limits and instruction following |

The folder follows the [Agent Skills format](https://agentskills.io/specification). Host paths were checked against [Codex documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code documentation](https://code.claude.com/docs/en/skills), and [VS Code documentation](https://code.visualstudio.com/docs/agent-customization/agent-skills) on 10 November 2026. Local installs do not automatically sync to cloud or mobile products.

## Research and evaluation

Read the [research notes](skills/human-writing-pro/references/research.md) for source links and limits, and the [evaluation guide](docs/EVALUATION.md) for a reproducible review process. The references distinguish research findings, vendor claims, and editorial decisions.

Two public detector checks of the sample were attempted; neither produced a completed score. No detector pass rate, independent reader study, or universal compatibility claim is made.

## Repository map

```text
skills/human-writing-pro/   Installable skill and references
prompts/                   Generated single-file prompt
docs/                      Installation, usage, evaluation, publishing
examples/                  Sample article and reusable brief
scripts/                   Optional installer, validator, release builder
tests/                     Installer and package checks
.github/workflows/         Windows and Linux checks
LICENSE                    MIT license
```

Maintainers: run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. Build release ZIPs with `python3 scripts/build.py`. See [publishing instructions](docs/PUBLISHING.md) and [contribution guidance](CONTRIBUTING.md).

## License

[MIT](LICENSE). You may use, modify, and redistribute the package under its license. External articles and linked projects retain their own licenses. The research notes are original summaries with attribution; the referenced papers are not bundled.
