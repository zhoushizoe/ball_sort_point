def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        if len(lines1) != len(lines2):
            return False

        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                return False

    return True


file1 = r'/Users/amber/PycharmProjects/Sortball_副本/case/test.txt'
file2 = r'/Users/amber/PycharmProjects/Sortball_副本/case/standard_point.txt'

result = compare_files(file1, file2)

if result:
    print("文件内容一致")
else:
    print("文件内容不一致")
