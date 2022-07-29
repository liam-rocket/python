print('Hello world')



































# from random import choice

# # Generate votes
# candidates = ["sam", "perry", "eng liang"]
# votes = []
# for _ in range(1000):
#   # Append 1000 random (of 3 choices) candidates to votes array
#   votes.append(choice(candidates))


# # Compile a tally of how many times an element appears in an array
# # The tally is stored in a dictionary.
# def get_winner(votes):
#   # Compile tally
#   tally = {}
#   for person in votes:
#     if person not in tally:
#       tally[person] = 0
#     tally[person] += 1

#   # Return the person with max votes as the winner
#   max_votes = max(tally.values())
#   for person, vote_count in tally.items():
#     if vote_count == max_votes:
#       return person

# # Output winner
# print(get_winner(votes))