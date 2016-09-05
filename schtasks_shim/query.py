from schtasks_shim.helper import lists
import logging

logger = logging.getLogger(__name__)

def get_all():
    """ return all tasks
    """
    tasks = lists("Query")
    return tasks


def get_by_name(name, partial=False):
    """ return task by name, if partial is true
        a list of tasks is returned otherwise a single task
    """
    if not partial:
        tasks = lists('Query /TN "{}"'.format(name))
        logger.debug(tasks)
        if len(tasks):
            return tasks[0]
        else:
            return None
    else:
        match_tasks = []
        tasks = lists("Query")
        match_tasks = [task for task in tasks if task['TaskName'].lower().find(name.lower()) > -1]
        return match_tasks


def get_by_status(status):
    """ return task by status, a list of tasks is returned
    """
    match_tasks = []
    tasks = lists("Query")
    match_tasks = [task for task in tasks if task['Status'].lower().find(status.lower()) > -1]
    return match_tasks