from django.urls import path
from job_application.views import get_all_states, get_all_countries,get_all_degrees,get_all_skills,get_all_industries, process_data

urlpatterns = [
    path('job-applications/', process_data, name='process_data'),
    path('states/', get_all_states, name='get_all_states'),
    path('countries/', get_all_countries, name='get_all_countries'),
    path('degrees/', get_all_degrees, name='get_all_degrees'),
    path('skills/', get_all_skills, name='get_all_skills'),
    path('industries/', get_all_industries, name='get_all_industries'),
    
]