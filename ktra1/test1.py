
with open("D:/min.txt", "r") as file:
    content = file.read()

    words = content.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    print("Thống kê và tần xuất xuất hiện của các từ trong file:")
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq} lần")
