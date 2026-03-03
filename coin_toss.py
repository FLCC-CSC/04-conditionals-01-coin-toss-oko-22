# FILE NAME - coin_toss.py

# NAME: Onyinye Ofornagoro
# DATE: 03/02/2026
# BRIEF DESCRIPTION: Flipping a coin  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    coin_toss()

def coin_toss():
    print("===== Coin Flipper =====")

    number = random.randint(1,100)

    if number >= 51:
        print("Tails")
    else:
        print("Heads")

main()





########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

The hardest part was figuring out how to store the random number for the coin toss.





'''
