from django.contrib import admin
from .models import test_table, Main_test, Counter
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.

admin.site.register(Main_test)
admin.site.register(Counter)


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


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'image')}),
    )

    def user_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"

    user_image.short_description = 'Image'

    list_display = ('username', 'email', 'phone_number', 'user_image')
    list_filter = ('phone_number',)  # Add filters for phone numbers if needed
    search_fields = ('username', 'email', 'phone_number')


admin.site.register(CustomUser, CustomUserAdmin)
