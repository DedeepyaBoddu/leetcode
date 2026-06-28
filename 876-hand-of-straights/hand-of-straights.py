class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = defaultdict(int)
        for card in hand:
            counter[card] +=1
        
        for card in sorted(hand):
            if counter[card] == 0:
                continue
            for nxt in range(card, card+groupSize):
                if counter[nxt] == 0:
                    return False
                counter[nxt] -=1
        return True



        