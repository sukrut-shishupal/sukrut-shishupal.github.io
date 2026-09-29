# Publish Dr. Sukrut Shishupal’s portfolio

This is the complete static website, ready for your current main branch. No Jekyll installation or custom workflow is required.

1. Extract Sukrut_Portfolio_Publish.zip.
2. Open your repository: https://github.com/sukrut-shishupal/sukrut-shishupal.github.io
3. On the main branch, choose Add file > Upload files at the repository root.
4. Drag ALL extracted contents into GitHub, including index.html, .nojekyll, and the folders. Do not upload the ZIP or a containing folder. Commit the upload.
5. Open Settings > Pages: https://github.com/sukrut-shishupal/sukrut-shishupal.github.io/settings/pages
6. Remove the Custom domain value and leave the field EMPTY. Use Remove if it is already saved. Do not enter either the repository address or the github.io address there.
7. Set Source to Deploy from a branch. Set Branch to main and Folder to /(root). Click Save.
8. Check Actions for the pages build and deployment run. Once it succeeds, open https://sukrut-shishupal.github.io/ and refresh with Ctrl+F5.

The index.html file must be visible directly on the repository’s first Code page. A file at PREVIEW/index.html or UPLOAD_THESE_FILES/_pages/about.md is not the homepage of the repository root.

The .nojekyll file is included to tell GitHub to publish these already-rendered files directly. If it was not included in your upload, use Add file > Create new file, name it .nojekyll, and commit it at the repository root.

Editing later: change index.html for the homepage, the other folders’ index.html files for their pages, assets/css/career.css for styling, and files/Sukrut_Shishupal_Resume.pdf for the résumé. This package uses plain HTML; the older Jekyll source files are not needed for this deployment.

No custom domain or DNS changes are needed for your free github.io website.

GitHub documentation:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
