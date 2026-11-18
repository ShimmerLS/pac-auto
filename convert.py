import urllib.request

# 你的源 .sorl 文件地址
url = "https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl"
output_file = "whitelist_rules.txt"

try:
    req = urllib.request.urlopen(url)
    lines = req.read().decode("utf-8").splitlines()

    rules = []
    for line in lines:
        line = line.strip()
        # 跳过空行和注释
        if not line or line.startswith((";", "[", "#", "!")):
            continue
        rules.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(rules))
        
    print(f"转换成功！共写入 {len(rules)} 条规则。")

except Exception as e:
    print(f"转换失败: {e}")
    exit(1)
