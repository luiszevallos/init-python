
data_user = [
    {
        "user": "lzevallos",
        "password": "12345",
        "name": "Luis"
    }
]


def auth(user, password):
    data = list(filter(lambda us: us["user"] == user and us["password"] == password, data_user))
    if len(data) > 0:
        return data[0]
    else:
        return False
