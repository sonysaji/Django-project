
from django.db import models
class registration(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=200)


class studentregistration(models.Model):
    admission_no=models.CharField(max_length=200)
    admission_date=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    dob=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    guardian=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    

class attendances(models.Model):

    student_name=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    status_h1=models.CharField(max_length=200)
    status_h2=models.CharField(max_length=200)
    status_h3=models.CharField(max_length=200)
    status_h4=models.CharField(max_length=200)
    status_h5=models.CharField(max_length=200)
class marksubmit(models.Model):
    student_name=models.CharField(max_length=200)
    assess_no=models.CharField(max_length=200)
    max_mark=models.CharField(max_length=200)
    subject_1=models.CharField(max_length=200)
    subject_2=models.CharField(max_length=200)
    subject_3=models.CharField(max_length=200)
    subject_4=models.CharField(max_length=200)
    subject_5=models.CharField(max_length=200)
class fac_leave_management(models.Model):
    leave_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    from_date=models.CharField(max_length=200)
    To_date=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
class stu_leave_management(models.Model):
    leave_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    from_date=models.CharField(max_length=200)
    To_date=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
class admin(models.Model):
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
class meta:
    db_name='registration'
    


    
# Create your models here.
