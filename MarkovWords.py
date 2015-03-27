"""Author: Dom Modica
Purpose: To solve the problem described @ http://www.reddit.com/r/dailyprogrammer/comments/2ovt2i/20141210_challenge_192_intermediate_markov_chain/
Essentially the purpose is to read in a large dictionary file of words, and analyze the frequencies of how letters follow each other.
For example in the english language one can detect patterns by analyzing the frequency of how often a letter is followed by another letter or vice versa.
Using this knowledge one can make educated guesses as to whether or not a word is spelt correctly or not."""



letters='abcdefghijklmnopqrstuvwxyz'
matrixdict = {x: {y : 0 for y in letters} for x in letters}
letterdict={x:0 for x in letters}

words=open('enable1.txt').read().splitlines() #used to build baseline data
for word in words:
    for i in range(len(word) - 1):
        matrixdict[word[i]][word[i+1]] += 1
    
for letter1 in letters: #the purpose of this operation is to get a total for number of letters in a particular letters subdictionary
    for letter2 in letters:
        letterdict[letter1]+=matrixdict[letter1][letter2]
for letter1 in letters:
    for letter2 in letters:
        matrixdict[letter1][letter2]=(matrixdict[letter1][letter2]/letterdict[letter1])  #divides the raw values of the original matrix dict by total value to create a percent

#matrixdict['a']['c'] will now show a percentage rather than raw input
        
def iswordviable(test):   #this function was designed to lookup in the rawdictionary
    word=str(test)
    for i in range(len(word) - 1):
        if matrixdict[word[i]][word[i+1]]==0:
            return False
    return True

def probofword(test): #this function is designed to work with percentages which semi standardizes the values
    word=str(test)
    for i in range(len(word) - 1):
        if matrixdict[word[i]][word[i+1]]<0.0020:
            #could add a line here to lookup in a larger dictionary to eliminate false positives
            return False
    return True

def main ():
    print(iswordviable('examqle')) #decides whether or not a word is viable
    print(probofword('examqle')) #shows probabilites in a word
    blist=[x for x in matrixdict['b'].items()]
    blist.sort()
    print(blist)
if __name__=="__main__":
    main()
