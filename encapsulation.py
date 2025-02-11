class archnids:
    def __init__(self,type,feature):

        self.type=type
        self.feature=feature

    def show(self):
        print('type:',self,type,'feature',self.feature)

spider=archnids('spider','eight legs')
print(spider.type)
scopion=archnids('scorpion','claws')