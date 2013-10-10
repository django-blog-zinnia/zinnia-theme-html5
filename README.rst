==================
Zinnia-theme-html5
==================

Zinnia-theme-html5 is a python package providing HTML5 templates for
`django-blog-zinnia`_.


Installation
============

First of all you need to install and configure
`django-app-namespace-template-loader`_ into your project.

Then once `Zinnia is installed`_ on your Django project and this package
installed on your `PYTHON_PATH`, simply register the `zinnia_html5`
application in the `INSTALLED_APP` section of your project's settings.

Now Zinnia is HTML5 ready.

.. warning::
   * `zinnia_html5` must be registered before the `zinnia` app to bypass
     the loading of the Zinnia's templates.
   * You need to use the ``django.template.loaders.eggs.Loader`` template
     loader if you have installed the package as an egg.


HTML5 Validation
================

If you want to have strict HTML5 documents and pass the validation tests
you must register the ``DraftHTML5ValidatorCleaner`` middleware to clean
the templates of the not already supported attributes or relationships. ::

    MIDDLEWARE_CLASSES = (
        ... # Your middlewares
        'zinnia_html5.middleware.DraftHTML5ValidatorCleaner',
        )

The problem is that HTML5 is still in draft, and some microformats are not
already allowed by the on-line validators.

Instead of rewriting all the Zinnia's templates it's easier to add this
middleware and disable it when the HTML5 specifications will be completed
and the on-line HTML5 validators up-to-date.

.. note::
   You need to install the `beautifulsoup4`_ and `html5lib`_ packages for
   using this middleware.

.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`django-app-namespace-template-loader`: https://github.com/Fantomas42/django-app-namespace-template-loader
.. _`Zinnia is installed`: http://docs.django-blog-zinnia.com/en/latest/getting-started/install.html
.. _`beautifulsoup4`: http://pypi.python.org/pypi/beautifulsoup4
.. _`html5lib`: http://pypi.python.org/pypi/html5lib
