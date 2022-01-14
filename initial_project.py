from getpass import getpass
import login_auth


def run():
    user = input("Ingrese usuario: ")
    password = getpass("Ingrese contraseña: ")
    data = login_auth.auth(user, password)
    if data:
        print("Bienvenido " + data["name"])
    else:
        print("Usuario o contraseña incorrecta")


if __name__ == "__main__":
    run()

