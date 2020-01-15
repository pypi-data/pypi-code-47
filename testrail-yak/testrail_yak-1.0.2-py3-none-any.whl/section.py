#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import TestRailException, ValidationException
import time


class SectionException(TestRailException):
    pass


class SectionValidationException(ValidationException):
    pass


class Section:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_sections(self, project_id, suite_id=None):
        """Get a list of test sections associated with a project_id and an optional suite_id

        :param project_id:
        :param suite_id:
        :return: response from TestRail API containing the collection of sections
        """
        if not project_id or project_id is None:
            raise SectionValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise SectionValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise SectionValidationException("[*] project_id must be > 0")

        result = None
        if suite_id is not None:
            if type(suite_id) not in [int, float]:
                raise SectionValidationException("[*] suite_id must be an int or float")

            if suite_id <= 0:
                raise SectionValidationException("[*] suite_id must be > 0")

            try:
                result = self.client.send_get("get_sections/{}&suite_id={}".format(project_id, suite_id))
            except SectionException:
                print("[!] Failed to get sections. Retrying")
                time.sleep(3)
                try:
                    result = self.client.send_get("get_sections/{}&suite_id={}".format(project_id, suite_id))
                except SectionException:
                    print("[!] Failed to get sections.")

        else:
            try:
                result = self.client.send_get("get_sections/{}".format(project_id))
            except SectionException:
                print("[!] Failed to get sections. Retrying")
                time.sleep(3)
                try:
                    result = self.client.send_get("get_sections/{}".format(project_id))
                except SectionException:
                    print("[!] Failed to get sections.")

        return result

    def get_section(self, section_id):
        """Get test section from a test suite by section_id.

        :param section_id: section ID to grab section from
        :return: response from TestRail API containing the test section
        """
        if not section_id or section_id is None:
            raise SectionValidationException("[*] Invalid section_id")

        if type(section_id) not in [int, float]:
            raise SectionValidationException("[*] section_id must be an int or float")

        if section_id <= 0:
            raise SectionValidationException("[*] section_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_section/{}".format(section_id))
        except SectionException:
            print("[!] Failed to get test section by ID. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_section/{}".format(section_id))
            except SectionException:
                print("[!] Failed to get test section by ID.")
        finally:
            return result

    def add_sprint_section(self, project_id, name, description=None, suite_id=None):
        """Add a new section representing a "sprint" to a TestRail project.

        For readability, this separate method is just for adding parent sections (Jira sprints) vs child sections (Jira stories).

        To populate a new child section with a Jira story, use add_story_section() and give it the id value returned here.

        :param project_id: project ID of the TestRail project
        :param name: name of the new TestRail test section
        :param description: description of the test section
        :param suite_id: suite ID of the test suite. This is ignored if the project is operating in single suite mode (suite_mode=1), required otherwise.
        :return: response from TestRail API containing the newly created test section
        """
        if suite_id is not None:
            raise NotImplementedError("Not currently using suite_id in this call")

        if not project_id or project_id is None:
            raise SectionValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise SectionValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise SectionValidationException("[*] project_id must be > 0")

        if not name or name is None:
            raise SectionValidationException("[*] Name field is required")

        sect_data = dict(
            name=name,
            description=description,
        )

        result = None
        try:
            result = self.client.send_post("add_section/{}".format(project_id), sect_data)
        except SectionException:
            print("[!] Failed to add new section for the current sprint. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_section/{}".format(project_id), sect_data)
            except SectionException:
                print("[!] Failed to add section.")
        finally:
            return result

    def add_story_section(self, project_id, parent_id, name, description=None):
        """Add a new section representing a "story" to a TestRail project.

        This section will be assigned to a parent/child relationship with a parent section, thus parent_id is required.

        Use the id value returned by add_sprint_section as the parent_id.

        Because of this parent id requirement, no suite_id will be needed. If it is ever used in the future, add_sprint_section is the more appropriate place for it.

        :param project_id: project ID of the TestRail project
        :param name: name of the new TestRail test section
        :param description: description of the test section
        :param parent_id: section ID of the parent section (to build section hierarchies)
        :return: response from TestRail API containing the newly created test section
        """
        if not project_id or project_id is None:
            raise SectionValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise SectionValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise SectionValidationException("[*] project_id must be > 0")

        if not name or name is None:
            raise SectionValidationException("[*] Name field is required")

        sect_data = dict(
            parent_id=parent_id,
            name=name,
            description=description,
        )

        result = None
        try:
            result = self.client.send_post("add_section/{}".format(project_id), sect_data)
        except SectionException:
            print("[!] Failed to add new section for the current Jira story. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_section/{}".format(project_id), sect_data)
            except SectionException:
                print("[!] Failed to add section.")
        finally:
            return result
