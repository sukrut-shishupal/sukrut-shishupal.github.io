# Your updated portfolio

This package updates your existing GitHub Pages repository. It is not a new hosting project.

## Preview first

Open `PREVIEW/index.html` in your browser after extracting the ZIP. The ten redesigned pages work locally; publication and research-system links need an internet connection. The source files in `UPLOAD_THESE_FILES` are for GitHub and contain Jekyll templates.

## Upload with drag and drop

1. Extract this ZIP using Windows **Extract All**.
2. Open https://github.com/sukrut-shishupal/sukrut-shishupal.github.io and select the **master** branch (the branch your existing deployment workflow uses).
3. Stay at the repository root, where `_config.yml` is visible.
4. Choose **Add file → Upload files**.
5. Open the extracted `UPLOAD_THESE_FILES` folder. Select **everything INSIDE it**: `_config.yml` plus the `_data`, `_layouts`, `_pages`, `_publications`, `assets`, and `files` folders. Drag that selection into GitHub’s upload area.
6. Check that paths look like `_pages/about.md` and `assets/css/career.css`. They must NOT start with `UPLOAD_THESE_FILES/` or `Sukrut_Portfolio_Job_Ready/`. Keep the existing filenames: GitHub will replace matching files and add new ones while retaining other files.
7. Commit with a message such as `Refresh portfolio for machine learning and health data science roles`.
8. Open the repository’s **Actions** tab and wait for **Deploy Jekyll site to Pages** to finish successfully. Then visit https://sukrut-shishupal.github.io and hard-refresh (Ctrl+F5).

Upload only the contents of `UPLOAD_THESE_FILES`. Do not upload this whole ZIP, the parent folder, `PREVIEW`, or `ORIGINAL_FILES`. No changes to your GitHub Pages settings or workflow are required by this update.

## What is included

- A responsive homepage with clear positioning, project evidence, and résumé/contact links.
- Four case studies: exposure patterns, telemedicine, nursing EHR activity, and protein affinity.
- Updated experience, publications, résumé, talks, and teaching pages.
- A one-page PDF résumé and editable résumé text.
- Metadata, navigation, and the existing SVI publication record corrected.
- Default sample blog posts and template demonstration pages excluded from the published site without deleting them.
- Local browser previews and the original versions of replaced files.

Your existing portrait, research PDFs, talks, older project detail pages, and deployment workflow remain in the repository. Both the new résumé URL and the original CV URL serve the updated résumé. The original CV is preserved in ORIGINAL_FILES as a backup.

## Before you publish

- Check that the résumé’s employment dates, degree names, and descriptions of your responsibilities are accurate. Dates come from your repository’s existing CV.
- Updated September 29, 2026 following your confirmation of a successful PhD defense. The site and résumé now use **Dr. Sukrut Shishupal** or **Sukrut Shishupal, PhD**. Employment details can be updated when your new appointment is confirmed.
- Review the ongoing nursing research brief. It uses your previously described method but does not publish patient data, unpublished outcome metrics, or a clinical-performance claim.

## Future edits

- Homepage: `_pages/about.md`.
- Case studies: `_pages/project-*.html`.
- Experience: `_pages/experience.md`.
- Publications: `_pages/publications.html` and the matching `_publications` record.
- Résumé webpage: `_pages/cv.md`; PDF: `files/Sukrut_Shishupal_Resume.pdf`.
- Design: `assets/css/career.css`; shared header/footer: `_layouts/career.html`.
- Portrait: replace `images/profile2.jpg` in your repository, keeping that filename.

`Resume_Editable.md` is the editable text. `resume_source.py` reproduces the provided PDF with Python and ReportLab; see its configuration notes at the top. Keep the PDF and résumé webpage aligned when updating them. The publication cards are curated manually, so adding a collection entry alone will not add a card to the homepage or publications index.

## Undo if needed

Restore the files in `ORIGINAL_FILES` to their matching paths. Delete the new files listed in `FILE_MANIFEST.md` to fully return to the original repository state. You can also revert the upload commit in Git. Save later edits before any rollback.

## Validation and limits

See `VALIDATION.md`. The preview validates rendered HTML and CSS with LiquidJS. Ruby/Jekyll is unavailable in this environment, so a production Jekyll build was not run here; the existing GitHub Actions build is the final production check. No remote commit, push, or deployment was performed.
