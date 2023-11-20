# models.py

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+ " - " +self.name 

    class Meta:
        verbose_name_plural = "Countries"

class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + " - " + self.name 

    class Meta:
        verbose_name_plural = "States"

class Degree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+ " - " +self.name 

    class Meta:
        verbose_name_plural = "Degrees"

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+ " - " +self.name 

    class Meta:
        verbose_name_plural = "Skills"

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='users_state', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='users_country', blank=True, null=True)


    def __str__(self):
        return self.first_name + str(self.id)
    

class Education(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='educations')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    year_of_passing = models.IntegerField()
    school = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} - {self.degree.name}"+ str(self.id)
    
class Certification(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='certifications')
    certification_name = models.CharField(max_length=255)
    year_of_certification = models.IntegerField()
    def __str__(self):
        return f"{self.user.first_name} - {self.certification_name}"+ str(self.id)
    

class WorkDetails(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='work_details')
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    total_years = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 21)])

    def __str__(self):
        return f"{self.user.first_name} - {self.skills.name}"+ str(self.id)

class EmploymentHistory(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='employment_details')
    work_details = models.ForeignKey(WorkDetails, on_delete=models.CASCADE, related_name='employment_histories')
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.work_details.user.first_name} - {self.job_title}"+ str(self.id)

class Award(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='awards')
    award_name = models.CharField(max_length=255)
    awarding_organization = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} - {self.award_name}"+ str(self.id)

class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+ " - " +self.name 

    class Meta:
        verbose_name_plural = "Industries"

class Preference(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='preferences')
    countries = models.ManyToManyField(Country, blank=True)
    industries = models.ManyToManyField(Industry, blank=True)
    position = models.CharField(max_length=255)
    available_from = models.DateField(null=True, blank=True)
    has_passport = models.BooleanField(default=False)
    salary_expectation = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.position}" + str(self.id)
