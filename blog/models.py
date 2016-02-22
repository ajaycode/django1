from django.db import models
from django.utils import timezone

# Create your models here.
class Post (models.Model):
    author = models.ForeignKey('auth.User')
    title  = models.CharField (max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField (default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish (self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title, self.created_date

class Person (models.Model):
    GENDER_CHOICES     = ( ('M', 'Male'),('F', 'Female'), ('D', 'Decline To State'))
    ACCOUNT_STATUS             = (('Y', "Yes"), ('N', "No"))

    first_name = models.CharField (max_length=50)
    last_name  = models.CharField (max_length=50)
    nickname   = models.CharField (max_length=50, blank=True)
    #given_name
    date_of_birth        = models.DateField (blank=True, null=True)
    time_of_birth        = models.TimeField (blank=True, null=True)
    #place_of_birth       = models.CharField (max_length=100, blank=True, null=True)
    #country_of_birth     = models.CharField (max_length=100, blank=True, null=True)
    #date_of_death        = models.DateField (blank=True, null=True)
    #place_of_death       = models.CharField (max_length=100 , blank=True, null=True)
    #country_of_death     = models.CharField (max_length=100, blank=True, null=True)

    #city       = models.CharField (max_length=50, blank=True)
    #country    = models.CharField (max_length=50, blank=True)
    gender     = models.CharField('Gender',max_length=2, choices=GENDER_CHOICES)
    parents    = models.ForeignKey('Family', verbose_name='Parents', null=True, blank=True)
    spouse     = models.ForeignKey('Person', verbose_name='Spouse', null=True, blank=True)
    email      = models.EmailField (blank=True)
    password   = models.CharField (max_length=50, blank=True, null=True)
    #user_is_confirmed = models.CharField ('User Status', max_length=2, blank=True, null=True,choices=ACCOUNT_STATUS)
    #twitter_handle = models.CharField(max_length=50,  blank=True, null=True)
    #linkedin_handle = models.URLField(max_length=100, blank=True, null=True)
    #facebook_profile_url = models.URLField (max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.__unicode__()

class Family (models.Model):
    husband     = models.ForeignKey(Person, verbose_name='Father', related_name='fk_husband', null=True, blank=True)
    wife     = models.ForeignKey(Person, verbose_name='Mother', related_name='fk_wife', null=True, blank=True)
    #spouse     = models.ForeignKey(Person, verbose_name='Spouse', related_name='fk_spouse', null=True, blank=True)
    date_of_marriage = models.DateField (blank=True, null=True)
    place_of_marriage = models.CharField (max_length=100,blank=True, null=True)
    date_of_divorce   = models.DateField (blank=True, null=True)

    def __unicode__(self):
        return self.father

    class Meta:
        verbose_name = 'family'
        verbose_name_plural = 'families'

class Education (models.Model):
    EDUCATION_LEVEL = ( ('S', 'School'),('I', 'Intermediate (+2)'), ('U', 'Undergraduate Degree'), ('P', 'Post Graduate Degree'), \
             ('PhD', 'Doctor of Philosophy'), ('D', 'Diploma'), ('NA', "Not Available"))
    #View the person's education by p = Person.objects.all()[0].his_education.all()  - to get all of his/her records
    person = models.ForeignKey (Person, verbose_name='Person', related_name='his_education' ,null=True, blank=True)
    start_year = models.PositiveIntegerField ()
    end_year = models.PositiveIntegerField ()
    education_level = models.CharField (max_length=3, blank=True, null=True, choices=EDUCATION_LEVEL)
    specialization = models.CharField (max_length=100, blank=True, null=True)
    institution = models.CharField (max_length=100, blank=True, null=True)
    place = models.CharField (max_length=100, blank=True)

    def __unicode__(self):
        return self.specialization

    class Meta:
        verbose_name = 'education'
        verbose_name_plural = 'education'
