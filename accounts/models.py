from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.timezone import now
class UserManager(BaseUserManager):
    
    def create_user(self,email,password,**extrafields): 
        if not email:
            raise ValueError(_("The Email must be set"))
        email=self.normalize_email(email=email)
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,password,**extrafields):
        user=self.create_user(email,password,**extrafields)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
        
     
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_("email address"), max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=now)
    
    
    objects=UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]
    
    def __str__(self) :
        return self.email
    
class PatientFamily(models.Model):
    parent=models.OneToOneField("Patient", null=True,blank=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.parent.full_name

    


class Patient(models.Model):
    patient_Family=models.ForeignKey(PatientFamily,on_delete=models.DO_NOTHING ,blank=True,null=True)
    email=models.OneToOneField(User, on_delete=models.DO_NOTHING,null=True ,blank=True)
    first_name=models.CharField( max_length=10)
    last_name=models.CharField(max_length=10)
    phone1=models.CharField(max_length=15)
    phone2=models.CharField(max_length=15)
    date_examination=models.DateTimeField( default=now)
    birth_day=models.DateField()
    create_date=models.DateTimeField(default=now)
    is_examined=models.BooleanField(default=False)
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name


#create family for each patient no has parent
def create_family_user_signal(sender, instance, created, **kwargs):
    if created and not(instance.patient_Family):
        PatientFamily.objects.create(parent=instance)

post_save.connect(create_family_user_signal,sender=Patient)



class Doctor(models.Model):
    doc_email=models.OneToOneField(User, verbose_name=_("doctor"),blank=True,null=True,on_delete=models.DO_NOTHING)
    first_name=models.CharField( max_length=10)
    last_name=models.CharField(max_length=10)    
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name

class Employee(models.Model):
    emp_email=models.OneToOneField(User, verbose_name=_("doctor"),blank=True,null=True,on_delete=models.DO_NOTHING)
    first_name=models.CharField( max_length=10)
    last_name=models.CharField(max_length=10)    
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name



# class FamilyAccounts(models.Model):    
#     relationtype=(
#         'father',
#         'mother',
#         'son',
#         'daughter',
#     )
#     parent=models.ForeignKey(User, verbose_name=_("responsible for the family"), on_delete=models.DO_NOTHING)
#     member=models.ForeignKey(User, verbose_name=_("one of the family"), on_delete=models.DO_NOTHING)
#     relation_type=models.CharField(_("type of relation"), max_length=50,choices=relationtype)
    
 
