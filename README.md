---
layout: post
title: build blog on github with jekyll
tagline: small title
categories: tutor
tags: [jekyll, bootstrap]
---

Prepare
=======
1. config ~/.gemrc  

        ---
        :backtrace: false
        :bulk_threshold: 1000
        :sources:
        - http://ruby.taobao.org/
        :update_sources: true
        :verbose: true
        gem: --user-install

<!--more-->
2. install jekyll

    **install to user home**

    + init  : `gem install github-pages`  
    + update: `gem update github-pages`

    **or install to bundler**  

    1. create file `Gemfile`

            source 'https://rubygems.org'
            gem 'github-pages'


    2. install gem with bundler

            gem install bundler
            bundle install

3. create new blog

        jekyll new myblog
        cd myblog
        jekyll serve --port 8080

for more details, see: https://help.github.com/articles/using-jekyll-with-pages

build boilerplate
=================

1. create basic layouts `default.html/post.html` in `_layouts` dir

2. create helper snippets in `_includes` dir

3. create `assets` dir for css/js/image files

