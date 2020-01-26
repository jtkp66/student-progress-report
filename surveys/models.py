from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Survey(models.Model):
    # Student Progress Report
    coordinator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_complete = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    stdate = models.CharField(max_length=20)
    stcoord = models.CharField(max_length=100)
    stsurname = models.CharField(max_length=100)
    sthost = models.CharField(max_length=100)
    stname = models.CharField(max_length=50)
    st1 = models.CharField(max_length=20)
    st1a = models.TextField(blank=True)
    st2 = models.TextField(blank=True)
    st3 = models.TextField(blank=True)
    st4 = models.CharField(max_length=10)
    st4a = models.TextField(blank=True)
    st4b = models.TextField(blank=True)
    st5 = models.CharField(max_length=10)
    st5a = models.TextField(blank=True)
    st6 = models.CharField(max_length=20)
    st6a = models.TextField(blank=True)
    st6b = models.TextField(blank=True)
    st7 = models.CharField(max_length=10)
    st7a = models.CharField(max_length=10)
    st7b = models.TextField(blank=True)
    stcomments = models.TextField(blank=True)

    # Host Family Progress Report
    hfname = models.CharField(max_length=100)
    hf1 = models.CharField(max_length=20)
    hf1a = models.TextField(blank=True)
    hf2 = models.TextField(blank=True)
    hf3 = models.CharField(max_length=10)
    hf3a = models.TextField(blank=True)
    hf3b = models.TextField(blank=True)
    hf4 = models.CharField(max_length=10)
    hf4a = models.TextField(blank=True)
    hf4b = models.TextField(blank=True)
    hf5 = models.CharField(max_length=10)
    hf5a = models.TextField(blank=True)
    hf6 = models.CharField(max_length=10)
    hf6a = models.TextField(blank=True)
    hf7 = models.CharField(max_length=20)
    hf7a = models.TextField(blank=True)
    hfcomments = models.TextField(blank=True)

    # School Progress Report
    schname = models.CharField(max_length=50)
    schstudent = models.CharField(max_length=100)
    sch1a = models.CharField(max_length=100)
    sch1b = models.TextField(blank=True)
    sch2 = models.CharField(max_length=20)
    sch2a = models.TextField(blank=True)
    sch3 = models.CharField(max_length=10)
    sch3a = models.TextField(blank=True)
    sch4 = models.CharField(max_length=10)
    sch4a = models.IntegerField(default=0)
    sch4b = models.CharField(max_length=10)
    sch4c = models.TextField(blank=True)
    sch5 = models.CharField(max_length=10)
    sch5a = models.CharField(max_length=100)
    sch6 = models.CharField(max_length=10)
    sch6a = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.stcoord
