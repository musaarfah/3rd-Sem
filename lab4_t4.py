from lab4 import ListBaseCircularQueue

class Processes:
    def __init__(self,processId,processName,ProcessExtime) :
        self.processId=processId
        self.processName=processName
        self.processExtime=ProcessExtime

class Scheduler:
 def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum
 
 def assignProcessor(self):
     
    circque=ListBaseCircularQueue(self.processArrayLength)   
    for i in range(self.processArrayLength):
         circque.enqueue(self.processArray[i].processExtime)

    circque.display()
    # while not circque.isempty():
    #     i=0
    #     while circque[i]:


if __name__ == "__main__":
    arr = [Processes(1, "notepad", 20), Processes(13, "mp3player", 5), Processes(4, "bcc", 30), Processes(11, "explorer", 2)]
    s = Scheduler(arr, 4, 5)

    s.assignProcessor()

