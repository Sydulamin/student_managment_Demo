from django.contrib import admin
from .models import test_table, Main_test

# Register your models here.

admin.site.register(Main_test)


class TestTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'get_father_name', 'get_mother_name', 'get_nationality')
    list_filter = ('parents__Nationality',)

    def get_father_name(self, obj):
        return obj.parents.Father_name if obj.parents else "No Parent"

    get_father_name.short_description = "Father Name"

    def get_mother_name(self, obj):
        return obj.parents.Mother_name if obj.parents else "No Parent"

    get_mother_name.short_description = "Mother Name"

    def get_nationality(self, obj):
        return obj.parents.Nationality if obj.parents else "No Nationality"

    get_nationality.short_description = "Nationality"


admin.site.register(test_table, TestTableAdmin)
