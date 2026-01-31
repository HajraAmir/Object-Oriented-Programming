class Tree:
    def __init__(self):
        self.item=[]
        self.pred=[]
        
    def  addObject(self,key,value,parentkey):
        
        self.item.append(key,value)
        self.pred.append(parentkey)
    def  printTreeAsArrays(self):
        
        print("self.item",self.item)   
        print("self.pred",self.pred)
        
    def searchParentkey(self,childkey): 
        
        index=-1
        for i in range(len(self.pred)):
            if self.item=e
    def printChildren(self,parentkey):
        
        children=[]
        for i in range(len(self.item)):
            
           if self.pred==parentkey:
               children.append(self.item[i][1])
               
        print|("children of",parentkey ,":", children)
               
    def countleaves(self):
               