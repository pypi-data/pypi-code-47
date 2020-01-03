import re


class UserInformation:
    OTHER = 0
    TEACHER = 1
    STUDENT = 2

    @staticmethod
    def regexr(regex, groups):
        reg = re.compile(regex)
        return reg.findall("\n".join(groups))

    @staticmethod
    def user_groups(user):
        raw_groups = user.groups.all()
        groups = [group.name for group in raw_groups]
        # print(groups)
        return groups

    @staticmethod
    def user_type(user):
        groups = UserInformation.user_groups(user)
        if "teachers" in groups:
            return UserInformation.TEACHER
        elif "students" in groups:
            return UserInformation.STUDENT
        else:
            return UserInformation.OTHER

    @staticmethod
    def _user_type_formatted(user_type):
        return "Lehrer" if user_type == UserInformation.TEACHER else (
            "Schüler" if user_type == UserInformation.STUDENT else "Sonstiges Mitglied")

    @staticmethod
    def user_type_formatted(user):
        user_type = UserInformation.user_type(user)
        return UserInformation._user_type_formatted(user_type)

    @staticmethod
    def user_classes(user):
        groups = UserInformation.user_groups(user)
        classes = UserInformation.regexr(r"class_(\w{1,3})", groups)
        return classes

    @staticmethod
    def user_courses(user):
        groups = UserInformation.user_groups(user)
        classes = UserInformation.regexr(r"course_(.{1,10})", groups)
        return classes

    @staticmethod
    def user_subjects(user):
        groups = UserInformation.user_groups(user)
        classes = UserInformation.regexr(r"subject_(\w{1,3})", groups)
        return classes

    @staticmethod
    def user_has_wifi(user):
        groups = UserInformation.user_groups(user)
        if "teachers" in groups or "students-wifi" in groups:
            return True
        return False
