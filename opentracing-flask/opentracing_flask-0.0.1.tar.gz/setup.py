#-*- coding:utf-8 -*-
from setuptools import setup

setup(
    name="opentracing_flask",
    version="0.0.1",
    keywords=("opentracing", "python", "flask"),
    license="MIT License",
    url="https://github.com/darinautilus/opentracing-flask",
    author="zhangbin",
    author_email="battlescars@qq.com",
    packages = ["opentracing_flask"],
    include_package_data = True,
    platforms = "any",
    install_requires = ["jaeger-client", "Flask-OpenTracing", "opentracing", "opentracing-instrumentation", "grequests"]
)

