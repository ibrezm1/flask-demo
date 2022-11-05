# Example Database app

This is an example database app using PostgreSQL, Flask-SQLAlchemy and Flask-Migrate

To begin using this app you can do the following:

1. Clone the repository to your local machine.
2. Create a Python virtual environment e.g. `python -m venv venv` (You may need to use `python3` instead)
3. Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. Note: Ensure you have PostgreSQL already installed and a database created.
5. Edit the `app/__init__.py` file and enter your database credentials and database name.
6. Run the migrations by typing `flask db upgrade`
7. Start the development server using `python run.py`.

## Separate Config file

I have included a separate config file `app/config.py` that can be used for setting up
configuration for different environments e.g. Development and Production

Edit `app/__init__.py` and uncomment the following lines:

```python
# from .config import Config
...
# app.config.from_object(Config)
```

Using the separate config file will also require you to set environment variables on your local computer or server at the command line. For example on Linux or MacOS:

```bash
export SECRET_KEY="my-super-secret-key"
export DATABASE_URL="postgresql://yourusername:yourpassword@localhost/databasename"
```

Or on Windows:

```powershell
set SECRET_KEY="my-super-secret-key"
set DATABASE_URL="postgresql://yourusername:yourpassword@localhost/databasename"
```

And on Heroku:

```bash
heroku config:set SECRET_KEY="my-super-secret-key"
heroku config:set DATABASE_URL="postgresql://yourusername:yourpassword@localhost/databasename"
```

### .env Files

You can also create a `.env` file in the root of your project and add your Environment variables there. See `.env.sample` as an example. The `config.py` file is already setup to automatically load the `.env` file.

## Git Location
[Current repo](https://github.com/uwi-info3180/flask-db-demo)
[Simple App](https://github.com/wftutorials/flask-beginner-tutorial)
[Quickstart with Auth](https://github.com/stribny/flask-api-quickstart)
[Good Tut in red ritmschool](https://www.rithmschool.com/courses/flask-fundamentals/using-jsonify)
[Crud with SQLCHEMY](https://www.educative.io/answers/how-to-connect-flask-to-a-database-with-flask-sqlalchemy)
[Flask Commands](https://nickjanetakis.com/blog/flask-db-helps-you-migrate-seed-and-reset-your-sql-database)
[Blueprints](https://testdriven.io/blog/flask-apifairy/)
[Complex db Relations migrate](https://github.com/RobertBoes/flask-migrate-example/blob/master/app.py)
[Real world example](https://github.com/gothinkster/flask-realworld-example-app)
[Heroku deployment](https://medium.com/thedevproject/use-flask-cli-to-create-commands-for-your-postgresql-on-heroku-in-6-simple-steps-e8166c024c8d)
[Other oninits](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
[Mega Tut Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)