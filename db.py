Response = namedtuple('Response', ['name','email_address','how_many'])
def append():
    try:
        needs_header = not os.path.exists(fp)
        with open('attending.csv', 'a') as fp:
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

