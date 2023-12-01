from message_schema import message_schema
import os
import sys

rpath = os.path.abspath('../../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)


def channel_schema():
    return {
        "name": str,
        "date": str,
        "messages": [message_schema()],
    }
