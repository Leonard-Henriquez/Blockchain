import hashlib
import datetime
import time


def timestamp():
    now = datetime.datetime.utcnow ()
    timestamp = time.mktime ( now.timetuple () )
    return timestamp

def hash(message):
    h = hashlib.sha3_256 ()
    h.update ( message )
    return h.hexdigest()
