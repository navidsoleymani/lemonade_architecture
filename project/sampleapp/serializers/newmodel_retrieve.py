from ..imports.serializers import BRetrieveSC as Parent

from ..models import NewModel as NewModelModel


class NewModelRetrieveSerializer(Parent):
    class Meta(Parent.Meta):
        model = NewModelModel
