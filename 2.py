# Python code to Reverse each word
# of a Sentence individually

# Function to Reverse words
def reverseWordSentence(Sentence):
    # Spliting the Sentence into list of words.
    words = Sentence.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique

    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)

    return newSentence

def Largest_word(Sentence):
    pool = Sentence.split()
    pool.sort(key=len, reverse=True)
    return pool[0]

def middle_Word(Sentence):
    d =Sentence.split(" ")
    print(d)
    if len(d) % 2 == 0:
        return d[int(len(d) / 2)], d[int(len(d) / 2 - 1)]
    else:
        return d[int(len(d) // 2)]


Sentence = input("Enter a String")
print("Reverse:",reverseWordSentence(Sentence))

print("Largest Word:",Largest_word(Sentence))

print("Middle Word:",middle_Word(Sentence))

