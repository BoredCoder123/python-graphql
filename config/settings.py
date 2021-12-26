from flask import Flask
from config.database import db_session
from .schema import schema
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "asdqwezxc123asxcweklrjsvklj"
app.config['REFRESH_EXP_LENGTH'] = 30
app.config["ACCESS_EXP_LENGTH"] = 10
app.config["JWT_SECRET_KEY"] = "Bearer"

auth = GraphQLAuth(app)

app.add_url_rule("/graphql",
                 view_func=GraphQLView.as_view(
                    "graphql",
                     schema=schema,
                     graphiql=True
                ))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
