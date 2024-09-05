import os
from bs4 import BeautifulSoup
import jieba
from collections import defaultdict
import pickle
import math


def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = [word for word in jieba.cut(text) if len(word) >= 2]
    return words


def build_inverted_index(html_files, urls):
    inverted_index = {}
    for html_file, url in zip(html_files, urls):
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
            words = parse_html(html_content)
            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = {'counts': defaultdict(int), 'score': {}}
                inverted_index[word]['counts'][url] += 1

    total_docs = len(urls)
    for entry in inverted_index.values():
        idf = {url: math.log(total_docs / (1 + len(entry['counts']))) for url in entry['counts']}
        for url, count in entry['counts'].items():
            if count > 0:
                tf = count
                entry['score'][url] = (1 + math.log(tf)) * idf[url]
            else:
                entry['score'][url] = 0

    return inverted_index


def load_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]
    return urls


def build_term_vectors(inverted_index, total_docs, documents):
    term_vectors = {}
    idf_cache = {}

    for term, entry in inverted_index.items():
        idf = math.log(total_docs / (1 + len(entry['counts'])))
        idf_cache[term] = idf
        for url, score in entry['score'].items():
            if url not in term_vectors:
                term_vectors[url] = defaultdict(float)
            term_vectors[url][term] = score

    for url, vector in term_vectors.items():
        magnitude = math.sqrt(sum(value ** 2 for value in vector.values()))
        for term in vector:
            vector[term] /= magnitude

    idf_cache['total_docs'] = total_docs
    return term_vectors, idf_cache


def build_query_vector(query_words, inverted_index, idf_cache):
    query_vector = defaultdict(float)
    total_docs = idf_cache['total_docs']

    for term in query_words:
        if term in inverted_index:
            idf = idf_cache.get(term, math.log(total_docs / (1 + len(inverted_index[term]['counts']))))
            tf = query_words.count(term)
            query_vector[term] = (1 + math.log(tf)) * idf

    magnitude = math.sqrt(sum(value ** 2 for value in query_vector.values()))
    for term in query_vector:
        query_vector[term] /= magnitude

    return query_vector


def cosine_similarity(v1, v2):
    dot_product = sum(v1[key] * v2.get(key, 0) for key in v1)
    magnitude_v1 = math.sqrt(sum(value ** 2 for value in v1.values()))
    magnitude_v2 = math.sqrt(sum(value ** 2 for value in v2.values()))
    return dot_product / (magnitude_v1 * magnitude_v2)


def compare_query_with_documents(query_vector, document_vectors):
    similarities = []

    for url, doc_vector in document_vectors.items():
        similarity = cosine_similarity(query_vector, doc_vector)
        similarities.append((url, similarity))

    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:20]
    return sorted_similarities


directory_path = r"C:\Users\azi\Desktop\pycharm_check\pythonProject2\第二天ai"

urls_file = os.path.join(directory_path, 'url_to_filename.txt')
urls = load_urls(urls_file)
html_files = [os.path.join(directory_path, f'{i}.html') for i in range(len(urls))]

data_file_path = os.path.join(directory_path, 'search_data.pkl')


def result(query: str) -> list:
    words = [word for word in jieba.cut(query) if len(word) >= 2]

    if os.path.exists(data_file_path):
        with open(data_file_path, 'rb') as data_file:
            search_data = pickle.load(data_file)
            inverted_index = search_data['inverted_index']
            document_vectors = search_data['document_vectors']
            idf_cache = search_data['idf_cache']
    else:
        inverted_index = build_inverted_index(html_files, urls)
        document_vectors, idf_cache = build_term_vectors(inverted_index, len(urls), urls)
        search_data = {
            'inverted_index': inverted_index,
            'document_vectors': document_vectors,
            'idf_cache': idf_cache
        }
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(search_data, data_file)

    query_vector = build_query_vector(words, inverted_index, idf_cache)
    sorted_results = compare_query_with_documents(query_vector, document_vectors)

    url_lists = [url for url, _ in sorted_results]
    return url_lists
if __name__ == '__main__':
    print(result("鼓足干劲"))