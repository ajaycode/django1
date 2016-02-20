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
    first_name = models.CharField (max_length=50)
    last_name  = models.CharField (max_length=50)
    nickname   = models.CharField (max_length=50, blank=True)
    #given_name
    dob        = models.DateField (blank=True, null=True)
    #tob        = models.TimeField (blank=True)
    email      = models.EmailField (blank=True)
    city       = models.CharField (max_length=50, blank=True)
    country    = models.CharField (max_length=50, blank=True)
    gender     = models.CharField('Gender',max_length=2, choices=GENDER_CHOICES)
    parents    = models.ForeignKey('Family', verbose_name='Parents', null=True, blank=True)
    spouse     = models.ForeignKey('Person', verbose_name='Spouse', null=True, blank=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.__unicode__()

class Family (models.Model):
    father     = models.ForeignKey(Person, verbose_name='Father', related_name='fk_father', null=True, blank=True)
    mother     = models.ForeignKey(Person, verbose_name='Mother', related_name='fk_mother', null=True, blank=True)
    spouse     = models.ForeignKey(Person, verbose_name='Spouse', related_name='fk_spouse', null=True, blank=True)

    def __unicode__(self):
        return self.father

    class Meta:
        verbose_name = 'family'
        verbose_name_plural = 'families'
