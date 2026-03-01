import hashlib

# "Base de datos" simulada
usuarios_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Crear usuario
def crear_usuario(username, password, email):
    if username in usuarios_db:
        return False, "Usuario ya existe"
    usuarios_db[username] = {
        "password": hash_password(password),
        "email": email
    }
    return True, "Usuario creado"

# Leer usuario
def obtener_usuario(username):
    return usuarios_db.get(username, None)

# Actualizar usuario
def actualizar_usuario(username, password=None, email=None):
    usuario = usuarios_db.get(username)
    if not usuario:
        return False, "Usuario no existe"
    if password:
        usuario["password"] = hash_password(password)
    if email:
        usuario["email"] = email
    return True, "Usuario actualizado"

# Borrar usuario
def eliminar_usuario(username):
    if username in usuarios_db:
        del usuarios_db[username]
        return True, "Usuario eliminado"
    return False, "Usuario no existe"

# Autenticación simple
def autenticar_usuario(username, password):
    usuario = usuarios_db.get(username)
    if usuario and usuario["password"] == hash_password(password):
        return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    '''
    print(crear_usuario("lau", "1234", "lau@example.com"))
    print(obtener_usuario("lau"))
    print(autenticar_usuario("lau", "1234"))
    print(actualizar_usuario("lau", password="5678"))
    print(autenticar_usuario("lau", "5678"))
    print(eliminar_usuario("lau"))
    print(obtener_usuario("lau"))
    '''
