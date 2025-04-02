'''

Welcome to the final challenge of this course! In this task, you'll focus on identifying and removing dead code, which refers to code that is no longer necessary. The goal is to streamline the application while preserving its current functionality.

The current code features a pricing strategy with several client tiers: PREMIUM, PLATINUM, GOLD, and SILVER. However, the PREMIUM tier is obsolete and adds unnecessary complexity to the codebase. Your assignment is to refactor the code by eliminating all components associated with the PREMIUM tier.

'''

from enum import Enum


class ClientTier(Enum) :
# {
    # PREMIUM = "premium"
    PLATINUM = "platinum"
    GOLD = "gold"
    SILVER = "silver"
# }

def apply_discount(price, tier) : 
# {
    '''
    if (tier == ClientTier.PREMIUM) :
    # {
        return price
    # }
    '''

    if (tier == ClientTier.PLATINUM) :
    # {
        return price * 0.8  # 20% discount
    # }

    elif (tier == ClientTier.GOLD) :
    # {
        return price * 0.85  # 15% discount
    # }

    elif (tier == ClientTier.SILVER) :
    # {
        return price * 0.9  # 10% discount
    # }

    else :
    # {    
        return price
    # }

# }

def main() :
# {
    base_price = 100.0
    platinum_discount_price = apply_discount(base_price, ClientTier.PLATINUM)
    gold_discount_price = apply_discount(base_price, ClientTier.GOLD)
    silver_discount_price = apply_discount(base_price, ClientTier.SILVER)
    # premium_discount_price = apply_discount(base_price, ClientTier.PREMIUM)

    print("Platinum Price:", platinum_discount_price)
    print("Gold Price:", gold_discount_price)
    print("Silver Price:", silver_discount_price)
    # print("Premium Price:", premium_discount_price)
# }

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

'''