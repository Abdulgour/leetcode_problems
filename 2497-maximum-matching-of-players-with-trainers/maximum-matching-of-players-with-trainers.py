class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pn=len(players)
        tn=len(trainers)
        c=0
        while pn and tn:
            if players[pn-1]<=trainers[tn-1]:
                c+=1
                pn-=1
                tn-=1
            else:
                pn-=1
        return c