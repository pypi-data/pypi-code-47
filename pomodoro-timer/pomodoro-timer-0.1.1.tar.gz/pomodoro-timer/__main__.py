#!/usr/bin/env python3
import time
import curses
from curses import wrapper
from curses import textpad
import simpleaudio as sa
import sys
import subprocess
import re
import os
import argparse
from argparse import ArgumentParser

APP_NAME='pomodoro-timer'
APP_TITLE = 'Pomodoro-Timer'
use_audio_cue = True
use_window_cue = True
max_play_time = 5

# can be overwritten by passing -c / --config-folder argument
CONFIG_FOLDER = os.path.expanduser(f"~/.config/{APP_NAME}")
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SOUNDS_DIR = os.path.join(SCRIPT_DIR, 'sounds')

try:
    sound_start_break = sa.WaveObject.from_wave_file(os.path.join(SOUNDS_DIR, 'tolling_bell.wav'))
    sound_start_work = sa.WaveObject.from_wave_file(os.path.join(SOUNDS_DIR, 'metal_gong_1.wav'))
except FileNotFoundError as err:
    print(err)
    print(f"{APP_NAME}: No Audio will be played!")
    use_audio_cue = False

if sys.platform == 'linux' or sys.platform == 'linux2':
    zenity_dialog_present = True

# do not open a notify window when the first block is started
# we do not need to be notified yet

def on_start_break(no_cues=False):
    if use_audio_cue and not no_cues:
        play_obj = sound_start_break.play()
    if use_window_cue and zenity_dialog_present and not no_cues:
        subprocess.Popen(['zenity', '--info','--width=200', '--height=50','--text=You can take a break.', '--ok-label=Take a well deserved break.'])

def on_start_work(no_cues=False):
    if use_audio_cue and not no_cues:
        play_obj = sound_start_work.play()
    if use_window_cue:
        if zenity_dialog_present and not no_cues:
            subprocess.Popen(['zenity', '--info','--width=200', '--height=50','--text=The work block begins.', '--ok-label=Ok start working.'])

def on_session_finished():
    if use_window_cue and zenity_dialog_present:
            result = subprocess.run(['zenity', '--info','--width=200', '--height=50','--text=Session finished!', '--ok-label=The current session is finished.'])

def setup_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True) # non-blocking I/O
    return stdscr

def time_format_seconds(seconds):
    minutes = int(seconds / 60)
    seconds = int(seconds % 60)
    hours = int(minutes / 60)
    minutes = minutes % 60
    out_str = ''
    if hours:
        out_str += f"{hours}h "
    if minutes:
        out_str += f"{minutes}m "
    if seconds or not (hours or minutes):
        out_str += f"{seconds}s"
    return out_str.strip()

# @TODO: maybe take time as a time_str --> unambigous
class Block:
    def __init__(self, name, time_s, is_break = False):
        self.name = name
        self.time_s = time_s
        self.is_break = is_break

    def __repr__(self):
        time_str = time_format_seconds(self.time_s)
        out_str = f"Block: {self.name}, t: {time_str}, is_break: {self.is_break}"
        return out_str

    def pretty_str(self):
        time_str = time_format_seconds(self.time_s)
        out_str = f"[{self.name} ({time_str})]"
        if self.is_break:
            out_str += " (B)"
        return out_str

    def time_in_minutes(self):
        return self.time_s // 60
    def time_in_seconds(self):
        return self.time_s
    
    def copy(self):
        return Block(self.name, self.time_s, self.is_break)

class Session:
    def __init__(self, name, description, blocks = [], auto_restart = True):
        self.name = name
        self.description = description
        # we check block references to get the next block or previous block
        # this doesn't work if we have the same block several times in the array
        # which might be done for convenience
        # @Audit, @Check: are we sure the creator of a session doesn't want valid
        # references to the blocks?
        self.blocks = [block.copy() for block in blocks]
        self.auto_restart = auto_restart

    def __repr__(self):
        out_str = f"Session: {self.name}, auto_restart: {self.auto_restart}" + ' {\n'
        for block in self.blocks:
            out_str += '    ' + str(block) + '\n'
        out_str += "}"
        return out_str

    def pretty_str(self):
        out_str = f"Session: {self.name}"
        if self.auto_restart:
            out_str += ' [auto_restart]'
        out_str += '\n'
        if self.description:
            out_str += f"    Descr: {self.description}\n"
        for block in self.blocks:
            out_str += '    ' + block.pretty_str() + '\n'
        return out_str


    def is_last_block(self, block):
        position = self.blocks.index(block)
        return position == len(self.blocks) - 1

    def get_blocks_before(self, block):
        assert(block in self.blocks)
        return self.blocks[:self.blocks.index(block)]

    def get_blocks_after(self, block):
        assert(block in self.blocks)
        position = self.blocks.index(block)
        return self.blocks[position+1:]

    def first_block(self):
        assert(len(self.blocks)> 0)
        return self.blocks[0]

    def is_first_block(self, block):
        return self.blocks.index(block) == 0

    # immediate version of 'next' block
    def block_after(self, block):
        assert(block in self.blocks)
        next_pos = self.blocks.index(block) + 1
        next_pos = next_pos % len(self.blocks)
        return self.blocks[next_pos]
    
    # immediate version of 'previous' block
    def block_before(self, block):
        assert(block in self.blocks)
        previous_pos = self.blocks.index(block) - 1
        if previous_pos < 0:
            previous_pos = len(self.blocks) - 1
        return self.blocks[previous_pos]


def default_session():
    work_minutes = 25 
    break_minutes = 5 
    work_block = Block('Work', work_minutes*60)
    break_block = Block('Break', break_minutes*60, is_break=True)
    longer_break_block = Block('Long Break', 20 * 60, is_break=True)
    blocks = [work_block, break_block] * 4
    blocks[-1] = longer_break_block # instead of a shorter break
    default_session = Session("Default", f"Work ({work_minutes}m) -> Break ({break_minutes}m)", blocks) 
    return default_session

def simple_timer_session(time_str):
    time_s = time_str_to_seconds(time_str) 
    return Session("Timer", "", [Block('Time', time_s), Block('Finished', 1)])

def progress_bar(percentage, max_blocks=50):
   num_blocks = int(percentage * max_blocks)
   num_fillers = max_blocks - num_blocks
   return f"[{'*'*num_blocks}{'-'*num_fillers}]"

help_str_general = """
list                    -   list all sessions
audio [on | off]        -   turn audio cues on or off (you can also start application with 'no-audio' option) option)
window [on | off]       -   turn window cues on or off (you can also start application with 'no-window' option)
start <session>         -   start a session by name or by number, if you just say start use the default session
pause                   -   pause current session (continue with 'resume', 'start')
stop
resume                  -   resume a paused session
next                    -   continue with the next block
previous                -   redo the previous block
start                   -   resume or start the default session
restart                 -   restart a session from the beginning
add <time>              -   add time spent ('1h15m', '15m' for example)
+ <time>
subtract <time>         -   subtract time spent on the current block ('5m' for example)
sub <time>
- <time>
restart_block           -   restart the current block
quit                    -   use 'quit' or 'exit' to quit the application
exit
help                    -   show this help text
"""
class PomodoroTimer:
    def __init__(self, session=default_session(),sessions=[default_session()]):
        self.session = session
        self.current_block = None
        self.start_time = None
        self.on_start_work = on_start_work
        self.on_start_break = on_start_break
        self.on_session_finished = on_session_finished
        self.is_paused = True
        self.elapsed_time = 0
        self.last_time = None 
        self.is_finished = False
        self.sessions = sessions

    def in_session(self):
        return self.session and self.current_block

    def start(self):
        self.start_block(self.session.first_block())

    def reset_timer(self):
        self.start_time = time.time()
        self.elapsed_time = 0
        self.last_time = self.start_time
    
    def start_next_block(self):
        self.start_block(self.session.block_after(self.current_block))

    def start_previous_block(self):
        self.start_block(self.session.block_before(self.current_block))

    def help_str(self):
        out_str = ''

    def list_sessions(self):
        out_str = 'Sessions:\n\n'
        for i, session in enumerate(self.sessions):
            out_str += f"{i+1}) {session.pretty_str()}"
            out_str += '\n\n'
        return out_str

    def run_command(self, command_str):
        tokens, success = consume_all_tokens(command_str)

        if len(tokens) == 0:
            return self.help()

        if len(tokens) == 1:
            command = tokens[0]
            if command == 'pause' or command == 'stop':
                self.pause()
            elif command == 'resume':
                self.resume()
            elif command == 'start':
                if self.in_session():
                    self.resume()
                else:
                    self.start_session()
            elif command == 'restart':
                self.restart_session()
            elif command == 'restart_block':
                self.restart_block()
            elif command == 'help':
                return self.help()
            elif command == 'no-audio':
                use_audio_cues = False
            elif command == 'no-window':
                use_window_cues = False
            elif command == 'exit' or command == 'quit':
                self.exit()
            elif command == 'next':
                self.start_next_block()
            elif command == 'previous':
                self.start_previous_block()
            elif command == 'list':
                return self.list_sessions()
        else: 
            if len(tokens) >= 3:
                first = tokens[0]
                rest = tokens[1:]
                tokens = [first, ''.join(rest)]
                #return f"'{command_str}' is not a valid command!\nType 'help' and press enter to show all available commands."
            command, param = tokens
            if command == 'add' or command == '+':
                time = time_str_to_seconds(param)
                if time == 0:
                    return f"'{param}' is not a valid time!\n"
                else:
                    self.add_time(time)
            elif command == 'subtract' or command == 'sub' or command == '-':
                time = time_str_to_seconds(param)
                if time == 0:
                    return f"'{param}' is not a valid time!\n"
                else:
                    self.subtract_time(time)
            elif command == 'audio':
                param = param.lower()
                global use_audio_cue
                if param == 'off' or param == 'false':
                    use_audio_cue = False
                    return f"Audio is turned off."
                elif param == 'on' or param == 'true':
                    use_audio_cue = True
                    return f"Audio is turned on."
                return f"Parameter: {param} not found for command: {command}!"
            elif command == 'window':
                global use_window_cue
                if param == 'off' or param == 'false':
                    use_window_cue = False
                    return f"No window signals will be shown."
                elif param == 'on' or param == 'true':
                    use_window_cue = True
                    return f"Window signals will be shown."
                else:
                    return f"Parameter: {param} not found for command: {command}!"

            elif command == 'start':
                name = param
                # search by exact name
                for session in self.sessions:
                    if name == session.name:
                        self.start_session(session)
                        return
                # search by number
                for i, session in enumerate(self.sessions):
                    if str(i+1) == name:
                        self.start_session(session)
                        return
                # search if part of name case insensitive
                for session in self.sessions:
                    if name.replace(' ', '').lower()  in session.name.replace(' ', '').lower():
                        self.start_session(session)
                        return
                return f"Session name: {name} not found!"

    # command
    def pause(self):
        self.is_paused = True
    # command
    def resume(self):
        self.last_time = time.time() # otherwise we count the time within the pause
        self.is_paused = False
    # command
    def restart_block(self):
        self.start_block(self.current_block, no_cues=True)
    # command
    def restart_session(self):
        self.start_block(self.session.first_block(), no_cues=True)
    # command
    def exit(self):
        exit(0)
    # command
    def help(self):
        return help_str_general
    # command
    def start_session(self, session=None):
        if session:
            self.session = session
        self.reset_timer()
        # use audio, as it helps to 'prime' / get ready for the session
        # even on starting the first block
        self.start_block(self.session.first_block(), no_cues=False)
    # command
    def subtract_time(self, time):
        self.elapsed_time -= time
        if self.elapsed_time < 0:
            self.elapsed_time = 0
    # command
    def add_time(self, time):
        self.elapsed_time += time

    def start_block(self, block, no_cues=False):
        last_block = self.current_block
        self.current_block = block
        self.reset_timer()
        self.is_paused = False # just in case
        self.is_finished = False
        if block.is_break:
            self.on_start_break(no_cues)
        else:
            # also check that we are not repeating a cycle, only show no audio / visual
            # when you actually start a new session
            self.on_start_work(no_cues)

    def elapsed_time_s(self):
        return self.elapsed_time

    def ready_for_block_change(self):
        return self.elapsed_time_s() > self.current_block.time_in_seconds()

    def update(self):
        if self.is_paused:
            pass # do nothing
        elif self.is_finished:
            pass
        else:
            now = time.time()
            self.elapsed_time += now - self.last_time
            self.last_time = now
            if self.ready_for_block_change():
                if self.session.is_last_block(self.current_block) and not self.session.auto_restart:
                    self.is_finished = True
                    if self.on_session_finished:
                        self.on_session_finished()
                else:
                    next_block = self.session.block_after(self.current_block)
                    self.start_block(next_block)
        return self.elapsed_time

    def finished(self):
        return self.is_finished

    def block_output_str_before(self):
        blocks_before = self.session.get_blocks_before(self.current_block) 
        out_str = ''
        for block in blocks_before:
            out_str += f"- {block.name}\n"
        return out_str
  
    def block_output_str_after(self):
        blocks_after = self.session.get_blocks_after(self.current_block) 
        out_str = ''
        for block in blocks_after:
            out_str += f"- {block.name}\n"
        return out_str
    
    def session_title_str(self):
        out_str = ''
        title = f"{self.session.name} - {self.session.description}"
        out_str += len(title)*'~' + '\n'
        out_str += title + '\n'
        out_str += len(title)*'~' + '\n\n'
        return out_str

    def app_title_str(self):
        out_str = ''
        title = f"{APP_TITLE}"
        out_str += len(title)*'*' + '\n'
        out_str += title + '\n'
        out_str += len(title)*'*' + '\n\n'
        return out_str

    def settings_str(self):
        out_str = f"Audio: {'on'*use_audio_cue}{'off'*(not use_audio_cue)}\n" 
        out_str += f"Window: {'on'*use_window_cue}{'off'*(not use_window_cue)}\n" 
        out_str += '\n'
        return out_str


    def session_progress_str(self):
        # Print Title
        out_str = '\n'
        elapsed_time_s = self.elapsed_time_s()
        finish_time = self.current_block.time_in_seconds()
        done_percentage = elapsed_time_s / finish_time
        
        # Print Blocks Before
        before = self.block_output_str_before()
        if before:
            out_str += before
            out_str += '\n'

        out_str += f"* {self.current_block.name}\n\n"

        if self.is_paused:
            out_str += f"[PAUSED]\n\n"

        out_str += f"{time_format_seconds(elapsed_time_s)} / {time_format_seconds(finish_time)}\n"
        out_str += progress_bar(done_percentage)

        # Print Blocks after
        out_str += '\n\n' + self.block_output_str_after()
        return out_str
SUCCESS = 1
ERROR = 0
def consume_token(line):
    i = 0
    while i < len(line) and line[i].isspace():
        i += 1
    start = i
    while i < len(line) and not line[i].isspace():
        i += 1
    if i >= len(line):
        return line[start:], '', SUCCESS
    if i > start+1:
        return line[start:i], line[i:], SUCCESS
    return '', '', ERROR

def consume_quoted(line):
    pos_double = len(line)
    pos_single = len(line)
    quote_double = '"'
    quote_single = "'"
    if quote_double in line:
        pos_double = line.index(quote_double)
        if line.count(quote_double) < 2:
            print(f"You are missing a second {quote_double} quote in the line: {line}")
            return '', line, ERROR
    if quote_single in line:
        pos_single = line.index(quote_single)
        if line.count(quote_single) < 2:
            print(f"You are missing a second {quote_single} quote in the line: {line}")
            return '', line, ERROR
    quote_used = quote_double
    if pos_single < pos_double:
        quote_used = quote_single
    start = line.index(quote_used) + 1
    end = line[start:].index(quote_used) + start 
    return line[start:end], line[end+1:], SUCCESS


def peek_next_non_whitespace_character(line):
    i = 0
    while i < len(line):
        if not line[i].isspace():
            return line[i]
        i += 1
    return None 

def is_next_token_quoted(line):
    quotes = ['"', "'"]
    return peek_next_non_whitespace_character(line) in quotes

def consume_all_tokens(line):
    line = line.strip()
    tokens = []
    while line:
        if is_next_token_quoted(line):
            token, line, CODE = consume_quoted(line)
            if CODE == ERROR:
                return tokens, ERROR
            tokens.append(token)
        else:
           token, line, CODE = consume_token(line)
           if CODE == ERROR:
               return tokens, ERROR
           tokens.append(token)
    return tokens, SUCCESS


def create_session_from_src(src):
    src = src.split('\n')
    session_name = None
    session_description = ''
    auto_restart = False
    labels = []
    blocks = []
    current_blocks = []
    multiplier = 1
    multiplier_regex = re.compile('(\d+)x')
    for i, line in enumerate(src):
        line = line.strip()
        if not line: # skip empty lines
            if current_blocks:
                blocks.extend(current_blocks * multiplier)
                current_blocks.clear()
            multiplier = 1
            continue
        if line[0] == '#': # skip comments
            if current_blocks:
                blocks.extend(current_blocks * multiplier)
                current_blocks.clear()
            multiplier = 1
            continue

        if not session_name:
            first, line, _ = consume_token(line)
            if first.lower() != 'session':
                print(f"First definition for a session should be 'session <name>'")
                print(f"But {first} was encountered!")
                return None, ERROR
            if not line:
                print(f"Please specify a session name after 'session'")
                print(f"Example: session Read All The Books Session")
                return None, ERROR
            rest, CODE = consume_all_tokens(line)
            if CODE == ERROR:
                return None, ERROR
            session_name = rest.pop(0)
            if len(rest) > 0:
                session_description = ''.join(rest)
        else:
            tokens, CODE = consume_all_tokens(line)
            if CODE == ERROR:
                return None, ERROR
            if len(tokens) == 1 and tokens[0] == 'auto_restart':
                auto_restart = True
                continue
            match = multiplier_regex.match(tokens[0])
            if match:
                if current_blocks:
                    blocks.extend(current_blocks * multiplier)
                    current_blocks.clear()
                multiplier = int(match.group(1))
                continue
            # block [break|work] <name> <time>
            if len(tokens) < 3:
                print(f"You need to specify at least 'block <name> <time>' or optionally if it is a break or work block: 'block break <name> <time> for example.")
                return None, ERROR
            first = tokens.pop(0)
            if first.lower() != 'block':
                print(f"Encountered: {first}, not a block definition! Specify a block after the session name! 'block <name> <time>'")
                return None, ERROR 
            second = tokens.pop(0)
            is_break = False
            if second == 'break':
                is_break = True
            if second == 'break' or second == 'work':
                labels.append(second)
                second, tokens = tokens
            else:
                labels.append(None)

            name = second
            if not tokens:
                print(f"You are missing the time in a block definition!")
                return None, ERROR

            time_str = ''.join(tokens)
            time_s = time_str_to_seconds(time_str)
            block = Block(name, time_s, is_break)
            current_blocks.append(block)
    if not session_name or not blocks:
        print(f"Please specify a session: 'session <name>' and at least one block!")
        return None, ERROR
    
    if not all(labels):
        if any(labels):
            print(f"If you specify a block as 'break' or 'work' you need to do this for every block present!")
            return None, ERROR
        else:
            for i in range(len(blocks)):
                block = blocks[i].copy()
                block.is_break = (i % 2 == 1)
                blocks[i] = block

    for i, label in enumerate(labels):
        if label:
            block = blocks[i]
            if label == 'break':
                block.is_break = True
            elif label == 'work':
                block.is_break = False
            else:
                print(f"If you specify at least one label 'work' or 'break' you need to specify it for everyone else!")
                print(f"You can also omit the labels, then every second block will automatically be labeled 'break'.")
                return None, ERROR
    return Session(session_name, session_description, blocks, auto_restart), SUCCESS

time_regex = re.compile('(\d+h)?(\d+m)?(\d+s)?')
def time_str_to_seconds(time_str):
    time_str = time_str.replace(' ', '')
    match = time_regex.match(time_str)
    total_seconds = 0
    if not match:
        print(f"Time: '{time_str}' is no valid time!")
        return None, ERROR
    if match.group(1):
        hours = int(match.group(1)[:-1])
        total_seconds += hours*60*60
    if match.group(2):
        minutes = int(match.group(2)[:-1])
        total_seconds += minutes * 60
    if match.group(3):
        seconds = int(match.group(3)[:-1])
        total_seconds += seconds
    return total_seconds


default_session_str="""
session 'Default' 'Work (25m) -> Break (5m)'
auto_restart
block Work 25m
block Break 5m is_break
"""

default_big_session_str="""
session 'Big Session' '3x[Work (25m) -> Break (5m)], Work (25m) -> Long Break (20m)'
3x
block Work 25m
block Break 5m is_break

block Work 25m
block 'Long Break' 20m is_break
"""

default_long_session_str="""
session Long 'Work (1h) -> Break (15m)'
auto_restart
block Work 1h
block Break 15m
"""

default_medium_session_str="""
session Medium 'Work (45m) -> Break (10m)'
auto_restart
block Work 45m
block Break 10m
"""

default_names = ['Default', 'BigSession', 'Long', 'Medium']
default_session_strs = [default_session_str, default_big_session_str,  default_long_session_str, default_medium_session_str]
def setup_and_read_config():
    sessions = []
    if not os.path.exists(CONFIG_FOLDER):
        print(f"Create config folder: {CONFIG_FOLDER}")
        os.makedirs(CONFIG_FOLDER)
        for i, name in enumerate(default_names):
            filename = os.path.join(CONFIG_FOLDER, name + '.session')
            f = open(filename, 'w')
            f.write(default_session_strs[i])
            f.close()
    for filename in os.listdir(CONFIG_FOLDER):
        if filename.endswith('.session'):
            filename = os.path.join(CONFIG_FOLDER, filename)
            with open(filename, 'r') as file:
                file_str = file.read()
            session, success = create_session_from_src(file_str)
            if success:
                sessions.append(session)
            else:
                print(f"The session {filename} could not be created!")
    return sessions

def read_specified_session(session_path):
    if not os.path.isabs(session_path):
        cur_dir = os.curdir
        print(f"The path: {session_path} is not absolute but relative.")
        session_path = os.path.abspath(session_path)
        print(f"Absolute path is: {session_path}")
    if not os.path.exists(session_path):
        if session_path.endswith('.session'): # maybe they forgot the extension
        # auto add it then check again
            session_path += '.session'
        if not os.path.exists(session_path):
            print(f"The path: {session_path} does not exist!")
            return None
    with open(session_path, 'r') as file:
        file_str = file.read()
        session, success = create_session_from_src(file_str)
    if success:
        return session
    else:
        print(f"The session {session_path} could not be created!")
        return None 
    
class Display:
    def __init__(self):
        self.text = ''
        self.app_title = ''
        self.settings_str = ''
        self.session_title = ''
        self.help_text = ''
        self.command_buffer = []

    def add_to_buffer(self, ch):
        self.command_buffer.append(ch)

    def clear_buffer(self):
        self.command_buffer = []

    def draw(self, stdscr):
        _, width = stdscr.getmaxyx()
        out_str = '\n'
        out_str += self.app_title
        out_str += '\n'
        out_str += self.settings_str
        out_str += '\n'
        out_str += self.session_title
        out_str += self.text
        out_str += self.help_text
        out_str += '\n>: '
        stdscr.addstr(out_str)
        typed_str = ''.join(self.command_buffer)
        stdscr.addstr(typed_str)

def run_command(command_str, pomodoro_timer, display):
    result = pomodoro_timer.run_command(command_str)
    display.clear_buffer()
    if result:
        display.help_text = result
    else:
        display.help_text = ''


def main(session=None):
    sessions = setup_and_read_config()
    if session:
        # @Question, @TODO, what if session is in config folder?
        sessions.insert(0, session)# what if session is already in here?

    stdscr = setup_curses() 
    stdscr.refresh()
    height, width = stdscr.getmaxyx()
    display_pad_height = 10000
    display_pad = curses.newpad(display_pad_height, width)
    display_pad.scrollok(True)
    display_pad_pos = 0
    display_pad_refresh = lambda: display_pad.refresh(display_pad_pos+2, 0, 0, 0, height-1, width)




    try:
        def input_validator(keystroke):
            if keystroke == 10: # Enter
                command = input_textbox.gather()
                return keystroke
            return keystroke
        display = Display()
        if sessions:
            pomodoro_timer = PomodoroTimer(sessions=sessions)
        else:
            pomodoro_timer = PomodoroTimer()
        display.app_title = pomodoro_timer.app_title_str()
        display.help_text = pomodoro_timer.list_sessions()
        display.settings_str = pomodoro_timer.settings_str()
        display.help_text += "\nType in 'help' to show all available commands!\n"
        stdscr.clear()
        if session:
            pomodoro_timer.start_session(session)
        time_since_draw = time.time()
        # we timeout the stdscr window for 50 ms every 50 ms
        # because we use nonblocking input for the 'command line'
        # otherwise curses uses too much CPU time
        time_to_next_input = 50 #ms
        while not pomodoro_timer.finished():
            pomodoro_timer.update()
            if pomodoro_timer.in_session():
                display.text = pomodoro_timer.session_progress_str()
                display.session_title = pomodoro_timer.session_title_str()
            else:
                display.text = ''
                display.session_title = ''

            display.settings_str = pomodoro_timer.settings_str()
            # draw command input
            c = stdscr.getch()
            if c == curses.KEY_RESIZE:
                height, width = stdscr.getmaxyx()
                while display_pad_pos > display_pad.getyx()[0] - height - 1:
                    display_pad_pos -=1
                display_pad_refresh()
                display_pad_refresh()
            elif c == curses.KEY_DOWN and display_pad_pos < display_pad.getyx()[0]-height-1:
                display_pad_pos += 1
                display_pad_refresh()
            elif c == curses.KEY_UP and display_pad_pos > -2:
                display_pad_pos -= 1
                display_pad_refresh()
            if c and (0 < c < 256):
                if c == 10: # Enter
                    command_str = ''.join(display.command_buffer).strip()
                    run_command(command_str, pomodoro_timer, display)
                elif c == 127:
                    if display.command_buffer:
                        display.command_buffer.pop()
                else:
                    display.command_buffer.append(chr(c))
            # drawing sometimes throws an error in ncurses if window is too small
            try:        
                if time.time() - time_since_draw > (time_to_next_input / 1000): # ms to s
                    display.draw(display_pad)
                    display_pad_refresh()
                    time_since_draw = time.time()
                    stdscr.timeout(time_to_next_input);
            except Exception as ex:
                f = open('test', 'w')
                f.write(str(ex))
                f.close()
                exit(1)
            time.sleep(0.05)
            display_pad.erase()
    except KeyboardInterrupt as ex:
        curses.endwin()
        exit(0)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--no-sound', action='store_true', dest='no_sound', help='do not play sound when starting / stopping blocks')
    parser.add_argument('--no-window', action='store_true', dest='no_window', help='do not show a notification window when starting / stopping blocks') 
    parser.add_argument('-c', '--config-folder', dest='config_folder', help='use the specified config folder for loading session files and storing configs')
    parser.add_argument('-s', '--start', dest='session_path', help='specify a specific session to start')
    parser.add_argument('-d', '--default', action='store_true', dest='default', help='Run the default 25m work, 5m break cycle')
    parser.add_argument('--timer', dest='timer', help='start a simple timer, then stop')
    args = parser.parse_args()
    args_str = ''.join([])

    if args.no_sound:
        use_audio_cue = False
    if  args.no_window: 
        use_window_cue = False
    if args.config_folder:
        if os.path.exists(args.config_folder):
            print(f"Use specified config folder: {args.config_folder}")
            CONFIG_FOLDER = args.config_folder
        else:
            print(f"Config folder: {args.config_folder} does not exist!")
            print(f"Use default folder: {CONFIG_FOLDER}!")

    session = None
    if args.session_path:
        session_path = args.session_path
        session = read_specified_session(session_path)
    if args.default:
        session = default_session()
    if args.timer:
        session = simple_timer_session(args.timer) 
    main(session)

