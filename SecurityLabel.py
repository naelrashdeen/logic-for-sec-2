from enum import Enum

class SecurityLabel(Enum):
    PUBLIC = (1, "Public")
    BIDDER_LEVEL_CONFIDENTIAL = (2, "Bidder-Level Confidential")
    AUCTION_HOUSE_CONFIDENTIAL = (3, "Auction House Confidential")

    def __init__(self, rank, description):
        self.rank = rank
        self.description = description

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.rank >= other.rank
        return NotImplemented
