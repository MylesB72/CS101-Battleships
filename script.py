import string 

class Board:
    def __init__(self,rows = 10,columns = 10):
        self.rows = rows
        rowList = []
        self.columns = columns 
        self.columnDict = {}
        alphabetListUpper = list(string.ascii_uppercase)
        for column in range(self.columns):
            self.columnDict[alphabetListUpper[column]] = ""
        for row in range(0,rows,1):
            rowList.append(row)
        for key in self.columnDict.keys():
            self.columnDict[key] = rowList
            

    #display a blank board
    def __repr__(self):
        topRow = ""
        for column in self.columnDict.keys():
            topRow += "|"
            topRow += str(column)
        topRow += "|"
        for value in self.columnDict:
            for key in self.columnDict:
                print(value)
            
        return topRow

        
board1 = Board()
print(board1)