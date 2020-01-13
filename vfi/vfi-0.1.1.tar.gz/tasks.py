import shutil

from invoke import task


@task
def dist(ctx):
    ctx.run("python setup.py sdist bdist_wheel")


@task
def publish(ctx):
    ctx.run("python -m pip install --upgrade pip")
    ctx.run("pip install setuptools wheel twine")
    ctx.run("twine upload dist/* --verbose")
    shutil.rmtree("build")
    shutil.rmtree("dist")
    shutil.rmtree("vfi.egg-info")


@task
def docs(ctx):
    ctx.run("cd docs && make html")


@task
def test(ctx):
    ctx.run("pytest -v --cov --cov-report term-missing")


@task
def lint(ctx):
    ctx.run("black vfi --check")
    ctx.run("flake8 vfi")
