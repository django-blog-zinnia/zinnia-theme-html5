==================
Zinnia-theme-html5
==================

Zinnia-theme-html5 is a python package providing an HTML5 theme for
`django-blog-zinnia`_.


Installation
============

Once django-blog-zinnia is installed on your Django project,
and this package installed on your `PYTHON_PATH`, simply register the
`zinnia_html5` application in the `INSTALLED_APP` section of your project's
settings.


.. warning::
   * `zinnia_html5` must be registered before the `zinnia` app.
   * You will probably need to activate the egg template loader.


.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
