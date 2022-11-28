class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # code is as per the "hash set" algorithm given in solution
        zero_loss, one_loss, more_loss = set(), set(), set()
        
        for winner, loser in matches: # list unpacking
            # print(zero_loss, one_loss, more_loss)
            # winner analysis, a new winner is found
            if (winner not in more_loss) and (winner not in one_loss):
                zero_loss.add(winner)
                
            # for loser, if found in any group
            # remove them and update from zero -> one -> more
            if loser in zero_loss:
                zero_loss.remove(loser); one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser); more_loss.add(loser)
            elif loser in more_loss:
                continue # not required further
            else:
                one_loss.add(loser)
                
        return sorted(list(zero_loss)), sorted(list(one_loss))