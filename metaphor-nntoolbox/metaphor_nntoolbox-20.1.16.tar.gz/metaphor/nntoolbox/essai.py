if __name__ == "__main__":
    import pandas as pd

    sheetname = "test_1"
    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
    
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('/Users/jeanluc/Desktop/pandas_simple.xlsx', engine='xlsxwriter')
    
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=sheetname)
    worksheet = writer.sheets[sheetname]
    worksheet.set_zoom(150)
    workbook = writer.book
    
    # Apply a conditional format to the cell range.
    worksheet.conditional_format('B2:B8', {'type': '3_color_scale'})

    
    # Create a chart object.
    chart = workbook.add_chart({'type': 'column'})
    
    # Configure the series of the chart from the dataframe data.
    chart.add_series({'values': '=test_1!$B$2:$B$8'})
    
    # Insert the chart into the worksheet.
    worksheet.insert_chart('D2', chart)
# Close the Pandas Excel writer and output the Excel file.
    writer.save()
