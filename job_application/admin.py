# admin.py

from django.contrib import admin
from .models import Country, Registration, State, Degree, Skill, Education, Certification, WorkDetails, EmploymentHistory, Award, Preference, Industry

class EducationInline(admin.StackedInline):
    model = Education

class CertificationInline(admin.StackedInline):
    model = Certification

class WorkDetailsInline(admin.StackedInline):
    model = WorkDetails

class EmploymentHistoryInline(admin.StackedInline):
    model = EmploymentHistory

class AwardInline(admin.StackedInline):
    model = Award

class PreferenceInline(admin.StackedInline):
    model = Preference

class ApplicationsAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline,
        CertificationInline,
        WorkDetailsInline,
        EmploymentHistoryInline,
        AwardInline,
        PreferenceInline,
    ]

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Degree)
admin.site.register(Skill)
admin.site.register(Industry)
admin.site.register(Registration, ApplicationsAdmin)