#!/usr/bin/python3
"""This is the console for use with all the CRUD
   Operations for the AirBnB clone project
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

   def do_EOF(self, line):
       return True
   def do_quit(self, line):
       print("See you next time!")
       return True
    
