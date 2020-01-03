from django.contrib import admin

from .models import Group, Person, School, SchoolTerm, Activity, Notification

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(School)
admin.site.register(SchoolTerm)
admin.site.register(Activity)
admin.site.register(Notification)
