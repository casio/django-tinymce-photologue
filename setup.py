#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'django-tinymce-photologue',
    version = '0.2.1',
    description = "photologue app for tinymce",
    long_description = open('README.rst').read(),
    author = 'Aljosa Mohorovic',
    author_email = 'aljosa.mohorovic@gmail.com',
    url='http://github.com/aljosa/django-tinymce-photologue/',
    packages = find_packages(),
    include_package_data = True,
    license = "MIT License",
    keywords = "django tinymce photologue",
    platforms = ['any'],
)
