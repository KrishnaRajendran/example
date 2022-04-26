from django.contrib import admin
from .models import Answer, CoreValue, OptionChoice, OptionGroup, Question


# Register your models here.
@admin.register(OptionChoice)
class OptionChoiceAdmin(admin.ModelAdmin):
    list_display = ("order", "value")


@admin.register(OptionGroup)
class OptionGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "display_option_choice")

    # String to represent option choice in the Admin
    def display_option_choice(self, obj):
        return "%s" % (", ".join(option.value for option in obj.options.all()))


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "type", "required", "option_group", "order", "core_value")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("choice_answer", "question")
