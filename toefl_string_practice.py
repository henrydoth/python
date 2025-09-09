# -*- coding: utf-8 -*-
"""
TOEFL String & Pronoun Practice with Python
"""

# -------------------------------
# Bài tập 1: Đếm số từ trong câu
# -------------------------------
print("\n=== Bài tập 1: Đếm từ trong câu ===")
sentence1 = "The mother took her son to the doctor's office because he was feeling sick."
words = sentence1.split()
print("Câu:", sentence1)
print("Số từ:", len(words))


# -------------------------------------
# Bài tập 2: Tìm tất cả đại từ trong câu
# -------------------------------------
print("\n=== Bài tập 2: Tìm đại từ ===")
sentence2 = "They saw Steve and I at the movies last night after class."
pronouns = ["I", "you", "he", "she", "it", "we", "they",
            "me", "him", "her", "us", "them"]

print("Câu:", sentence2)
for word in sentence2.split():
    clean_word = word.strip(".,")
    if clean_word.lower() in [p.lower() for p in pronouns]:
        print("Found pronoun:", clean_word)


# ---------------------------------
# Bài tập 3: Sửa đại từ sai
# ---------------------------------
print("\n=== Bài tập 3: Sửa đại từ sai ===")
sentence3 = "Mary and Mark invited theirs parents to see their new apartment."
print("Câu sai:", sentence3)
corrected = sentence3.replace("theirs parents", "their parents")
print("Câu đúng:", corrected)


# ---------------------------------
# Bài tập 4: Thay thế đại từ bằng danh từ
# ---------------------------------
print("\n=== Bài tập 4: Thay thế đại từ ===")
sentence4 = "She gave it to him."
print("Trước:", sentence4)
sentence4 = sentence4.replace("She", "Sally").replace("it", "the book").replace("him", "John")
print("Sau:", sentence4)


# ---------------------------------
# Bài tập 5: Viết hàm kiểm tra đại từ
# ---------------------------------
print("\n=== Bài tập 5: Kiểm tra loại đại từ ===")
def check_pronoun(word):
    subject_pronouns = ["I","you","he","she","it","we","they"]
    object_pronouns  = ["me","you","him","her","it","us","them"]
    if word in subject_pronouns:
        return "Subject pronoun"
    elif word in object_pronouns:
        return "Object pronoun"
    else:
        return "Not a pronoun"

test_words = ["him", "they", "apple"]
for w in test_words:
    print(w, "→", check_pronoun(w))
