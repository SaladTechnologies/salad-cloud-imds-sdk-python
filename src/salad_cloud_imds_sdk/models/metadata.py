from enum import Enum


class Metadata(Enum):
    """An enumeration representing different categories.

    :cvar TRUE: "true"
    :vartype TRUE: str
    """

    TRUE = "true"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Metadata._member_map_.values()))
