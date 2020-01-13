"""Tools to manipulate Pandas DataFrames for Data Science tasks.
"""
import os
import pandas as pd

def setRowsToDisplayPandas(rows: int):
    """Set the number of rows Pandas will display when showing a DataFrame.

    Arguments:
        rows {int} -- Number of rows.
    """
    pd.options.display.max_rows = rows

def getIdxmaxIntegerPosOfSeries(series: pd.Series) -> int:
    """Get the index of the largest entry in a Pandas series as an integer.

    Arguments:
        series {pd.Series} -- Series

    Returns:
        int -- Integer index of maximum value
    """
    currentIndex = 0
    maxIndex = 0
    maxValue = 0
    for value in series:
        if value > maxValue:
            maxValue = value
            maxIndex = currentIndex
        currentIndex += 1
    return maxIndex

def readCsvFiles(csvFiles: list) -> list:
    csvDataFrames = []
    for filename in csvFiles:
        dataFrame = pd.read_csv(filename, sep=';')
        csvDataFrames.append(dataFrame)
    return csvDataFrames

def stackCsvFiles(csvFiles: list, writeTofile=False) -> pd.DataFrame:
    csvDataFrames = readCsvFiles(csvFiles)
    stackedDataFrame = pd.concat(csvDataFrames, axis=0, ignore_index=True)
    stackedDataFrame.drop(stackedDataFrame.columns[0], axis=1, inplace=True)
    if writeTofile:
        stackedDataFrame.to_csv('stacked-dataframe.csv', sep=';', index=False)

    return stackedDataFrame
    