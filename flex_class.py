

class FlexClass:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            attr_name = "_"+k
            self.__setattr__(attr_name, v)

    def __str__(self):
        return_str = ""
        for k,v in self.__dict__.items():
            return_str += f"{k}: {v}\n"
        return return_str


if __name__ == "__main__":
    import logging

    logger = logging.getLogger("myapp")
    logger.error("something wrong")

    my_flex = FlexClass(p1=123, p2="abc")
    print(my_flex)
