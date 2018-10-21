---
layout: default
title:  "Make your own blog with Jekyll"
date:   2018-10-17 17:00:54 +0800
categories: jekyll
tags: jekyll GitHub-Pages
---
## Overview
[Jekyll](https://jekyllrb.com/) convert [Markdown](https://daringfireball.net/projects/markdown/), [Liquid](https://github.com/Shopify/liquid/wiki), also HTML&CSS into static blogs that easily hosting with [GitHub Pages](https://pages.github.com/).


See [Simple site](https://kbroman.org/simple_site/) and its github [simple_site](https://github.com/kbroman/simple_site).

### Test Blog locally
1. [Intall ruby](https://www.ruby-lang.org/en/installation/), or use [RubyInstaller](https://rubyinstaller.org/) in Windows.
2. Install the github-pages gem (including jekyll)
    ```
    gem install github-pages
    ```
3. Clone existed Blog or create a new blog
    ```
    jekyll new path
    ```
4. Build and run
    ```
    jekyll build
    jekyll serve

    # or just type
    jekyll b
    jekyll s
    ```
5. visit http://localhost:4000
6. Use bundle to manage jekyll
    ```
    gem install bundler

    #build and run
    bundle exec jekyll serve
    ```

### refs
- [jekyll-docs](https://jekyllrb.com/docs/home)
- [jekyll-github](https://github.com/jekyll/jekyll)
- [jekyll theme](https://jekyllrb.com/docs/themes/)
- [pages theme](https://github.com/pages-themes)

