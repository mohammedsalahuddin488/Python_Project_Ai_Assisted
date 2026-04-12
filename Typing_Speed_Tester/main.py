import time
import random

sentenses = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that can be improved with practice.",
    "Python is a popular programming language.",
    "The rain in Spain stays mainly in the plain.",
    "A journey of a thousand miles begins with a single step."
]

# def measure_accuracy(original, typed):
#     original_words = original.split()
#     typed_words = typed.split()
#     correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
#     accuracy = (correct_words / len(original_words)) * 100
#     return accuracy

def measure_accuracy(original, typed):
    # ----- WORD ACCURACY -----
    original_words = original.split()
    typed_words = typed.split()

    correct_words = sum(
        1 for o, t in zip(original_words, typed_words) if o == t
    )

    if len(original_words) == 0:
        word_accuracy = 0
    else:
        word_accuracy = (correct_words / len(original_words)) * 100

    # ----- CHARACTER ACCURACY -----
    correct_chars = sum(
        1 for o, t in zip(original, typed) if o == t
    )

    if len(original) == 0:
        char_accuracy = 0
    else:
        char_accuracy = (correct_chars / len(original)) * 100

    return round(word_accuracy, 2), round(char_accuracy, 2)

def typing_speed_tester():
    test_sentence = random.choice(sentenses)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input('\n Start typing here: \n')
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_seconds = time_taken 
    words_typed = len(user_input.split())

    print("Results:")
    print(f"Time taken: {time_taken_seconds:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {words_typed / time_taken_seconds:.2f} words per second  ")
    word_accuracy, char_accuracy = measure_accuracy(test_sentence, user_input)
    print(f"Word Accuracy: {word_accuracy:.2f}%")   
    print(f"Character Accuracy: {char_accuracy:.2f}%")


typing_speed_tester()