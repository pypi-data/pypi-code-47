import pickle
import calendar

with open('../.credentials/youtubeAnalytics.pkl', 'rb') as file:
	analytics_service = pickle.load(file)

def endMonth(year, month):
	endDay = calendar.monthrange(year, month)[1]
	return endDay