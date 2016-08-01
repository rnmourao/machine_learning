import itertools
import collections


def apriori(data, support_ratio):
    """
    Given a list of sets (data), discover subsets that occurs at a minimum percentage (support_ratio).
    Example:
        data: [{1, 2, 3, 4}, {1, 2, 3}, {1, 2}, {2, 3, 4}, {2, 3}, {3, 4}, {2, 4}]
        support_ratio: 0.42
        Returns:
            {(1,): 0.42857142857142855,
             (1, 2): 0.42857142857142855,
             (2,): 0.8571428571428571,
             (2, 3): 0.5714285714285714,
             (2, 4): 0.42857142857142855,
             (3,): 0.7142857142857143,
             (3, 4): 0.42857142857142855,
             (4,): 0.5714285714285714}
    """
    
    # get number of itemsets
    total_itemsets = len(data)

    # control size of subsets
    length = 0
    longest_itemset = max([len(itemset) for itemset in data])

    # initialize control of accepted subsets
    support = {}

    # initialize control of rejected subsets
    discards = []

    # stopping criteria - if a iteration is rejected completely, it's time to stop
    foundit = True

    while foundit and length <= longest_itemset:
        # increment size of subsets
        length += 1

        # generate subsets and remove not supported combinations
        items = set([combination
                     for itemset in data
                     for combination in itertools.combinations(itemset, length)
                     if combination not in discards])

        # count subsets in data
        s = collections.Counter([item
                                 for item in items
                                 for itemset in data
                                 if itemset.issuperset(item)])

        # add subsets that have support and discard those don't have
        foundit = False
        for key, value in s.items():
            ratio = value / total_itemsets
            if ratio >= support_ratio:
                foundit = True
                support[key] = ratio
            else:
                discards += key

    return support
