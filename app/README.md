# NatLanUtils Module

The **NatLanUtils** module is a Python utility library designed for preprocessing and analyzing text data, particularly tweets. It provides easy-to-use functions for cleaning and analyzing textual information.

## Features

### TweetPreprocessing Class

The `TweetPreprocessing` class within this module offers functionalities for cleaning and preprocessing tweets. It includes methods for:

- Removing URLs from tweets.
- Removing mentions (e.g., @username) from tweets.
- Eliminating non-letter characters, keeping only alphabetic characters.
- Removing single-letter words.
- Lowercasing all text.
- Optionally, removing stopwords (provided as a list) from the text.

### TextDistribution Class

The `TextDistribution` class allows you to create frequency tables for text data. It offers a method for:

- Generating a frequency table of word occurrences in a list of texts.
- Calculating absolute and relative frequencies.
- Calculating cumulative frequencies.
- Ranking words by frequency.

## Installation

You can easily install the **NatLanUtils** module using `pip`:

```bash
pip install natlanutils
```

## Usage

Here's a basic example of how to use the **NatLanUtils** module in your Python code:

```python
from NatLanUtils import TweetPreprocessing, TextDistribution

# Initialize the TweetPreprocessing and TextDistribution classes
tweet_preprocessor = TweetPreprocessing()
text_distribution = TextDistribution()

# Clean tweet data
cleaned_tweets = tweet_preprocessor.clean(tweet_list, stopwords=stopwords)

# Handle duplicate tweets and get frequency information
unique_tweets, duplicate_tweets, most_common_tweets = tweet_preprocessor.handle_duplicates(cleaned_tweets)

# Analyze word frequency in the cleaned tweets
word_frequency_df = text_distribution.frequency_table(cleaned_tweets)
```

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Contact

- Author: Francesco Ortame
- Email: francesco.ortame@gmail.com
