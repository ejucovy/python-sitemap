#! /usr/bin/env python
""" 
Transforms a sitemap into an HTML list of links.
"""

import sys
sys.path.append('..')
import urllib2
import socket

import sitemap
import tempita

template = tempita.HTMLTemplate("""\
<ul>
{{for url in set}}
  <li>
    <a {{if url.pageclass}}class="{{url.pageclass}}"
       {{endif}}href="{{url.loc}}">{{url.title or url.loc}}</a>
  </li>
{{endfor}}
</ul>""")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./transform-sitemap.py url_or_path'
        sys.exit(1)

    set = sitemap.UrlSet.from_url(sys.argv[1], validate=False)
    print template.substitute(set=set)
