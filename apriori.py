# this algorithm is not completed.

import itertools
import collections


def apriori(data, support_ratio):
    # get number of itemsets
    total_itemsets = len(data)

    # get individual items
    elements = frozenset([item for itemset in data for item in itemset])

    # generate combinations of items
    items = [x for i in range(len(elements) + 1) for x in itertools.combinations(elements, i) if x]

    # count combined items in data
    s = collections.Counter([i for i in items for itemset in data if itemset.issuperset(i)])

    # remove itemsets that don't have minimum support
    support = {key: value / total_itemsets for key, value in s.items() if value / total_itemsets >= support_ratio}

    return support
