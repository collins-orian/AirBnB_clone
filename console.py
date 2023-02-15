#!/usr/bin/python3

'''the hbnb console '''

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb) "

    def emptyline(self):
        '''overwriting the emptyline method'''
        return False

    def do_quit(self, arg):
        '''quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''exits the console'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
