from schtasks_shim.helper import lists, action
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all sites
    """
    sites = lists("Query")
    return sites

def get_by_name(name, partial=False):
    """ return all sites
    """
    sites = lists("Query /TN {}".format(name))
    return sites