Description of the project
	This project is trying to build a replicate of the airbnb web application

Description of the command interpreter
	This is more like a shell and provide a framework for building simple, interative command-line interpreter application within Python


How to start the interpreter
 - Define a command Interpreter Class (cmd.Cmd)
 - Initiate your command interpreter (Create your custom command)
 - Start the command loop

How to use the command interpreter
 - Entering commands
 - Command Execution
 - Command output
 - Exiting the interpreting

Examples:

import cmd

class MyCmdInterpreter(cmd.Cmd):

	intro = "Welcome to My command  Interpreter. Type 'Help'"
	prompt = "(mycmd) "

	def do_greet(self, name):
		"""Greets the user"""
		print("Hello,", name)

	def do_quit(self, arg):
		"""Exit the command interpreter"""
		print("Exiting...")
		return True

if __name__ == "__main__":
	MyCmdInterpreter().cmdloop()
