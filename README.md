# Python web app example

Example of Python web app with a debian packaging.

Features:

 * `dh_virtualenv`
   
   `dh_virtualenv` takes care of creating venv in the debian package with
   all Python dependencies. You can set up dependencies in `setup.py` which
   is then used to collect dependencies during the build and then distributed
   with your app bundle. It takes more space in your build and more time to
   create it, but brings stability without colision with installed Python
   packages on the server (becase of some tools for administrator or other
   application on shared web server).

 * systemd
    
   Package also includes services to run uwsgi and nginx. This one is
   questionable. I prefer to distribute app which can be installed without
   any special configuration and cannot do any harm to other apps installed
   on the same server, so all my apps uses own nginx process. It uses more
   CPU, but usually it's not even noticeable. Start of the app is then as
   simple as `systemctl statr webapp`.

   Service for the proxy (nginx) is dependendy of the first one (uwsgi),
   which is started automatically. But when you need to do restart or
   other trick with the app, you need to call for example also 
   `systemctl stop webapp.proxy`. Maybe little bit odd, but brings
   better maintenance options.
   
 * Configuration files

   Both, uwsgi and nginx, have configuration in the package, which is good.
   I personaly like when I can install package without need to configure it
   on the server and keep configuration files separated. All configuration
   files are tracked in one repository. Easy to deploy.

   Same is valid for configuration files of application. See `config` module
   where is module for every environment. Same technique could be applied
   for any configuration file.

   Secure options, like secure key or credentials to the database, are
   handled by an environment.

 * Scripts

   As systemd doesn't allow you to create custom commands for services, if you
   need some specific command, like database migrations, to be ready for
   you, just create business logic in your module and then specify your
   commands in your `setup.py`, in section `console_scripts` similarly like
   example script.

   Because of use of `dh_virtualenv`, script is installed in venv 
   (`/var/www/webapp/venv/webapp/bin/SCRIPT`). To have that script handy
   in the system, write link also in `debian/webapp.links` as shown for an
   example script.

 * Development `Makefile`

   During development is available `Makefile` which can be used to quickly
   run lint tools, tests, application in development mode or build the
   debian package. `Makefile` is designed to use a virtualenv and update
   dependencies every time you change them in `setup.py`. More about that
   in my blog post:

   https://blog.horejsek.com/makefile-with-python/

 * Base Flask app

   For now it's very simple app, but shows usage of mypy, pytest, configuration
   files and database connection in Flask's global.

For more info you can go to my blog post about it:

https://blog.horejsek.com/python-packaging/

## Development

To prepare your dev envrionment in Debian-like system, run this command:

    (sudo) make prepare-dev

To run lint tools or tests, use this commands:

    make lint
    make test

To run web server in development mode:

    make run

More useful commands can be explored by typing `make`.

## Deployment

Create deb package and install it to your system:

    make build
    (sudo) make install

Start included service:

    systemctl start webapp

That's it!

## Docker

For comparison I included also simple docker version managed by docker-compose.
I'm not big fan of docker--I don't think docker is answer for everything--but
the ideas are the same. To have simple development environment and package for
the deployment with included configuration files and services. The question
is whether you need orchestration or just simple plain one instance.
