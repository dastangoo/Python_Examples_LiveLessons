class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parnet.spam', self.value)

    def grok(self):
        print('Parent.grok')
        self.spam()
