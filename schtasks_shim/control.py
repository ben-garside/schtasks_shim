from schtasks_shim.helper import lists, action
import logging

logger = logging.getLogger(__name__)


def run_by_name(name):
    result = action("run", name)
    logger.debug("Result: {}".format(result))
    if "SUCCESS:" in result:
        return {"message": result}
    return None


def end_by_name(name):
    result = action("end", name)
    logger.debug("Result: {}".format(result))
    if "SUCCESS:" in result:
        return {"message": result}
    return None