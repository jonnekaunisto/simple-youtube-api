import re


def c_to_u(name):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def u_to_c(name):
    name = "".join(x.capitalize() or "_" for x in name.split("_"))
    name = name[0].lower() + name[1:]
    return name
