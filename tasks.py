from invoke import task


@task
def test(c, verbose=False):
    """Run pytest for the project."""
    command = ['pytest -W ignore::DeprecationWarning --color=yes']
    command.append('--verbose' if verbose else '')
    c.run(' '.join(command))


@task
def build(c):
    """Build the conda package."""
    c.run('conda build pkg')
