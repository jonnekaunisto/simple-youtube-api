'''Convert from YouTube name to simple-youtube-api name and vice versa'''
import re


def c_to_u(name):
    ''' Converts from camel case '''
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def u_to_c(name):
    ''' Converts to camelcase '''
    name = "".join(x.capitalize() or "_" for x in name.split("_"))
    name = name[0].lower() + name[1:]
    return name
