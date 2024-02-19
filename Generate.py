import tkinter as tk
import tkinter.font as tkFont
import re, json, random

def load_probabilities(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def post_process_text(text):
    cleaned_text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)  # 去除重複連續的詞語
    return cleaned_text

def generate_text(start_ngram, length, probabilities):
    result = [start_ngram]
    current_ngram = start_ngram

    all_chars = list(set("".join(probabilities.keys())))

    for _ in range(length - 1):
        if current_ngram not in probabilities or not probabilities[current_ngram]:
            next_char = random.choice(all_chars)
        else:
            next_chars = probabilities[current_ngram]
            next_char = random.choices(list(next_chars.keys()), list(next_chars.values()))[0]

        result.append(next_char)
        if len(current_ngram + next_char) > len(start_ngram):
            current_ngram = current_ngram[1:] + next_char
        else:
            current_ngram += next_char

    return ''.join(result)

def create_gui(probabilities):
    def on_generate():
        start_ngram = entry.get()
        generated_text = generate_text(start_ngram, 500, probabilities)
        generated_text = post_process_text(generated_text) # 新增後處理步驟
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, generated_text)

    window = tk.Tk()
    window.title("文本生成器")

    label_font = tkFont.Font(size=14, family="Arial")
    entry_font = tkFont.Font(size=12, family="Arial")
    button_font = tkFont.Font(size=12, family="Arial")
    text_font = tkFont.Font(size=12, family="Arial")

    label = tk.Label(window, text="請輸入文本的開頭：", font=label_font)
    label.pack(pady=10)

    entry = tk.Entry(window, font=entry_font)
    entry.pack(pady=5)

    generate_button = tk.Button(window, text="生成文本", command=on_generate, font=button_font)
    generate_button.pack(pady=5)

    text_display = tk.Text(window, height=15, width=60, font=text_font)
    text_display.pack(pady=10)

    window.mainloop()

probabilities = load_probabilities('Output.txt')
create_gui(probabilities)
