from django.contrib import admin
from .models import Client, Project


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "client", "project_manager", "display_members")

    # String to represent first three members in the Admin
    @admin.display(description="members")
    def display_members(self, obj):
        return "%s ..." % (", ".join(user.username for user in obj.members.all()[:3]))
