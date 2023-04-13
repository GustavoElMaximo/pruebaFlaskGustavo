# materializadora 2022
# BackEnd source
# Holistic Diet application


from flask_graphql import GraphQLView
from schemas import schema


@app.route('/')
def hello_world():
    return 'Hello World!'


"""app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    ),
)"""


if __name__ == "__main__":
#    init_db()
    app.run()