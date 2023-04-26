#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import uuid
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """the HBNBCommand class"""

    prompt = "(hbnb)"

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes_dict():
            print("** class doesn't exist **")
            return
        count = 0
        param_key = []
        param_value = []

        for param in args[1:]:
            param = param.split("=")
            count = count + 1
            match = re.search('^"(.*)"$', param[1])
            cast = str
            if match:
                value = match.group(1)
                value = value.replace("_", " ")
            if not match:
                value = param[1]
                if "." in value:
                    cast = float
                else:
                    cast = int
                try:
                    value = cast(value)
                except ValueError:
                    pass
            param_key.append(param[0])
            param_value.append(value)

        # new_instance = HBNBCommand.classes[args[0]]()
        new_instance = storage.classes_dict()[args[0]]()
        i = 0
        while i < count:
            setattr(new_instance, param_key[i], param_value[i])
            i = i + 1

        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""

        if line == "" or line is None:
            print("** class name missing **")
        else:
            class_atr = line.split(" ")
            if class_atr[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            elif len(class_atr) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(class_atr[0], class_atr[1])
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        obj = all_objs[key]
                        print(obj)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            class_atr = line.split(" ")
            if class_atr[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            elif len(class_atr) == 1:
                print("** instance id missing **")
            else:
                key = f"{class_atr[0]}.{class_atr[1]}"
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        obj = all_objs[key]
                        del storage.all()[key]
                        obj.save()
                        return
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""

        list = []
        all_objs = storage.all()

        if line != "" and line is not None:
            arg = line.split(" ")
            if arg[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            else:
                for key in all_objs.keys():
                    if all_objs[key].__class__.__name__ == arg[0]:
                        obj = all_objs[key]
                        list.append(obj.__str__())
        else:
            for key in all_objs.keys():
                obj = all_objs[key]
                list.append(obj.__str__())
        if len(list) > 0:
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line_pattern1 = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|\
                          (?:(\S)+)))?)?)?'
            m = re.search(line_pattern1, line)
            class_name = m.group(1)
            class_id = m.group(2)
            attribute = m.group(3)
            value = m.group(4)

            line_pattern2 = r"^(\S+)\s(\S+)\s(.*)"
            m1 = re.search(line_pattern2, line)
            class_name = m1.group(1)
            class_id = m1.group(2)
            attr_dict = m1.group(3)

            if class_name not in storage.classes_dict():
                print("** class doesn't exist **")
            elif class_id is None:
                print("** instance id missing **")
            else:
                key = f"{class_name}.{class_id}"
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        if m:
                            if attribute is None:
                                print("** attribute name missing **")
                                return
                            elif value is None:
                                print("** value missing **")
                                return
                            else:
                                cast = None
                                if not re.search('^".*"$', value):
                                    if "." in value:
                                        cast = float
                                    else:
                                        cast = int
                                else:
                                    value = value.replace('"', "")
                                if cast:
                                    try:
                                        value = cast(value)
                                    except ValueError:
                                        pass
                                setattr(all_objs[key], attribute, value)
                                all_objs[key].save()
                                return
                        if m1:
                            res = all_objs.update(json.loads(attr_dict))
                            print(res)
                            all_objs[key].save()
                print("** no instance found **")

    def do_count(self, line):
        """Retrieves the number of instances of a class
        Usage: <class name>.count()"""
        objs = storage.all()
        args = line.split(".")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            instances = 0
            for id in objs.keys():
                classs = id.split(".")
                if line == classs[0]:
                    instances += 1
            print(instances)

    def precmd(self, line):
        """precmd command that handles class cmds: <class name>.func()"""
        pattern = r"^(\S+)\.(\S+)\((.*)\)"
        match = re.search(pattern, line)
        if match:
            classname, command, arg = match.groups()
            # arg = arg.replace('"', "")
            if "," in arg:
                arg_pattern1 = r"^(\S+),\s(\S+),\s(\S+)"
                match1 = re.search(arg_pattern1, arg)
                arg_pattern2 = r"^(\S+),\s(.*)"
                match2 = re.search(arg_pattern2, arg)
                if match1:
                    id, attr_name, value = match1.groups()
                    id = id.replace('"', "")
                    attr_name = attr_name.replace('"', "")
                    arg = "{} {} {}".format(id, attr_name, value)
                elif match2:
                    id, attr_dict = match2.groups()
                    id = id.replace('"', "")
                    attr_dict = attr_dict.replace("'", '"')
                    arg = "{} {}".format(id, attr_dict)
            line = "{} {} {}".format(command, classname, arg)
        return cmd.Cmd.precmd(self, line)

    def emptyline(self):
        """empty line is entered in response to the prompt"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Hit ctrl+D (EOF) to exit the program"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
