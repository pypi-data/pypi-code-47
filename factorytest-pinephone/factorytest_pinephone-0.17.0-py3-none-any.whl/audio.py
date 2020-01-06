import subprocess


def set_sound_device(name):
    script = 'reset\nset _verb HiFi\nset _enadev {}\n'.format(name)
    subprocess.run(['alsaucm', '-b', '-'], input=script, timeout=10, encoding='utf-8')


def test_earpiece():
    set_sound_device('Earpiece')
    subprocess.run('amixer set Earpiece 100%')
    subprocess.run('speaker-test -c 1 -t wav -s 1')


def test_headphones():
    set_sound_device('Headphone')
    subprocess.run('amixer set Headphone 50%')
    subprocess.run('speaker-test -c 2 -t wav -s 1')
