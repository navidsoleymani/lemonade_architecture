from rest_framework import serializers


class BaseModelSerializerClass(serializers.ModelSerializer):
    class Meta:
        pass


class BaseCreateModelSerializerClass(BaseModelSerializerClass):
    class Meta(BaseModelSerializerClass.Meta):
        pass


class BaseListModelSerializerClass(BaseModelSerializerClass):
    class Meta(BaseModelSerializerClass.Meta):
        pass


class BaseRetrieveModelSerializerClass(BaseModelSerializerClass):
    class Meta(BaseModelSerializerClass.Meta):
        pass


class BaseUpdateModelSerializerClass(BaseModelSerializerClass):
    class Meta(BaseModelSerializerClass.Meta):
        pass


class BaseDestroyModelSerializerClass(BaseModelSerializerClass):
    class Meta(BaseModelSerializerClass.Meta):
        pass
