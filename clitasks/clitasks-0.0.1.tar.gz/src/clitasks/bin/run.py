#!/usr/bin/python
"""
Command line task management system in python.

Main file which provides the command line interface
"""

import argparse as ap
from clitasks.tasks import Task


def main():
	"""
	Main function which runs when cli-tasks is called
	"""
	arg = ap.ArgumentParser(description="cli-tasks command line taskbook\n. ",usage='''
			clitasks <command> [<args>]

			Short guide
			-----------
			task -n (--new) : description
			optional: -w (--when) : due date
				  -p (--priority) : 1(high),2(medium) or 3(low)
				  -g (--group) : name of the task group
			show (--fetch) [all, <groupname> ]
				   fetch all tasks or by group
			done (--done) <task number> : mark the task as done

		''')

	#add a subarg parser
	subarg = arg.add_subparsers(dest='main_option')

	#th main parser part for task
	arg_task = subarg.add_parser("task",help="keyword to add a task")
	#now sub args for this one
	#description
	arg_task.add_argument("-d", "--description", required=True,
	help="specify -d followed by task description")
	#due date
	arg_task.add_argument("-w", "--when", required=False,
	help="specify -w followed by task due date")
	#priority
	arg_task.add_argument("-p", "--priority", required=False, type=int, choices=[1,2,3],
	help="specify -p followed by priority of 1,2 or 3")
	#group
	arg_task.add_argument("-g", "--group", required=False,
	help="specify -g followed by groupname")


	#the show commands
	arg_task = subarg.add_parser("show",help="keyword to add a task")
	arg_task.add_argument("-g", "--group", required=False,
	help="specify -g followed by groupname")

	#the mark commands
	arg_task = subarg.add_parser("done",help="keyword to add a task")

	#the mark commands
	arg_task = subarg.add_parser("delete",help="keyword to add a task")

	#the reset command
	arg_task = subarg.add_parser("reset",help="reset the tasks file")


	taskdetails = vars(arg.parse_args())

	task = Task()

	if taskdetails['main_option'] == 'task':
		task.create_task(taskdetails)
		print("task created")
	elif taskdetails['main_option'] == 'show':
		print("showing")
		dontneed = task.output_tasks(taskdetails["group"])
	elif taskdetails['main_option'] == 'reset':
		task.reset()
	elif taskdetails['main_option'] == 'done':
		task.done()
	elif taskdetails['main_option'] == 'delete':
		task.delete()
	else:
		print(taskdetails['main_option'])
		print("Unknown main option")
