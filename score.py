
import random

for user in range(20,30):
    grade=[]
    grade = {1: random.randrange(1,7) for item in user}
    classnumber = {1: random.randrange(7) for item in user}
    english_score={}
    english_score = {1: random.randrange(0,101) for item in score}
    laguage_score={}
    laguage_score = {1: random.randrange(0,101) for item in score}
    Math_score={}
    Math_score = {1: random.randrange(0,101) for item in score}
    science_score={}
    science_score = {1: random.randrange(0,101) for item in score}
    score=[english_score, laguage_score,Math_score,science_score]

DB ={user:{grade,classnumber,score}}

print(DB)

