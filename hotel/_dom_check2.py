import io
import os
import re

path = r"C:\Users\CTX\AppData\Local\Temp\opencode\hotel_dom2.txt"
t = io.open(path, encoding="utf-8", errors="replace").read()
m = re.search(r'<div class="status" id="status">(.*?)</div>', t, re.S)
out = ["status=" + (m.group(1).strip() if m else "?")]
m2 = re.search(r'<div id="result">(.*?)</div>\s*<div class="card" id="about"', t, re.S)
out.append("result_len=" + str(len(m2.group(1)) if m2 else -1))
out.append("result_head=" + (m2.group(1)[:200] if m2 else "?"))
out.append("has_loading=" + str("正在加载模型" in t))
out.append("has_ready=" + str("模型就绪" in t))
out.append("has_fail=" + str("加载失败" in t))
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_dom_check2.txt"),
        "w", encoding="utf-8").write("\n".join(out))
