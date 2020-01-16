...
from pytrends.request import TrendReq
import pandas as pd
import string

"""upgradedTrends.py: Unofficial Python API for accessing Google Trends"""

__author__ = "Asher Noel"
__license__ = "MIT"
__maintainer__ = "Asher Noel"
__email__ = "asher13a@gmail.com"

# ------------------------------------------------------------------------------- #


class pytrendsUpgrade:

    @staticmethod
    def get_interest_over_time(keywords, region, timeframe, flagTopic):
        """Constructs a new trends over time instance
                Args:
                    keywords: The input terms, e.g. ["Harvard University", "Yale University"]
                        NOTE:
                            1) keywords cannot contain duplicates
                            2) All terms are scaled by the 1st (0th index) term.
                    region: The chart region. By default, the region is the world.
                        EXAMPLES:
                            "" for world, "US" for US
                    timeframe: A string in "YYYY-MM-DD YYYY-MM-DD" or "START END" format

                    topic_flag: If FLAG = FALSE, keywords will be "Search Terms" in Google Trends
                                If FLAG = TRUE, keywords will be the first "Topic" that come up when typing in a keyword on Trends.

                """

        pytrends = TrendReq(hl='en-US', tz=360)

        # Initialize flag and temporary list of queries with the keyword that should be in all of them.
        old = 0
        tempList = [pytrends.suggestions(keywords[0])[0]['mid']] if flagTopic else [keywords[0]]

        # Initialize the Dataframes
        trendData = pd.DataFrame()
        oldData = pd.DataFrame()

        for index in range(1, len(keywords)):

            # Add the next keyword in the list to the temporary list of queries
            keyword = keywords[index]

            # If the keyword does not have enough traffic, it will not be a topic; in these cases, add it as a search term.
            try:
                tempList.append(pytrends.suggestions(keyword)[0]['mid']) if flagTopic else tempList.append(keyword)
            except IndexError:
                tempList.append(keyword)

            # The maximum query request is five terms
            if index // 4 != old or (index == len(keywords) - 1):

                # Build the payload
                pytrends.build_payload(tempList, cat=0, timeframe=timeframe, geo=region, gprop='')

                newData = pytrends.interest_over_time()

                # Adjust the data so that the first column, the master column, has a maximum of 100
                maxMaster = newData[pytrends.suggestions(keywords[0])[0]['mid']].max() if flagTopic else newData[
                    keywords[0]].max()

                newData.iloc[:, :-1] *= 100 / (maxMaster)

                # Merge the old and new DataFrames
                if old == 0:
                    oldData = newData.iloc[:, :-1]
                    trendData = oldData
                else:
                    try:
                        trendData = oldData.join(newData.iloc[:, 1:-1])
                    except ValueError:
                        trendData = oldData.join(newData.iloc[:, 1:-1], lsuffix='_left', rsuffix='_right')
                    oldData = trendData

                # Reset the temporary queries and increase the flag.
                tempList = [pytrends.suggestions(keywords[0])[0]['mid']] if flagTopic else [keywords[0]]
                old += 1

        # Update the columns of the trend data with the original names
        trendData.columns = keywords

        # Reorder the columns based off of their mean values.
        return trendData.reindex(trendData.mean().sort_values(ascending=False).index, axis=1)

    @staticmethod
    def get_viral_keywords(keyword, region, timeframe, interval, cutoff):
        """Finds viral keywords related to ONE keyword
                Args:
                    keyword: The ONE input term
                    region: The chart region. By default, the region is the world.
                        EXAMPLES:
                            "" for world, "US" for US
                    timeframe: A string in "YYYY-MM-DD YYYY-MM-DD" or "START END" format
                    interval: The interval of time between virality checks.
                        EXAMPLES:
                            7, 10
                    cutoff: This integer is the minimum % increase in searches over the INTERVAL to be caught by
                            the algorithm (e.g., 100% = 100)
                        EXAMPLES:
                            100, 1000
                """

        pytrends = TrendReq(hl='en-US', tz=360)

        keywords = [keyword]

        # Track the type of related topic
        keyword_types = []

        # Track the number of rising topics per time interval over time.
        virality = []

        def get_rising_related_topics(keyword, region, timeframe, cutoff):
            # Inputs:
            # keyword is a string format
            # region: "" for world, "US" for US
            # timeframe: YYYY-MM-DD YYYY-MM-DD format
            # cutoff: INT the % minimum % increase in searches over the period to be interesting (e.g., 100% = 100)

            pytrends.build_payload([pytrends.suggestions(keyword)[0]['mid']], cat=0, timeframe=timeframe, geo=region,
                                   gprop='')
            topics = pytrends.related_topics()

            # Only return the topics above the cutoff
            return topics[pytrends.suggestions(keyword)[0]['mid']]['rising'].loc[
                topics[pytrends.suggestions(keyword)[0]['mid']]['rising']['value'] >= cutoff]

        def getTimeframes(start, end, interval):
            # Start and end are in YYYY-MM-DD format.
            # interval is an integer in days.
            # return a list of all of the intervals in [YYYY-MM-DD YYYY-MM-DD] between a start and end date

            intervals = []

            startYear = int(start[:4]);
            startMonth = int(start[5:7]);
            startDay = int(start[8:])

            def decimalTime(time):
                # input in YYYY-MM-DD format
                # output in YYYY.XX format.
                return int(time[:4]) + int(time[5:7]) / 12 + int(time[8:]) / 365

            while decimalTime(start) < decimalTime(end):
                tempDay = startDay + interval;
                tempYear = startYear;
                tempMonth = startMonth

                # Adjust the day and month
                if tempDay > 30 and startMonth != 2:
                    tempDay = tempDay % 30
                    tempMonth += 1
                elif tempDay > 28 and startMonth == 2:
                    tempDay = tempDay % 28
                    tempMonth += 1

                # Adjust the month and year
                if tempMonth > 12:
                    tempYear += 1
                    tempMonth = tempMonth % 12

                def toDatetime(year, month, day):
                    # input as integers, output as YYYY-MM-DD
                    MM = "0" + str(month) if month < 10 else str(month)
                    return str(year) + "-" + str(MM) + "-" + str(day)

                # add the new interval to intervals
                start = toDatetime(tempYear, tempMonth, tempDay)

                intervals.append(toDatetime(startYear, startMonth, startDay) + " " + start)

                startDay = tempDay;
                startMonth = tempMonth;
                startYear = tempYear

            return intervals


        # Add all of the related topics over that timeframe to the keywords list
        times = getTimeframes(timeframe[:10], timeframe[11:], interval)
        for time in times:
            topics = get_rising_related_topics(keyword, region, time, cutoff)
            keyword_types.extend(topics['topic_type'].tolist())
            keywords.extend(topics['topic_title'].tolist())
            virality.append(len(topics['topic_title'].tolist()))

        # Remove duplicates and punctuation from keywords:
        adjKeywords = []
        [adjKeywords.append(word.translate(str.maketrans('', '', string.punctuation))) for word in keywords if (word.translate(str.maketrans('', '', string.punctuation)) not in adjKeywords) and len(word) > 2]

        # Remove single words that are too common in english like Mother or July
        adj2Keywords = []
        [adj2Keywords.append(word) for word in adjKeywords if not (" " not in word and zipf_frequency(word, 'en') > 5.1)]

        # Remove words with the same topics.
        topics = []
        adj3Keywords = []

        for word in adj2Keywords:
            try:
                if pytrends.suggestions(word)[0]['mid'] not in topics:
                    adj3Keywords.append(word)
                    topics.append(pytrends.suggestions(word)[0]['mid'])
            except IndexError:
                continue

        return adj3Keywords

# ------------------------------------------------------------------------------- #

get_interest_over_time = pytrendsUpgrade.get_interest_over_time
get_viral_keywords = pytrendsUpgrade.get_viral_keywords








