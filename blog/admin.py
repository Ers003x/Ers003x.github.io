from django.contrib import admin
from .models import *

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Images)
admin.site.register(FrontSlider)