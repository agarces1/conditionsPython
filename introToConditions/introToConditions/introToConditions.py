#If statements with strings
#answer = input("Would you like express shipping?");
#if answer == "yes" : 
#    print("That will be an extra $10");
#print("Have a nice day");
#favoriteTeam = input("What is your favorite hockey team? ");
#if favoriteTeam.upper() == "SENATORS" : 
#    print("Go team Go!");
#    print("But I miss alfreson");
#print("It is okay if you dont like hockey");
#Almost every IF Statement can be written two ways
#if answer == "Yes" :
#IF not answer == "no" :

#if total <100 :
#if not total >= 100:
#IF with numbers and branching
#always test >,< and boundry conditions.
freeToaster = False# It is always a good idea to initialize your variables!.
deposit = int(input("How much would you like to deposit? "))
if deposit > 100 :
    freeToaster = True
    print("Enjoy your FREE toaster!");
    if freeToaster :
        print("MMM Bread.");

else:#when the condition is NOT true
    print("You qualify for a mug!");
print("Have a nice day!");