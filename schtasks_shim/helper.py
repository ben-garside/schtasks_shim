from schtasks_shim.handler import run
from schtasks_shim.config import SCHTASK_CMD
import xml.etree.cElementTree as ET
import logging

log = logging.getLogger(__name__)

def lists(action, style="/FO CSV /V"):
    cmd = "{} /{} {}".format(SCHTASK_CMD, action, style)
    output = run(cmd)
    if "CSV" in style:
        output = process_csv(output)
    return output

def action(action, prop, name, style="/XML", processXml=True):
    cmd = '{} {} {} "{}" {}'.format(SCHTASK_CMD, action, prop, name, style)
    output = run(cmd)
    if processXml:
        output = process_xml(output)
    return output

def process_csv(csv):
    tasks = []
    lines = csv.splitlines()
    headers = lines[0][1:-1].split('","')
    del lines[0]
    for line in lines:
        i = 0
        task = {}
        for item in line[1:-1].split('","'):
            task[headers[i]] = item
            i+=1
        tasks.append(task)
    return tasks