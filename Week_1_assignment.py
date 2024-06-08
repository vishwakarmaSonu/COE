'''Here are 15 stars in linear form. Now make a triangle pattern using these 15 stars'''
print("* "*15)
print(" ")
print("Triangle pattern here...")
NUM = 5
for i in range(NUM+1):
    print(" "*(NUM-i)+" *"*i)
