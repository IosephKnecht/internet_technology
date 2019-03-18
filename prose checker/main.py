from math import pow, sqrt

delimiters = ['.', ',', '?', '!']
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


def calculate_standard_deviation(elements, average_value):
    hydrate_value = 0
    for element in elements:
        hydrate_value += pow(element.__len__() - average_value, 2)

    return sqrt(hydrate_value / elements.__len__())


def calculate_for_word(sentence):
    words = sentence.split(" ")
    word_count = words.__len__()
    average_length_word = 0
    common_vowel_count = 0
    common_consonant_count = 0

    def calculate_sym(word):
        vowel_count = 0
        consonant_count = 0

        for sym in word:
            if vowels.__contains__(sym.lower()):
                vowel_count += 1
            elif consonants.__contains__(sym.lower()):
                consonant_count += 1

        return {
            'vowels_in_word': vowel_count,
            'consonants_in_word': consonant_count,
        }

    for word in words:
        bundle = calculate_sym(word)
        common_vowel_count += bundle['vowels_in_word']
        common_consonant_count += bundle['consonants_in_word']

        average_length_word += word.__len__()

    average_length_word /= word_count

    deviation = calculate_standard_deviation(words, average_length_word)

    return {
        'sentence_count': sentence.__len__(),
        'average_length_word_in_sentence': average_length_word,
        'word_count_in_sentence': word_count,
        'vowels_in_sentence': common_vowel_count,
        'consonants_in_sentence': common_consonant_count,
        'standard_deviation_in_sentence': deviation
    }


filename = "C:\\Users\\IosephKnecht\\PycharmProjects\\prose_checker\\prose.txt"

sentences = None

with open(filename, 'r') as file:
    sentences = file.read().split(".")

sentence_count = sentences.__len__()
average_length_sentence = 0
average_length_word = 0
word_count = 0
vowel_count = 0
consonant_count = 0
word_deviation = 0
deviation_for_sentences = 0

for sentence in sentences:
    word_bundle = calculate_for_word(sentence)

    average_length_sentence += word_bundle['sentence_count']
    average_length_word += word_bundle['average_length_word_in_sentence']
    word_count += word_bundle['word_count_in_sentence']
    vowel_count += word_bundle['vowels_in_sentence']
    consonant_count += word_bundle['consonants_in_sentence']
    word_deviation += word_bundle['standard_deviation_in_sentence']

average_length_word /= sentence_count
average_length_sentence /= sentence_count
word_deviation /= sentence_count
sentence_deviation = calculate_standard_deviation(sentences, average_length_sentence)

print("words = {0}\n"
      "sentences = {1}\n"
      "average length word = {2}\n"
      "average length sentence = {3}\n"
      "word deviation = {4}\n"
      "sentence deviation = {5}\n"
      "vowels = {6}\n"
      "consonants = {7}\n"
      .format(word_count, sentence_count, average_length_word,
              average_length_sentence, word_deviation,
              sentence_deviation, vowel_count, consonant_count))
