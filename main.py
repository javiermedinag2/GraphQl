from flask import Flask
# Este código es un ejemplo de una aplicación Flask que utiliza GraphQL para crear una API.
from flask_graphql import GraphQLView
# Graphene es una biblioteca de Python para crear APIs GraphQL. GraphQLView es una vista de Flask que maneja las solicitudes GraphQL.
import graphene
class User(graphene.ObjectType):
        name = graphene.String()
        id = graphene.ID()
        email = graphene.String()

Usrs = [
            User(name="Mustafo", id=1, email="mustafo@example.com"),
            User(name="Chilpandolfo", id=2, email="chilpandolfo@example.com"),
            User(name="Mustafo Chilpandolfo", id=3, email="mustafochilpandolfo@example.com")
]

# La clase Query define los campos que estarán disponibles en la API GraphQL. En este caso, hay dos campos: "hello" y "Chilpandolfo". Cada campo tiene un resolver que devuelve una cadena de texto personalizada.
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    Chilpandolfo = graphene.String(name=graphene.String(default_value="Chilpandolfo"))
    Usurio = graphene.Field(User, id=graphene.ID(required=True))
    Usuarios = graphene.List(User)
    # El resolver de "hello" devuelve un saludo personalizado utilizando el nombre proporcionado. El resolver de "Chilpandolfo" devuelve una cadena que indica que el nombre proporcionado es un gran amigo de Mustafo.
    def resolve_hello(self, info, name):
        return f'Hello {name}!'
    # El resolver de "Chilpandolfo" devuelve un mensaje personalizado que indica que el nombre proporcionado es un gran amigo de Mustafo.
    def resolve_Chilpandolfo(self, info, name):
        return f'{name}! Es un gran amigo de Mustafo.'
    def resolve_Usurio(self, info, id):
        for user in Usrs:
            if str(user.id) == id:
                return user
        return None 
    # El resolver de "Usuarios" devuelve una lista de usuarios predefinidos. Cada usuario tiene un nombre y un ID. Esta lista se define como una variable de clase dentro de
    def resolve_Usuarios(self, info):
        return Usrs

class NewUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        email = graphene.String()
    user = graphene.Field(User)
    def mutate(self, info, id, name, email=None):
        user = User(name=name, id=id, email=email)
        Usrs.append(user)
        return NewUser(user=user)

class Mutation(graphene.ObjectType):
    createUser = NewUser.Field()
    

# Finalmente, se crea un esquema GraphQL utilizando la clase Query y se configura la aplicación Flask para manejar las solicitudes GraphQL en la ruta "/graphql". La aplicación se ejecuta en modo de depuración en el puerto 5000 y está disponible en todas las interfaces de red.
schema = graphene.Schema(query=Query, mutation=Mutation)
app = Flask(__name__)   
# La función add_url_rule se utiliza para agregar una nueva ruta a la aplicación Flask. En este caso, se agrega la ruta "/graphql" que está asociada con la vista GraphQLView. La vista GraphQLView se configura con el esquema GraphQL que se ha definido y se habilita la interfaz gráfica de GraphiQL para facilitar las pruebas de la API.
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')