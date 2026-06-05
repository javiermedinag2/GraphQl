from flask import Flask
# Este código es un ejemplo de una aplicación Flask que utiliza GraphQL para crear una API.
from flask_graphql import GraphQLView
# Graphene es una biblioteca de Python para crear APIs GraphQL. GraphQLView es una vista de Flask que maneja las solicitudes GraphQL.
import graphene
class User(graphene.ObjectType):
        name = graphene.String()
        id = graphene.ID()

# La clase Query define los campos que estarán disponibles en la API GraphQL. En este caso, hay dos campos: "hello" y "Chilpandolfo". Cada campo tiene un resolver que devuelve una cadena de texto personalizada.
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    Chilpandolfo = graphene.String(name=graphene.String(default_value="Chilpandolfo"))
    
    Usuarios = graphene.List(User)
 
    # El resolver de "hello" devuelve un saludo personalizado utilizando el nombre proporcionado. El resolver de "Chilpandolfo" devuelve una cadena que indica que el nombre proporcionado es un gran amigo de Mustafo.
    def resolve_hello(self, info, name):
        return f'Hello {name}!'
    # El resolver de "Chilpandolfo" devuelve un mensaje personalizado que indica que el nombre proporcionado es un gran amigo de Mustafo.
    def resolve_Chilpandolfo(self, info, name):
        return f'{name}! Es un gran amigo de Mustafo.'
    # El resolver de "Usuarios" devuelve una lista de usuarios predefinidos. Cada usuario tiene un nombre y un ID. Esta lista se define como una variable de clase dentro de
    def resolve_Usuarios(self, info):
        Usuarios = [
            User(name="Mustafo", id=1),
            User(name="Chilpandolfo", id=2),
            User(name="Mustafo Chilpandolfo", id=3)
        ]
        return Usuarios

# Finalmente, se crea un esquema GraphQL utilizando la clase Query y se configura la aplicación Flask para manejar las solicitudes GraphQL en la ruta "/graphql". La aplicación se ejecuta en modo de depuración en el puerto 5000 y está disponible en todas las interfaces de red.
schema = graphene.Schema(query=Query)
app = Flask(__name__)   
# La función add_url_rule se utiliza para agregar una nueva ruta a la aplicación Flask. En este caso, se agrega la ruta "/graphql" que está asociada con la vista GraphQLView. La vista GraphQLView se configura con el esquema GraphQL que se ha definido y se habilita la interfaz gráfica de GraphiQL para facilitar las pruebas de la API.
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')