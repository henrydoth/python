### 1. `import random`

- **`import`**: nạp (load) một thư viện có sẵn trong Python.
- **`random`**: thư viện chuyên tạo số ngẫu nhiên.

👉 Mình dùng nó để sinh ra số bí mật mà người chơi cần đoán.

------

### 2. `secret = random.randint(1, 10)`

- **`random.randint(a, b)`**: trả về một số nguyên ngẫu nhiên trong khoảng từ **a đến b**, có cả hai đầu.
- Ở đây: chọn một số ngẫu nhiên trong `[1, 10]`.
- Ví dụ: có thể là 3, 7, hoặc 10.

👉 `secret` chính là số bí mật.

------

### 3. `tries = 5`

- Gán số lượt chơi còn lại là 5.
- Mỗi lần đoán sai sẽ giảm đi 1.

------

### 4. `print("🎯 Đoán số 1–10 (5 lượt)")`

- In ra màn hình hướng dẫn trò chơi.
- **`print()`**: hàm hiển thị nội dung.

------

### 5. `while tries > 0:`

- **`while`**: vòng lặp → lặp lại các bước bên trong chừng nào điều kiện còn đúng.
- Điều kiện: `tries > 0` (còn lượt).
- Khi hết lượt (`tries == 0`), vòng lặp dừng.

------

### 6. `guess = input(f"👉 Nhập số ({tries} lượt): ")`

- **`input()`**: yêu cầu người dùng nhập dữ liệu từ bàn phím (luôn trả về chuỗi).
- **`f"..."`**: f-string, cho phép chèn giá trị biến vào trong chuỗi.
  - `{tries}` sẽ được thay bằng số lượt còn lại.