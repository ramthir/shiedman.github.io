#!/usr/bin/env python
import re,os

code_re = re.compile(r'```([a-z]+)(.+?)```', re.S)


def convert_tag(filename):
    with open(filename, 'rb') as f: s = f.read()
    while 1:
        m = code_re.search(s)
        if not m: break
        lang = m.group(1)
        s = s[:m.start()] \
            + r"{% highlight " + lang + " %}" \
            + r"{% raw %}" \
            + m.group(2) \
            + r"{% endraw %}"  \
            + r"{% endhighlight %}" \
            + s[m.end():]
    print s

def convert_all(path):
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.endswith(".md"):
                print os.path.join(root,f)
                #convert_tag(f)

convert_all("_posts")
