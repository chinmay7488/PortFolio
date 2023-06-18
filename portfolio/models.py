from django.db import models

# Create your models here.
class Skill(models.Model):
    SKILL_PRIORITY = (
        ('1', 'LOW'),
        ('2', 'MEDIUM'),
        ('3', 'HIGH'),
    )

    Skill_Name = models.CharField(max_length=50,blank=False)
    Skill_priority  = models.CharField(max_length=10, choices=SKILL_PRIORITY,blank=False)
    Skill_Image = models.ImageField(upload_to='skill_image',blank=False)

    def __str__(self):
        return self.Skill_Name


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=150,blank=False)
    institute_name  = models.CharField(max_length=100,blank=False)
    completion_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=False)

    def __str__(self):
        return self.certificate_name