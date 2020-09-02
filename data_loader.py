import xml.etree.ElementTree as ET
from Entity import Task, Platform, Core

path = 'test_cases/'


def taskLoader(task):
    tree = ET.parse(path + task + '.xml')
    root = tree.getroot()
    app, platform = root.find('Application'), root.find('Platform')
    tasks = []
    MCPs = []
    for task in app.findall("Task"):
        tasks.append(Task(task.attrib['Id'], task.attrib['Deadline'],
                          task.attrib['Period'], task.attrib['WCET']))
    for mcp in platform.findall("MCP"):
        _platform = Platform(mcp.attrib["Id"])
        for core in mcp.findall("Core"):
            _platform.addCore(
                Core(core.attrib["Id"], core.attrib["WCETFactor"]))
        MCPs.append(_platform)

    return tasks, MCPs
