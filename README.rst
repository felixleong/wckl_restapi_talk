Rest API 101 - Webcamp KL, May 2013 Code Demo
=============================================

Installation
------------

1. Create a virtualenv instance.

   .. note::

        All commands below are prepended with an expected bash prompt.
        
        * "$" indicates a normal bash prompt, virtualenv is not activated
        * "(.env)$" indicates a bash prompt with virtualenv activated

   .. code-block:: bash

        $ virtualenv .env
        $ source .env/bin/activate
        (.env)$

2. Install the required packages.

   .. code-block:: bash

        (.env)$ pip install -r requirements.txt

3. Create the local settings file and configure it to your liking.

   .. code-block:: bash

        (.env)$ cp restapi_talk/settings/local.example.py restapi_talk/settings/local.py
        (.env)$ vim restapi_talk/settings/local.py

4. Generate the database file. Follow any on-screen instructions that is shown.

   .. code-block:: bash

        (.env)$ ./manage.py syncdb && ./manage.py migrate

5. If needed, you can load up some sample data to get you started:


   .. code-block:: bash

        (.env)$ ./manage.py loaddata restapi_talk/fundtracking/ixtures/sample_data.json

Demo
----

The demo page is implemented in iPython Notebook and for you to execute the
code samples of accessing the API, here's what you'd need to do:

1. Start the Django server

   .. code-block:: bash

        python manage.py runserver

2. Start the iPython Notebook server

   .. code-block:: bash

        ipython notebok --pprint

3. If the iPython Notebook web interface is not loaded on your default web
   browser, you can access it by visiting http://localhost:8888/

4. Access the "REST API Demo" notebook and you can execute all codes that are
   listed there by selecting the cell and click on the "Run Cell" button.

Presentation
------------

The presentation slides are available at presentation/build/slides/index.html.
You can also `read the slide deck in one page`_.

If you want to adapt the content, you can follow the steps below:

1. Install the requirements for documentation generation:

   .. code-block:: bash

        (.env)$ pip install -r requirements.docs.txt

2. Edit presentation/source/index.rst, it's a `ReStructured Text`_ document.

3. Once you make the edits, you can generate the new slide show with the
   following command.

   .. code-block:: bash

        (.env)$ cd presentation
        (.env)$ make slides

License
-------

This work is licensed under a `Creative Commons Attribution-ShareAlike 3.0 Unported License`_.

.. _Creative Commons Attribution-ShareAlike 3.0 Unported License: http://creativecommons.org/licenses/by-sa/3.0/deed.en_US


.. _read the slide deck in one page: https://github.com/felixleong/wckl_restapi_talk/blob/master/presentation/source/index.rst
.. _ReStructured Text: http://docutils.sourceforge.net/rst.html
