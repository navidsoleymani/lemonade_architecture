from django.utils.translation import gettext_lazy as _

from django.apps import AppConfig


class SampleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sampleapp'
    verbose_name = _('SampleApp')
