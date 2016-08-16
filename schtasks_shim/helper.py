from schtasks_shim.handler import run
from schtasks_shim.config import SCHTASK_CMD
import xml.etree.cElementTree as ET
import logging

logger = logging.getLogger()

def lists(action, style="/FO CSV /V"):
    cmd = '{} /{} {}'.format(SCHTASK_CMD, action, style)
    logger.debug("Runnign command: {}".format(cmd))
    output = run(cmd)
    if 'None|' in "{}|".format(output):
        return ""
    if "CSV" in style:
        logger.debug("CSV file provided")
        output = process_csv(output)
    return output


def action(action, name):
    cmd = '{} /{} /TN "{}" '.format(SCHTASK_CMD, action, name)
    output = run(cmd)
    return output


def process_csv(csv):
    logger.debug("Processing the csv...")
    tasks = []
    lines = csv.splitlines()
    headers = lines[0][1:-1].split('","')
    del lines[0]
    logger.debug("{} lines found, start looping".format(len(lines)))
    for line in lines:
        i = 0
        task = {}
        if "HostName" not in line:
            for item in line[1:-1].split('","'):
                task[headers[i]] = item
                i+=1
            tasks.append(task)
    logger.debug("DONE")
    return tasks