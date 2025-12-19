class DatabaseConfig:
    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self,db_name,user,password):
        if not hasattr(self,'initialized'):
            self.db_name=db_name
            self.user=user
            self.password=password
            self.initialized=True