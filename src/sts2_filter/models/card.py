from sts2_filter.enums.cards import CardID

class Card:
    id: CardID
    upgrade: bool
    enchant: None

    @classmethod
    def from_json(data):
        id = data.get("id")
        #upgrade = 
        return