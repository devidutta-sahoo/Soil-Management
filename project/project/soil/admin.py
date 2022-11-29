from django.contrib import admin
from .models import Crops, Fertilisers
from import_export.admin import ImportExportModelAdmin
# from soil.models import User_Login

# admin.site.register(User_Login)
@admin.register(Crops)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(Fertilisers)
class userdat(ImportExportModelAdmin):
    pass
