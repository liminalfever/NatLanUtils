"""NatLanUtils Module"""
import re
from collections import Counter
import pandas as pd
from tqdm import tqdm

class TweetPreprocessing:
    """TweetPreprocessing class for preprocessing tweets."""

    def __init__(self):
        """Constructor for TweetPreprocessing class"""

        self.url_pattern = re.compile(r'http\S+')
        self.mention_pattern = re.compile(r'@[A-Za-z0-9_]+')
        self.non_letter_pattern = re.compile(r'[^#a-zA-Zàèéìíîòóùú]')
        self.single_letter_pattern = re.compile(r'\b\w\b')

    def clean(self, text_list: list[str], stopwords: list[str] = None) -> list[str]:
        """
        Clean the given text data.

        Args:
            text_list (list[str]): List of texts to clean.
            stopwords (list[str], optional): List of stopwords to remove. Defaults to None.

        Returns:
            list[str]: List of cleaned texts.
        """

        clean_text = []
        stopwords_set = set(stopwords) if stopwords else set()

        with tqdm(total=len(text_list)) as pbar:
            for text in text_list:
                text = self.url_pattern.sub('', text)  # remove urls
                text = self.mention_pattern.sub('', text)  # remove mentions
                text = self.non_letter_pattern.sub(' ', text)  # remove non-letters
                text = self.single_letter_pattern.sub('', text)  # remove single letters
                text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
                text = text.lower()  # lowercase
                if stopwords_set is not None:
                    words = text.split()
                    filtered_words = [word for word in words if word not in stopwords_set]  # remove stopwords  
                    text = ' '.join(filtered_words)
                clean_text.append(text)
                pbar.update(1)
            
            return clean_text
    
    def handle_duplicates(self, text_list: list[str], get_most_common: int = 10, get_info: bool = True):
        """
        Remove duplicate texts from the given list.

        Args:
            text_list (list[str]): List of texts to remove duplicates from.
            get_most_common (int, optional): Number of most common texts to return. Defaults to 10.
            get_info (bool, optional): Whether to return the number of duplicates removed. Defaults to True.

        Returns:
            list[str]: List of texts without duplicates.
        """

        uniques = set(text_list)
        len_tot = len(text_list)
        len_unique = len(uniques)

        def list_duplicates(seq):
            seen = set()
            seen_add = seen.add
            seen_twice = set(x for x in seq if x in seen or seen_add(x))
            return list(seen_twice)   
        duplicates = list_duplicates(text_list)
        if get_info:
            print(f"Removed {len_tot-len_unique} duplicates out of {len_tot} tweets ({round((len_tot-len_unique)*100/len_tot, 2)}%).")
            print(f"{len_unique} unique tweets, {len(duplicates)} unique duplicates.")
        
        most_common = Counter(text_list).most_common(get_most_common)

        return uniques, duplicates, most_common
    

class TextDistribution:

    def __init__(self):
        """
        Initialize the TextDistribution class.
        """

    def frequency_table(self, text_list: list[str]) -> pd.DataFrame:
        """
        Generates a frequency table of word occurrences in the given list of texts.

        Args:
            text_list (list[str]): A list of texts.

        Returns:
            pd.DataFrame: A DataFrame containing columns for word, absolute frequency,
                        relative frequency, cumulative frequency, and position.

        """

        word_frequency = Counter()

        with tqdm(total=len(text_list), desc='Processing texts') as pbar:
            for text in text_list:
                words = text.split()
                word_frequency.update(words)
                pbar.update(1)

        total_words = sum(word_frequency.values())

        word_frequency_tuple = list(word_frequency.items())
        word_frequency_df = pd.DataFrame(word_frequency_tuple, columns=['word', 'abs_freq'])
        word_frequency_df.sort_values('abs_freq', inplace=True, ascending=False)

        word_frequency_df['rel_freq'] = word_frequency_df['abs_freq'] / total_words
        word_frequency_df['cum_freq'] = word_frequency_df['rel_freq'].cumsum()
        word_frequency_df['position'] = range(1, len(word_frequency_df) + 1)

        return word_frequency_df
