rows = []
diemtb = {}

def tinhdiem_trungbinh(filename):
    with open(filename, "r") as rec:
        for line in rec:
            line = line.strip()
            row = line.split(";")
            rows.append(row)
        for x in range(1, len(rows)):
            tblist = []
            for y in range(1, 9):
                diemhs = {}
                diem = rows[x][y].split(',')
                monlist = rows[0][0].split(', ')
                if y < 5:
                    diem = tinhdiem_tn(diem)
                    tblist.append(diem)
                else:
                    diem = tinhdiem_xh(diem)
                    tblist.append(diem)

            for i in range(1, 9):
                mon = monlist[i]
                diemhs[mon] = tblist[i - 1]

            mahs = rows[x][0]
            diemtb[mahs] = diemhs

        return diemtb
    rec.close()

# Tính điểm theo hệ số
def tinhdiem_tn(grade):
    diem = int(grade[0]) * 5 / 100 + int(grade[1]) * 10 / 100 + int(
        grade[2]) * 15 / 100 + int(grade[3]) * 70/100
    return round(diem, 2)

def tinhdiem_xh(grade):
    diem = int(grade[0]) * 5 / 100 + int(grade[1]) * 10 / 100 +  int(
        grade[2]) * 10 / 100 + int(grade[3]) * 15 / 100 + int(grade[4]) * 60/100
    return round(diem, 2)

def luudiem_trungbinh(f1, f2):
    file1 = open(f1, "r")
    file2 = open(f2, "w")

    for line in file1:
        file2.write(line)
        break
    for i in diemtb:
        file2.write(i)
        thongtin = diemtb[i]
        for x in thongtin:
            file2.write("; "+str(thongtin[x]))
        file2.write("\n")
    file1.close()
    file2.close()
    print("Luu du lieu thanh cong")


def main():
    print("--- BAI TOAN PHAN TICH DIEM: TINH DIEM TRUNG BINH ---")
    # asm2_data.txt
    print("NHAP TEN FILE DU LIEU DE TINH DIEM ")
    file1 = input()
    print(tinhdiem_trungbinh(file1))

    print("NHAP TEN FILE CAN LUU DIEM TRUNG BINH ")
    file2 = input()
    luudiem_trungbinh(file1, file2)


main()