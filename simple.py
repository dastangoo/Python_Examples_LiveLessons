# simple.py

x = 42

def spam():
    print('x is', x)

def run():
    print('Calling anohter spam')
    spam()

if __name__ == '__main__':
    print('Running')
    run()