import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import pandas as pd


def crawler(url, n = 10, stopwords = []):
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
    text = ''.join(str(x) for x in data[0])
    # print(text)
    #freq(text)
    lines = ''.join(re.sub('\[\d+\]', '', text))
    # print(lines)
    res = re.sub(r'[^\w\s]', '', lines)
    # print(res)
    freq(res, n, stopwords)
        # text = ''.join(str(e) for e in data)
        # result = re.sub(r'[^a-zA-Z]', " ", text)
        # print(result)


def freq(str, x=10, stopwords = []):

    # break the string into list of words
    str_list = str.split()
    strs = [word for word in str_list if word.lower() not in stopwords]
    frequency = Counter(strs)
    df = pd.DataFrame.from_records(frequency.most_common(), columns=['Word','# of occurences'])
    # df = pd.DataFrame.from_dict(frequency, orient='index').reset_index()
    # df = df.rename(columns={'index':'Word', 0:'# of occurences'})
    df.style.hide(axis='index')
    #df.sort_values(by='# of occurences', ascending=False)
    #print(df.dtypes)
    df2 = df.head(x)
    print(df2.to_string(index=False))
    # print(df.nlargest(x, '# of occurences'))
    #print(df['# of occurences'].nlargest(n=10))
    # for word in frequency:
    # 	print('Frequency of ', word, 'is :', frequency[word])


# driver code
if __name__ == "__main__":

    URL = "https://en.wikipedia.org/wiki/Microsoft"

    # calling crawler function
    crawler(URL)
