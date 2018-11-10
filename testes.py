import os

class MyTest(object):
    def __init__(self, myArray, filename):
        self.myArray = myArray
        self.filename = filename

    def checkLength(self):
        assert len(self.myArray) == 3, 'Os dados não foram obtidos corretamente!'
        return True

    def isFileCreated(self):
        assert os.path.exists(self.filename) == True, 'O arquivo "'+self.filename+'" não foi criado!'
        return True