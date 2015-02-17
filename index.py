#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pyxel(object):

    def __init__(self, user):
        self.user = user

    def test(param):
        def wrapper(fn):
            print "First", param

            def runner(self, *args, **kwargs):
                print param
                fn(" Help me to understand ")
                return self
            return runner

        return wrapper

    @test(param="VAR")
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

    def fun3(self):
	print  "Function number 3"

My("customer").so().send()


