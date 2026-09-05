import string
def text_analysis(paragraph):
    translator=str.maketrans("","",string.punctuation)
    cleaned_paragraph=paragraph.translate(translator)

    words=cleaned_paragraph.split()
    word_count=len(words)

    freq={}
    for word in words:
        word_lower=word.lower()
        freq[word_lower]=freq.get(word_lower,0)
        freq[word_lower]+=1
    longest_word=max(words,key=len) if words else None
    shortest_word=min(words,key=len) if words else None
    sentences=[s for s in paragraph.replace("!",".").replace("?",".").split(".") if s.strip()]
    sentence_count=len(sentences)

    avg_word_length=sum(len(word) for word in words)/word_count if word_count else None

    return{
        "word_count":word_count,
        "sentence_count":sentence_count,
        "average_word_length":avg_word_length,
        "longest_word":longest_word,
        "shortest_word":shortest_word,
        "word_frequencies":freq
    }
paragraph=input("Enter a paragraph of text:")
analysis=text_analysis(paragraph)
print(f"\nWord Count: {analysis['word_count']}")
print(f"\nSentence Count: {analysis['sentence_count']}")
print(f"\nAverage Word Length: {analysis['average_word_length']:.3f}")
print(f"\nLongest Word: {analysis['longest_word']}")
print(f"\nShortest Word: {analysis['shortest_word']}")
print(f"\nWord Frequencies:")
for word,count in analysis['word_frequencies'].items():
    print(f"{word}:{count}")

# import string
# from collections import Counter

# def text_analysis(paragraph):
#     # Remove punctuation and split into lowercase words
#     words = paragraph.translate(str.maketrans('', '', string.punctuation)).lower().split()
#     sentences = [s for s in paragraph.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    
#     return {
#         "word_count": len(words),
#         "sentence_count": len(sentences),
#         "avg_word_length": sum(len(w) for w in words) / len(words) if words else 0,
#         "longest_word": max(words, key=len) if words else None,
#         "shortest_word": min(words, key=len) if words else None,
#         "word_frequencies": Counter(words)
#     }

# # Execution
# p = input("Enter a paragraph: ")
# data = text_analysis(p)

# for key, value in data.items():
#     if key != "word_frequencies":
#         print(f"{key.replace('_', ' ').capitalize()}: {value}")

# print("\nWord Frequencies:")
# for word,count in data["word_frequencies"].items():
#     print(f'\n{word}:{count}')