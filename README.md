# Heroku Python Skeleton

This repository has all the base files ready for deploying a Heroku application, including a simple database model managed with flask-sqlalchemy.

My 'contribution' here is incorporation of the [SB Admin 2 bootstrap template](http://startbootstrap.com/template-overviews/sb-admin-2/)
It will no longer be a 'simple' app but ideally will have working links to pages which use jinja templates accordingly

## Bower installation

```bash
$ sudo apt-get install nodejs
$ sudo apt-get install npm
$ sudo npm install -g bower
```

when trying `$ bower`, should you get the following error : 
`$ /usr/bin/env: node: No such file or directory`

You can use a symlink to fix:
$ sudo ln -s /usr/bin/nodejs /usr/bin/node

Once bower is installed you can simply run in the /static directory:

$ bower install startbootstrap-sb-admin-2

## Usage

### Initial

```bash
$ git clone https://github.com/yuvadm/heroku-python-skeleton.git
$ cd heroku-python-skeleton
$ heroku create
$ git push heroku master
```

### Database

```bash
$ heroku addons:add heroku-postgresql:dev
-----> Adding heroku-postgresql:dev to some-app-name... done, v196 (free)
Attached as HEROKU_POSTGRESQL_COLOR
Database has been created and is available
$ heroku pg:promote HEROKU_POSTGRESQL_COLOR
$ heroku run python
```

and in the Python REPL:

```python
>>> from app import db
>>> db.create_all()
```

For a detailed introduction see [http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/](http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/).
