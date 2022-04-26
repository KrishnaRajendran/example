from django.db import models
from django.utils.translation import gettext_lazy as _
from sample_project.project import models as project_models
from sample_project.question import models as question_models


# Create your models here.
class FeedbackSectionChoices(models.IntegerChoices):
    """
    Choices for the type field of FeedbackSection model.
    """

    PROJECT = (0, _("Project"))
    TEAM_MEMBER = (1, _("Team Member"))
    PROJECT_MANAGER = (2, _("Project Manager"))
    CLIENT = (3, _("Client"))


class FeedbackSection(models.Model):
    """
    Model to store Feedback Section details
    """
    description = models.CharField(max_length=250, verbose_name=_("Section Description"))
    type = models.PositiveSmallIntegerField(choices=FeedbackSectionChoices.choices, verbose_name=_("Section Type"))
    questions = models.ManyToManyField(question_models.Question, verbose_name=_("Related Questions"))

    class Meta:
        db_table = "feedback_section"

    def __str__(self):
        return "Feedback Section - %s" % (self.get_type_display())


class Feedback(models.Model):
    """
    Model to store Feedback details
    """
    description = models.CharField(max_length=250, verbose_name=_("Feedback Description"))
    projects = models.OneToOneField(project_models.Project, on_delete=models.CASCADE, verbose_name=_("Related Project"))
    sections = models.ManyToManyField(FeedbackSection, verbose_name=_("Feedback Sections"))
    is_completed = models.BooleanField(default=False, verbose_name=_("Feedback Completed"))
    start_date = models.DateField(auto_now_add=True, verbose_name=_("Feedback Start Date"))
    end_date = models.DateField(verbose_name=_("Feedback End Date"))

    class Meta:
        db_table = "feedback"

    def __str__(self):
        return "Feedback - %s" % self.projects.name


class Template(models.Model):
    """
    Model to store Template details
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Template Name"))
    sections = models.ManyToManyField(FeedbackSection, verbose_name=_("Feedback Sections"))

    class Meta:
        db_table = "template"

    def __str__(self):
        return self.name
