#!/usr/bin/python3
import cmd
import sys
import models
import shlex

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
        'Creates an instance of BaseModel'
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

    def emptyline(self):
        'Empty line'
        return ""

    def do_show(self, args):
        'show by id'
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in models.list_class:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist**")

    def do_destroy(self, args):
        'delete by id'
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in models.list_class:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist**")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
