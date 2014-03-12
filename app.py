#!/usr/bin/env python3
import datetime
import os

from bottle import Bottle, request, response, abort, redirect

import db

sink = db.write()
next(sink)

app = Bottle()
with open('nyc.sh', 'r') as fp:
    nyc_sh = fp.read()

@app.get('/')
def index():
    response.set_header('Content-Type', 'text/x-shellscript')
    return nyc_sh

@app.route('/attending/')
def slash():
    redirect('/attending')

@app.get('/attending')
def read():
    response.set_header('Content-Type', 'text/csv')
    return db.read()

@app.post('/attending')
def write():
    if {'name','email.address','how.many'}.issubset(set(request.query)):
        r = db.Response(request.query['name'], request.query['email.address'], request.query['how.many'])
        sink.send(r)
        return 'Your response has been received.'
    else:
        abort(400, "You must specify \"name\", \"email.address\" and \"how.many\".")

app.run()
