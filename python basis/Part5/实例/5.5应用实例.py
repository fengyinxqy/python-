import csv


def readtxt(filename):
    with open(filename, "r")as f:
        ls = []
        for line in f:
            s = line.strip("\n").split("，")
            ls.append(s)
        xing_all = []
        for row in ls:
            xing_one = []
            if len(row[2]) == 3:
                yue1 = row[2][0]
                ri1 = row[2][1:3]
            else:
                yue1 = row[2][0:2]
                ri1 = row[2][2:4]
            if len(row[3]) == 3:
                yue2 = row[3][0]
                ri2 = row[3][1:3]
            else:
                yue2 = row[3][0:2]
                ri2 = row[3][2:4]
            xing_one.append(row[1])
            xing_one.append(int(yue1))
            xing_one.append(int(ri1))
            xing_one.append(int(yue2))
            xing_one.append(int(ri2))
            xing_all.append(xing_one)
    return xing_all


def readcsv(filename, xing):
    with open(filename, "r") as f:
        f.readline()
        sr = f.readlines()
        people = []
        for item in sr:
            person = []
            per = item.strip("\n").split("\t")
            date = per[1].split("-")
            person.append(per[0])
            person.append(date[1]+"月"+date[2]+"日")
            for line in xing:
                if (int(date[1]) == line[1] and int(date[2]) >= line[2]) or (int(date[1]) == line[3] and int(date[2]) <= line[4]):
                    per.append(line[0])
                    break
            people.append(per)
    return people


def writecsv(filename, people):
    with open(filename, "w", newline="")as f:
        w = csv.writer(f)
        w.writerow(["姓名", "生日", "星座"])
        w.writerows(people)


def Stats(people):
    dict_num = {}
    for line in people:
        dict_num[line[2]] = dict_num.get(line[2], 0)+1
    return dict_num


def writetxt(filename):
    with open(filename, "w")as f:
        f.write("星座    人数"+"\n")
        f.write("-------------"+"\n")
        for key, value in dict_num.items():
            f.write(key+"  "+str(value)+"\n")


if __name__ == '__main__':
    list_xing = readtxt("星座.txt")
    list_people = readcsv("生日.csv", list_xing)
    writecsv("生日星座.csv", list_people)
    dict_num = Stats(list_people)
    writetxt("星座统计.txt")
