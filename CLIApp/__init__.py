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

__doc__ = """
Command Line Application

"""

from CLIApp.ansiconsole import *
from CLIApp.app import *

def main():
    class MyCLIApp(CLIApp):
        _action_unknown = "action_unknown"
        def action_default(self, isDirect=True):
            if isDirect:
                self.c.writeln("Default action")
            self.c.writeln("Global options: "+str(self._options))
            self.c.writeln("Action        : "+str(self._action))
            self.c.writeln("Action options: "+str(self._action_options))
            self.c.writeln("Arguments     : "+str(self._arguments))

        def action_test(self):
            self.c.writeln("Test action")
            self.action_default(False)

        def action_unknown(self):
            self.c.setForegroundColor(self.c.getColor("RED"))
            self.c.writeln("Unknown action: "+self._action)
            self.setExitCode(1)
            self.c.setAttribute("RESET")
            
    my_app = MyCLIApp()
    my_app.run()
    my_app.exit()

if __name__ == "__main__":
    main()
