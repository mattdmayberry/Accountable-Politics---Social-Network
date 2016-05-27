from invoke import run, task


@task
def install():
    run('sudo pip install -r requirements.txt')
    run('bundle')

@task
def serve():
    run('PYTHONPATH=. python accountable/app.py')

@task
def serve_debug():
    run('PYTHONPATH=. FLASK_DEBUG=1 python accountable/app.py')