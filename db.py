import csv, os
import datetime
from collections import namedtuple

Response = namedtuple('Response', ['name','email_address','how_many'])
fn = 'attending.csv'

def read():
    with open(fn) as fp:
        attending = fp.read()
    return attending

def pull(queue):
    try:
        fieldnames = ['submitted','name','email.address','how.many']
        if not os.path.exists(fn):
            with open(fn, 'x') as fp:
                w = csv.DictWriter(fp, fieldnames = fieldnames)
                w.writeheader()
        while True:
            response = queue.get()
            record = {'submitted':datetime.datetime.now().isoformat(),
                      'name': response.name,
                      'email.address': response.email_address,
                      'how.many': response.how_many}
            with open(fn, 'a') as fp:
                w = csv.DictWriter(fp, fieldnames = fieldnames)
                w.writerow(record)
            queue.task_done()
    except GeneratorExit:
        pass

