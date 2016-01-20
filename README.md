# pyCLIApp

pyCLIApp is a basic bootstrap framework for command line applications
written in Python, mainly on GNU/Linux and other Unix–Systems.

## Installation

Before installing, especially if you cloned the Git master branch, you
should run ```test.sh``` to ensure everything works before installing.
After that, you can run setup.py to install:

    ./test.sh && python setup.py install

## Example

```python
from CLIApp.simple_app import SimpleCLIApp

APP_NAME       = "Hello World Example"
APP_VERSION    = "0.1"
APP_EXECUTABLE = "example"

class HelloWorldApp(SimpleCLIApp):
	def _version(self):
		self.c.writeln(APP_NAME + " " + APP_VERSION)
		
	def _help(self):
		self.c.writeln("Usage: {} <name>".format(APP_EXECUTABLE))
		
	def _greet(self, name):
		self.c.writeln("Hello, {}!".format(name))
		
	def run(self):
		if "-h" in self._options:
			self._help()
		elif "-V" in self._options or "-v" in self._options:
			self._version()
		else:
			if len(self._arguments) > 0:
				name = " ".join(self._arguments)
			else:
				name = "World"
			self._greet(name)
		
def main():
	app = HelloWorldApp()
	app.run()

if __name__=="__main__":
	main()
```
