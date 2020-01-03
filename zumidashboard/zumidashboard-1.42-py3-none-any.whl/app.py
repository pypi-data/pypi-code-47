from flask import Flask
from flask_socketio import SocketIO
import time, subprocess
from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.protocol import Note
import zumidashboard.scripts as scripts
import zumidashboard.sounds as sound
import zumidashboard.updater as updater
from zumidashboard.drive_mode import DriveMode
import os
import os, re
import logging
from logging.handlers import RotatingFileHandler

if not os.path.isdir('/home/pi/Dashboard/debug'):
    os.mkdir('/home/pi/Dashboard/debug')
app = Flask(__name__, static_url_path="", static_folder='dashboard')
app.zumi = Zumi()
app.screen = Screen(clear=False)
app.ssid = ''
app.action = ''
app.action_payload = ''
socketio = SocketIO(app)
handler = RotatingFileHandler('/home/pi/Dashboard/debug/dashboard.log', maxBytes=10000, backupCount=1)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.drive_mode = DriveMode(app.zumi)


def _awake():
    app.screen.hello()
    sound.wake_up_sound(app.zumi)

def log(msge):
    app.logger.info(time.strftime('{%Y-%m-%d %H:%M:%S} ')+msge)

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# first page render (select wifi page)
@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/select-network')
def select_network():
    return app.send_static_file('index.html')

@app.route('/success')
def success():
    return app.send_static_file('index.html')

@socketio.on('ssid_list')
def ssid_list(sid):
    print('getting ssid list')
    app.action = 'ssid_list'
    log('getting ssid list')

    _list = scripts.get_ssid_list()
    socketio.emit('ssid_list',str(_list))


@socketio.on('disconnect')
def test_disconnect():
    print('Socket disconnected')
    log('client disconnected')

@socketio.on('connect')
def test_connect():
    print('a client is connected')
    log('a client is connected')
    log(app.action)
    if app.action == 'check_internet':
        time.sleep(1)
        socketio.emit(app.action, app.action_payload)
        app.action = ''
        app.action_payload = ''

# confirm check internet msge was receive
@socketio.on('acknowledge_check_internet')
def acknowledge_check_internet():
     log('msge check internet was receive')
     app.action = ''

# connect wifi functions
@socketio.on('connect_wifi')
def connect_wifi(ssid, passwd):
    print('app.py : connecting wifi start')
    log('app.py : connecting wifi start')

    print(str(type(ssid))+ssid)
    scripts.add_wifi(ssid, passwd)
    print("personality start")
    app.screen.draw_image_by_name("tryingtoconnect")
    sound.try_calibrate_sound(app.zumi)
    sound.try_calibrate_sound(app.zumi)
    print("personality done")
    log('app.py : connecting wifi:'+ssid+' end')
    print('app.py : connecting wifi end')


@socketio.on('check_internet')
def check_internet(mode):
    app.action = 'check_internet'
    connected, ssid = scripts.check_wifi()
    app.ssid = ssid
    if not connected: 
        print('emit fail to connect')
        log('app.py : emit fail to connect - Silent Mode')
        if mode != 'SILENT_MODE':
            app.screen.draw_text_center("Failed to connect.\n Try again.")
        socketio.emit('check_internet', '') 
        return
    time.sleep(5)

    app.connected_to_internet = scripts.check_internet()
    print("version check : {}".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0]))
    if connected and "zumidashboard" in app.connected_to_internet['dashboard_version']:
        print('app.py: emit check internet success')
        log('app.py : emit check internet success')
        socketio.emit('check_internet', app.connected_to_internet)
    elif connected:
        print('app.py : conected to local network but not internet')
        log('app.py : conected to local network but not internet')
        app.connected_to_internet = 'LOCAL_NETWORK'
        socketio.emit('check_internet', 'LOCAL_NETWORK')
    elif mode == 'SILENT_MODE':
        print('emit fail to connect - Silent Mode')
        log('app.py : emit fail to connect - Silent Mode')
        socketio.emit('check_internet', '')
    else:
        print('emit fail to connect')
        log('app.py : emit fail to connect')
        app.screen.draw_text_center("Failed to connect.\n Try again.")
        socketio.emit('check_internet', '')
    app.action_payload = app.connected_to_internet

@socketio.on('zumi_success')
def zumi_success():
    app.screen.draw_text_center("I'm connected to \"" + app.ssid + "\"")
    sound.calibrated_sound(app.zumi)
    time.sleep(2)
    _awake()

@socketio.on('kill_supplicant')
def kill_supplicant():
    scripts.kill_supplicant()

@socketio.on('zumi_fail')
def zumi_success():
    app.screen.draw_text_center("Failed to connect.\n Try again.")
    app.zumi.play_note(Note.A5, 100)
    app.zumi.play_note(Note.F5, 2 * 100)
    time.sleep(2)
    app.screen.draw_text_center("Go to \"zumidashboard.ai\" in your browser")


# zumi run demo and lesson event link is in frontend already
@socketio.on('activate_offline_mode')
def activate_offline_mode():
    app.screen.draw_text_center("Starting offline mode")
    subprocess.Popen(['sudo', 'killall', 'wpa_supplicant'])
    time.sleep(3)
    _awake()


@socketio.on('run_demos')
def run_demos():
    print('Run demos event from dashboard')


@socketio.on('goto_lessons')
def goto_lessons():
    print('Go to lessons event from dashboard')


# updater function and page
@app.route('/update')
def update():
    return app.send_static_file('index.html')


@socketio.on('update_firmware')
def update_firmware():
    print('update firmware from dashboard')
    print('server down soon')
    time.sleep(1)
    print(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    command = "sudo killall -9 python3 && sudo python3 -c 'import zumidashboard.updater as update; "
    command += "update.run(v={})'".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    subprocess.run([command], shell=True)


@socketio.on('update_everything')
def update_everything():
    print('update firmware & content from dashboard')
    print('server down soon')
    time.sleep(1)
    print(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    command = "sudo killall -9 python3 && sudo python3 -c 'import zumidashboard.updater as update; "
    command += "update.run_everything(v={})'".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    subprocess.run([command], shell=True)


@socketio.on('update_content')
def update_content():
    print('update content from dashboard')
    if updater.check_content_version():
        print("need update")
        updater.update_content(app.zumi, app.screen)
    else:
        print("up-to-date")
    print('emit update content')
    socketio.emit('update_content')



# shutdown function and page
@app.route('/shutting-down')
def shutting_down():
    return app.send_static_file('index.html')


@socketio.on('shutdown')
def shutdown():
    app.screen.draw_text_center("Please switch off after 15 seconds.")
    scripts.shutdown()


# this is for refresh page
@app.route('/step2')
def step2():
    return app.send_static_file('index.html')

@socketio.on('battery_percent')
def battery_percent():
   socketio.emit('battery_percent',str(app.zumi.get_battery_percent()))

@socketio.on('hardware_info')
def hardware_info():
    import psutil, uuid
    from gpiozero import CPUTemperature

    cpu_info = str(int(psutil.cpu_percent()))
    ram_info = str(int(psutil.virtual_memory().percent))
    mac_address = str(':'.join(re.findall('..', '%012x' % uuid.getnode())))
    cpu_temp = CPUTemperature(min_temp=50, max_temp=90)
    cpu_temp_info = str(int(cpu_temp.temperature))
    with open('/home/pi/Zumi_Content/README.md', 'r') as zumiContentVersionFile:
        content_version = zumiContentVersionFile.readline().replace("\n", "")
    board_version = str(app.zumi.get_board_firmware_version())

    hardward_info = {"cpu_info": cpu_info, "ram_info": ram_info, "mac_address": mac_address,
                     "cpu_temp": cpu_temp_info, "content_version": content_version, "board_version": board_version}

    socketio.emit('hardware_info', hardward_info)
    socketio.emit('battery_percent', str(app.zumi.get_battery_percent()))

@app.route('/lesson')
def lesson():
    # update_lessonlist_file()
    return app.send_static_file('index.html')

@socketio.on('update_lessonlist_file')
def update_lessonlist_file():
    import json
    print("update lesson json")
    lesson_files_path = "/home/pi/Zumi_Content/Lesson/"
    lesson_file_list = os.listdir(lesson_files_path)
    lesson_file_list.sort()

    lesson_list = []

    lesson_id = 0
    for lesson_name in lesson_file_list:
        if lesson_name != '.ipynb_checkpoints':
            with open(lesson_files_path + lesson_name, 'r') as lesson_file:
                file_content = json.loads(lesson_file.read())
            try:
                description = file_content["cells"][1]["source"][2].split(">")[1].split("<")[0].replace("\n", " ")

                if len(description) > 175:
                    description = description[:175] + "..."
            except:
                description = " "
            lesson_info = {"id": lesson_id, "title": lesson_name[:-6], "description": description}
            lesson_list.append(lesson_info)
            lesson_id = lesson_id + 1

    lesson_list_json = {"LessonList": lesson_list}

    with open('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/LessonList.json', 'w') as lesson_list_file:
        json.dump(lesson_list_json, lesson_list_file)


def firmware_updater_check(base):
    print("checker")
    if not os.path.isdir(base+'update'):
        os.mkdir(base+'update')
    if not os.path.isfile(base+'update/update_log.txt'):
        f = open(base+'update/update_log.txt','w')
        f.close()

    try:
        update_list = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/update_scripts/')
        for line in open(base + 'update/update_log.txt'):
            try:
                update_list.remove(line.rstrip('\n'))
            except:
                pass

    except FileNotFoundError:
        update_list = []

    if len(update_list):
        firmware_updater(update_list)
        return "updated"
    else:
        return "no update"


def firmware_updater(update_list):
    print(update_list)
    update_list.sort()
    print(update_list)
    f = open('/home/pi/Dashboard/update/update_log.txt', 'a')
    for version in update_list:
        print("update {}".format(version))
        p = subprocess.Popen(
            ['sudo', 'sh', os.path.dirname(os.path.abspath(__file__)) + '/update_scripts/'+version, '.'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        stdout, stderr = p.communicate()
        p.wait()
        f.write(version+"\n")

@app.route('/drive')
def drive():
    return app.send_static_file('index.html')

@socketio.on('open_drive_mode')
def open_drive_mode():
    p = subprocess.Popen(
        ['sudo', 'sh', os.path.dirname(os.path.abspath(__file__)) + '/shell_scripts/drivemode.sh', '.'])

@socketio.on('zumi_direction')
def zumi_direction(input_key):
    app.drive_mode.zumi_direction(input_key)

@socketio.on('zumi_stop')
def zumi_stop():
    app.drive_mode.zumi_stop()

@socketio.on('camera_stop')
def drive_mode_camera_stop():
    print('camera should be stopped')
    subprocess.Popen(['fuser', '-k', '3456/tcp'])

def run(_debug=False):
    if not os.path.isfile('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/hostname.json'):
        subprocess.run(["sudo ln -s /etc/hostname /usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/hostname.json"], shell=True)
    firmware_updater_check('/home/pi/Dashboard/')

    socketio.run(app, debug=_debug, host='0.0.0.0', port=80)


if __name__ == '__main__':
    run()
