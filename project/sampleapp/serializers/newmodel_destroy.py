from ..imports.serializers import BDestroySC as Parent
from ..models import NewModel as NewModelModel


class NewModelDestroySerializer(Parent):
    class Meta(Parent.Meta):
        model = NewModelModel
