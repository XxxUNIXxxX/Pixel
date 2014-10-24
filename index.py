# -*- coding: utf-8 -*-

class MO(object):

    def __init__(self, user):
        self.user = user

    def test(param):
        def wrapper(fn):
            print "1", param

            def runner(self, *args, **kwargs):
                print param
                fn(" Help me to understand ")
                return self
            return runner

        return wrapper

    @test(param="asd")
    def send(word = "Hello"):
        print word

    @test(param='ASV')
    def so(self, tom="TOM"):
        print tom
        print "SELF ", self


    def fun1(self):
        print self.user

    def fun2(self):
        print "123\n"


MO("customer").so().send()