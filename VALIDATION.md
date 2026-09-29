# Validation

- Rendered ten new pages with LiquidJS and Markdown parsing for local preview.
- Browser checked at 1440, 768, 390, and 320 pixels wide: no horizontal overflow, missing images, unresolved Liquid, or missing/duplicate main headings.
- Checked homepage anchor navigation with the enhancement script blocked.
- Checked 144 local preview links and anchors: zero unresolved targets.
- Inspected desktop homepage, mobile homepage, project page, and one-page résumé renderings.
- The résumé PDF is one page, contains selectable text, and includes clickable contact/publication links.
- `git diff --check` passed.
- The existing research system and GitHub profile responded. The DOI links resolve to the intended publishers, although automated access to the JAMIA Open page was blocked by the publisher; that publication was checked against a University of Utah bibliographic record.

## Production limitation

This was not a full Jekyll build. Ruby/Jekyll was not available locally. The local preview uses the new Liquid layout, CSS, JavaScript, and content, but does not reproduce every legacy Jekyll plugin. The existing GitHub Actions deployment remains the production build check after upload. Legacy detail pages retain their original AcademicPages layouts.

No changes were pushed to GitHub and no deployment was triggered.

## September 29 doctoral-status revision

Updated the visible name, biography, education, metadata, editable résumé, both résumé download URLs, and supporting instructions following the successful-defense confirmation. Re-rendered the résumé (one page) and browser preview, and checked current source/preview files for obsolete PhD Candidate wording. Historical backups intentionally retain their original content.
