import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'pym2149',
        version = '6',
        description = 'YM2149 emulator supporting YM files, OSC, MIDI to JACK, PortAudio, WAV',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/pym2149',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = ['bpmtool', 'lc2txt', 'ym2portaudio', 'lc2wav', 'dosound2jack', 'midi2wav', 'ym2wav', 'dosound2wav', 'ym2txt', 'dosound2txt', 'ym2jack', 'midi2jack', 'dsd2wav', 'lc2jack'],
        install_requires = ['mock', 'pyaudio', 'pillow', 'pyrbo', 'diapyr', 'aridity', 'outjack', 'mynblep', 'lagoon', 'splut', 'timelyOSC', 'pyven', 'Lurlene'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = ['bpmtool.py', 'lc2txt.py', 'ym2portaudio.py', 'lc2wav.py', 'dosound2jack.py', 'midi2wav.py', 'ym2wav.py', 'dosound2wav.py', 'ym2txt.py', 'dosound2txt.py', 'ym2jack.py', 'midi2jack.py', 'dsd2wav.py', 'lc2jack.py'])
