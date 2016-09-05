import re

def ask(message=None, required=True, default=None, type=None):
    if message:
        if default:
            required = False
            var = input("{}: (default:{}) ".format(message, default))
            if not var:
                var = default
        else:
            var = input("{}: ".format(message))
            if required:
                if not var:
                    print("This value is required, please try again.")
                    return ask(message=message, required=required, default=default, type=type)
        if type:
            if var:
                valid = do_validation(type, var)
                if not valid:
                    print("This value is not valid, it should be a '{}', please try again.".format(type))
                    return ask(message=message, required=required, default=default, type=type)
                else:
                    if type == "boolean":
                        if var.lower() == "y":
                            var = True
                        else:
                            var = False
    return var


def validate_re(value, reg):
    if re.match(reg, value):
        return True
    return False


def do_validation(type, value):
    valid = {"number"       : r"[0-9]",
             "numbers"      : r"[0-9]*",
             "letters"      : r"[a-Z]*",
             "string"       : r"[0-9a-zA-Z\s]*",
             "letter"       : r"[a-zA-Z]",
             "alphanumeric" : r"[0-9a-zA-Z]",
             "alphanumerics": r"[0-9a-zA-Z]*",
             "boolean"      : r"(y|n|Y|N)",
             "ip"           : r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
             "hostName"     : r"(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])",
             "path"         : r"(.+)\\([^\\]+\..+)",
             "log_mode"     : r".*"
            }
    if type in valid:
        test = validate_re(value, "^{}$".format(valid[type]))
        if test:
            return True
    else:
        print('not a valid validation check >_<')
    return False


def setup():
    HOST = ask(message="enter Hostname", default="localhost", type="hostName")
    PORT = ask(message="enter Port", default="30080", type="numbers")
    SSL = ask(message="would you like to use ssl? (y/n)", required=True, type="boolean")

    SSL_CERT = None
    SSL_KEY = None

    if SSL:
        SSL_CERT = ask("enter certificate absolute path", required=True, type="path")
        SSL_KEY = ask("enter key absolute path", required=True, type="path")
    
    ID = ask("enter service ID", default="sru", type="alphanumerics")
    NAME = ask("enter service NAME", default="SRU", type="alphanumerics")
    DESC = ask("enter service Description", default="SRU Automator", type="string")
    EXE = ask("enter python path", default="python")
    LOGMODE = ask("enter service Logmode", default="rotate", type="log_mode")

    print("")
    print("HOST: {}".format(HOST))
    print("PORT: {}".format(PORT))
    print("SSL: {}".format(SSL))
    if SSL:
        print("SSL_CERT: {}".format(SSL_CERT))
        print("SSL_KEY: {}".format(SSL_KEY))

    print("ID: {}".format(ID))
    print("NAME: {}".format(NAME))
    print("DESC: {}".format(DESC))
    print("EXE: {}".format(EXE))
    print("LOGMODE: {}".format(LOGMODE))

setup()


