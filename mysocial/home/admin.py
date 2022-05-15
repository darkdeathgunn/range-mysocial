from django.contrib import admin
from .models import *

admin.site.register(Postmodel)
admin.site.register(Followmodel)
admin.site.register(likes)
admin.site.register(comments)

