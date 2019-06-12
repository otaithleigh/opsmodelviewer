from invoke import task


@task
def test(c, verbose=False):
    """Run pytest for the project."""
    command = ['pytest -W ignore::DeprecationWarning --color=yes']
    command.append('--verbose' if verbose else '')
    c.run(' '.join(command))


@task
def build(c):
    """Build the packages."""
    c.run('python setup.py bdist_wheel')
    c.run('conda build pkg')
