# Research and design notes

Reviewed 10 November 2026. This is an original editorial skill informed by the sources below, not a copied or installed third-party package. Repository descriptions and benchmark claims are authors' reports, not independently established proof of effectiveness.

## Existing skills reviewed

### blader/humanizer
Source: https://github.com/blader/humanizer/blob/main/SKILL.md

The inspected skill focuses on revising AI-sounding prose. Useful features include examining repetitive rhetorical structures, preserving information during editing, and adapting to a writing sample. Its visible instructions sometimes favor aggressive pattern removal and a multi-stage output. For this broader writing task, contextual judgment and returning the finished deliverable are better defaults. Assessment is based on instruction review, not comparative testing.

### harshaneel/humanize
Source: https://github.com/harshaneel/humanize

The repository describes rewriting and AI-checking skills, voice matching, and a self-reported benchmark. Its documentation acknowledges differing detector outcomes. Voice calibration and a revision pass are useful design ideas. Detector-oriented scores and inferred authorship percentages are not adopted here. A changed model pair and self-reported sample results are insufficient grounds for general performance guarantees. This review covered repository documentation, not every implementation file.

## Editorial foundations

Mailchimp, Voice and Tone: https://styleguide.mailchimp.com/voice-and-tone/

Distinguish a stable voice from a tone adapted to the situation. Favor clarity and avoid forcing humor. Adopt that distinction without copying Mailchimp's brand personality.

Mailchimp, TL;DR: https://styleguide.mailchimp.com/tldr/

Useful content is clear and appropriate for the reader. Consistent terminology matters more than unnecessary synonym variation.

Google, Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

Focus on reader value, useful original contribution, trustworthy support, and titles that accurately describe the content. This supports research discipline and avoiding empty SEO expansion. It does not establish a formula for natural-sounding prose.

Google, Title links: https://developers.google.com/search/docs/appearance/title-link

Titles should be descriptive, concise, and distinctive. Avoid keyword stuffing. Search title display can be truncated to fit available width; a character count is not a universal Google rule.

Google, Snippets: https://developers.google.com/search/docs/appearance/snippet

Descriptions should accurately summarize the particular page. Search snippets can be generated from page content and vary by query; a supplied meta description is not guaranteed to appear.

## Recommendation and limitations

A single custom skill fits this request because original drafting, voice matching, fact preservation, and format-specific editing belong in one coherent workflow. Existing humanizer skills are useful candidates for rewriting alone. This recommendation is editorial judgment, not a measured ranking of all available tools.

Success should be judged by readers: usefulness, accuracy, clarity, voice fit, and whether the title's promise is fulfilled. No blind reader study or detector evaluation was performed for this custom skill. The GOV.UK writing guide was also sought, but its redirected page did not return usable body text; it was not used as evidence.

## Research verification, 10 November 2026

These studies support editorial choices, not a universal specification for human writing. Findings about particular models or English-language datasets should not be generalized to all languages or current models. Reported data were reviewed; the original experiments were not independently replicated.

### Reading effort

Oppenheimer (2006), Applied Cognitive Psychology: https://onlinelibrary.wiley.com/doi/10.1002/acp.1178

The publisher's abstract reports five experiments; unnecessary vocabulary complexity reduced perceived author intelligence in the first three, with processing fluency mediating the effect. This supports familiar wording when meaning is preserved. It does not justify removing essential specialist terms or equating simplicity with truth. Access scope: publisher abstract; attempted full-text university PDF retrieval failed.

### Information that readers can find and use

Morkes and Nielsen (1997): https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/

Read the report's methods and results. Its measurement study involved 51 users and five versions of a sample website. The combined concise, scannable, objective condition scored 124% above the promotional control on a composite usability measure. This is a historical, task-specific result, not an expected gain for this skill or a rule for literary prose. Implication: retain purposeful headings and front-loaded answers; add explicit findability and comprehension review.

### Variation across genres

Zanotto and Aroyehun (EMNLP 2025): https://aclanthology.org/2025.emnlp-main.1163.pdf

Reviewed the paper's scope and reported findings: texts from eight domains and eleven models were compared on linguistic and stylistic features. Human texts tended toward simpler syntax and more diverse semantic content, with greater variability in the studied features. This supports reducing needless structural difficulty while retaining genre differences. It does not supply a sentence-length quota or prove any individual text's authorship.

### Personal voice is difficult to reproduce

Wang et al. (Findings of EMNLP 2025): https://aclanthology.org/2025.findings-emnlp.532.pdf

Reviewed the paper's task and reported results: over 40,000 generations per model, from more than 400 authors across news, email, forums, and blogs. Models approximated structured genres more successfully than nuanced informal styles. Implication: use relevant samples, compare observable choices, invite correction when useful, and avoid claiming perfect voice replication. The revised skill makes this limitation and feedback step explicit.

### More diverse vocabulary is not automatically more human

Kendro, Maloney, and Jarvis (2025): https://arxiv.org/abs/2508.00086

Access scope: research abstract, not full paper. Four ChatGPT models were compared with 240 human writers across six lexical-diversity dimensions. The reported differences did not reduce to a rule that higher diversity equals more human writing. Implication: retain accurate terminology and meaningful repetition; reject lexical-diversity optimization as an editorial objective. This supports an explicit clarification in the revised skill, not a quantitative target.

### Detector scores are not quality measures

Liang et al. (2023), Patterns: https://arxiv.org/html/2304.02819v3

Read the study's results. Seven detectors were assessed on 91 TOEFL essays and 88 US eighth-grade essays; the reported average false-positive rate for the TOEFL set was 61.22%. These samples differ in context and population, and this is not a current performance estimate for every detector. It demonstrates why a score cannot establish writing quality or reliable authorship. The skill already rejects detector guarantees and invented authorship probabilities.

## Coverage verdict

The revised instructions align with the reviewed principles: appropriate vocabulary, manageable syntax, useful structure, genre sensitivity, cautious voice matching, factual fidelity, and reader-centered evaluation. This is evidence-informed design with editorial spot checks, not scientific certification or proof that all future outputs will sound human. Full-text data reanalysis and blinded reader testing remain unperformed.
