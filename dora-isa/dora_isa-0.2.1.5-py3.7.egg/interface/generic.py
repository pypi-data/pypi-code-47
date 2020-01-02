import os

class Generic:
    def __init__(self,*args,**kargs):
        pass

    def get_user(self):
        return dict(user = os.environ.get('DORA_USER'))

    def show(self, dataframe):
        dataframe.show()

    def command_aux(self, ISAContext):
        pass

    def command_ml(self, MLContext):
        pass