#!/usr/bin/python3
import cmd
import sys
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
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
                obj = eval(args)()
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

    def do_all(self, args):
        'show all'
        ls = []
        arg = shlex.split(args)
        if len(arg) == 0:
            for i in models.storage.all().values():
                ls.append(str(i))
            print("[\"" + ", ".join(ls) + "\"]")
        elif arg[0] in models.list_class:
            for key in models.storage.all():
                if arg[0] in key:
                    ls.append(str(models.storage.all()[key]))
            print("[\"" + ", ".join(ls) + "\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        'update'
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in models.list_class:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
