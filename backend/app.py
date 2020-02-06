import os

from flask import Flask
from flask_graphql import GraphQLView

from schema import schema
from database import create_db


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    app.secret_key = app.config['SECRET_KEY']

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    create_db()

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
