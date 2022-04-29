from base64 import encode
from types import coroutine

# main function(Entry point)
def cat(f, case_insensitive, child):
    if case_insensitive :
        line_processor = lambda l: l.lower()
        
    else :
        line_processor = lambda l: l
    
    for line in f:
        child.send(line_processor(line))

@coroutine
def grep(substring, case_insensitive, child):
    if case_insensitive : 
        substring = substring.lower()
    
    while True :
        text = (yield) # yield를 통해서 받아온다. 중간에 넣어지는 값을!
        child.send(text.count(substring))

@coroutine
def count(substring):
    n = 0
    try :
        while True:
            n += (yield)
    
    except GeneratorExit:
        print(substring, n)
        
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action = 'store_true', dest = 'case_insensitive')
    parser.add_argument('pattern', type=str)
    parser.add_argument('infile', type=argparse.FileType('r'))
    
    args = parser.parse_args()
    
    cat(args.infile, args.case_insensitive, 
            grep(args.pattern, args.case_insensitive, count(args.pattern)))