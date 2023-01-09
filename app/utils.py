from requests import get


def get_user():
    res = get('https://random-data-api.com/api/v2/users')
    if res.ok:
        return res.json()
    return None


def get_fullname_and_len():
    user = get_user()
    if user:
        full_name = f'{user["first_name"]} {user["last_name"]}'
        return full_name, len(full_name)
    return '', 0
