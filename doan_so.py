import random

secret = random.randint(1, 10)
tries = 5
print("🎯 Đoán số 1–10 (5 lượt)")

while tries > 0:
    guess = input(f"👉 Nhập số ({tries} lượt): ")
    if not guess.isdigit(): 
        print("Nhập số!"); continue
    guess = int(guess)
    if guess == secret: 
        print("✅ Đúng! Bạn thắng 🎉"); break
    print("↑ Lớn hơn" if guess < secret else "↓ Nhỏ hơn")
    tries -= 1
else:
    print(f"❌ Hết lượt! Số đúng là {secret}")
