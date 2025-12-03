def get_num_words(text):
    words = text.split()
    return len(words)


def character_counts(text):
    text = text.lower()
    counts = {}
    
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts


def sort_letters(text):
    counts = character_counts(text)
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts 
