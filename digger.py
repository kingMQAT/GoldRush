from requests import get, post


class Digger:
    def __init__(self, url):
        self._balance = 0
        self._x = 0
        self._y = 0
        self._url = url
        self._wallet = []
        self._licenses = []

    def get_balance(self):
        response = get(
            url=f'{self._url}/balance'
        ).json()
        self._balance = response['balance']
        self._wallet = response['wallet']
        return self._balance

    def get_license(self, pay=False):
        if pay:
            response = post(
                url=f'{self._url}/licenses'
            ).json()
        else:
            response = post(
                url=f'{self._url}/licenses',
                data={self._wallet}
            ).json()
        self._licenses.append(response)
