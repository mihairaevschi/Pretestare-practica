from django.contrib import admin
from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    fields = ('name','email','subject','company_name','content')

admin.site.register(Feedback, FeedbackAdmin)
