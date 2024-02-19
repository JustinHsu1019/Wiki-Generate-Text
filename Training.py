from collections import defaultdict
import json
from tqdm import tqdm

def generate_probability_set(file_path, output_path, ngram_size=3, write_frequency=10000): # 修改 ngram size to 3
    transition_counts = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()[:1000000]

    total_ngrams = len(text) - ngram_size
    probabilities = {}

    for i in tqdm(range(total_ngrams), desc="Processing n-grams"):
        current_ngram = text[i:i+ngram_size]
        next_char = text[i + ngram_size]
        transition_counts[current_ngram][next_char] += 1

        if i % write_frequency == 0:
            update_probabilities(transition_counts, probabilities)
            write_probabilities(output_path, probabilities)

    update_probabilities(transition_counts, probabilities)
    write_probabilities(output_path, probabilities)

def update_probabilities(transition_counts, probabilities):
    for current_ngram, transitions in transition_counts.items():
        total = sum(transitions.values()) + len(transitions)  # 加入拉普拉斯平滑
        probabilities[current_ngram] = {char: (count + 1) / total for char, count in transitions.items()}

def write_probabilities(output_path, probabilities):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(probabilities, file, ensure_ascii=False)

generate_probability_set('DataSet.txt', 'Output.txt')
