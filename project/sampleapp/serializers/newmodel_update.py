from ..imports.serializers import BUpdateSC as Parent

from ..models import NewModel as NewModelModel


class NewModelUpdateSerializer(Parent):
    class Meta(Parent.Meta):
        model = NewModelModel
