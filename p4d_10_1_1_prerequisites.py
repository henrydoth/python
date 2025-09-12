import altair as alt
import pandas as pd
import numpy as np
from pathlib import Path

# Tạo DataFrame
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 1, 1, 1, 1]  # y phải là list, không phải số đơn
}).assign(z=lambda t: t.x**2 + t.y)

print(df)

# Vẽ thử với Altair
chart = alt.Chart(df).mark_line(point=True).encode(
    x='x:Q',
    y='z:Q',
    tooltip=['x', 'y', 'z']
).properties(
    title='Demo Altair: z = x^2 + 1'
)

# Lưu ra HTML để xem trong trình duyệt
out_dir = Path("charts")
out_dir.mkdir(exist_ok=True)
out_file = out_dir / "altair_demo.html"
chart.save(out_file.as_posix())
print(f"Saved chart to: {out_file}")
