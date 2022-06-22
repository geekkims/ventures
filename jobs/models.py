from django.db import models
import uuid
from django_countries.fields import CountryField
from django.urls import reverse



# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=25)


    def __str__(self):
        return self.title


class Industry(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1024*2, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255,null=True, blank=True)
    active = models.BooleanField(default=False)  
    created_date = models.DateField(auto_now=True,blank=True, null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True, null=True) 

    def __str__(self):
        return str(self.title)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(**kwargs)

    class Meta:
        verbose_name = "Job Industry"
        verbose_name_plural = "Job Industry"

class Company(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1024*2, blank=True, null=True)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE,blank=True,null=True,related_name="company_industry")
    since = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    team_size = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False) 
    slug = models.SlugField(unique=True, max_length=255,null=True, blank=True)
    created_date = models.DateField(auto_now=True,blank=True, null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True, null=True) 

    def __str__(self):
        return str(self.title)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super().save(**kwargs)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"



class Categories(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1024*2, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255,null=True, blank=True)
    active = models.BooleanField(default=False)  
    created_date = models.DateField(auto_now=True,blank=True, null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True, null=True) 

    def __str__(self):
        return str(self.title)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(**kwargs)

    class Meta:
        verbose_name = "Job Categories"
        verbose_name_plural = "Job Categories"



class Jobs(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True,related_name="company")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1024*2, blank=True, null=True)
    categories = models.ManyToManyField(Categories,blank=True,related_name="job_category")
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE,blank=True,null=True,related_name="job_industry")
    slug = models.SlugField(unique=True, max_length=255,null=True, blank=True)
    active = models.BooleanField(default=False) 
    salary = models.PositiveIntegerField(default=0, blank=True, null=True) 
    positions = models.PositiveIntegerField(default=0, blank=True, null=True)
    application_deadline = models.DateField(auto_now=False,blank=True, null=True)
    country = CountryField(blank_label='(select country)',blank=True, null=True)
    remote = models.BooleanField(default=False)
    schedule = models.BooleanField(default=False)
    created_date = models.DateField(auto_now=True,blank=True, null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True, null=True) 

    def __str__(self):
        return str(self.title)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(**kwargs)

  

    def get_absolute_url(self):
        return reverse("home", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = "Jobs"
        verbose_name_plural = "Jobs"

