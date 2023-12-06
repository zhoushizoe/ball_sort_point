def get_file1():
    with open("test.txt", "r") as file1:
        lines1 = file1.readlines()
    filtered_lines = []
    for line in lines1:
        filtered_line = line[96:-55]  # 使用切片截取想要的内容
        filtered_lines.append(filtered_line)
    for line in filtered_lines:
        print(line)
        line = line.strip()
    return line


def write_file1():
    with open("test_123.txt", "a", encoding="utf-8") as f:
        f.write(get_file1() + "\n")
    return

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


file1 = r'/Users/amber/PycharmProjects/Sortball_副本/case/test_123.txt'
file2 = r'/Users/amber/PycharmProjects/Sortball_副本/case/test2.txt'

result = compare_files(file1, file2)

if result:
    print("文件内容一致")
else:
    print("文件内容不一致")
