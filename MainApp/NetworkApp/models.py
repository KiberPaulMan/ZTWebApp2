from django.db import models


class Networks(models.Model):
    device = models.CharField(max_length=50)

    ip = models.GenericIPAddressField()
    mask = models.GenericIPAddressField()
    gw = models.GenericIPAddressField()

    dns = models.GenericIPAddressField()

    def __str__(self):
        return self.device.title()

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'