import datetime
from collections import namedtuple

from bottle import Bottle, request, response, abort, redirect

import db

sink = db.append()
next(sink)

app = Bottle()
with open('nyc.sh', 'r') as fp:
    nyc_sh = fp.read()

@app.get('/')
def index():
    return nyc_sh

@app.route('/attending/')
def slash():
    redirect('/attending')

@app.get('/attending')
def read():
    response.set_header('Content-Type', 'text/csv')
    with open('attending.csv') as fp:
        attending = fp.read()
    return attending

@app.post('/attending')
def write():
    if {'name','email.address','how.many'}.issubset(set(request.params)):
        r = db.Response(request.params['name'], request.params['email.address'], request.params['how.many'])
        sink.send(r)
        return 'Your response has been received.'
    else:
        abort(400, "You must specify \"name\", \"email.address\" and \"how.many\".")

app.run()
