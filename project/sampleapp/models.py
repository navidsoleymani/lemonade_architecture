from .imports.db import BaseDBModel as Parent

from .imports.db import ObjectManager


class Manager(ObjectManager):
    pass


class NewModel(Parent):
    pass
