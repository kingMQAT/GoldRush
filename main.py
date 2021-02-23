from digger import Digger
from os import getenv


def main():
    address = getenv('ADDRESS')
    port = getenv('Port')
    sheme = getenv('Schema')
    digger = Digger(
        url=f'{sheme}://{address}:{port}'
    )
    digger.get_license()
