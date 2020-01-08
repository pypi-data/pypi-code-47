import json
import os
from clitasks.task_container import task
from clint.textui import puts, colored
from clint.textui import columns
import datetime
import sys
import random
from clitasks.quote import quotes

#some things that re needed
StrptimeFmt = "%Y-%m-%d %H:%M:%S.%f"

class Task:
    """
    Class to hold all task details
    """
    def __init__(self):
        """
        Do an init run
        """
        self.taskdir = os.path.join(os.environ['HOME'],'cli-tasks')
        self.taskfile = os.path.join(self.taskdir, 'tasks.json')
        self.taskbackup = ".".join([self.taskfile, 'bkup'])
        if not os.path.exists(self.taskdir):
            print("task dir not found, creating one..")
            os.mkdir(self.taskdir)
        if not os.path.exists(self.taskfile):
            print("task file not found, creating one..")
            open(self.taskfile, 'a').close()

    def create_task(self, taskdetails):
        #remove the main_option
        taskdetails.pop('main_option', None)
        #we have to add the current date as the date of setting the task
        now = datetime.datetime.now()
        #add the time to the dictionary
        taskdetails["created"] = now.__str__()
        taskdetails["status"] = False
        #print taskdetails["created"]
        #try to reconvert
        self.write_task(taskdetails)

    def fetch_task(self):
        data = []
        with open(self.taskfile, "r") as read_file:
            for line in read_file:
                data.append(json.loads(line))
        return data

    def output_tasks(self, group = None):
        #first sort by groups
        data = self.fetch_task()
        if group!=None:
            data = [d for d in data if d["group"]==group ]
        self.formatted_print(data)


    def formatted_print(self, data):
        if len(data) == 0:
            print("empty task file")
            return
        #we need autoformating
        colsize = self.find_colsize(data)
        col = colsize+5
        col2 = 50
        colsupersmall = 1
        colnum = 3
        #do header
        totcol = col+col2+colsupersmall+colnum
        self.header(totcol)

        count=0
        showorder=[]
        donetasks=[]
        for c,d in enumerate(data):
            if not d["status"]:
                count+=1
                showorder.append(c)
                #fix the time
                d = self.fix_when(d)
                #find when the task was added
                ttime,tstring = self.find_from_when(d)
                #format the color according to priority
                taskname = self.color_priority(d)
                #now we are ready to print out
                taskstring = ((" added %d %s ago, due %s, @%s")%(ttime,tstring,d["when"],d["group"]))
                taskstring = colored.white(taskstring)

                #get the status
                status = colored.red("0")

                puts(columns([(str(count)), colnum],[(status), colsupersmall],[(taskname), col], [(taskstring), col2]))
                #puts('{0: <80}'.format(taskname)+ taskstring)
            else:
                donetasks.append(c)

        #now process done tasks
        for c in donetasks:
            count+=1
            showorder.append(c)
            #fix the time
            d = self.fix_when(data[c])
            #find when the task was added
            ttime,tstring = self.find_from_when(d)
            #format the color according to priority
            taskname = self.color_priority(d)

            status = colored.green("0")
            taskstring = ((" done %d %s ago, @%s")%(ttime,tstring,d["group"]))
            taskstring = colored.blue(taskstring)

            puts(columns([(str(count)), colnum],[(status), colsupersmall],[(taskname), col], [(taskstring), col2]))


        finished = len(donetasks)/float(len(data))
        self.footer(totcol)
        print(" %2.2f %% tasks done!"%(finished*100))
        self.footer(totcol)
        puts(columns([(colored.blue(self.random_quote())), totcol]))
        self.footer(totcol)
        return showorder

    def delete(self):
        data = self.fetch_task()
        showorder = self.formatted_print(data)
        doneid = input("Serial number of task to be deleted: ")
        data.pop(showorder[doneid-1])
        self.reset()
        for d in data:
            self.write_task(d)
        print("deleted!")

    def done(self):
        data = self.fetch_task()
        showorder = self.formatted_print(data)
        doneid = int(input("Serial number of task to be marked done: "))
        #print data[doneid-1]
        data[showorder[doneid-1]]["status"]=True
        data[showorder[doneid-1]]["finished"]=datetime.datetime.now().__str__()
        self.reset()
        for d in data:
            self.write_task(d)
        print("done!")

    def random_quote(self):
        i = random.randint(0,len(quotes)-1)
        return quotes[i]

    def reset(self):
        if os.path.exists(self.taskbackup):
            os.remove(self.taskbackup)
        os.rename(self.taskfile, self.taskbackup)
        open(self.taskfile, 'a').close()


    #some random helpers
    def header(self, col):
        puts(columns([(colored.blue('-'*col)), col]))
        print("Tasks")
        #puts(columns([(colored.white('Tasks')), col]))
        puts(columns([(colored.blue('-'*col)), col]))

    def footer(self, col):
        puts(columns([(colored.blue('-'*col)), col]))


    def fix_when(self, d):
        if d["when"]==None:
            d["when"]="whenever"
        return d

    def find_from_when(self, d):
        created = datetime.datetime.strptime(d["created"],StrptimeFmt)
        if d["status"]==True:
            created = datetime.datetime.strptime(d["finished"],StrptimeFmt)
        now = datetime.datetime.now()
        diff = now-created
        days = diff.days
        tstring = "days"
        ttime = days
        if days==1:
            tstring = "day"
        elif days<=0:
            hours = diff.seconds/3600
            tstring = "hours"
            ttime = hours
            if hours==1:
                tstring = "hour"
            elif hours<1:
                ttime = diff.seconds/60
                tstring = "minutes"
                if ttime<=1:
                    tstring = "minute"
            elif hours<=0:
                tstring = "seconds"
                ttime = diff.seconds
                if ttime==1:
                    tsrting="second"

        return ttime,tstring

    def color_priority(self, d):

        if d["status"]==True:
            return colored.blue(d["description"])
        if d["priority"]==None:
            return colored.white(d["description"])
        elif d["priority"]==1:
            return colored.red(d["description"])
        if d["priority"]==2:
            return colored.yellow(d["description"])
        if d["priority"]==3:
            return colored.green(d["description"])



    def find_colsize(self, data):

        maxlength = 0
        lens = [len(x["description"]) for x in data ]
        return max(lens)

    def write_task(self, taskdetails):
        print("writing tasks")
        with open(self.taskfile,"a") as write_file:
            json.dump(taskdetails,write_file)
            write_file.write("\n")
        write_file.close()
