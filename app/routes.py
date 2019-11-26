from flask import render_template, url_for
from app import app, db
from app.models import Subject, Update
from app.helpers import *

@app.route('/')
@app.route('/index')
def index():
    sections = {
        'Sciences': ['ib-physics', 'ib-chemistry', 'ib-biology'],
        'Social Sciences': ['ib-psychology', 'ib-business', 'ib-economics'],
        'Languages': ['ib-spanish-ab', 'ib-mandarin-ab', 'ib-french-b', 'ib-spanish-b'],
        'Others': ['ib-math-aa-hl', 'ib-eng-langlit-sl']
    }

    updates = Update.query.all()

    sections_subjects = {}
    for header in sections:
        L = []
        for id_name in sections[header]:
            sub = db.session.query(Subject).filter_by(id_name=id_name).all()[0]
            L.append({
                'name': sub.display_name,
                'link': pathToLink(sub.path)
            })
            print(L[-1]['link'])
        sections_subjects[header] = L

    for update in updates:
        update.link = pathToLink(update.subject.path)

    table = dictToTable(sections_subjects)

    return render_template('homepage.html', title='TISB Notes', table=table, updates=updates)


@app.route('/<path:subpath>')
def notes(subpath):
    path = os.getcwd() + '/app/notes/' + subpath

    subject_query = Subject.query.filter_by(path=('/notes/' + subpath).replace('//', '/')).all()
    print(subject_query)
    if subject_query:
        subject = subject_query[0]
        pages = getPages(subpath)
        return render_template('subject.html', subject=subject, pages=pages, updates=[])

    if isfile(path):
        return convert_notes(path)

    return 'my answer is no'
