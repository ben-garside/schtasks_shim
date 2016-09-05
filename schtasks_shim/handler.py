import subprocess
import xml.etree.cElementTree as ET
import os
import logging

logger = logging.getLogger(__name__)

def run(cmd):
    """ run given commands in a subprocess
    """
    try:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        if type(output) == bytes:
            output = output.decode(encoding='UTF-8')
        if "[Error]" in output or proc.returncode != 0:
            logger.warn("{} - {}".format(output, err))
            return {"status": False, "message": "%s\r\n%s" % (output, err)}
        return {"status": True, "message": output}
    except Exception as e:
        logger.error("Exception in run: {}".format(e))
        return {"status": False, "message": "An error occured"}