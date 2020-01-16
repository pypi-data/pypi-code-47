from IPython.core.display import display, HTML
from ..isa import ISAMagic
from ..ml import MLMagic
from .generic import Generic


class Jupyter(Generic):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def show(self, dataframe, limit=100):
        display(HTML(dataframe.limit(limit).toPandas().to_html()))

    def command_aux(self, ISAContext):
        ISAMagic(ISAContext)

    def command_ml(self, MLContext):
        MLMagic(MLContext)