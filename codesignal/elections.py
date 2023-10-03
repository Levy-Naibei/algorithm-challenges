"""
Given an array of the numbers of votes given to each of the candidates so far,
and an integer k equal to the number of voters who haven't cast their vote yet,
find the number of candidates who still have a chance to win the election.
The winner of the election must secure strictly more votes than any other candidate.
If two or more candidates receive the same (maximum) number of votes,
assume there is no winner at all.
"""

def election_winners(votes, k):
    votes.sort(reverse=True)
    n = len(votes)
    winners = 0

    # Check for the case where k == 0 and there's only one winner
    if k == 0 and votes[0] != votes[1]:
        winners = 1

    # Count the number of candidates who can still win
    for i in range(len(votes)):
        if votes[i] + k > votes[0]:
            winners += 1
        else:
            break
    return winners

print(election_winners([2, 3, 5, 2], 3))
print(election_winners([1, 3, 3, 1, 1], 0))
print(election_winners([1, 1, 1, 1], 1))
