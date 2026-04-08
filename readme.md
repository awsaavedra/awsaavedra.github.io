
Hugo basic commands

Quickstart: https://gohugo.io/getting-started/quick-start/

```
hugo server -D
```

If you need help 

```
hugo -h
```

Adding markdown images to markdown posts

https://tutorialedge.net/golang/hugo/hugo-adding-images-to-posts/


Add a new page to site

```
make post name=my-first-post.md
```

This is a shortcut for `hugo new content/posts/my-first-post.md`.


## Image Optimization

All images in `static/` are served as WebP. A script converts PNG, JPG, JPEG, and GIF files in `static/` (recursively) to WebP.

**Prerequisites:** Python 3 + Pillow (`pip install Pillow`)

```bash
# Preview what would be converted (no files modified)
python3 convert-images.py --dry-run

# Convert all images in static/ to WebP and delete originals
python3 convert-images.py
```

Animated GIFs are automatically skipped. Files that already have a `.webp` counterpart are also skipped.

# Website TODO Features

- [ ] Add Subscribe feed to website
    - Potentially use https://listmonk.app/ 
    - The Derek Sivers method for truly independent newsletters:
    - Collect emails via a simple HTML form on your Hugo site​
    - Store addresses in a database or simple text file you control
    - Send plain-text emails using your own mail server or SMTP relay like smtp2go.com​

Note: Keep it personal, human, and simple—no fancy template
- [x] Add LaTeX support for math equations in blog posts using Hugo Native Server-Side LaTeX Rendering (No JavaScript Required).
- [ ] Add search functionality to website
- [x] Disclaimer to website
- [ ] Add RSS feed to website