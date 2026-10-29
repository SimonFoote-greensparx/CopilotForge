# Hosting the website

The CopilotForge website is built from this repository, so the site, the catalogue and the plugins cannot drift apart
(decision D14). It is designed for professional web hosting at https://copilotforge.ai/.

| Part | Built by | Where |
|---|---|---|
| Core pages (home, catalogue, programmes, templates, programme builder, author, contributors, privacy) | `scripts/build-site.py` | `site/` (committed and checked) |
| The full site: every guide, department, skill, template and programme page, downloads, licence texts, 404, `.htaccess`, `robots.txt`, `sitemap.xml` | `scripts/build-hosting.py` | `dist/website/` and `dist/copilotforge-website.zip` (git-ignored) |

## Build the hosted site

```
bash scripts/build-all.sh
python3 scripts/build-hosting.py
```

The build checks that every link and image on every page resolves and fails if one does not. Pass `--site-url` to
build for another address.

While the repository is private (open decision O5), references to files that exist only in the repository are shown
as plain text, so visitors never meet GitHub's "page not found". Once the repository is public, set
`GITHUB_LINKS = True` in `scripts/_site.py` (or pass `--github-links`) and rebuild; a GitHub item then appears in the
navigation and repository references become links.

## Upload to your web host

1. In your hosting control panel, open **File Manager** for the copilotforge.ai website.
2. Open `public_html`. If it holds a placeholder page, such as `default.php`, delete it.
3. Upload `copilotforge-website.zip` into `public_html`.
4. Extract it into `public_html` itself, not into a new folder. The archive holds the site files at its top level, so
   `index.html` ends up directly in `public_html`.
5. Delete the archive once it has been extracted.
6. Turn on SSL for the domain and force HTTPS if it is not already on. The `.htaccess` file also redirects HTTP to HTTPS.
7. Open the site and check the home page, a skill page, the programme builder and a download.

The site is plain HTML and CSS with two small scripts (the catalogue search and the programme builder). It needs no
PHP, no database and no build step on the server.

## Update the hosted site

Rebuild, then upload and extract the new archive over the old files. If pages have been removed or renamed, empty
`public_html` first so that stale pages do not linger.

## Privacy

The privacy page says the site sets no cookies and has no analytics, and that the web host may log requests. If you
add analytics, a cookie banner or a contact form, update the privacy page in `scripts/build-site.py` first.
