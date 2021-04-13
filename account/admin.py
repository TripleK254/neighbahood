from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Users, Neighborhood

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('name','email', 'username','date_joined', 'last_login','is_admin','is_neighborhood_admin','neighborhood_name')
    search_fields = ('email', 'username','neighborhood_name')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Users,AccountAdmin)
admin.site.register(Neighborhood)
