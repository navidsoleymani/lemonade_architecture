from .__base import project_settings, import_class

psa = project_settings.get('ADMIN', {})

BaseModelAdmin = import_class(psa.get('BASE', 'sampleapp.utils.admin.BaseModelAdminClass'))
