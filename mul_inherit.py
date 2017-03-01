class Document:
    def __init__(self, content):
        self.content = content
        
    def format(self):
        pass
    
    def display(self):
        pass
    
    
class Monitor:
    def display(self):
        print('{0} on monitor'.format(self.content))
        
    
class Word(Document):
    def format(self):
        self.content = 'i am word, my content is {0}'.format(self.content)
        
        
class Excel(Document):
    def format(self):
        self.content = 'i am excel, my content is {0}'.format(self.content)
        
        
class HP:
    def display(self):
        print('{0} on HP'.format(self.content))
        
        
class WorldWithMonitor(Monitor, Word):
    pass


class ExcelWithMonitor(Monitor, Excel):
    pass
