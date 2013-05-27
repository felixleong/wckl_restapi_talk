from django.db import models
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField)


class FundHouse(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Fund(models.Model):
    fund_house = models.ForeignKey(FundHouse)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Price(models.Model):
    fund = models.ForeignKey(Fund)
    date = models.DateField()
    nav = models.DecimalField(max_digits=6, decimal_places=4)

    def __unicode__(self):
        return u'{0} - {1}: {2}'.format(self.fund, self.date, self.nav)


class Annotation(models.Model):
    price = models.ForeignKey(Price)
    time_added = CreationDateTimeField()
    time_modified = ModificationDateTimeField()
    note = models.TextField()
