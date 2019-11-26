import os
from os.path import isfile, join, isdir
from app import app, db
from app.models import Subject, Update


def getChildren(shortpath):
    path = os.getcwd() + shortpath
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

def init_subjects():
    import os
    from os.path import isfile, join, isdir
    from app import app, db
    from app.models import Subject, Update

    for subject in Subject.query.all():
        db.session.delete(subject)

    subjectList = [
        {'display_name': 'IB Biology', 'path': '/notes/ib/biology', 'id_name': 'ib-biology'},
        {'display_name': 'IB Business', 'path': '/notes/ib/business', 'id_name': 'ib-business'},
        {'display_name': 'IB Chemistry SL', 'path': '/notes/ib/chemistry', 'id_name': 'ib-chemistry'},
        {'display_name': 'IB Economics', 'path': '/notes/ib/economics', 'id_name': 'ib-economics'},
        {'display_name': 'IB English Language and Literature',
         'path': '/notes/ib/eng-langlit-sl', 'id_name': 'ib-eng-langlit-sl'},
        {'display_name': 'IB French B', 'path': '/notes/ib/french-b', 'id_name': 'ib-french-b'},
        {'display_name': 'IB Mandarin AB', 'path': '/notes/ib/mandarin-ab', 'id_name': 'ib-mandarin-ab'},
        {'display_name': 'IB Mathematics Analysis and Approaches',
            'path': '/notes/ib/math-aa-hl', 'id_name': 'ib-math-aa-hl'},
        {'display_name': 'IB Physics', 'path': '/notes/ib/physics', 'id_name': 'ib-physics'},
        {'display_name': 'IB Psychology', 'path': '/notes/ib/psychology', 'id_name': 'ib-psychology'},
        {'display_name': 'IB Spanish AB', 'path': '/notes/ib/spanish-ab', 'id_name': 'ib-spanish-ab'},
        {'display_name': 'IB Spanish B', 'path': '/notes/ib/spanish-b', 'id_name': 'ib-spanish-b'},
        {'display_name': 'ToK', 'path': '/notes/ib/tok', 'id_name': 'ib-tok'},
        {'display_name': 'IG Additional Mathematics', 'path': '/notes/ig/addmath', 'id_name': 'ig-addmath'},
        {'display_name': 'IG Biology', 'path': '/notes/ig/biology', 'id_name': 'ig-biology'},
        {'display_name': 'IG Economics', 'path': '/notes/ig/economics', 'id_name': 'ig-economics'},
        {'display_name': 'IG Global Perspectives', 'path': '/notes/ig/gp', 'id_name': 'ig-gp'},
        {'display_name': 'IG English Literature', 'path': '/notes/ig/englit', 'id_name': 'ig-englit'},
        {'display_name': 'IG Physics', 'path': '/notes/ig/physics', 'id_name': 'ig-physics'}
    ]

    for subject in subjectList:
        s = Subject(display_name = subject['display_name'], path = subject['path'], id_name = subject['id_name'])
        db.session.add(s)
    db.session.commit()

"""
from import_file import init_subjects
init_subjects()
"""
