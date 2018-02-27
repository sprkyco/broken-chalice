from chalice import Chalice
from os import popen

app = Chalice(app_name='broken-chalice')

def rp(command):
    return popen(command).read()

@app.route('/{address}')
def nslookup(address):
    return rp("nslookup "+address)
