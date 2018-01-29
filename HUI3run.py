import HUI3 as eq

print("Score for ", [2, 1, 1, 2, 1, 2, 1, 3])
print(eq.get_score(vision=2, hearing=1, speech=1, ambulation=2, dexterity=1, emotion= 2, cognition=1, pain=3))

print("Score for perfect health")
print(eq.get_score(vision=1, hearing=1, speech=1, ambulation=1, dexterity=1, emotion= 1, cognition=1, pain=1))

# an unacceptable value for self-care
#print(eq.get_score(mobility=1, self_care=0, usual_activity=1, pain_discomfort=1, anxiety_depression=1))
# an unacceptable value for usual activity
#print(eq.get_score(mobility=1, self_care=1, usual_activity=5, pain_discomfort=1, anxiety_depression=1))
