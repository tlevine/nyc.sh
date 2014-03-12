#!/usr/bin/env python3
import os
from queue import Queue
from threading import Thread

from bottle import Bottle, request, response, abort, redirect

import db

queue = Queue()
Thread(None, target = db.pull, args = (queue,), daemon = True).start()

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
    if {'name','email.address','how.many'}.issubset(set(request.forms)):
        r = db.Response(request.forms['name'], request.forms['email.address'], request.forms['how.many'])
        queue.put(r)
        return 'echo Your response has been received.\nwget -O - http://nyc.sh/attending'
    else:
        abort(400, "You must specify \"name\", \"email.address\" and \"how.many\".")

app.run()
