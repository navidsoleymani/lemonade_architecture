from ..imports.serializers import BListSC as Parent

from ..models import NewModel as NewModelModel


class NewModelListSerializer(Parent):
    class Meta(Parent.Meta):
        model = NewModelModel
