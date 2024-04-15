from AuctionHouse import AuctionHouse


def main():
    auction_house = AuctionHouse()
    # Register two bidders, one with a reference and one without
    auction_house.register_bidder("B001", "Bidder B", is_new=True)
    auction_house.register_bidder("C001", "Bidder C", is_new=False)
    auction_house.register_bidder("B002", "Bidder D", is_new=True, reference={"auction_house": "Auction House B", "status": "good"})

    auction = auction_house.create_auction()

    # Initial commission bids
    auction.place_commission_bid(auction_house.registered_bidders["B001"], 500)
    auction.place_commission_bid(auction_house.registered_bidders["B002"], 1000)

    # Live bidding sequence
    auction.receive_live_bid(auction_house.registered_bidders["C001"], 450)
    auction.receive_live_bid(auction_house.registered_bidders["C001"], 500)
    auction.receive_live_bid(auction_house.registered_bidders["C001"], 550)
    auction.receive_live_bid(auction_house.registered_bidders["C001"], 800)

    # Finalize auction
    auction.finalize_auction()

if __name__ == "__main__":
    main()
