from django.db import models

class Feedback(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, null=True)
    email = models.EmailField(verbose_name='Email', max_length=70, null=True)
    subject = models.CharField(verbose_name='Subject', max_length=100, null=True)
    company_name = models.CharField(verbose_name="Company Name", max_length=50, null=True)
    content = models.TextField(verbose_name="Content", null=True)

    def __str__(self):
        return self.subject
