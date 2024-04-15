import unittest
from Auction import Auction
from AuctionHouse import AuctionHouse
from Bidder import Bidder
from SecurityLabel import SecurityLabel

class TestAuction(unittest.TestCase):
    
    def setUp(self):
        # Set up an AuctionHouse and Auction
        self.auction_house = AuctionHouse()
        self.auction_house.security_level = SecurityLabel.AUCTION_HOUSE_CONFIDENTIAL
        self.auction = Auction(self.auction_house)
        
        # Register bidders
        self.bidder1 = self.auction_house.register_bidder("B001", "Alice")
        self.bidder2 = self.auction_house.register_bidder("B002", "Bob")

        # Place initial commission bids
        self.auction.place_commission_bid(self.bidder1, 700)
        self.auction.place_commission_bid(self.bidder2, 800)

    def test_place_commission_bid(self):
        # Test that commission bids are placed correctly
        self.assertIn(self.bidder1.bidder_id, self.auction.commission_bids)
        self.assertEqual(self.auction.commission_bids[self.bidder1.bidder_id], 700)
        self.assertEqual(self.auction.commission_bids[self.bidder2.bidder_id], 800)

    def test_receive_live_bid_higher_than_commission(self):
        # Test live bid higher than any commission bid
        self.auction.receive_live_bid(self.bidder1, 850)
        self.assertEqual(self.auction.highest_bid, 850)
        self.assertEqual(self.auction.winning_bidder, self.bidder1)

    def test_commission_bid_priority(self):
        # Test commission bid priority when live bid matches the commission bid
        self.auction.receive_live_bid(self.bidder2, 800)
        self.assertEqual(self.auction.highest_bid, 800)
        self.assertEqual(self.auction.winning_bidder, self.bidder2)

    def test_finalize_auction(self):
        # Simulate bids and finalize auction
        self.auction.receive_live_bid(self.bidder2, 900)
        self.auction.finalize_auction()
        expected_result = f"going once... going twice... sold to {self.bidder2.pseudonym} for 900 Kr"
        self.assertEqual(self.auction.finalize_auction(), expected_result)

if __name__ == '__main__':
    unittest.main()
