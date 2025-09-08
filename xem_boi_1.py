import random

# Bát quái cơ bản (dùng dạng nhị phân: 1 = dương, 0 = âm)
bat_quai = {
    (1,1,1): "乾 - Kiền (Trời)",
    (0,0,0): "坤 - Khôn (Đất)",
    (1,0,0): "震 - Chấn (Sấm)",
    (0,1,1): "巽 - Tốn (Gió)",
    (0,1,0): "坎 - Khảm (Nước)",
    (1,0,1): "離 - Ly (Lửa)",
    (0,0,1): "艮 - Cấn (Núi)",
    (1,1,0): "兌 - Đoài (Đầm)"
}

# Bảng 64 quẻ (thượng + hạ)
que_64 = {
    ("乾","乾"): ("乾 - Kiền", "Đại cát, khởi đầu hanh thông."),
    ("坤","坤"): ("坤 - Khôn", "Nhu thuận, tốt cho hợp tác, nhưng dễ bị động."),
    ("坎","坎"): ("坎 - Khảm", "Nguy hiểm, phải thận trọng."),
    ("離","離"): ("離 - Ly", "Minh triết, sáng suốt, thuận lợi về văn chương."),
    # 👉 ở đây chỉ demo vài quẻ, có thể bổ sung đủ 64 quẻ
}

def gieo_que():
    # Gieo 6 hào (0 = âm, 1 = dương)
    lines = [random.choice([0,1]) for _ in range(6)]
    
    # Hạ quái (hào 1-3), Thượng quái (hào 4-6)
    ha_quai = tuple(lines[0:3])
    thuong_quai = tuple(lines[3:6])
    
    # Tra tên quái
    ha_ten = bat_quai.get(ha_quai, "Unknown")
    thuong_ten = bat_quai.get(thuong_quai, "Unknown")
    
    # Rút ra quẻ chính
    que_info = que_64.get((thuong_ten.split()[0], ha_ten.split()[0]), ("Chưa định nghĩa", "Chưa có ý nghĩa"))
    
    return lines, ha_ten, thuong_ten, que_info

# Gieo thử
lines, ha_ten, thuong_ten, (ten_que, y_nghia) = gieo_que()

print("🔮 Quẻ Kinh Dịch của bạn hôm nay:")
for i, line in enumerate(lines, 1):
    print(f"Hào {i}: {'Dương (———)' if line==1 else 'Âm (— —)'}")

print(f"\nHạ quái: {ha_ten}")
print(f"Thượng quái: {thuong_ten}")
print(f"👉 Quẻ: {ten_que}")
print(f"📖 Ý nghĩa: {y_nghia}")
