from flask import Flask
from flask_graphql import GraphQLView
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    Chilpandolfo = graphene.String(name=graphene.String(default_value="Chilpandolfo"))
    def resolve_hello(self, info, name):
        return f'Hello {name}!'
    def resolve_Chilpandolfo(self, info, name):
        return f'{name}! Es un gran amigo de Mustafo.'
schema = graphene.Schema(query=Query)
app = Flask(__name__)   
app.Eadd_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')