#/usr/bin/python
# coding=utf-8

import zlib
import StringIO
import gzip
from src.libs.rc4 import RC4
from config import CTYPE_KEY


def pack(string):
    output = StringIO.StringIO()
    output.write(string)
    return gzip.GzipFile(fileobj=output)


def unpack(string):
    output = StringIO.StringIO()
    output.write(string)
    return gzip.open(output)


def dordata(data):
    rc4 = RC4(CTYPE_KEY)
    rdata = rc4.decode(data)
    try:
        result = zlib.decompress(rdata)
        return result
    except Exception as e:
        pass
    return None


def dopdata(data):
    rc4 = RC4(CTYPE_KEY)
    result = rc4.encode((zlib.compress(data)))
    if result:
        return result
    else:
        return False
