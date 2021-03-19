'''
Paul is an excellent coder and sits high on the CW leaderboard. 
He solves kata like a banshee but would also like to lead a normal life, with other activities. 
But he just can't stop solving all the kata!!

Given an array (x) you need to calculate the Paul Misery Score. 
The values are worth the following points:

kata = 5 Petes kata = 10 life = 0 eating = 1

The Misery Score is the total points gained from the array. Once you have the total, return as follows:

<40 = 'Super happy!'
<70 >=40 = 'Happy!'
<100 >=70 = 'Sad!'
>=100 = 'Miserable!'
'''



def paul(x):
    scores = {'kata': 5, 'kata': 10, 'life': 0, 'eating': 1}
    finalScore = 0
    for word in x:
        finalScore += scores[word]
    answers = ['Super happy!','Happy!','Sad!','Miserable!']
    if finalScore >= 100:
        return answers[-1]
    elif finalScore >= 70:
        return answers[-2]
    elif finalScore >= 40:
        return answers[-3]
    else:
        return answers[0]