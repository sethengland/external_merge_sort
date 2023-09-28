import os

def tear_down_previous(ts, s):
    for fn in (ts, s):
        if os.path.exists(fn):
            os.remove(fn)
    for fn in os.listdir():
        if fn.startswith('out_'):
            os.remove(fn)