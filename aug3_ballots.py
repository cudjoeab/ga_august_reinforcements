# Each dictionary represents a voting ballot, with three names in gold, silver, and bronze tiers.

# 'gold' is worth 3 points,
# 'silver' is worth 2 points,
# 'bronze' is worth 1 point.

# For example, the first ballot {'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'}
# shows that this voter chose Smudge for first place, Tigger for 2nd, and Simba for 3rd.
# Smudge would be awarded 3 points, Tigger would be awarded 2 points, and Simba would be awarded 1 point.

# Tally up all the votes and determine who won.

ballots = [
    {"gold": "Smudge", "silver": "Tigger", "bronze": "Simba"},
    {"gold": "Bella", "silver": "Lucky", "bronze": "Tigger"},
    {"gold": "Bella", "silver": "Boots", "bronze": "Smudge"},
    {"gold": "Boots", "silver": "Felix", "bronze": "Bella"},
    {"gold": "Lucky", "silver": "Felix", "bronze": "Bella"},
    {"gold": "Smudge", "silver": "Simba", "bronze": "Felix"},
]

# desired_output = {"Smudge": 3, "Tigger": 2, "Simba": 1}

ranks = {"gold": 3, "silver": 2, "bronze": 1}

results = {}

for ballot in ballots:
    for ranking, name in ballot.items():
        points = ranks[ranking]
        if name in results.keys():
            results[name] += points
        else:
            results[name] = 0

            

print(results)


winner = max(results, key=results.get)
print(f"The winner is {winner}!")