import hashlib
import datetime
import time
import json

def timestamp():
    now = datetime.datetime.utcnow ()
    timestamp = time.mktime ( now.timetuple () )
    return timestamp

def hash(message):
    h = hashlib.sha3_256 ()
    h.update ( message )
    return h.hexdigest()

def block_hash(block):
    block_string = json.dumps( block, sort_keys=True ).encode()
    return hash( block_string )
