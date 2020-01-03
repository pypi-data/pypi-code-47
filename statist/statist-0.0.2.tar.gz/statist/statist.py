import todoist
from .graph import daily, weekly
import datetime
import sys
import colorama
colorama.init()

def statist():
    try:
        if len(sys.argv) == 2 and len(sys.argv[1]) == 40:
            api = todoist.TodoistAPI(sys.argv[1])
            stat = api.completed.get_stats()
            
            print(colorama.Fore.GREEN + 'Karma: ' + str(int(stat['karma'])))
            print(colorama.Fore.MAGENTA + 'Total Task Completed: ' + str(int(stat['completed_count'])))
            print(colorama.Style.RESET_ALL, end="")
            print('\n············································\n')
            
            # Daily
            
            total_completed = []
            daily_date = []
            for i in stat['days_items']:
                total_completed.append(i['total_completed'])
                daily_date.append(datetime.datetime.strptime(i['date'], '%Y-%m-%d').strftime('%A'))
            
            goal = stat['goals']['daily_goal']
            print(colorama.Fore.GREEN + 'Daily - ' + datetime.datetime.strptime(stat['days_items'][0]['date'], '%Y-%m-%d').strftime('%d %b %Y'))
            print(colorama.Fore.CYAN + 'Daily Goal: ' + str(stat['days_items'][0]['total_completed']) + '/' + str(goal) + ' tasks')
            print(colorama.Fore.YELLOW + 'You\'ve completed your goal ' + str(stat['goals']['last_daily_streak']['count']) + ' days in a row.')
            print(colorama.Fore.BLUE + '(' + datetime.datetime.strptime(stat['goals']['last_daily_streak']['start'], '%Y-%m-%d').strftime('%d %b %Y') + ' - ' + datetime.datetime.strptime(stat['goals']['last_daily_streak']['end'], '%Y-%m-%d').strftime('%d %b %Y') + ')\n')
            print(colorama.Style.RESET_ALL, end="")
            daily(list(zip(daily_date, total_completed)), goal)
            print('\n············································\n')
            
            # Weekly
            
            total_completed = []
            weekly_date = []
            for i in stat['week_items']:
                total_completed.append(i['total_completed'])
                weekly_date.append(
                    datetime.datetime.strptime(i['from'], '%Y-%m-%d').strftime('%d %b %Y')
                    + ' - ' + 
                    datetime.datetime.strptime(i['to'], '%Y-%m-%d').strftime('%d %b %Y')
                )
            
            goal = stat['goals']['weekly_goal']
            print(colorama.Fore.GREEN + 'Weekly')
            print(colorama.Fore.CYAN + 'Weekly Goal: ' + str(stat['week_items'][0]['total_completed']) + '/' + str(goal) + ' tasks')
            print(colorama.Fore.YELLOW + 'You\'ve completed your goal ' + str(stat['goals']['max_weekly_streak']['count']) + ' weeks in a row.')
            print(colorama.Fore.BLUE + '(' + datetime.datetime.strptime(stat['goals']['max_weekly_streak']['start'], '%Y-%m-%d').strftime('%d %b %Y') + ' - ' + datetime.datetime.strptime(stat['goals']['max_weekly_streak']['end'], '%Y-%m-%d').strftime('%d %b %Y') + ')\n')
            print(colorama.Style.RESET_ALL, end="")
            weekly(list(zip(weekly_date, total_completed)), goal)
            
            # karma_avg = []
            # karma_date = []
            # for i in stat['karma_graph_data']:
            #     karma_avg.append(i['karma_avg'])
            #     karma_date.append(i['date'])
            
            # print('\nKarma Trend')
            # graph.karmaTrend(list(zip(karma_date, karma_avg)))
        else:
            if len(sys.argv) == 2:
                print (colorama.Fore.RED + 'Not a valid token\n' + colorama.Style.RESET_ALL)
            else:
                pass
            
            print('Usage: statist <token>')
    except:
        print (colorama.Fore.RED + 'Auth Error' + colorama.Style.RESET_ALL)
