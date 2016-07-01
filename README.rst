afilnet
===============

This package is an easy way to use send sms, email and voice(texto-to-speech) using Afilnet services in python.


Installation
------------

.. code-block:: bash

    pip install django-txtlocal


Receiving Messages
~~~~~~~~~~~~~~~~~~

Add to your ``urls.py``:

.. code-block:: python

    url(r'^', include('txtlocal.urls'))

Add to your ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'txtlocal',
        ...
    )

Run:

.. code-block:: bash

    python manage.py syncdb


Sending Messages
~~~~~~~~~~~~~~~~

Add to your ``settings.py``:

.. code-block:: python

    TXTLOCAL_USERNAME = Your username with textlocal
    TXTLOCAL_PASSWORD = Your password with textlocal
    TXTLOCAL_FROM = Word up to 11 characters or number up to 14 digits. String.


You can also set ``TXTLOCAL_ENDPOINT``. This defaults to ``https://www.txtlocal.com/sendsmspost.php``


Infrequently Asked Questions
----------------------------

**Why txtlocal, not tExtlocal?**

Because textlocal.com used to be txtlocal.co.uk
