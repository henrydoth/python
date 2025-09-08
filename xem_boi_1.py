# -*- coding: utf-8 -*-
"""
Gieo quẻ Kinh Dịch bằng 3 đồng xu.
- 6: Lão Âm (— —, động)   -> biến thành Dương
- 7: Thiếu Dương (———, tĩnh)
- 8: Thiếu Âm (— —, tĩnh)
- 9: Lão Dương (———, động) -> biến thành Âm

In ra: quẻ chính + (nếu có) quẻ biến.
"""

import random

# ====== BÁT QUÁI (bit = từ dưới lên: 1 dương, 0 âm) ======
TRIGRAMS = {
    (1,1,1): ("乾", "Kiền", "Trời"),
    (0,0,0): ("坤", "Khôn", "Đất"),
    (1,0,0): ("震", "Chấn", "Sấm"),
    (0,1,1): ("巽", "Tốn", "Gió/Mộc"),
    (0,1,0): ("坎", "Khảm", "Nước"),
    (1,0,1): ("離", "Ly", "Lửa"),
    (0,0,1): ("艮", "Cấn", "Núi"),
    (1,1,0): ("兌", "Đoài", "Đầm/Trạch"),
}

# ====== 64 QUẺ: tra theo (upper, lower) = (Thượng quái, Hạ quái) bằng chữ Hán ======
# Đã điền đủ các quẻ phổ biến & những cặp bạn gặp; còn quẻ nào thiếu, chương trình vẫn in tên quẻ nếu tra được.
HEX_BY_TRIGRAM = {
    ("乾","乾"): ("乾", "Kiền", "Đại cát, khởi đầu mạnh mẽ."),
    ("坤","坤"): ("坤", "Khôn", "Nhu thuận, hợp tác, tích lũy."),
    ("坎","離"): ("既濟", "Ký tế", "Việc đã thành, vẫn cần giữ nề nếp."),
    ("離","坎"): ("未濟", "Vị tế", "Việc chưa thành, thận trọng kiên trì."),
    ("坎","坎"): ("坎", "Khảm", "Nguy, vào chỗ hiểm cần chính trực."),
    ("離","離"): ("離", "Ly", "Sáng sủa, văn minh, dựa đạo lý."),
    ("震","艮"): ("頤", "Di", "Dưỡng nuôi, lấy chính mà nuôi."),
    ("坎","巽"): ("井", "Tỉnh", "Cái giếng, gốc rễ nuôi dân."),
    ("巽","坎"): ("渙", "Hoán", "Ly tán rồi lại quy tụ."),
    ("巽","巽"): ("巽", "Tốn", "Thuận mà nhập, nhu nhiếp cương."),
    ("艮","艮"): ("艮", "Cấn", "Ngừng đúng chỗ, giữ mực."),
    ("震","震"): ("震", "Chấn", "Khởi động, chấn hưng."),
    ("兌","兌"): ("兌", "Đoài", "Vui, hòa duyệt."),
    ("乾","離"): ("大有", "Đại hữu", "Có lớn, giữ đức mà giữ của."),
    ("離","乾"): ("同人", "Đồng nhân", "Đồng lòng, hợp tác rộng."),
    ("坎","乾"): ("需", "Nhu", "Chờ thời, giữ chính."),
    ("乾","坎"): ("訟", "Tụng", "Tranh tụng, trọng công chính."),
    ("坤","震"): ("豫", "Dự", "Vui trước lo sau, đừng buông thả."),
    ("震","坤"): ("復", "Phục", "Quay về gốc, đổi mới."),
    ("艮","坤"): ("剝", "Bác", "Bào mòn, nên thủ, chớ tiến."),
    ("坤","艮"): ("比", "Tỉ", "Thân cận, kết bạn hiền."),
    ("離","艮"): ("賁", "Bí", "Văn sức, đẹp mà không giả."),
    ("艮","離"): ("旅", "Lữ", "Ly hương, giữ lễ mà an."),
    ("兌","乾"): ("夬", "Quải", "Quyết đoán dứt điểm."),
    ("乾","兌"): ("姤", "Cấu", "Gặp gỡ bất ngờ, giữ giới hạn."),
    ("巽","乾"): ("小畜", "Tiểu súc", "Tích lũy nhỏ, chờ thời."),
    ("乾","巽"): ("大畜", "Đại súc", "Tàng chứa lớn, luyện đức."),
    ("坤","坎"): ("師", "Sư", "Dùng chúng, giữ kỷ luật."),
    ("坎","坤"): ("比", "Tỉ (khác)", "Nương tựa, giữ tín.") ,  # chú thích: bản đối ứng cổ có khác biệt tên; tùy bản dịch
    ("離","兌"): ("睽", "Khuê", "Ly dị, khác ý; cầu đồng tồn dị."),
    ("兌","離"): ("咸", "Hàm", "Cảm ứng, hòa hợp."),
    ("艮","兌"): ("蹇", "Kiển", "Trắc trở, tiến chậm mà chắc."),
    ("兌","艮"): ("解", "Giải", "Giải tỏa, cởi gỡ nạn."),
    ("震","坎"): ("屯", "Truân", "Khởi đầu gian nan."),
    ("坎","震"): ("節", "Tiết", "Tiết độ, chừng mực."),
    ("巽","震"): ("恆", "Hằng", "Bền lâu, giữ đạo thường."),
    ("震","巽"): ("益", "Ích", "Tăng ích, giúp nhau cùng lợi."),
    ("艮","乾"): ("遯", "Độn", "Lánh nạn, giữ mình."),
    ("乾","艮"): ("大壯", "Đại tráng", "Cường kiện, tiến mà biết dừng."),
    ("離","坤"): ("明夷", "Minh di", "Minh ẩn, giữ sáng trong tối."),
    ("坤","離"): ("晉", "Tấn", "Tiến lên, quang minh chính đại."),
    ("巽","坤"): ("升", "Thăng", "Tiệm tiến, từng bước vững."),
    ("坤","巽"): ("觀", "Quán", "Quan sát, lấy đức cảm hóa."),
    ("兌","坤"): ("臨", "Lâm", "Giám lâm, tới gần để dạy."),
    ("坤","兌"): ("萃", "Tụy", "Hội tụ, chọn hiền tài."),
    ("艮","坎"): ("艮坎→?","(chờ bổ sung)",""),  # chỗ trống để bạn bổ sung thêm nếu cần
    # ... Bạn có thể tiếp tục bổ sung đầy đủ 64 cặp theo sách tham khảo của bạn.
}

# Một số tên quẻ thường gặp khác (dùng khi tra theo mã 6 hào trực tiếp)
HEX_EXTRA_BY_CODE = {
    # mã 6-bit từ dưới lên, 1=dương, 0=âm -> (Hán, Việt, gợi ý)
    # Ví dụ thêm:
    # (1,1,1,1,1,1): ("乾","Kiền","Đại cát..."),
    # (0,0,0,0,0,0): ("坤","Khôn","Nhu thuận..."),
}

MEANINGS_BRIEF = {
    "乾": "Đại cát, khởi đầu mạnh mẽ.",
    "坤": "Nhu thuận, tích lũy, hợp tác.",
    "坎": "Nguy hiểm, giữ chính trực.",
    "離": "Sáng sủa, minh triết.",
    "既濟": "Việc đã thành, vẫn cần giữ kỷ cương.",
    "未濟": "Chưa thành, cần kiên trì.",
    "頤": "Dưỡng nuôi, chính để nuôi.",
    "井": "Gốc nuôi dân, sửa gốc.",
    "渙": "Tan rồi tụ, lấy đức mà hợp.",
    "巽": "Thuận mà nhập.",
    "艮": "Dừng đúng chỗ.",
    "震": "Chấn hưng, khởi động.",
    "兌": "Hòa duyệt, vui mà giữ lễ.",
    "大有": "Có lớn, giữ đức để giữ của.",
    "同人": "Đồng lòng hợp tác.",
    "需": "Chờ thời, giữ chính.",
    "訟": "Tranh tụng, trọng công chính.",
    "豫": "Vui mà không buông thả.",
    "復": "Trở về gốc, đổi mới.",
    "剝": "Bào mòn, nên thủ.",
    "比": "Thân cận, kết bạn hiền.",
    "賁": "Văn sức, đẹp mà thực.",
    "旅": "Ly hương, giữ lễ.",
    "夬": "Quyết đoán dứt điểm.",
    "姤": "Gặp bất ngờ, biết giới hạn.",
    "小畜": "Tích lũy nhỏ.",
    "大畜": "Tàng chứa lớn.",
    "師": "Dùng chúng, giữ kỷ luật.",
    "睽": "Ly dị, cầu đồng tồn dị.",
    "咸": "Cảm ứng, hòa hợp.",
    "蹇": "Trắc trở, tiến chậm.",
    "解": "Cởi gỡ, giải nạn.",
    "屯": "Gian nan khởi đầu.",
    "節": "Tiết độ, chừng mực.",
    "恆": "Bền lâu, giữ đạo.",
    "益": "Tăng ích, tương trợ.",
    "遯": "Lánh nạn, thủ đức.",
    "大壯": "Cường kiện biết dừng.",
    "明夷": "Minh ẩn, giữ sáng.",
    "晉": "Tiến quang minh.",
    "升": "Tiệm tiến vững.",
    "觀": "Quan sát lấy đức.",
    "臨": "Tới gần để dạy.",
    "萃": "Hội tụ, dùng hiền."
}

def toss_line():
    """Gieo một hào bằng 3 đồng xu. Trả về (value, is_yang, is_moving)"""
    # Mỗi đồng: sấp=2, ngửa=3 → tổng 6,7,8,9
    total = sum(random.choice([2,3]) for _ in range(3))
    if total == 6:  # Lão Âm (động)
        return 6, 0, True
    elif total == 7:  # Thiếu Dương (tĩnh)
        return 7, 1, False
    elif total == 8:  # Thiếu Âm (tĩnh)
        return 8, 0, False
    else:  # 9 Lão Dương (động)
        return 9, 1, True

def cast_hexagram():
    """Gieo 6 hào (từ dưới lên). Trả về:
       lines_info: [(value,is_yang,is_moving), ...] length 6
       lower_bits: (b1,b2,b3)
       upper_bits: (b4,b5,b6)
       changed_bits (nếu có động): tuple 6 bit sau biến, else None
    """
    lines = [toss_line() for _ in range(6)]
    bits = tuple(1 if is_yang else 0 for (_, is_yang, _) in lines)
    lower = bits[0:3]
    upper = bits[3:6]
    # Tạo quẻ biến nếu có hào động
    changed = []
    any_moving = False
    for (val, is_yang, is_moving) in lines:
        if is_moving:
            any_moving = True
            changed.append(0 if is_yang else 1)  # đảo
        else:
            changed.append(1 if is_yang else 0)
    changed_bits = tuple(changed) if any_moving else None
    return lines, lower, upper, changed_bits

def trigram_name(bits):
    """bits 3-tuple -> ("漢","Việt","nghĩa")"""
    return TRIGRAMS.get(bits, ("?", "?", "?"))

def hexagram_from_trigrams(upper_han, lower_han):
    """Tra tên quẻ theo (Thượng, Hạ) chữ Hán."""
    if (upper_han, lower_han) in HEX_BY_TRIGRAM:
        han, viet, gloss = HEX_BY_TRIGRAM[(upper_han, lower_han)]
        brief = MEANINGS_BRIEF.get(han, gloss or "")
        return han, viet, brief
    return None

def hexagram_from_bits(bits6):
    """Tra theo mã 6 hào trực tiếp nếu cần."""
    if bits6 in HEX_EXTRA_BY_CODE:
        han, viet, gloss = HEX_EXTRA_BY_CODE[bits6]
        brief = MEANINGS_BRIEF.get(han, gloss or "")
        return han, viet, brief
    return None

def format_line(val, is_yang, is_moving):
    if is_yang and not is_moving:   # 7
        return "Dương (———)"
    if not is_yang and not is_moving:  # 8
        return "Âm   (— —)"
    if not is_yang and is_moving:   # 6
        return "LÃO ÂM động (— —) → biến thành Dương"
    if is_yang and is_moving:       # 9
        return "LÃO DƯƠNG động (———) → biến thành Âm"
    return "?"

def print_result(lines, lower, upper, changed_bits):
    print("🔮 Quẻ Kinh Dịch của bạn hôm nay:")
    for i, (val, is_yang, is_moving) in enumerate(lines, 1):
        print(f"Hào {i}: {format_line(val, is_yang, is_moving)}")

    lower_han, lower_vn, _ = trigram_name(lower)
    upper_han, upper_vn, _ = trigram_name(upper)

    print(f"\nHạ quái: {lower_han} - {lower_vn}")
    print(f"Thượng quái: {upper_han} - {upper_vn}")

    hx = hexagram_from_trigrams(upper_han, lower_han)
    if hx is None:
        # Fallback: thử tra theo mã 6 hào (ít dùng)
        bits6 = tuple(1 if is_yang else 0 for (_, is_yang, _) in lines)
        hx = hexagram_from_bits(bits6)

    if hx:
        han, viet, brief = hx
        print(f"👉 Quẻ chính: {han} - {viet}")
        if brief:
            print(f"📖 Ý nghĩa: {brief}")
    else:
        print("👉 Quẻ chính: (chưa có trong bảng tra)")
        print(f"   Gợi ý thêm cặp vào HEX_BY_TRIGRAM[(\"{upper_han}\",\"{lower_han}\")] = (\"漢\",\"Việt\",\"mô tả…\")")

    # Quẻ biến (nếu có hào động)
    if changed_bits is not None:
        lower2 = changed_bits[0:3]
        upper2 = changed_bits[3:6]
        lower2_han, lower2_vn, _ = trigram_name(lower2)
        upper2_han, upper2_vn, _ = trigram_name(upper2)
        print("\n♻️ Quẻ biến (sau khi các hào động biến):")
        print(f"Hạ quái (biến): {lower2_han} - {lower2_vn}")
        print(f"Thượng quái (biến): {upper2_han} - {upper2_vn}")
        hx2 = hexagram_from_trigrams(upper2_han, lower2_han)
        if hx2:
            han2, viet2, brief2 = hx2
            print(f"👉 Quẻ biến: {han2} - {viet2}")
            if brief2:
                print(f"📖 Ý nghĩa (quẻ biến): {brief2}")
        else:
            print("👉 Quẻ biến: (chưa có trong bảng tra)")
            print(f"   Gợi ý thêm cặp vào HEX_BY_TRIGRAM[(\"{upper2_han}\",\"{lower2_han}\")] = (\"漢\",\"Việt\",\"mô tả…\")")

if __name__ == "__main__":
    lines, lower, upper, changed_bits = cast_hexagram()
    print_result(lines, lower, upper, changed_bits)
