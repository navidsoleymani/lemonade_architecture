from .__base import project_settings, import_class

pss = project_settings.get('SERIALIZER_BASE_CLASSES', {})

BSC = import_class(pss.get('BASE', 'sampleapp.utils.serializers.BaseModelSerializerClass'))

BCreateSC = import_class(pss.get('CREATE', 'sampleapp.utils.serializers.BaseCreateModelSerializerClass'))

BListSC = import_class(pss.get('LIST', 'sampleapp.utils.serializers.BaseListModelSerializerClass'))

BRetrieveSC = import_class(pss.get('RETRIEVE', 'sampleapp.utils.serializers.BaseRetrieveModelSerializerClass'))

BUpdateSC = import_class(pss.get('UPDATE', 'sampleapp.utils.serializers.BaseUpdateModelSerializerClass'))

BDestroySC = import_class(pss.get('DESTROY', 'sampleapp.utils.serializers.BaseDestroyModelSerializerClass'))
