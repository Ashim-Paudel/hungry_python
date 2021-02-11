high_score = open("test_high.txt", "a+")


high_score.seek(0)

list_of_scores = [int(scores) for scores in high_score.readlines()]

print(list_of_scores)
print(f"High score is {max(list_of_scores)}")
