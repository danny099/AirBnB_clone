#!/usr/bin/python3
import cmd
import sys
import models

"""console"""


class HBNBCommand(cmd.Cmd):
    """console"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        'exit'
        return True

    def do_quit(self, line):
        'exit whit command quit'
        return True

    def do_create(self, args):
        """Creates an instance of BaseModel"""
        if args:
            if args in models.list_class:
                obj = models.base_model.BaseModel()
                print(obj.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
