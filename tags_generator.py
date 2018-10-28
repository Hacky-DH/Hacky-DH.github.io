#!/usr/bin/env python

'''
tags_generator.py
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.

modified from https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*.md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = os.path.join(tag_dir, tag + '.md')
    f = open(tag_filename, 'w')
    write_str = '---\nlayout: tagpage\ntitle: "Tag: {0}"\ntag: {0}\nrobots: noindex\n---\n'.format(tag)
    f.write(write_str)
    f.close()
print("Tags generated, count", len(total_tags))
