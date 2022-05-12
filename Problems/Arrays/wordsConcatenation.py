"""
Given a string and a list of words, find all the starting indices of substrings in the given string that 
are a concatenation of all the given words exactly once without any overlapping of words. 
It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""

input = [
    {
        "string": "catfoxcat",
        "words": ["cat", "fox"],
        "output": [0, 3]
    },
    {
        "string": "catcatfoxfox",
        "words": ["cat", "fox"],
        "output": [3]
    }
]

def findWordConcatenation(string, words):
    wordLen = len(words[0])
    numOfWords = len(words)
    wordsFreq = {}
    result = []

    for word in words:
        if word not in wordsFreq:
            wordsFreq[word] = 1
        else:
            wordsFreq[word] += 1

    for fastPtr in range((len(string) - wordLen * numOfWords) + 1):
        seenWords = {}
        
        for i in range(numOfWords):
            nextWordStartIndex = fastPtr + i * wordLen
            newWord = string[nextWordStartIndex: nextWordStartIndex + wordLen]

            # if new word doesnt match, we don't need to continue
            if newWord not in wordsFreq:
                break
            
            # adds new word in to hashmap of seen words
            if newWord not in seenWords:
                seenWords[newWord] = 0
            seenWords[newWord] += 1

            if seenWords[newWord] > wordsFreq[newWord]:
                break

            if i + 1 == numOfWords:
                result.append(fastPtr)
    return result


    
for i in range(len(input)):
    print("input " + str(i + 1) + ": ", end="")

    if findWordConcatenation(input[i]["string"], input[i]["words"]) == input[i]["output"]:
        print("Correct! ✅")
    else:
        print("Not Quite! ❌")