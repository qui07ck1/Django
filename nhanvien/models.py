from django.db import models

# Create your models here.

class sex_choice(models.IntegerChoices):
    Male = 1,"Nam"
    Fmale = 0, "Nữ"
    
class Marry_choice(models.IntegerChoices):
    Marry = 1,"Yes"
    UnMarry = 0, "No"
    
    

class nhanvien(models.Model):
    section_code = models.CharField(max_length=255)
    emp_no = models.IntegerField()
    english_name = models.CharField(max_length=255)
    emp_name = models.CharField(max_length=255)
    sex = models.IntegerField(choices=sex_choice.choices)
    marry = models.IntegerField(choices=Marry_choice.choices)
    position_name = models.CharField(max_length=255)
    grade_code = models.CharField(max_length=255)
    join_date = models.DateField()
    id_no = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.emp_name