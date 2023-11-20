from rest_framework.response import Response
from rest_framework.decorators import api_view
from job_application.serializers import PreferenceSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CountrySerializer, StateSerializer, DegreeSerializer, SkillSerializer,
    RegistrationSerializer, EducationSerializer,CertificationSerializer, WorkDetailsSerializer,
    EmploymentHistorySerializer, AwardSerializer, IndustrySerializer, PreferenceSerializer
)
from django.db import transaction
from .models import Certification, Country, Education, State, Degree, Skill, Registration, Education,Certification, WorkDetails, EmploymentHistory, Award, Industry, Preference
from .serializers import RegistrationSerializer, EducationSerializer, CertificationSerializer, WorkDetailsSerializer, EmploymentHistorySerializer, AwardSerializer, IndustrySerializer, PreferenceSerializer



@api_view(['GET'])
def get_all_states(request):
    """
    Get a list of all states.

    Returns:
        Response: List of serialized state data.
    """
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_countries(request):
    """
    Get a list of all countries.

    Returns:
        Response: List of serialized country data.
    """
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_degrees(request):
    """
    Get a list of all degrees.

    Returns:
        Response: List of serialized degree data.
    """
    degrees = Degree.objects.all()
    serializer = DegreeSerializer(degrees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_skills(request):
    """
    Get a list of all skills.

    Returns:
        Response: List of serialized skill data.
    """
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_industries(request):
    """
    Get a list of all industries.

    Returns:
        Response: List of serialized industry data.
    """
    industries = Industry.objects.all()
    serializer = IndustrySerializer(industries, many=True)
    return Response(serializer.data)


@transaction.atomic
@api_view(['POST'])
def process_data(request):
    """
    Process user registration data.

    Args:
        request (Request): HTTP request object containing user registration data.

    Returns:
        Response: JSON response indicating success or failure.
    """
    try:
        # Extract data from the request
        person_details = request.data.get('person_details')
        education_data = request.data.get('education', [])
        certifications_data = request.data.get('certifications', [])
        work_details_data = request.data.get('work_details', {})
        employment_history_data = request.data.get('employment_history', [])
        awards_data = request.data.get('awards', [])
        preferences_data = request.data.get('preferences', {})

        # Validate and save Registration (Person Details)
        registration_serializer = RegistrationSerializer(data=person_details)
        registration_serializer.is_valid(raise_exception=True)
        user_instance = registration_serializer.save()

        # Serialize and save Education instances using the user_instance
        education_serializer = EducationSerializer(data=education_data, many=True)
        education_serializer.is_valid(raise_exception=True)
        education_serializer.save(user=user_instance)

        # Serialize and save Certification instances using the user_instance
        certification_serializer = CertificationSerializer(data=certifications_data, many=True)
        certification_serializer.is_valid(raise_exception=True)
        certification_serializer.save(user=user_instance)

        # Serialize and save WorkDetails instance using the user_instance
        work_details_serializer = WorkDetailsSerializer(data=work_details_data)
        work_details_serializer.is_valid(raise_exception=True)
        work_details_instance = work_details_serializer.save(user=user_instance)

        # Serialize and save EmploymentHistory instances using the user_instance
        employment_history_serializer = EmploymentHistorySerializer(data=employment_history_data, many=True)
        employment_history_serializer.is_valid(raise_exception=True)

        # Save the WorkDetails instance before passing it to EmploymentHistorySerializer
        employment_history_serializer.save(user=user_instance, work_details=work_details_instance)

        # Serialize and save Award instances using the user_instance
        award_serializer = AwardSerializer(data=awards_data, many=True)
        award_serializer.is_valid(raise_exception=True)
        award_serializer.save(user=user_instance)

        # Serialize and save Preference instance using the user_instance
        preference_serializer = PreferenceSerializer(data=preferences_data)
        preference_serializer.is_valid(raise_exception=True)
        preference_serializer.save(user=user_instance)

        return Response({"success": True, "message": "User registered successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)