#!/usr/bin/python3
""" Class definition """
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand that inherits from cmd """
    prompt = '(hbnb)'

#    def default(self, line):
#        """Default"""
##       arg = (line.replace('(', '.')).split('.')
#        pattern = r"[(.)]"
#        arg = re.split(pattern, line)
#        print(arg)
#        func = self.aliases
#        command = arg[1]
#        if len(arg) > 3:# and func[arg[1]]:
#            (func[command])(f"{str(arg[0])} {str(arg[2])}")
#        else:
#            print("*** Unknown syntax: %s" % line)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """If a line is empty it does nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id. Usage create \33[31m<class name>\33[30m"""
        if len(arg.split()) == 0:
            print("** class name missing **")
        else:
            try:
                new_instance = storage.classes()[arg.split()[0]]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the \
class name and id. Usage \33[31mshow <class name> <id>\33[0m or \33[31m<class \
name>.show(<id>)\33[0m"""

        if len(arg.split()) == 0:
            print("** class name missing **")
        elif arg.split()[0] not in storage.classes():
             print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            dic = storage.all()
            if f"{arg.split()[0]}.{arg.split()[1]}" in dic:
                print(dic[f"{arg.split()[0]}.{arg.split()[1]}"])
            else:
                print("** no instance found **")

#    def do_count(self, arg):
#        """Retrieve the number of instances of a class"""
#        if len(arg.split()) == 0:
#            print("** class name missing **")
#        elif len(arg.split()) > 0:
#            try:
#                eval(arg.split()[0])
#            except NameError:
#                print("** class doesn't exist **")
#                return
#        if len(arg.split()) < 1:
#            print("** instance id missing **")
#            return
#        else:
#            count = 0
#            d = storage.all()
#            for key in d:
#                if f"{str(arg.split()[0])}" in key:
#                    count += 1
#            print(count)

    def do_all(self, arg):
        """Retrieve the number of instances of a class"""
        if len(arg.split()) < 2:
            dic = []
            for value in storage.all().values():
                dic.append(str(value))
            print(dic)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
