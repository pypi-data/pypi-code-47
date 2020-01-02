__version__ = '0.0.8'
"""Extensions to the 'distutils' for large or complex distributions"""
NAME = "AIserver"
from AIserver.chartAI import run
__metaclass__ = type
__all__ = [
    'chartAI'
]


def AI_chart():
    try:
        run(APIkey="ds34dfj58dfh4h3")
    except:
        print("AI开小差了呢")
