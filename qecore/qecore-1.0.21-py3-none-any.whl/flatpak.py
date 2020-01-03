#!/usr/bin/env python3
from os import walk, path
from iniparse import ConfigParser

from qecore import run
from qecore.application import Application

__author__ = """Martin Krajnak <mkrajnak@redhat.com>"""


class Flatpak(Application):
    def __init__(self, flatpak_id, **kwargs):
        """
        Initiate Flatpak instance, inherits Application

        @param flatpak_id : str
            Unique flatpak identifier, mandatory format has 2 dots.
            Param is passed to Application contructor as .component
        """

        if flatpak_id.count(".") != 2:
            raise Exception(
                f"Incorrect flatpak name {flatpak_id}, e.g.: org.gnome.gedit")

        super().__init__(component=flatpak_id, **kwargs)


    def start_via_command(self, command=None, **kwargs):
        """
        Currently the safest and only option to run flatpak due to
            duplicated .desktop files
        """

        command = command or f"flatpak run {self.component}"
        super().start_via_command(command=command, **kwargs)


    def kill_application(self):
        """
        Killing via 'flatpak kill <flatpak_id>', sudo for @system flatpaks
        """

        if self.is_running() and self.kill:
            run(f"sudo flatpak kill {self.component}")


    def get_desktop_file_data(self):
        """
        Provide information from .desktop file, two possible locations:
            1.flatpak installed as --user:
                ~/.local/share/flatpak/app/<flatpak_id>/<arch>/....
            2.flatpak instaled as @system (sudo, root):
                /var/lib/flatpak/app/<flatpak_id>/<arch>/.....
        """

        def get_desktop_file_path(flatpak_dir):
            for root, _, files in walk(flatpak_dir):
                for f in files:
                    if '.desktop' in f:
                        return path.join(root, f)
            return None

        for pth in ['~/.local/share/flatpak/app/', '/var/lib/flatpak/app/']:
            pth = path.expanduser(pth)
            if path.isdir(f'{pth}{self.component}'):
                desktop_file = get_desktop_file_path(f'{pth}{self.component}')
                break

        if not desktop_file:
            raise Exception(f"Desktop file for {self.component} not found.")

        desktop_file_config = ConfigParser()
        desktop_file_config.read(desktop_file)

        self.name = desktop_file_config.get("Desktop Entry", "name")


    def is_running(self):
        """
        Double check if running application is really a flatpak
        """
        return super().is_running() and (self.component in run('flatpak ps'))


    @property
    def start_via_menu(self):
        """
        Since flatpaks .desktop files cannot be distinguished,
        safest option to run flatpak is start_via_command
        """

        raise NotImplementedError("Not available for flatpak objects")


    @property
    def get_pid_list(self):
        """
        Not required, killing via flatpak kill <flatpak_id>
        """

        raise NotImplementedError("Not available for flatpak objects")


    @property
    def get_all_kill_candidates(self):
        """
        Not required, killing via flatpak kill <flatpak_id>
        """

        raise NotImplementedError("Not available for flatpak objects")
