from Auction import Auction
from Bidder import Bidder
from SecurityLabel import SecurityLabel


class AuctionHouse:
    def __init__(self):
        self.trusted_auction_houses = ["Auction House B", "Auction House D"]
        self.registered_bidders = {}
        self.auctions = []
        self.security_level = SecurityLabel.AUCTION_HOUSE_CONFIDENTIAL

    def register_bidder(self, bidder_id, pseudonym, is_new=None, reference=None):
        bidder = Bidder(bidder_id, pseudonym)
        self.registered_bidders[bidder_id] = bidder
        print(f"Bidder {pseudonym} registered successfully.")
        return bidder

    def verify_and_update_reputation(self, bidder, reference):
        # Simulate checking the reference from another auction house
        if reference['auction_house'] in self.trusted_auction_houses:
            if reference['status'] == "good":
                bidder.update_limit_based_on_reference("good")
                print(f"Updated bidding limit for {bidder.pseudonym} based on reference from {reference['auction_house']}.")

    def create_auction(self):
        new_auction = Auction(self)
        self.auctions.append(new_auction)
        return new_auction
