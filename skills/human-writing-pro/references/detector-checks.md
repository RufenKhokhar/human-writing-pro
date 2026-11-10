# Detector evidence and testing

Reviewed 10 November 2026. Apply this reference only when detection is part of the request. A skill changes instructions, not the underlying model or a detector's proprietary classifier. Never guarantee universal human classification or misstate generated text as human-authored.

## What the evidence establishes

Statistical detectors may examine how probable words or sequences are under a language model. Other detectors learn distinctions from examples of human, generated, edited, and mixed text. Linguistic repetition, structure, vocabulary, and contextual relationships may contribute to learned distinctions; proprietary feature weights and thresholds are generally not available. A list of stock phrases is not a complete detector specification.

GPTZero's support page says it stopped using perplexity and burstiness in autumn 2023. Its 2026 technical report describes supervised deep learning with document and sentence predictions, hierarchical classes, and training on rewritten text. Exact architecture and hyperparameters are proprietary. This is vendor documentation, not independent proof of its advertised accuracy.
Sources:
- https://support.gptzero.me/articles/9585228410-how-do-i-interpret-burstiness-or-perplexity
- https://arxiv.org/html/2602.13042v1

GPTZero also acknowledges both false positives and false negatives, and says short passages are less reliable than whole documents. Do not infer how a title or description would score from an article's score.
Source: https://support.gptzero.me/articles/1787085022-what-are-the-limitations-of-gptzeros-ai-classifier

Turnitin says its percentage describes qualifying prose flagged by the model; it is not a probability that the author used AI. Its guidance warns of misclassification, suppresses exact results below 20%, and requires at least 300 words of qualifying long-form prose. Verify current requirements before use.
Source: https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report

RAID (ACL 2024) evaluated twelve detectors against a benchmark spanning multiple models and domains and found sensitivity to changes in generation and text. These historical findings establish generalization concerns, not current performance numbers for every service.
Source: https://aclanthology.org/2024.acl-long.674/

## Apply findings to writing

Improve unnecessary repetition, vague content, mechanical section structure, and mismatched register through the main editorial workflow. Use authentic user-supplied details when relevant. Preserve good prose, meaningful repetition, factual qualifications, and the user's voice. Do not impose a numerical randomness or sentence-variation target. Do not add mistakes, fabricated experiences, invisible characters, or misleading provenance claims to change a score.

A detector highlight can identify a passage to inspect, but does not prove a specific phrase caused the result. Revise when there is an identifiable writing problem and check meaning afterward. Passing a detector is not evidence of factual accuracy, originality, or actual human authorship.

## Reproducible checks when requested

1. Freeze the exact submitted text, including whether the title, description, and headings are present. Preserve a plain-text copy and a content hash when practical.
2. Use the requested service or a small explicitly identified set of accessible services. Authorization to check the supplied text permits submission of that text; do not submit unrelated private material. Do not purchase access or create accounts without authorization.
3. Record date, service URL, model/version if displayed, input scope, and the exact label and scores. State whether a score means class confidence or estimated text proportion; if unclear, say so.
4. Keep a screenshot or report when available. If access, minimum length, CAPTCHA, or payment blocks the check, report 'not tested' rather than guessing. Do not bypass access controls.
5. Report every completed result, including unfavorable or contradictory findings. Do not average unlike scores. A label applies only to that submitted text and service at that time.
6. If substantive revisions are made and a recheck is within the user's request, preserve both versions and report both results. Do not claim improvement without comparable observations. Stop after the agreed scope or a limited initial check; never silently run an open-ended rewrite-and-resubmit loop.

For broader verification, use multiple representative articles and human-written controls with known provenance. Separate detector behavior from intended readers' judgments of clarity, usefulness, and voice. No finite test can establish that all detectors will accept all future outputs.
