from lib.owner import Owner  # needed only if you do owner checks

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")

        self.name = name
        self.pet_type = pet_type
        self._owner = None
        Pet.all.append(self)

        if owner:
            self.owner = owner  # uses setter

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        from lib.owner import Owner  # avoid circular import at runtime
        if not isinstance(value, Owner):
            raise Exception("owner must be an instance of Owner")
        self._owner = value
