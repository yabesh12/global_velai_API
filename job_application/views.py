from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from job_application.serializers import PreferenceSerializer
from job_application.models import Registration, Country, Industry, Preference, State
from job_application.models import (
    State,
    Country,
    Degree,
    Skill,
    Registration,
    Education,
    Certification,
    WorkDetails,
    EmploymentHistory,
    Award,
    Industry,
    Preference,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, EducationSerializer, CertificationSerializer, WorkDetailsSerializer, EmploymentHistorySerializer, AwardSerializer, PreferenceSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CountrySerializer, StateSerializer, DegreeSerializer, SkillSerializer,
    RegistrationSerializer, EducationSerializer,CertificationSerializer, WorkDetailsSerializer,
    EmploymentHistorySerializer, AwardSerializer, IndustrySerializer, PreferenceSerializer
)
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Certification, Country, Education, State, Degree, Skill, Registration, Education,Certification, WorkDetails, EmploymentHistory, Award, Industry, Preference
from .serializers import RegistrationSerializer, EducationSerializer, CertificationSerializer, WorkDetailsSerializer, EmploymentHistorySerializer, AwardSerializer, IndustrySerializer, PreferenceSerializer




@api_view(['GET'])
def get_all_states(request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_countries(request):
    states = Country.objects.all()
    serializer = CountrySerializer(states, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_degrees(request):
    states = Degree.objects.all()
    serializer = DegreeSerializer(states, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_skills(request):
    states = Skill.objects.all()
    serializer = SkillSerializer(states, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_industries(request):
    states = Industry.objects.all()
    serializer = IndustrySerializer(states, many=True)
    return Response(serializer.data)




@transaction.atomic
@api_view(['POST'])
def process_data(request):
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

        print(work_details_data)
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




# @api_view(['POST'])
# @transaction.atomic
# def process_data(request):
#     try:
#         # Extract data from the request
#         person_details = request.data.get('person_details')
#         education_data = request.data.get('education', [])
#         certifications_data = request.data.get('certifications', [])
#         work_details_data = request.data.get('work_details', {})
#         employment_history_data = request.data.get('employment_history', [])
#         awards_data = request.data.get('awards', [])
#         preferences_data = request.data.get('preferences', {})

#         # Validate and save Registration (Person Details)
#         registration_serializer = RegistrationSerializer(data=person_details)
#         registration_serializer.is_valid(raise_exception=True)
#         user_instance = registration_serializer.save()

#         # Create EducationCertification instances using the user_instance
#         educations = []
#         for education_item in education_data:
#             education_item["user"] = user_instance
#             try:
#                 degree_obj = Degree.objects.get(id=education_item.get("degree"))
#                 education_item["degree"] = degree_obj
#                 education = Education(**education_item)
#                 educations.append(education)
#             except Degree.DoesNotExist:
#                 return Response({"success": False, "error": "Degree not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Use bulk_create to insert all instances into the database
#         Education.objects.bulk_create(educations)

#         # Create Certification instances using the user_instance
#         certifications = []
#         for certification_item in certifications_data:
#             certification_item["user"] = user_instance
#             certification = Certification(**certification_item)
#             certifications.append(certification)
#         # Use bulk_create to insert all instances into the database
#         Certification.objects.bulk_create(certifications)
#         print(certifications)

#         # Create Work details instance using the user_instance
#         try:
#             skill_obj = Skill.objects.get(id=work_details_data.get("skills"))
#         except Degree.DoesNotExist:
#                 return Response({"success": False, "error": "Skill not found"}, status=status.HTTP_400_BAD_REQUEST)

#         work_obj = WorkDetails.objects.create(skills=skill_obj,user=user_instance,
#                                    total_years=work_details_data.get("total_years_of_experience", 0))

        
#         # Create employment details instances using the user_instance
#         # Create EducationCertification instances using the user_instance
#         employment_details = []
#         for employment_item in employment_history_data:
#             employment_item["user"] = user_instance
#             employment_item["work_details"] = work_obj
#             try:
#                 state_obj = State.objects.get(id=employment_item.get("state"))
#                 employment_item["state"] = state_obj
#                 country_obj = Country.objects.get(id=employment_item.get("country"))
#                 employment_item["country"] = country_obj
#                 employment = EmploymentHistory(**employment_item)
#                 employment_details.append(employment)
#             except State.DoesNotExist:
#                 return Response({"success": False, "error": "State not found"}, status=status.HTTP_400_BAD_REQUEST)
#             except Country.DoesNotExist:
#                 return Response({"success": False, "error": "Country not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Use bulk_create to insert all instances into the database
#         EmploymentHistory.objects.bulk_create(employment_details)

#         awards_list = []
#         for award_item in awards_data:
#             award_item["user"] = user_instance        
#             award = Award(**award_item)
#             awards_list.append(award)

#         # Use bulk_create to insert all instances into the database
#         Award.objects.bulk_create(awards_list)

#         # Create Preference instance
#         preference = Preference.objects.create(
#             user=user_instance,
#             position=preferences_data.get("position"),
#             available_from=preferences_data.get("available_from"),
#             salary_expectation=preferences_data.get("salary_expectation"),
#             has_passport = preferences_data.get("has_passport")
#         )
#         print(f"Preferences - {preference}")

#         # Add countries to the Preference instance
#         for preferences_country in preferences_data.get("countries"):
#             try:
#                 country_obj = Country.objects.get(id=preferences_country.get("country"))
#                 preference.countries.add(country_obj)
#             except Country.DoesNotExist:
#                 return Response({"success": False, "error": "Country not found"}, status=status.HTTP_400_BAD_REQUEST)

#         # Add industries to the Preference instance
#         for preferences_industry in preferences_data.get("industries"):
#             try:
#                 industry_obj = Industry.objects.get(id=preferences_industry.get("industry"))
#                 preference.industries.add(industry_obj)
#             except Industry.DoesNotExist:
#                 return Response({"success": False, "error": "Industry not found"}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({"success": True, "message": "Data processed and saved successfully."}, status=status.HTTP_201_CREATED)

#     except Exception as e:
#         return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
