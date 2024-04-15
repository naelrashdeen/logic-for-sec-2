from SecurityLabel import SecurityLabel

class Auction:
    def __init__(self, auction_house):
        self.auction_house = auction_house
        self.commission_bids = {}
        self.starting_price = 450  # Start with an initial bid of 450
        self.highest_bid = 550  # Start with an initial bid of 550
        self.winning_bidder = None
        self.increment_bid = 50
        self.current_bid = None
        self.auction_security_level = SecurityLabel.PUBLIC

    def place_commission_bid(self, bidder, amount):
        # Check security level before placing commission bid
        if self.auction_house.security_level >= SecurityLabel.AUCTION_HOUSE_CONFIDENTIAL:
            self.commission_bids[bidder.bidder_id] = amount
            print(f"start: auction house bids for {bidder.pseudonym}: {self.starting_price + self.increment_bid} Kr")
        else:
            raise PermissionError("Insufficient security level for placing commission bids.")

    def receive_live_bid(self, bidder, amount):
        print(f"{bidder.pseudonym} bids {amount} Kr")
        if amount > self.highest_bid:
            self.highest_bid = amount
            self.winning_bidder = bidder
            self.respond_to_live_bid(amount)
        elif amount == self.highest_bid:
            # Only check commission priority if the live bid matches the highest bid exactly
            self.check_commission_priority(amount)
        else:
            # The live bid is lower and should not affect the highest bid or trigger a commission response
            print(f"Live bid of {amount} Kr by {bidder.pseudonym} is too low.")


    def respond_to_live_bid(self, live_bid):
        # Calculate next possible bid
        next_bid = self.highest_bid + 50
        for bidder_id, max_bid in self.commission_bids.items():
            if next_bid <= max_bid:
                print(f"Auction house bids for {self.auction_house.registered_bidders[bidder_id].pseudonym}: {next_bid} Kr")
                self.highest_bid = next_bid
                self.winning_bidder = self.auction_house.registered_bidders[bidder_id]
                return
        # No commission bid can exceed the live bid, check for exact matches
        self.check_commission_priority(self.highest_bid)

    def check_commission_priority(self, amount):
        for bidder_id, max_bid in self.commission_bids.items():
            if max_bid == amount:
                print(f"Auction house bids for {self.auction_house.registered_bidders[bidder_id].pseudonym}: {amount} Kr")
                self.highest_bid = amount
                self.winning_bidder = self.auction_house.registered_bidders[bidder_id]
                break

    def finalize_auction(self):
        result = f"going once... going twice... sold to {self.winning_bidder.pseudonym} for {self.highest_bid} Kr"
        print(result)
        return result
