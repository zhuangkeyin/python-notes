# 第一次跑通的代码 —— 2026-11-03
# 运行方法：终端里执行  ~/WorkBuddy/2026-10-29-21-47-10/.venv/bin/python hello.py
# 或者：cd 到这个文件夹后执行  .venv/bin/python hello.py

print("hello, 我开始了")

# 变量与字符串
name = "庄可茵"
school = "广东金融学院"
print(f"我是{name}，{school}金融科技专业")

# 列表 + 循环
stocks = ["平安银行", "招商银行", "贵州茅台"]
for s in stocks:
    print("关注:", s)

# 字典 + 条件
prices = {"平安银行": 12.5, "招商银行": 38.2}
for k, v in prices.items():
    if v > 30:
        print(k, "是高价股")
    else:
        print(k, "是低价股")
