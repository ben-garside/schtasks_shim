from .helper import lists, action, edit
import re
import logging


logger = logging.getLogger(__name__)

valid_schedules = ["MINUTE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ONCE", "ONLOGON", "ONIDLE", "ONEVENT"]
valid_options = ["RU","RP","MO","D","M","I","ST","RI","ET","DU","K","SD","ED","EC","IT","NP","Z","V1","F","RL","DELAY",]
valid_option_values = { "I"  : "^[1-9]\d{0,2}$",
                        "D"  : "^(MON|TUE|WED|THU|FRI|SAT|SUN|\*|[1-9]|1[1-9]|2[1-9]|30|31)$",
                        "M"  : "^(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|\*)$",
                        "ST" : "^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$",
                        "RI" : "^([1-9]|[1-8][0-9]|9[0-9]|[1-8][0-9]{2}|9[0-8][0-9]|99[0-9]|[1-8][0-9]{3}|9[0-8][0-9]{2}|99[0-8][0-9]|999[0-9]|[1-8][0-9]{4}|9[0-8][0-9]{3}|99[0-8][0-9]{2}|999[0-8][0-9]|9999[0-9]|[1-4][0-9]{5}|5[0-8][0-9]{4}|59[0-8][0-9]{3}|599[0-8][0-9]{2}|5999[0-3][0-9]|599940)$",
                        "ET" : "^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$",
                        "DU" : "^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$",
                        "SD" : "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$",
                        "ED" : "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$",
                        "RL" : "^(LIMITED|HIGHEST)$"
                    }


def validate_re(value, reg):
    if re.match(reg, value):
        return True
    return False


def validate_task_options(options={}):
    error = False
    for option in options:
        if option not in valid_options:
            logger.debug("{} is an invalid option".format(option))
            error = True
        else:
            if option in valid_option_values:
                logger.debug("Checking {}({}) with regex {}".format(option, options[option], valid_option_values[option]))
                if not validate_re(options[option], valid_option_values[option]):
                    logger.warn("regex match failed for {}, value is not valid".format(option))
                    error = True
    if not error:
        return True
    return False


def create_options_cmd(options):
    out = ""
    for option in options:
        logger.debug("adding '{}' to cmd".format(option))
        out = out + ' /{} "{}"'.format(option, options[option])
    return out



def create_task(taskName=None, taskRun=None, schedule=None, options=None):
    if taskName and isinstance(taskName, str):
        if taskRun and isinstance(taskRun, str):
            if schedule in valid_schedules:
                base_cmd = '/SC "{}" /TN "{}" /TR "{}"'.format(schedule, taskName, taskRun)
                logger.debug("base cmd:{}".format(base_cmd))
                if options:
                    logger.debug("task has options, we need to validate them")                    
                    if validate_task_options(options):
                        logger.debug("All options have valid options")
                        options_cmd = create_options_cmd(options)
                        logger.debug("options cmd:{}".format(options_cmd))
                        cmd = "{} {}".format(base_cmd, options_cmd)                
                    else:
                        logger.warn("Options contain invalid values")
                        return None
                else:
                    cmd = base_cmd
                logger.debug("cmd to run: {}".format(cmd))
                test = edit("create", cmd)
                logger.debug(test)
                if test['status']:
                    logger.debug("OK")
                else:
                    logger.debug("ERROR")
            else:
                logger.warn("schedule not valid")
                return None
        else:
            logger.warn("taskRun not provided or is not a string")
            return None
    else:
        logger.warn("taskname not provided")
        return None


def delete_task(**kw):
    return None


def change_task(**kw):
    return None