class sourcedopps:
    def __init__(self, 
                 dataset,
                 period,
                 sources,
                 minstage = 0,
                 maxstage = 9,
                 regions = ['emea', 'americas', 'hls', 'strategic', 'apac'],
                 regionclass = 'RVP',
                 regionabv = 'no',
                 typeoverride = ['Add-on Subscription', 'New Business - New Logo', 'New Business - New Operating Division', 'New Business - New Product'],
                 direction = 'both'):
        '''
            Constructor for this class.
        '''

        self.dataset = dataset
        self.period = period
        self.sources = sources
        self.minstage = minstage
        self.maxstage = maxstage
        self.regions = regions
        self.regionclass = regionclass
        self.regionabv = regionabv
        self.typeoverride = typeoverride
        self.direction = direction

    def bymonth(self, segment):
        '''
            Creates a stacked bar chart that counts the total opportunities sourced by a given segment.
        '''

        #Library imports.
        import pandas as pandas
        import numpy as np
        import datetime as dt
        import matplotlib.pyplot as plt
        from matplotlib import rc

        #Local function definitions.
        def convert_oppsource(source, in_out):
            '''
                Combines a list with opportunity source and inbound/outbound for a final classification. Returns a converted list.
            '''
            #Create empty list to populate.
            oppsource = [None] * len(source)

            #Iterate through inputted lists.
            for x in range(len(oppsource)):
                #List of conditionals. Add correct conditional to list to return.
                if (source[x] == 'AE') and (in_out[x] == 'Inbound'): oppsource[x] = 'AE (Inbound)'
                elif (source[x] == 'AE') and (in_out[x] == 'Outbound'): oppsource[x] = 'AE (Outbound)'
                elif (source[x] == 'N3') and (in_out[x] == 'Inbound'): oppsource[x] = 'N3 (Inbound)'
                elif (source[x] == 'N3') and (in_out[x] == 'Outbound'): oppsource[x] = 'N3 (Outbound)'
                else: 'Not Found'

            #Return now populated list.
            return oppsource
        def convert_salesterritory(region, subregion, classification = 'RVP', abbreviated = 'no'):
            '''
                Takes in a list of regions and subregions and converts them into Sales Territory as defined
                by the most up-to-date Sales Organization territories. Returns a list of convertedvalues.
            '''
            #Define region sets by how they should be aggregated to make the following iteration more efficient.
            regions_to_not_change = ['APAC', 'North America Commercial', 'Strategic Accounts', 'HLS'] #Regions that equal territory.
            emea_conditionals = ['Southern Europe', 'North EMEA'] #May or may not be grouped depending on passed classification.
            dach = ['DACH', 'DACH & Nordics'] #Variations of DACH to be merged together.
            na_enterprise_sub_regions = ['West', 'South', 'East', 'Central'] #Sub-regions that determine the NA Enterprise territories.
            
            #Fill NA values
            region.fillna('No Region', inplace = True)
            subregion.fillna('NoRegion', inplace = True)
            
            #Define an empty list that will hold the new territory values.
            territory = [None] * len(region)
            
            #Group into sales territory according to the above definitions.
            for x in range(len(region)):
                if region[x] in regions_to_not_change: territory[x] = region[x]
                elif region[x] in emea_conditionals:
                    if classification == 'RVP': territory[x] = 'EMEA'
                    elif classification == 'Region': territory[x] = region[x]
                elif region[x] in dach: territory[x] = 'DACH & Nordics'
                elif region[x] == 'North America Enterprise': 
                    if abbreviated == 'no':
                        if subregion[x] in na_enterprise_sub_regions: territory[x] = region[x] + ' ' + subregion[x]
                        else: territory[x] = 'No Region'
                    elif abbreviated == 'yes':
                        if subregion[x] in na_enterprise_sub_regions: territory[x] = 'NA Enterprise' + ' ' + subregion[x]
                        else: territory[x] = 'No Region'
                else: territory[x] = 'No Region'
            
            #Return the new territory list.
            return territory
        def get_monthname(dates):
            '''
                Pull out the month number from a date string in the formt yyyy-mm-dd and return the month's name.
            '''
            #Create a dictionary with the month names.
            monthnames = {1 : 'January', 
                        2 : 'February', 
                        3 : 'March', 
                        4 : 'April', 
                        5 : 'May', 
                        6 : 'June', 
                        7 : 'July', 
                        8 : 'August', 
                        9 : 'September', 
                        10 : 'October', 
                        11 : 'November', 
                        12 : 'December'}

            #Create an empty list to populate.
            months = [None] * len(dates)

            #Populate months list using the month names dictionary as the converter.
            for x in range(len(dates)):
                months[x] = monthnames[int(dates[x][5:7])]
            
            #Return the populated list.
            return months
        def convert_fiscalperiod(datecol):
            ''' 
                Takes in a list of date strings in the format yyyy-mm-dd and returns a list of the fiscal quarters that those dates are in.
            '''
            #Define which months belong to which quarter. This format is for accessibility in the iteration.
            q1 = ['02', '03', '04']
            q2 = ['05', '06', '07']
            q3 = ['08', '09', '10']
            q4 = ['11', '12', '01']

            #Create a new list to hold the fiscal period values.
            fiscalperiod = [None] * len(datecol)

            for x in range(len(datecol)):
                #Create a blank string to temporarily house the concatenated fiscal period.
                period = ''

                #Calculates the fiscal year by using the month.
                #Fiscal year is the calendar year if the month is January, but it is the calendar year plus one in all other cases.
                if datecol[x][5:7] == '01': 
                    period = 'FY' + datecol[x][2:4]
                else: period = 'FY' + str(int(datecol[x][:4]) + 1)[2:4]
                
                #Classify the date into a fiscal quarter depending on the month.
                if datecol[x][5:7] in q1: 
                    period = period + '-Q1'
                elif datecol[x][5:7] in q2:
                    period = period + '-Q2'
                elif datecol[x][5:7] in q3:
                    period = period + '-Q3'
                elif datecol[x][5:7] in q4:
                    period = period + '-Q4'
                
                #Place the new fiscal period definition in the associated index in the new fiscal period list.
                fiscalperiod[x] = period
            
            #Return the new list of fiscal periods
            return fiscalperiod
        def fiscalperiods_inyear_ofdate(date):
            '''
                Takes in a date and determines all the fical periods in the year of that date. 
                Fiscal periods are in the format FY__-Q_. Returns a list.
            '''
            #Use the month of the date to determine if fiscal year is the year of the date, or the year of the date + 1.
            if int(date[5:7]) == 1:
                q1 = 'FY' + date[2:4] + '-Q1'
                q2 = 'FY' + date[2:4] + '-Q2'
                q3 = 'FY' + date[2:4] + '-Q3'
                q4 = 'FY' + date[2:4] + '-Q4'
            else:
                q1 = 'FY' + str(int(date[2:4]) + 1) + '-Q1'
                q2 = 'FY' + str(int(date[2:4]) + 1) + '-Q2'
                q3 = 'FY' + str(int(date[2:4]) + 1) + '-Q3'
                q4 = 'FY' + str(int(date[2:4]) + 1) + '-Q4'

            #Return a list with the fiscal quarters.
            return [q1, q2, q3, q4]
        def convert_fiscalperiod_single(date):
            '''
                Takes in a single date string in the format yyyy-mm-dd and returns the fiscal quarter as a string.
            '''
            #Define which months belong to which quarter. This format is for accessibility in the itation.
            q1 = ['02', '03', '04']
            q2 = ['05', '06', '07']
            q3 = ['08', '09', '10']
            q4 = ['11', '12', '01']

            #Create a blank string to temporarily house the concatenated fiscal period.
            period = ''

            #Calculates the fiscal year by using the month.
            #Fiscal year is the calendar year if the month is January, but it is the calendar year plus one in all other cases.
            if date[5:7] == '01': 
                period = 'FY' + date[2:4]
            else: period = 'FY' + str(int(date[:4]) + 1)[2:4]
            
            #Classify the date into a fiscal quarter depending on the month.
            if date[5:7] in q1: 
                period = period + '-Q1'
            elif date[5:7] in q2:
                period = period + '-Q2'
            elif date[5:7] in q3:
                period = period + '-Q3'
            elif date[5:7] in q4:
                period = period + '-Q4'
            
            #Return the new list of fiscal periods
            return period

        #Define dataframe.
        df = pandas.DataFrame({'Name' : self.dataset['NAME'],
                               'Type' : self.dataset['TYPE'],
                               'Stage' : self.dataset['STAGENAME'],
                               'Region' : self.dataset['REGION__C'],
                               'Sub Region' : self.dataset['SUB_REGION__C'],
                               'Loss Reason' : self.dataset['LOSS_REASON__C'],
                               'Created Date' : self.dataset['CREATEDDATE'],
                               'Source' : self.dataset['OPPORTUNITY_SOURCE__C'],
                               'Inbound/Outbound' : self.dataset['INBOUND_OUTBOUND_OPPORTUNITY__C']})

        #Convert the current date into a string of the format yyyy-mm-dd for later date operations.
        currentdate = str(dt.date.today().year) + '-' #Year as is converted to string from datetime.
        if dt.date.today().month in [10, 11, 12]: currentdate = currentdate + str(dt.date.today().month) + '-' #Month if double digits.
        else: currentdate = currentdate + '0' + str(dt.date.today().month) + '-' #Month if single digits.
        if dt.date.today().day in [1, 2, 3, 4, 5, 6, 7, 8, 9]: currentdate = currentdate + '0' + str(dt.date.today().day) #Day if single digits.
        else: currentdate = currentdate + str(dt.date.today().day)#Month if double digits.

        #Dataframe calculations.
        df['Source'] = convert_oppsource(df['Source'], df['Inbound/Outbound']) #Include inbound/outbound in opportunity source.
        df['Sales Territory'] = convert_salesterritory(df['Region'], df['Sub Region'], self.regionclass, self.regionabv) #Convert regions to sales territories.
        df['Created Date'] = df['Created Date'].dt.strftime('%Y-%m-%d') #Convert start date from timestamp to string format.
        df['Month'] = get_monthname(df['Created Date']) #Get month names for the created dates.
        df['Fiscal Period Created'] = convert_fiscalperiod(df['Created Date']) #Get fiscal period notation for created date.

        #Caulculate full list of sources used.
        sourcesfull = []
        for x in range(len(self.sources)):
            if self.direction == 'both':
                sourcesfull.append(self.sources[x] + ' (Inbound)')
                sourcesfull.append(self.sources[x] + ' (Outbound)')
            elif self.direction == 'in':
                sourcesfull.append(self.sources[x] + ' (Inbound)')
            elif self.direction == 'out':
                sourcesfull.append(self.sources[x] + ' (Outbound)')

        #Calculate full list of stages used.
        allstages = {0 : '0 - Cultivate',
                    1 : '1 - Set Vision',
                    2 : '2 - Discovery',
                    3 : '3 - Value Proposition', 
                    4 : '4 - Validate/Prove',
                    5 : '5 - Vendor of Choice/Propose',
                    6 : '6 - Negotiate',
                    7 : '7 - Pending Closed Won',
                    8 : '8 - Closed Won',
                    9 : '9 - Closed Lost'}
        stages = []
        for x in range(self.minstage, self.maxstage + 1):
            stages.append(allstages[x])

        #Calculate full list of months used.
        allmonths = {1 : 'February',
                    2 : 'March',
                    3 : 'April',
                    4 : 'May',
                    5 : 'June',
                    6 : 'July', 
                    7 : 'August',
                    8 : 'September',
                    9 : 'October',
                    10 : 'November',
                    11 : 'December',
                    12 : 'January'}
        months = []
        for x in range(1, 12 + 1):
            months.append(allmonths[x])

        #Calculate full list of territories.
        territories = []
        if 'emea' in self.regions: #Add EMEA regions based on conditionals.
            if self.regionclass == 'RVP': emeaterritories = ['DACH & Nordics', 'North EMEA', 'Southern Europe']
            elif self.regionclass == 'Region' : emeaterritories = ['DACH & Nordics', 'EMEA']
            for x in range(len(emeaterritories)):
                territories.append(emeaterritories[x])
        if 'americas' in self.regions: #Add America regions based on conditionals.
            if  self.regionabv == 'no': americaterritories = ['North America Commercial',
                                                        'North America Enterprise Central',
                                                        'North America Enterprise South',
                                                        'North America Enterprise West',
                                                        'North America Enterprise East']
            elif self.regionabv == 'yes' : americaterritories = ['North America Commercial',
                                                            'NA Enterprise Central',
                                                            'NA Enterprise South',
                                                            'NA Enterprise West',
                                                            'NA Enterprise East']
            for x in range(len(americaterritories)):
                territories.append(americaterritories[x])
        if 'hls' in self.regions: territories.append('HLS') #Add HLS.
        if 'strategic' in self.regions: territories.append('Strategic Accounts') #Add strategic accounts.
        if 'apac' in self.regions: territories.append('APAC') #Add APAC.

        #Filter dataframe downb ased on type, loss reason, source, territory, and created date.
        if self.period == 'YTD':
            df = df[(df['Type'].isin(self.typeoverride)) &
                    (df['Loss Reason'] != 'Duplicate') &
                    (df['Source'].isin(sourcesfull)) &
                    (df['Sales Territory'].isin(territories)) &
                    (df['Stage'].isin(stages)) &
                    (df['Fiscal Period Created'].isin(fiscalperiods_inyear_ofdate(currentdate)))].reset_index()
        elif self.period == 'QTD':
            df = df[(df['Type'].isin(self.typeoverride)) &
                    (df['Loss Reason'] != 'Duplicate') &
                    (df['Source'].isin(sourcesfull)) &
                    (df['Sales Territory'].isin(territories)) &
                    (df['Stage'].isin(stages)) &
                    (df['Fiscal Period Created'] == convert_fiscalperiod_single(currentdate))].reset_index()
        
        #Map secondary segment input.
        segmentlist = {'stage' : stages,
                       'territory' : territories,
                       'source' : sourcesfull,
                       'type' : self.typeoverride}
        segmentmap = {'stage' : 'Stage',
                      'territory' : 'Sales Territory',
                      'source' : 'Source',
                      'type' : 'Type'}

        #Store counts by segment.
        barvalues = {}
        for x in range(len(segmentlist[segment])):
            for y in range(len(months)):
                barvalues[str(x + 1) + '_' + months[y]] = df[(df['Month'] == months[y]) &
                                                             (df[segmentmap[segment]] == segmentlist[segment][x])]['Name'].nunique()
        
        #Write data to chart series, based on month.
        datalists = []
        for x in range(len(segmentlist[segment])):
            datalists.append([])
            for y in range(len(months)):
                datalists[x].append(barvalues[str(x + 1) + '_' + months[y]])

        #Check for bars of all 0's
        indexestoremove = []
        for x in range(len(months)):
            counter = 0
            for l in datalists:
                counter = counter + l[x]
            if counter == 0: indexestoremove.append(x)

        #Position of the bars on the x-axis.
        r = []
        for x in range(len(datalists[0]) - len(indexestoremove)):
            r.append(x)

        #Names of the group and bar width.
        monthnames = ['Feb',
                      'Mar',
                      'Apr',
                      'May',
                      'Jun',
                      'Jul',
                      'Aug',
                      'Sep',
                      'Oct',
                      'Nov',
                      'Dec',
                      'Jan']
        names = []
        for x in range(len(datalists[0])):
            if x not in indexestoremove: names.append(monthnames[x])

        #Remove all bars of 0's.
        for l in datalists:
            for index in sorted(indexestoremove, reverse = True):
                del l[index]

        #Add bars together to get cumulative height.
        heights = [datalists[0]]
        heightsindex = 0
        for x in range(len(datalists) - 2):
            heights.append(np.add(heights[heightsindex], datalists[x + 1]))
            heightsindex += 1

        #Create the bars for the graph.
        plt.bar(r, datalists[0]) 
        for x in range(len(heights)):
            plt.bar(r, datalists[x + 1], bottom = heights[x])

        #Add a legend.
        ax = plt.subplot(111)
        if self.period == 'YTD': ncol = 3
        elif self.period == 'QTD': ncol = 2
        for a in range(len(segmentlist[segment])):
            if a == 0: ax.plot(x, y, label = segmentlist[segment][a])
            else: ax.plot(x, y+(a+1), label = segmentlist[segment][a])
        ax.legend(loc = 'upper center', bbox_to_anchor = (0.5, -0.05), ncol = ncol)

        #Add a title.
        sourcesused = []
        for x in range(len(self.sources)):
            if self.sources[x] not in sourcesused: sourcesused.append(self.sources[x])
        if len(sourcesused) > 1:
            title = sourcesused[0]
            for x in range(1, len(sourcesused)):
                title = title + ', ' + sourcesused[x]
        else: title = sourcesused[0]
        plt.title(title + ' Sourced ' + self.period + ' by Month - ' + segmentmap[segment], fontsize = 12, fontweight = 'bold')
        
        #Customize x-axis
        plt.xticks(r, names, fontsize = 8)
        plt.xlabel('Month Created', fontsize = 8)

        #Customize y-axis
        plt.ylabel('Number of Opportunities', fontsize = 8)

        #Show chart.
        plt.show
