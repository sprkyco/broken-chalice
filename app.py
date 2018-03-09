from os import popen
from chalice import Chalice, Response


app = Chalice(app_name='broken-chalice')
app.debug = True

def rp(command):
    return popen(command).read()

@app.route('/{address}')
def nslookup(address):
    return rp("nslookup "+address)

# code injection
@app.route('/evaluate', methods = ['POST', 'GET'], content_types=['application/json'])
def evaluate():
    expression = None
    if app.current_request.method == 'POST':
        expression = app.current_request.json_body['expression']
    return "Result:\n" + (str(eval(expression)).replace('\n', '\n')  if expression else "No expression provided")
    
@app.route('/trial-balloon-art', methods=['POST'])
def getTrialBalloonArt():
    request = app.current_request
    if request.method == 'POST':
        version = request.json_body['version']
        print("version equals: "+version)
        return rp("curl https://dl.signalsciences.net/trial-balloon/{}/art".format(version))