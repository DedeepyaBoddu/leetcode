class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for card in range(first, first+groupSize):
                # here checking if key isnt present in dict is enough because if key has value and its becoming zero, we are handling it down after decrementing counter, any count reaches zero. if its min of heap, pop it. if its not min, it automatically means consecutivity is missing, so we return False. so our code will never even go into situation where you start a group with a card and one of the following cards will have a counter 0
                if card not in count:
                    return False
                count[card] -=1
                if count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True





        