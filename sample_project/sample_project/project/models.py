from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()


class Client(models.Model):
    """
    Model to store Client details.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Client Name"))

    class Meta:
        db_table = "client"

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Model to store Project details.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Project Name"))
    description = models.CharField(max_length=200, verbose_name=_("Project Description"))
    icon = models.URLField(verbose_name=_("Project Icon"))
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name=_("Project Client"))
    project_manager = models.ForeignKey(User, on_delete=models.PROTECT, related_name="project_manager",
                                        verbose_name=_("Project Manager"))
    members = models.ManyToManyField(User, verbose_name=_("Project Members"))

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name
