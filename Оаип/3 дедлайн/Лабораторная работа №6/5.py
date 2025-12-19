class SmartList(list):
    def __getitem__(self,index):
        if index<0:
            index=abs(index)-1
        return super().__getitem__(index)