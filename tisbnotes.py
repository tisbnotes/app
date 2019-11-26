from app import app, db
from app.models import Subject, Update

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Subject': Subject, 'Update': Update}
