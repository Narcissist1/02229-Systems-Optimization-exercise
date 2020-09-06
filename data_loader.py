import xml.etree.ElementTree as ET
from Entity import Task, Core

path = 'test_cases/'


class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self, name):
        '''
        Load input data from an xml file
        Input: filename
        Output: A list of Task objects and Core objects
        '''
        tree = ET.parse(self.path + name + '.xml')
        root = tree.getroot()
        app, platform = root.find('Application'), root.find('Platform')
        tasks = []
        cores = []
        prioritySet = set()
        for task in app.findall("Task"):
            t = Task(task.attrib['Id'], task.attrib['Deadline'],
                     task.attrib['Period'], task.attrib['WCET'])
            _priority = 1.0 / float(task.attrib['Deadline'])
            while _priority in prioritySet:
                _priority = _priority + _priority / 10

            t.setPriority(_priority)
            prioritySet.add(_priority)
            tasks.append(t)

        for mcp in platform.findall("MCP"):
            for core in mcp.findall("Core"):
                cores.append(
                    Core(core.attrib["Id"], mcp.attrib["Id"], core.attrib["WCETFactor"]))

        return tasks, cores

    def dump(self, name, tasks):
        '''
        Dump a solution to an xml file
        Input: Filename to write in and a list of SolutionTask
        Output: None
        '''
        solution = ET.Element('solution')
        for task in tasks:
            taskElement = ET.SubElement(solution, 'Task')
            taskElement.set('Id', str(task.id))
            taskElement.set('MCP', str(task.MCP))
            taskElement.set('Core', str(task.core))
            taskElement.set('WCRT', str(task.WCRT))

        tree = ET.ElementTree(solution)
        tree.write(self.path + name + '.xml')
