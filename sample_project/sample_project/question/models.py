from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class OptionChoice(models.Model):
    """
    Model to store Option Choice details
    """
    order = models.PositiveSmallIntegerField(verbose_name=_("Option Choice Order"))
    value = models.CharField(max_length=100, unique=True, verbose_name=_("Option Choice Value"))

    class Meta:
        db_table = "option_choice"
        ordering = ["order"]

    def __str__(self):
        return self.value


class OptionGroup(models.Model):
    """
    Model to store Option Group details
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Option Group Name"))
    options = models.ManyToManyField(OptionChoice, verbose_name=_("List of Option Choices"))

    class Meta:
        db_table = "option_group"

    def __str__(self):
        return self.name


class CoreValue(models.Model):
    """
    Model to store Core Value details
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Core Value Name"))

    class Meta:
        db_table = "core_value"

    def __str__(self):
        return self.name


class QuestionChoices(models.IntegerChoices):
    """
    Choices for the type field of Question model.
    """
    MULTIPLE_CHOICE = (0, _("Multiple Choice"))


class Question(models.Model):
    """
    Model to store Question details
    """
    text = models.CharField(max_length=250, verbose_name=_("Question Text"))
    subtext = models.CharField(max_length=250, verbose_name=_("Question Subtext"))
    type = models.PositiveSmallIntegerField(choices=QuestionChoices.choices, default=QuestionChoices.MULTIPLE_CHOICE,
                                            verbose_name=_("Question Type"))
    required = models.BooleanField(default=True, verbose_name=_("Required"))
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, verbose_name=_("Related Option Group"))
    order = models.PositiveSmallIntegerField(verbose_name=_("Question Order"))
    core_value = models.ForeignKey(CoreValue, on_delete=models.PROTECT, verbose_name=_("Core Value"))

    class Meta:
        db_table = "question"

    def __str__(self):
        return self.text


class Answer(models.Model):
    """
    Model to store Answer details
    """
    choice_answer = models.ForeignKey(OptionChoice, on_delete=models.PROTECT, verbose_name=_("Answer from Choices"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("Related Question"))

    class Meta:
        db_table = "answer"

    def __str__(self):
        return self.choice_answer.value
