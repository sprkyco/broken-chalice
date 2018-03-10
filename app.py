from os import popen
from chalice import Chalice, Response


app = Chalice(app_name='broken-chalice')
app.debug = True

def rp(command):
    return popen(command).read()

# Code Injection
@app.route('/evaluate', methods = ['POST', 'GET'], content_types=['application/json'])
def evaluate():
    expression = None
    if app.current_request.method == 'POST':
        expression = app.current_request.json_body['expression']
    return "Result:\n" + (str(eval(expression)).replace('\n', '\n')  if expression else "No expression provided")

# Command Execution
@app.route('/trial-balloon-art', methods=['POST'])
def getTrialBalloonArt():
    if request.method == 'POST':
        version = app.current_request.json_body['version']
        print("version equals: "+version)
        sigsciBalloon = "https://dl.signalsciences.net/trial-balloon/{}/art".format(version)
        out = rp("curl {}".format(sigsciBalloon))
        return out