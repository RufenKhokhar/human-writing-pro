# Evaluation and limits

Evaluate the writing separately from whether the package installs.

## Package checks

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks this package's deliberately simple frontmatter, linked
reference files, version, license, and expected structure. It is not a general
YAML parser or an official certification. Installer tests use temporary
directories and cover copying, repeat-install refusal, dry runs, and path
mapping. GitHub Actions repeats these checks on Windows and Linux.

## Editorial evaluation

Try the [review cases](../skills/human-writing-pro/references/editorial-review.md)
on the model and host you actually use. Record the exact brief, model/version,
skill version, output, and failures. Check factual fidelity, reader usefulness,
voice fit, structure, and hard length limits separately.

For stronger evidence, compare outputs with and without the skill using the
same briefs and model settings. Randomize presentation order and ask intended
readers to judge clarity, usefulness, trust, and voice fit without knowing the
condition. Use multiple genres and report unfavorable results too. Do not turn
a small convenience sample into a claim about all writing or all models.

## Current evidence

The initial skill underwent six author-reviewed spot checks for factual
qualifiers, title constraints, product facts, formal tone, missing personal
experience, and preserving effective prose. Those are developmental examples,
not independent tests. There is no published blinded reader study of this skill.

Public GPTZero and QuillBot checks of the example article were attempted on
10 November 2026. GPTZero returned no completed result and QuillBot's detect
control remained disabled. No detector pass was established. Those incomplete
checks are not a benchmark or a claim about either detector's general ability.

Read [detector-checks.md](../skills/human-writing-pro/references/detector-checks.md)
for a reproducible protocol when a user requests detection tests. A favorable
classification does not change AI-generated text into human-authored text.

## Research scope

The [research notes](../skills/human-writing-pro/references/research.md) link
the studies and identify what was accessed. Evidence supports editorial
principles, not a universal recipe for sounding human. Several studies concern
specific English-language samples and older models. Browsing and factual
verification depend on the host's available tools.
