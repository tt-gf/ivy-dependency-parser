#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.dom.minidom as minidom

class DependencyKey:
    def __init__(self, org, name, rev):
        self.__org = org
        self.__name = name
        self.__rev = rev

    def __str__(self):
        return 'org=%s|name=%s|rev=%s' % (self.__org, self.__name, self.__rev)

    def __eq__(self, other):
        return self.__org == other.__org and \
               self.__name == other.__name and \
               self.__rev == other.__rev

    def __hash__(self):
        return hash(str(self))

class DependencyConfs:
    def __init__(self):
        self.__confs = set()

    def __str__(self):
        return 'conf=' + ','.join(self._escape(conf) for conf in self.__confs)

    def add(self, conf):
        self.__confs.add(conf)

    def union(self, confs):
        self.__confs = self.__confs.union(confs.__confs)

    @classmethod
    def _escape(cls, string):
        result = string
        for old, new in cls.__escape_table.iteritems():
            result = result.replace(old, new)
        return result

    __escape_table = {';': ',',
                      '|': ':',
                      '=': ':'}
class Dependencies:
    def __init__(self, node_list):
        self.__deps = {} # DependencyKey/DependencyConfs
        for node in node_list:
            key, confs = self._to_key_confs(node)
            if key in self.__deps:
                self.__deps[key].union(confs)
            else:
                self.__deps[key] = confs

    def __str__(self):
        return ';'.join(str(key) + '|' + str(confs) for key, confs in self.__deps.iteritems())

    @classmethod
    def _to_key_confs(cls, node):
        """Returns a tuple (DependencyKey, DependencyConfs) corresponding to the given dependency
        XML node.
        """
        xml_attrs = {}
        for attr in ('org', 'name', 'rev', 'conf'):
            try:
                xml_attrs[attr] = node.attributes[attr].value
            except KeyError:
                xml_attrs[attr] = ''

        key = DependencyKey(xml_attrs['org'], xml_attrs['name'], xml_attrs['rev'])
        confs = DependencyConfs()
        for conf in xml_attrs['conf'].split(';'):
            confs.add(conf)
        return (key, confs)

def convert(file):
    document = minidom.parse(file)
    dependencies = Dependencies(document.documentElement.getElementsByTagName('dependency'))
    return str(dependencies)

def main():
    print convert(sys.stdin)
