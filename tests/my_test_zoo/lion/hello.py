import datetime


def say_hi(name=''):
    print("Hello. {}".format(datetime.datetime.utcnow()))

    # Test using 3rd-party library
    # repo = requests.get('http://httpbin.org/get')
    # ujson.dumps({"foo": "bar"})
    return 'Hi, {}'.format(name)
