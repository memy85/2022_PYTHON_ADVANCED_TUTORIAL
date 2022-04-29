import asyncio
from types import coroutine

def main(sub):
    print('Hello ...')
    sub.send(None) # First we have to initiate Generator with None-type
    sub.send('say it!!')
    
@coroutine
def sub_func(anything):
    print('uh..uh..')
    while True :
        anything = (yield)
        if anything :
            print('...World!')
    

if __name__== "__main__":
    main(sub_func(False))
    