#!/usr/bin/env python

import pprint
import sys

import six
import yaml

#
# usage: convert_i18n_yaml.py i18n.yml ../behave/i18n.py
#
languages = yaml.load(open(sys.argv[1]))

for language in languages:
    keywords = languages[language]
    for k in keywords:
        v = keywords[k]
        # bloody YAML parser returns a mixture of unicode and str
        if not isinstance(v, six.text_type):
            v = v.decode('utf8')
        keywords[k] = v.split('|')

content = '''#-*- encoding: UTF-8 -*-

# file generated by convert_i18n_yaml.py from i18n.yaml

languages = \\
'''

i18n_py = open(sys.argv[2], 'w')
i18n_py.write(content.encode('UTF-8'))
i18n_py.write(pprint.pformat(languages).encode('UTF-8'))
i18n_py.write(u'\n')
i18n_py.close()
