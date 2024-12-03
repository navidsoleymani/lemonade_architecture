from ..imports.serializers import BCreateSC as Parent

from ..models import NewModel as NewModelModel


class NewModelCreateSerializer(Parent):
    class Meta(Parent.Meta):
        model = NewModelModel
