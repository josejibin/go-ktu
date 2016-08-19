from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from ktu.base.models import TimeAuditModel


@python_2_unicode_compatible
class Institute(TimeAuditModel):

    name = models.CharField(max_length=100)
    aicte_id = models.IntegerField(null=True, blank=True)
    institute_id = models.CharField(max_length=100)
    address = models.TextField(
        verbose_name="Address", null=True, blank=True)
    phone = models.CharField(
        verbose_name="Office Mobile No", max_length=20, null=True, blank=True)
    fax = models.CharField(
        verbose_name="Office Mobile No", max_length=20, null=True, blank=True)
    email = models.EmailField(
        verbose_name="Office E-mail", null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
