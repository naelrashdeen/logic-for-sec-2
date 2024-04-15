import unittest
from AuctionHouse import AuctionHouse
from Bidder import Bidder
from SecurityLabel import SecurityLabel

class TestAuctionSystem(unittest.TestCase):
    
    def setUp(self):
        # Initialize the auction house with a high security level
        self.auction_house = AuctionHouse()
        self.auction_house.security_level = SecurityLabel.AUCTION_HOUSE_CONFIDENTIAL

        # Register bidders through the auction house to ensure consistent use of Bidder instances
        self.bidder1 = self.auction_house.register_bidder("B001", "Alice")
        self.bidder2 = self.auction_house.register_bidder("B002", "Bob")

        # Create an auction
        self.auction = self.auction_house.create_auction()

    def test_place_commission_bid(self):
        # Place a commission bid and check it was placed correctly
        self.auction.place_commission_bid(self.bidder1, 700)
        self.assertEqual(self.auction.commission_bids[self.bidder1.bidder_id], 700)

        # Test handling of security level for placing bids
        self.auction_house.security_level = SecurityLabel.PUBLIC
        with self.assertRaises(PermissionError):
            self.auction.place_commission_bid(self.bidder2, 800)

    def test_receive_live_bid(self):
        # Test reception of a live bid and updating of auction state
        self.auction.receive_live_bid(self.bidder1, 600)
        self.assertEqual(self.auction.highest_bid, 600)
        self.assertEqual(self.auction.winning_bidder, self.bidder1)

        # Ensure lower bids do not override the current highest bid
        self.auction.receive_live_bid(self.bidder2, 500)
        self.assertEqual(self.auction.highest_bid, 600)

    def test_commission_bid_priority(self):
        # Test that commission bids take priority appropriately
        self.auction.place_commission_bid(self.bidder1, 750)
        self.auction.receive_live_bid(self.bidder2, 750)
        self.assertEqual(self.auction.highest_bid, 750)
        self.assertEqual(self.auction.winning_bidder, self.bidder1)

    def test_finalize_auction(self):
        # Test the finalization and output of the auction
        self.auction.receive_live_bid(self.bidder1, 1000)
        result = f"going once... going twice... sold to {self.auction.winning_bidder.pseudonym} for {self.auction.highest_bid} Kr"
        self.auction.finalize_auction()
        self.assertEqual(self.auction.finalize_auction(), result)

if __name__ == '__main__':
    unittest.main()
