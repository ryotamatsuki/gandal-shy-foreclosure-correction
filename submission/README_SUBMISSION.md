# Submission Package

The active target on this branch is **Review of International Economics (RIE)**.

Use:

- `submission/README_RIE_SUBMISSION.md` for the current upload instructions;
- `submission/rie_checklist.md` for the current submission checklist;
- `submission/cover_letter.txt` for the RIE cover letter;
- `submission/title_page.tex` for the RIE title-page template.

The older *International Economics* flat-LaTeX/export machinery is retained in this branch only as development provenance from the validated C6.1 base. It is **not** the upload workflow for Wiley Research Exchange.

Build the current manuscript with:

```bash
make verify
make pdf
```

This produces the review PDF at `output/manuscript.pdf` in a normal local checkout. Private street-address and phone fields must be entered only in the submission portal or a local-only title-page copy and must not be committed.
