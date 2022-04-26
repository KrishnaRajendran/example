from django.contrib import admin
from .models import Feedback, FeedbackSection, Template


# Register your models here.
@admin.register(FeedbackSection)
class FeedbackSectionAdmin(admin.ModelAdmin):
    list_display = ("description", "type", "display_count")

    # String to represent count of questions
    @admin.display(description="number of questions")
    def display_count(self, obj):
        return "%s" % (obj.questions.all().count())


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "projects",
        "display_sections",
        "is_completed",
        "start_date",
        "end_date",
    )

    # String to represent all feedback section types in the Admin
    @admin.display(description="feedback sections")
    def display_sections(self, obj):
        return "%s" % (", ".join(section.get_type_display() for section in obj.sections.all()))


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "display_sections")

    # String to represent all feedback section types in the Admin
    @admin.display(description="feedback sections")
    def display_sections(self, obj):
        return "%s" % (", ".join(section.get_type_display() for section in obj.sections.all()))
