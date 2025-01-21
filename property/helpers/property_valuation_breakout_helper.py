class PropertyValuationBreakoutHelper:
    def __init__(self):
        pass

    def calculate_amount_proportion_with_valuation(self, amount, valuation):
        stake_in_property = amount / valuation
        stake_in_property_in_percentage = stake_in_property * 100
        return f"{stake_in_property:.15f}", f"{stake_in_property_in_percentage:.15f}"
    
    