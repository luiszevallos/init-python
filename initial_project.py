

def login_user():
    data_user = [
        {
            "user": "lzevallos",
            "password": "12345",
            "name": "Luis"
        }
    ]
    user_name = input("Ingrese usuario: ")   
    user_password = input("Ingrese contraseña: ")   
    data = list(filter(lambda us: us["user"] == user_name and us["password"] == user_password, data_user))
    if len(data) > 0:
        
        return True
    else:
        return False


def run():
    auth = login_user()
    if auth:
        print("Esta logeado")
    else:
        print("Usuario o contraseña incorrecta")


if __name__ == "__main__":
    run()

