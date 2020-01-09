import setuptools

setuptools.setup(
        name = 'pomodoro-timer',
        packages=['pomodoro-timer'],
        version = '0.1.1',
        license='MIT',
        description='A pomodoro timer with sound and notification window using the python curses library.',
        author = 'laeri',
        author_email = 'lars.wuethrich@hotmail.com',
        url = 'https://github.com/laeri/pomodoro-timer',
        download_url= 'https://github.com/laeri/pomodoro-timer/archive/v_0.1.3.tar.gz',
        keywords = ['pomodoro', 'timer', 'pomodoro-timer'],
        install_requires=[
            'simpleaudio'],
        package_data={'':['sounds/*']},
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 3 - Alpha',
            'Intended Audience :: End Users/Desktop',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7']
)
