from .models import User
from app import app
from . import db

import click
from flask.cli import with_appcontext

@app.cli.command("seed-db")
@click.command()
@with_appcontext
def seed():
    """Seed the database."""
    seed_db()


def seed_db():
    for number in range(11, 20):
        user = User(username=f'Test user {number}',email=f'{number}@gmail.com')
        db.session.add(user)
        db.session.flush()
    db.session.commit()