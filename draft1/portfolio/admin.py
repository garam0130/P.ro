from django.contrib import admin
from portfolio.models import Group, GroupType, SiType, GuType, Register, Status
# Register your models here.
admin.site.register(Group)
admin.site.register(GroupType)
admin.site.register(SiType)
admin.site.register(GuType)
admin.site.register(Register)
admin.site.register(Status)