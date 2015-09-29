#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.dom.minidom as minidom

class Dependency:
    def __init__(self, node):
        for attr in self.__attr_names:
            try:
                setattr(self, '_' + attr, node.attributes[attr].value)
            except KeyError:
                setattr(self, '_' + attr, '')

    def __str__(self):
        key_value_pairs = []
        for attr in self.__attr_names:
            key_value_pairs.append(attr + '=' + self._escape(getattr(self, '_' + attr)))
        return '|'.join(key_value_pairs)

    @classmethod
    def _escape(cls, string):
        result = string
        for old, new in cls.__escape_table.iteritems():
            result = result.replace(old, new)
        return result

    __attr_names = ('org', 'name', 'rev', 'conf')
    __escape_table = {';': ',',
                      '|': ':',
                      '=': ':'}

class Dependencies:
    def __init__(self, node_list):
        self.__deps = []
        for node in node_list:
            self.__deps.append(Dependency(node))

    def __str__(self):
        return ';'.join(str(dep) for dep in self.__deps)

if __name__ == '__main__':
    document = minidom.parse(sys.stdin)
    dependencies = Dependencies(document.documentElement.getElementsByTagName('dependency'))
    print dependencies
