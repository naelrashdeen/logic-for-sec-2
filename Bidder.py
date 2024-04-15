from SecurityLabel import SecurityLabel

class Bidder:
    def __init__(self, bidder_id, pseudonym, is_new_customer=True, trusted_reference=None):
        self.bidder_id = bidder_id
        self.pseudonym = pseudonym
        self.is_new_customer = is_new_customer
        self.trusted_reference = trusted_reference
        self.max_bid = 0
        self.security_label = SecurityLabel.BIDDER_LEVEL_CONFIDENTIAL
        self.bid_limit = 500 if is_new_customer else 1000  # Default limits

    def place_bid(self, amount):
        if amount > self.bid_limit:
            raise ValueError("Bid exceeds your current limit.")
        self.max_bid = amount
        self.security_label = SecurityLabel.BIDDER_LEVEL_CONFIDENTIAL

    def get_bid_info(self, requestor_security_level):
        if requestor_security_level >= self.security_label:
            self.security_label = SecurityLabel.PUBLIC
            return self.pseudonym, self.max_bid
        else:
            raise PermissionError("Access denied due to insufficient security clearance.")

    def update_limit_based_on_reference(self, reference_status):
        if reference_status == "good":
            self.bid_limit = 1000  # Increase limit based on good reference
