import io
import os

path = r"C:\Users\CTX\AppData\Local\Temp\opencode\hotel_raw.html"
t = io.open(path, encoding="utf-8", errors="replace").read()
keys = ["逐句分析", "隔音", "舒适度", "设施", "位置", "服务", "清洁度",
        "未提及", "提及", "模型就绪", "负面", "正面", "汽车喇叭声", "aspect"]
out = [f"len={len(t)}"]
for k in keys:
    out.append(("FOUND " if k in t else "MISS  ") + k)
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_dom_check.txt"),
        "w", encoding="utf-8").write("\n".join(out))
