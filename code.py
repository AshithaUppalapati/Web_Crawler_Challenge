import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import pandas as pd
import sys


# Crawler function to scape the text data
def crawler(url, n, stopwords):

    m = requests.get(url)
    data = []
    soup = BeautifulSoup(m.content, 'html.parser')
    h2s = soup.find_all('h2')
    for h2 in h2s:
        if h2.text == 'History':
            temp_data = []
            for tag in h2.next_siblings:
                if tag.name == 'h2':
                    break
                elif tag.name == 'p':
                    temp_data.append(tag.get_text())
        else:
            continue
        data.append(temp_data)
    # Convert text into lower case to avoid counting same word multiple times e.g. On - 15, on - 12
    text = ''.join(str(x).lower() for x in data[0])
    # Cleaning the data - Remove citations e.g. MS-DOS[12]
    lines = ''.join(re.sub('\[\d+\]', '', text))
    # Cleaning the data - Remove punctuations to avoid counting same word multiple times e.g. 'employees.', 'employees'
    res = re.sub(r'[^\w\s]', '', lines)
    # Calling the freqency count function
    freq(res, n, stopwords)


# Counts and displays Frequency of each word
def freq(str, x, nowords):

    # break the string into list of words
    str_list = str.split()
    strs = [word for word in str_list if word not in nowords]
    frequency = Counter(strs)
    # Creating Dataframe for simplicity and displaying
    df = pd.DataFrame.from_records(frequency.most_common(), columns=[
                                   'Word', '# of occurences'])
    df.style.hide(axis='index')
    df2 = df.head(x)
    print(df2.to_string(index=False))


# driver code
if __name__ == "__main__":

    URL = "https://en.wikipedia.org/wiki/Microsoft"
    sys.argv = sys.argv[1:]
    exclude = []
    n, flag = 10, True
    while len(sys.argv) > 0:
        code = sys.argv[0]
        if code.isdigit() and flag:
            n = int(code)
            flag = False
        else:
            exclude.append(code.lower())
        sys.argv = sys.argv[1:]
    # calling crawler function
    crawler(URL, n, exclude)
