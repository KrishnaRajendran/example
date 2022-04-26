from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Team(models.Model):
    """
    Model to store the Team details.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Team Name"))

    class Meta:
        db_table = "team"

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Model to store the Department details.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Department Name"))
    team = models.ManyToManyField(Team, related_name="departments_teams", verbose_name="Department Teams")

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.name


class Designation(models.Model):
    """
    Model to store the Designation details.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Designation Name"))

    class Meta:
        db_table = "designation"

    def __str__(self):
        return self.name
