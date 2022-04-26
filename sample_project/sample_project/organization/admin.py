from django.contrib import admin
from .models import Department, Designation, Team


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "display_teams")

    # String to represent first three teams in the Admin
    @admin.display(description="teams")
    def display_teams(self, obj):
        return "%s ..." % (", ".join(team.name for team in obj.teams.all()[:3]))


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ("name",)
