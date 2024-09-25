'''
Holiday_gifts
Calculate gift costs

author: jazielinho
create_at: 2024 - july
'''


import time
import numpy as np


def _load_gift_cost(gift_path: str) -> np.array:
    '''Load gift cost from path.'''
    with open(gift_path, 'r', encoding="utf-8") as path:
        gift_costs = path.read().split('\n')
    return np.array(gift_costs).astype(int)


def _get_total_price(gift_costs: np.array, cost_filter: int, cost_taxt: float) -> float:
    '''Get total price with taxt for cost lower than cost_filter.'''
    return gift_costs[gift_costs < cost_filter].sum() * cost_taxt


def load_get_total_price(gift_path: str, cost_filter: int, cost_taxt: float) -> float:
    '''Load and get total price with taxt for cost lower than cost_filter.'''
    gift_costs = _load_gift_cost(gift_path=gift_path)
    total_price = _get_total_price(
        gift_costs=gift_costs,
        cost_filter=cost_filter,
        cost_taxt=cost_taxt
    )
    return total_price


if __name__ == '__main__':
    start = time.time()
    TOTAL_PRICE = load_get_total_price(
        gift_path='gift_costs.txt',
        cost_filter=25,
        cost_taxt=1.08
    )
    print(TOTAL_PRICE)
    print(f'Duration: {time.time() - start} seconds')
