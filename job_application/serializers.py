# serializers.py

from rest_framework import serializers
from .models import Country, State, Degree, Skill, Registration, Education,Certification, WorkDetails, EmploymentHistory, Award, Industry, Preference

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['user']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        exclude = ['user']

class WorkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDetails
        exclude = ['user']

class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        exclude = ['user']

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        exclude = ['user']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        exclude = ['user']