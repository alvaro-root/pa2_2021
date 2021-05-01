import abc
import random
import string


class MyAbstractBase(metaclass=abc.ABCMeta):
    how_many_objects = 0

    def __init__(self, *args, **kwargs):
        self._num_args = len(args)
        self._kwarg_keys = []
        self._args_string = ""
        self._kwargs_string = ""
        for i in range(len(args)):
            setattr(self, f"_arg{i}", args[i])
            self._args_string += f"{args[i]}, "
        for k, v in kwargs.items():
            setattr(self, f"_{k}", v)
            self._kwarg_keys.append(k)
            self._kwargs_string += f"{k}={v}, "

        self.__class__.how_many_objects += 1

    def __str__(self):
        self_string = f"Class: {self.__class__.__name__}\nArgs: {self._args_string}\nKwargs: {self._kwargs_string}"
        return self_string

    def __repr__(self):
        self_string = f"{self.__class__.__name__}({self._args_string}{self._kwargs_string})"
        return self_string

    def show_arguments(self):
        args_string = "Args:\n"
        for i in range(self._num_args):
            this_attr = getattr(self, f"_arg{i}")
            args_string += f"{this_attr}\n"
        args_string += "Kwargs:\n"
        for k in self._kwarg_keys:
            this_attr = getattr(self, f"_{k}")
            args_string += f"_{k}={this_attr}\n"

        return args_string


class MyConcreteClass(MyAbstractBase):
    pass


if __name__ == '__main__':
    class_names = ("This", "That", "Other")

    for item in class_names:
        globals()[item] = MyConcreteClass

        globals()[f"{item.lower()}_object"] = globals()[item](
            string.ascii_lowercase[random.randint(1, 25)],
            string.ascii_lowercase[random.randint(1, 25)],
            random_number=random.randint(100, 199)
        )

        print("-"*80)
        print(item)
        print(globals()[item])
        print(globals()[f"{item.lower()}_object"])
        print(globals()[f"{item.lower()}_object"].show_arguments())
        repr_string = globals()[f"{item.lower()}_object"].__repr__()
        print(f"{item.lower()} = {repr_string}")
        print(globals()[f"{item.lower()}_object"].__repr__())
        print(globals()[f"{item.lower()}_object"].__dict__)
        print("-" * 80)

    print(f"{MyConcreteClass.how_many_objects} instances were created")
    print("-" * 80)
