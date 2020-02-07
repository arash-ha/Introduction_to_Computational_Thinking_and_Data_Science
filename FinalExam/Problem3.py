"""
Problem 3
20.0/20.0 points (graded)
You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

Write a Monte Carlo simulation that meets the specifications below. Feel free to write a helper function if you wish.
"""

def drawing_without_replacement_sim(numTrials):
    c = 0
    
    for i in range(numTrials):
        
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            
            c += 1
            
    return c/numTrials