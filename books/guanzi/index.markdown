---
layout: book_index
title: 管子
permalink: /books/guanzi/
author: 稷下学宫
date: 2014-03-10 09:43:00 +0800
groupby: [經言, 外言, 内言, 短语, 區言, 雜篇, 管子解, 輕重]

---


{% comment %}
<ul class="entries">
  {% assign posts = site.categories['管子'] | sort: 'id' %} 
{% for post in posts %}
  <li>
  <h3>{{ post.title }}<a href="{{ post.url }}" class=""> &rarr;</a><time>{{ post.date | date_to_string }}</time> </h3>
  </li>
{% endfor %}
</ul>
{% endcomment %}
