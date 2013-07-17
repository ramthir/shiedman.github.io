---
layout: post
category: lessons
tagline: improve your blog
tags: [jekyll, tutorial]
---
#### find related posts with category

<!--excerpt:end-->
{% raw %}
```
{% for post in site.related_posts limit:5 %}
  {% assign match = false %}
  {% for category in post.categories %}
    {% if page.categories contains category %}
      {% assign match = true %}
    {% endif %}
  {% endfor %}
  {% if match %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endif %}                       
{% endfor %}
```
{% endraw %}
since `site.related_posts` limited by 10, using `site.posts` instead of `site.related_posts` as you wishes
@see: [filter site related posts in jekyll](http://stackoverflow.com/questions/10906574/filter-site-related-posts-in-jekyll)

---

#### fency code block with raw tag

when running locally, if you included liquid template syntax like <code>&#123;% %}</code> or <code>&#123;{ }}</code>, just remember to embrace them with raw tag: <code>&#123;% raw %} ... &#123;% endraw %}</code>, or your code block would accidently broken.
@see: [mojombo/jekyll#814](https://github.com/mojombo/jekyll/issues/814)

reference:
+ [GFM markdown help](https://help.github.com/articles/github-flavored-markdown)
+ [redcarpet2 help](https://github.com/vmg/redcarpet/blob/master/README.markdown)

