# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Malte Bublitz
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
# 
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# 

import sys

class ANSIColor(object):
    _name = None
    _code = None
    def __init__(self, n=None, c=None):
        self._name = n
        self._code = c
        
    def getName(self):
        return self._name
        
    def setName(self, n):
        self._name = n
        
    def getCode(self):
        return self._code
        
    def setCode(self, c):
        self._code = c
        
class ANSIConsole(object):
    """
    A small helper class for ANSI terminals.
    Based on de.malte_bublitz.util.ANSIConsole from malte70/java-util
    """
    STDIN  = None
    STDOUT = None
    STDERR = None
    _colors = {
            "BLACK":        "0;30m",
            "RED":          "0;31m",
            "GREEN":        "0;32m",
            "YELLOW":       "0;33m",
            "BLUE":         "0;34m",
            "DARK_MAGENTA": "0;35m",
            "GREY":         "0;37m",
            "DARK_GREY":    "1;30m",
            "LIGHT_RED":    "1;31m",
            "LIGHT_GREEN":  "1;32m",
            "LIGHT_YELLOW": "1;33m",
            "LIGHT_BLUE":   "1;34m",
            "MAGENTA":      "1;35m",
            "CYAN":         "1;36m",
            "WHITE":        "1;37m"
        }
    _attributes = {
            "BOLD":      "1m",
            "UNDERLINE": "4m",
            "RESET":     "0m"
            }
    def __init__(self):
        self.STDIN  = sys.stdin
        self.STDOUT = sys.stdout
        self.STDERR = sys.stderr
        
    def escape(self, code):
        self.STDOUT.write(chr(27)+"["+code)
        
    def clear(self):
        self.escape("H")
        self.escape("2J")
        
    def getColor(self, color_name):
        try:
            return ANSIColor(
                    color_name,
                    ANSIConsole._colors[color_name]
                    )
        except IndexError:
            return None
        
    def setForegroundColor(self, color):
        self.escape(color.getCode())
        
    def setAttribute(self, attribute):
        try:
            self.escape(self._attributes[attribute])
        except IndexError:
            return False
        return True
        
    def write(self, _string):
        self.STDOUT.write(_string)
        
    def writeln(self, _string):
        self.STDOUT.write(_string+"\n")
        
    def write_err(self, _string):
        self.STDERR.write(_string)
        
    def writeln_err(self, _string):
        self.STDERR.write(_string+"\n")
        
    def readLine(self):
        return input()
        
    def printLine(self, element, length=10):
        for x in range(0,length-1):
            self.write(element)
        
    def printTux(self):
        """
        The most important function of course ;-)
        """
        self.write(
			"    .--.\n" + 
			"   |o_o |\n" +
			"   |:_/ |\n" +
			"  //   \\ \\\n" +
			" (|     | )\n" +
			"/'\\_   _/`\\\n" +
			"\\___)=(___/\n"
		)
