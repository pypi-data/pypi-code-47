import subprocess


def set_sound_device(name):
    script = 'reset\nset _verb HiFi\nset _enadev {}\n'.format(name)
    subprocess.run(['alsaucm', '-b', '-'], input=script, timeout=10, encoding='utf-8')


def set_volume(control, level):
    subprocess.run(['amixer', 'set', control, level])


def speaker_test(channels=1):
    subprocess.run(['speaker-test', '-c', str(channels), '-t', 'wav', '-s', '1'])


def test_earpiece():
    set_sound_device('Earpiece')
    set_volume('Earpiece', '100%')
    speaker_test(1)


def test_headphones():
    set_sound_device('Headphone')
    set_volume('Headphone', '50%')
    speaker_test(2)
