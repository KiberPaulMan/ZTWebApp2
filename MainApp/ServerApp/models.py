from django.db import models
from NetworkApp.models import Networks


class PhysicalServers(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    domain_name = models.CharField(max_length=40)
    server_ip = models.ForeignKey(Networks, on_delete=models.CASCADE)

    is_physical = models.BooleanField(default=True)
    # virtual_machine = models.ForeignKey('self', on_delete=models.CASCADE) # 'self', on_delete=models.CASCADE, blank=True

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Physical Server'
        verbose_name_plural = 'Physical Servers'


class VirtualServers(models.Model):
    virtual_machine = models.OneToOneField(PhysicalServers, on_delete=models.CASCADE)

    def __str__(self):
        self.virtual_machine.title()

    class Meta:
        verbose_name = 'Virtual Server'
        verbose_name_plural = 'Virtual Servers'
