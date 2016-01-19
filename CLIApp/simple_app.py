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
from CLIApp.ansiconsole import ANSIColor, ANSIConsole

class SimpleCLIApp(object):
    _options = []
    _arguments = []
    _exitcode = 0
    c = None
    
    def __init__(self):
        self.c = ANSIConsole()
        self.parseArgs()
        
    def parseArgs(self):
        if len(sys.argv) > 1:
            for i, arg in enumerate(sys.argv[1:]):
                if len(arg) > 2 and arg[0:2] == "--":
                    self._options.append(arg)
                elif arg == "--":
                    self._arguments += sys.argv[i:]
                    break
                elif arg[0:1] == "-":
                    self._options.append(arg)
                else:
                    self._arguments.append(arg)
                
    def setExitCode(self, code):
        self._exitcode = code
        
    def run(self):
        return True
        
    def exit(self):
        sys.exit(self._exitcode)
        
def main():
    class MyCLIApp(SimpleCLIApp):
        def run(self):
            self.c.writeln("Options:")
            for option in self._options:
                self.c.writeln("\t" + option)
            
    my_app = MyCLIApp()
    my_app.run()
    my_app.exit()

if __name__ == "__main__":
    main()
