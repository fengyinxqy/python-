StuInfo = [["王硕", "男", 18], ["李梅", "女", 21], ["赵翔", "男", 20], ["王楠", "女", 19], [
    "张力", "男", 20], ["陈昊", "男", 18], ["丁宁", "女", 19], ["王飞", "男", 20]]
StuDict = {}
for item in StuInfo:
    sex = item[1]
    StuDict[sex] = StuDict.get(sex, 0)+1
print("统计结果为:")
for key, value in StuDict.items():
    print(key, value, "人")
