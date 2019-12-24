from django.db import models
from django.utils.translation import ugettext_lazy as _


class Options(models.Model):
    title = models.CharField(
        max_length=200, verbose_name=_('Option title'), db_index=True)
    value = models.BooleanField(verbose_name=_('Enabled'))

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')

    def __str__(self):
        return self.title


class Pushes(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created time'))
    sent = models.DateTimeField(
        null=True, blank=True, verbose_name=_('Sent time'))

    title = models.CharField(
        max_length=50, verbose_name=_('Notification title'), db_index=True)
    text = models.TextField(_('Notification body'))
    is_sent = models.BooleanField(verbose_name=_('Sent'), default=False)
    count_sent = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = _('Push notification')
        verbose_name_plural = _('Push notifications')

    def __str__(self):
        return self.title