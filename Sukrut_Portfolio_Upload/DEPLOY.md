# Publish on GitHub Pages

## Upload this folder's contents

1. Extract Sukrut_Portfolio_Upload.zip on your computer.
2. Open https://github.com/sukrut-shishupal/sukrut-shishupal.github.io on the main branch.
3. Choose Add file > Upload files.
4. Open the extracted Sukrut_Portfolio_Upload folder. Drag its CONTENTS into GitHub,
   including index.html, assets, projects, files and the other folders. Do not upload
   the ZIP or the enclosing Sukrut_Portfolio_Upload folder.
5. Commit the changes. The new index.html must appear at the repository root.
6. Ensure .nojekyll exists at the root. If your file picker hides it, use Add file >
   Create new file and name it .nojekyll (empty contents are sufficient).
7. Under Settings > Pages, use Deploy from a branch, main, /(root).
   Keep Custom domain empty when using sukrut-shishupal.github.io.
8. Wait for the Pages deployment to finish, then open the live site and refresh.

## Clean up old files separately

Uploading replaces matching files, but DOES NOT delete old files. The package
omits the obsolete ORIGINAL_FILES, UPLOAD_THESE_FILES and PREVIEW directories.
After the new site is live and checked, remove those old directories from the
repository if they are still present. They are not used by this package.
Do not delete the active assets, images, files, projects or other page directories.

Old root-level upload guides and generated review notes can also be removed after
checking you no longer need them. Existing Git history preserves committed versions.

## Check the result

- Homepage reflects the Research Associate appointment.
- Exposure, nursing and pneumonitis project pages load.
- Download résumé opens the revised two-page PDF.
- Runnable example ZIP downloads and contains Python, CSV and instructions.
- Navigation works on a phone-sized screen.

This package updates the website only. It does not change the separately hosted
University of Utah research application or publish confidential research data.
