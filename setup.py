"""Setup script of zinnia-theme-html5"""
from setuptools import setup
from setuptools import find_packages

import zinnia_html5

setup(
    name='zinnia-theme-html5',
    version=zinnia_html5.__version__,

    description='HTML5 theme for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, theme, skin, html5',

    author=zinnia_html5.__author__,
    author_email=zinnia_html5.__email__,
    url=zinnia_html5.__url__,

    packages=find_packages(exclude=['demo_zinnia_html5']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_html5.__license__,
    include_package_data=True,
    zip_safe=False
)
