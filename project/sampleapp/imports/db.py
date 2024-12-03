from .__base import project_settings, import_class

psdb = project_settings.get('DATABASE', {})

BaseDBModel = import_class(psdb.get('MODEL', 'sampleapp.utils.db.BaseDBModel'))
ObjectManager = import_class(psdb.get('OBJECT_MANAGER', 'sampleapp.utils.db.SoftDeleteManager'))
Sender = import_class(psdb.get('SENDER', 'sampleapp.utils.senders.Sender'))
VerificationCodeGenerator = import_class(
    psdb.get('VerificationCodeGenerator', 'sampleapp.utils.db.RandomCodeGenerator'))
