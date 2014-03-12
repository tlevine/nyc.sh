import csv, os
from collections import namedtuple

Response = namedtuple('Response', ['name','email_address','how_many'])
fn = 'attending.csv'

def read():
    with open(fn) as fp:
        attending = fp.read()
    return attending

def write():
    try:
        needs_header = not os.path.exists(fn)
        with open(fn, 'a') as fp:
            w = csv.DictWriter(fp, fieldnames = ['submitted','name','email.address','how.many'])
            if needs_header:
                w.writeheader()
            while True:
                response = (yield)
                record = {'submitted':datetime.datetime.now().isoformat(),
                          'name': response.name,
                          'email.address': response.email_address,
                          'how.many': response.how_many}
                w.writerow(w)
    except GeneratorExit:
        pass

