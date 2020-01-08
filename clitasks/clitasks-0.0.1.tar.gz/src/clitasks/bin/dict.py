
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from PyInquirer import  style_from_dict, Token,prompt, print_json, Separator
import json
import os
import sys
from clint.arguments import Args
from clint.textui import puts, colored, indent

#process the args
args = Args()

#here we switch between interactive or command line mode
#terminal mode - 0, interactive - 1
vmode=False

#now process the flags
argflags = dict(args.grouped)
#print(argflags)
#process the arguments
#at this point, mode, firstname and surname
#lets simplify modes
vmodelist = ['interactive','i']

#style for the cli
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '#E91E63 bold',
})

#now lets assign the value
if '-m' in args.flags:
        if argflags["-m"].all[0] in vmodelist:
                vmode=True
		puts(colored.red("interactive2"))
elif '-mode' in args.flags: 
	if argflags["-mode"].all[0] in vmodelist:
                vmode=True
		

identity = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    },
    
    {
        'type': 'input',
        'name': 'surname',
        'message': 'What\'s your surname',
    }
]

#some questions for the identity
#first read in json-first task
infofound = False
if os.path.exists("test.json"):
	with open("test.json", "r") as read_file:
		data = json.load(read_file)
    	if data["first_name"]!='':
    		infofound=True

if not infofound:
	puts(colored.red("Your info was not found!"))
        gidentity = prompt(identity,style=style)
        with open("test.json", "w") as write_file:
                json.dump(gidentity, write_file)

#now if info is found alright
questions = [
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [ 
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
            },
            {
                'name': 'Extra cheese'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)