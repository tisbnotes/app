import os
import time
from os.path import isfile, join, isdir
from bs4 import BeautifulSoup


def dictToTable(sections):
    sections_keys = list(sections.keys())

    table = [sections_keys, ]
    maxRows = 0
    for section in sections:
        maxRows = max(len(sections[section]), maxRows)

    for i in range(maxRows):
        table.append([])

    for i in range(maxRows):
        for s in range(len(sections)):
            section = sections_keys[s]
            if len(sections[section]) < i + 1:
                table[i + 1].append('')
            else:
                table[i + 1].append(sections[section][i])
    return table


def pathToLink(path):
    path = path.replace('/notes', '')
    return path


def getPages(shortpath):
    children = getChildren(os.getcwd() + '/app/notes/' + shortpath)
    pages = []
    for child in children:
        filename = os.getcwd() + '/app/notes/' + shortpath + '/' + child
        fp = open(filename, 'r')
        soup = BeautifulSoup(fp, features='html.parser')
        pages.append({
            'link': ('/' + shortpath + '/' + child).replace('//', '/'),
            'title': soup.title.string,
            'contributor': 'Vishnu Nittoor',
            'mtime': time.strftime('%d %B, %Y', time.localtime(os.path.getmtime(filename)))
        })
    return pages


def getChildren(path):
    children = os.listdir(path)
    files = []
    directories = []
    children.sort()
    for file in children:
        filename, ext = os.path.splitext(join(path, file))
        if isfile(join(path, file)) and ext == '.md' or ext == '.html':
            files.append(file)
        elif isdir(join(path, file)):
            directories.append(file)
    return files + directories


def convert_notes(path):
    return open(path).read()
