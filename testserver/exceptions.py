#!/usr/bin/env
# -*- coding: utf-8 -*-


class TimeOut(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return repr(self.value)
