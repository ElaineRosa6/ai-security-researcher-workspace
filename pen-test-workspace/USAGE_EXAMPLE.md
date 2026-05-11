# Skills Library 使用示例

## 给 Claude Code / Codex / 其他 Agent 使用的示例

### 1. 基本导入

```python
from pen_test_workspace.skills import (
    scan_website,
    test_xss,
    nmap_scan,
    generate_markdown_report
)
```

---

### 2. 完整Web测试示例

```python
# Step 1: 扫描网站
scan_result = scan_website("https://example.com")
print(scan_result["summary"])
findings = scan_result["findings"]

# Step 2: 如果发现可能的漏洞，测试特定参数
if findings:
    for finding in findings:
        if "XSS" in finding["title"]:
            test_xss(finding["url"], "q")

# Step 3: 生成报告
report = generate_markdown_report(
    findings=findings,
    target_info={"url": "https://example.com"},
    title="Example.com 安全测试报告"
)

with open("report.md", "w") as f:
    f.write(report)
```

---

### 3. 网络扫描示例

```python
from pen_test_workspace.skills import nmap_scan, port_scan

# 快速端口扫描
quick_result = port_scan("192.168.1.1")
print(f"开放端口: {quick_result['open_ports']}")

# 完整Nmap扫描
full_scan = nmap_scan(
    "192.168.1.1",
    ports="1-1000",
    options={"version_detection": True}
)

for port_info in full_scan["results"]:
    print(f"端口 {port_info['port']}: {port_info['service']} {port_info['version']}")
```

---

### 4. 测试SQL注入示例

```python
from pen_test_workspace.skills import test_sql_injection

result = test_sql_injection(
    url="https://example.com/search",
    param="id"
)

if result["vulnerable"]:
    print("发现SQL注入漏洞!")
```
