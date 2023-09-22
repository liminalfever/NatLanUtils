from natlanutils.natlanutils import TweetPreprocessing, TextDistribution
import pandas as pd

example_texts = [
    "Just finished reading an amazing book! Highly recommended. #booklovers",
    "Just finished reading an amazing book! Highly recommended. #booklovers",
    "Just finished reading an amazing book! Highly recommended. #booklovers",
    "Good morning, @NatLanUtils! How's the weather today?",
    "Check out this cool website: https://www.example.com",
    "Check out this cool website: https://www.example.com",
    "Received an A+ on my latest project. Feeling proud! 😊 #achievement",
    "Received an A+ on my latest project. Feeling proud! 😊 #achievement",
    "Received an A+ on my latest project. Feeling proud! 😊 #achievement",
    "Received an A+ on my latest project. Feeling proud! 😊 #achievement",
    "The quick brown fox jumps over the lazy dog.",
    "I can't believe it's already September. Time flies!",
    "I can't believe it's already September. Time flies!",
    "I can't believe it's already September. Time flies!",
    "Python is such a versatile language with a vibrant community. #Python",
    "Python is such a versatile language with a vibrant community. #Python",
    "Let's meet at the café at 3:00 PM. ☕",
    "Working on my #NLP project. Natural Language Processing is fascinating!",
    "Don't worry, be happy! 🎶😄"
    "Don't worry, be happy! 🎶😄"
    "Don't worry, be happy! 🎶😄"
    "Don't worry, be happy! 🎶😄"
    "Don't worry, be happy! 🎶😄"
    "Don't worry, be happy! 🎶😄"
]

text_preprocessing = TweetPreprocessing()

# test text cleaner
clean_texts = text_preprocessing.clean(example_texts)

raw_vs_clean = pd.DataFrame({'original_text': example_texts, 'clean_text': clean_texts})
print('Original vs Clean:\n', raw_vs_clean, '\n')

# test duplicate handler
unique_texts = text_preprocessing.handle_duplicates(clean_texts)
print('\nUnique texts:\n', unique_texts)
