from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField

class User(AbstractUser):
    pass
# apartir daqui pode adicionar seus fields personalizado 

class UserProfile(models.Model):

    Marital_Status_Choices = (
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
    )

    School_Level_Choices = (
        ('FI', 'Fundamental Incompleto'),
        ('FC', 'Fundamental Completo'),
        ('MI', 'Médio Incompleto'),
        ('MC', 'Médio Completo'),
        ('SGI', 'Superior Graduação Incompleto'),
        ('SG', 'Superior Graduação Cursando'),
        ('SGC', 'Superior Graduação Completo'),
        ('PGI', 'Pós Graduação Incompleto'),
        ('PG', 'Pós Graduação Cursando'),
        ('PGC', 'Pós Graduação Completo'),
        ('M', 'Mestrado'),
        ('D', 'Doutorado'),
    )

    photo_profile = models.ImageField('Photo', upload_to='photos')
    telephone = models.CharField("Telephone", max_length=11, blank=True, null=True)
    cell = models.CharField("Cell", max_length=11, blank=True, null=True)
    gender = models.CharField("Gender",max_length=250, blank=True, null=True)
    marital_status = models.CharField("Marital Status", max_length=1, choices=Marital_Status_Choices)
    school_level = models.CharField("School Level",  max_length=3, blank=True, null=True, choices=School_Level_Choices)
    occupation = models.CharField("Occupation", max_length=255)
    linkedin = models.CharField("Linkedin", max_length=100, default='#')
    twiter = models.CharField("Twiter", max_length=100, default='#')
    instagram = models.CharField("Instagram", max_length=100, default='#')
    birth = models.DateField()
    description = models.TextField()
    user = models.OneToOneField(
        User,
        related_name="user_profile",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    cpf = BRCPFField("CPF")
    postal_code = BRPostalCodeField("CEP")
    address = models.CharField("Address", max_length=300)
    number = models.CharField("Number", max_length=150)
    complement = models.CharField("Complement", max_length=150, blank=True)
    district = models.CharField("District", max_length=250)
    city = models.CharField("City", max_length=300)
    state = BRStateField("State")

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
        
