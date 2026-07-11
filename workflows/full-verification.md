# Full verification workflow

Run this workflow for a near-submission manuscript or an R&R package.

## Inputs

1. Submission-package JSON using `examples/full-workflow-package.json` as the schema.
2. Official journal policy configuration with HTTPS URLs and keyword categories.
3. Revised manuscript in `.txt`, `.md`, `.tex`, `.docx`, or `.pdf`.
4. Reviewer-response matrix with `comment_id`, `location`, and exact `revised_text`.

## Commands

```bash
python tools/scholarly_verify.py references.json --output reference-report.json
python tools/journal_policy_verify.py journal-policy.json --output policy-report.json
python tools/revision_trace.py revised.docx response-matrix.json --output revision-report.json
python tools/run_full_workflow.py workflow-config.json --output full-report.json
```

Set optional environment variables:

```text
CROSSREF_MAILTO=researcher@example.org
OPENALEX_API_KEY=your-free-key
```

Crossref works without registration. OpenAlex permits limited keyless access and offers a larger free allowance with an API key. Never commit API keys.

## Interpretation

- Crossref/OpenAlex agreement verifies metadata consistency, not that a paper supports a manuscript claim.
- Policy keyword hits preserve auditable excerpts, hashes, and access times; a human/agent must interpret the requirement in context.
- Revision trace verifies promised text and section labels, not the scientific adequacy of the revision.
- A workflow `PASS` is a structural/retrieval result, not a publication guarantee.

## Completion sequence

1. Resolve submission gate failures.
2. Resolve DOI/title/year mismatches.
3. Review official-policy evidence and translate it into an item-level checklist.
4. Resolve every response/manuscript mismatch.
5. Re-run until no blocking stage remains.

