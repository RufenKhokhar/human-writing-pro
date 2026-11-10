# Publish on GitHub

This folder is the repository root. It is ready for you to publish; packaging
does not create a GitHub repository or push anything automatically.

## 1. Check the package

Review `README.md`, `LICENSE`, and `skills/human-writing-pro/SKILL.md`.
The package uses the MIT license with a collective contributor notice. You
can add your preferred public author name before publishing.

Run from this folder:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

Windows: replace `python3` with `py` if appropriate. The builder refreshes
the portable prompt and creates release ZIPs plus SHA-256 checksums in `dist`.
Commit the generated portable prompt. The `dist` folder is intentionally ignored.

## 2. Create a repository

On GitHub, create a new **public** repository, for example `human-writing-pro`.
Leave GitHub's README, license, and .gitignore initialization options unchecked
because those files are already included here. Copy its HTTPS or SSH URL.

## 3. Push this folder

Run these commands inside this package folder, not its parent:

```sh
git init -b main
git add .
git commit -m "Release Human Writing Pro 1.0.0"
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL you copied. It is the only
placeholder in these commands. Git may ask you to configure your public commit
identity or sign in. Use your normal GitHub authentication method. If using an
existing repository, inspect its history and remotes first; these steps assume
a new empty repository.

For a browser-only upload, upload the contents of this folder with GitHub's
file-upload feature. Check that `.github/workflows/check.yml` and `.gitignore`
are included, since file pickers can hide dot-prefixed items.

## 4. Create a release

After the automated checks pass, create a GitHub release tagged `v1.0.0` and
attach the ZIP files and `SHA256SUMS.txt` from `dist`. The skill-only ZIP contains
one top-level `human-writing-pro` folder; the repository ZIP includes all guides
and tools. Product upload screens vary, so use their required archive layout.

Suggested repository description:

> An open Agent Skill for natural articles, titles, descriptions, and copy, with voice matching and evidence-informed editing.

Suggested topics: `agent-skills`, `writing`, `copywriting`, `codex`, `claude-code`.

## Future versions

Update `VERSION`, the skill's `metadata.version`, and `CHANGELOG.md` together.
Rerun the checks and builder. Describe actual behavior changes and validation;
avoid unmeasured claims about conversion gains or AI detector performance.
