==================
Zinnia-theme-html5
==================

Zinnia-theme-html5 is a python package providing HTML5 templates for
`django-blog-zinnia`_.


Installation
============

Once `Zinnia is installed`_ on your Django project and this package installed
on your `PYTHON_PATH`, simply register the `zinnia_html5` application in
the `INSTALLED_APP` section of your project's settings.

Now Zinnia is HTML5 ready.

.. warning::
   * `zinnia_html5` must be registered before the `zinnia` app to bypass
     the loading of the Zinnia's templates.
   * You need to use the ``django.template.loaders.eggs.Loader`` template
     loader if you have installed the package as an egg.


.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`Zinnia is installed`: http://django-blog-zinnia.com/documentation/getting-started/install/
