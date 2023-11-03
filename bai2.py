# Hàm xeploai_hocsinh
rows = []
diemtk = {}

def xeploai_hocsinh(file):
    with open(file, "r") as rec:

        # Tạo danh sách bảng điểm trung bình cho các học sinh theo thứ tự từ 1 đến 6 và theo môn học
        xep_loai = {}

        for line in rec:
            if line.startswith("Ma HS"):
                continue
            else:
                line_split = line.strip().split(";")
                Ma_HS = line_split[0]
                # Chuyển điểm TB của từng môn học từ dạng str sang float
                bangdiem = [float(i) for i in line.split[1:9]]

                # Tính điểm TB chuẩn và xếp hạng các môn của từng học sinh
                dtb_chuan = round((sum(bangdiem) + bangdiem[0] + bangdiem[4] + bangdiem[5]) / 11, 2)
                if all(i >= 8.0 for i in bangdiem) and dtb_chuan > 9.0:
                    xep_loai[Ma_HS] = "Xuat sac"
                elif all(i >= 6.5 for i in bangdiem) and dtb_chuan > 8.0:
                    xep_loai[Ma_HS] = "Gioi"
                elif all(i >= 5.0 for i in bangdiem) and dtb_chuan > 6.5:
                    xep_loai[Ma_HS] = "Kha"
                elif all(i >= 4.5 for i in bangdiem) and dtb_chuan > 6.0:
                    xep_loai[Ma_HS] = "TB Kha"
                else:
                    xep_loai[Ma_HS] = "TB"

        return xep_loai
    rec.close()


# Hàm xeploai_thidaihoc_hocsinh

def xeploai_thidaihoc_hocsinh(file):
    with open(file, 'r') as rec:
        xeploai_thidaihoc = {}  # Dictionary Output

        for line in rec:
            if line.startswith("Ma HS"):
                continue
            else:
                line_split = line.strip().split(";")
                Ma_HS = line_split[0]
                bangdiem = [float(i) for i in line_split[1::]]  # Bảng điểm TB các môn học

                khoiA = round(sum(bangdiem[0:3]), 2)  # Tổng điểm Toán, Lí, Hóa
                khoiA1 = round(bangdiem[0] + bangdiem[1] + bangdiem[5], 2)  # Tổng điểm Toán, Lí, Anh
                khoiB = round(bangdiem[0] + bangdiem[2] + bangdiem[3], 2)  # Tổng điểm Toán, Hóa, Sinh
                khoiC = round(bangdiem[4] + bangdiem[6] + bangdiem[7], 2)  # Tổng điểm Văn, Sử, Địa
                khoiD = round(bangdiem[0] + bangdiem[4] + (bangdiem[5] * 2), 2)  # Tổng điểm Toán, Văn, Anh

                # Phân loại năng lực học sinh theo khối A
            if khoiA >= 24:
                Xeploai_khoi_A = 1
            elif khoiA >= 18 and khoiA < 24:
                Xeploai_khoi_A = 2
            elif khoiA >= 12 and khoiA < 18:
                Xeploai_khoi_A = 3
            else:
                Xeploai_khoi_A = 4

                # Phân loại năng lực học sinh theo khối A1
            if khoiA1 >= 24:
                Xeploai_khoi_A1 = 1
            elif khoiA1 >= 18 and khoiA1 < 24:
                Xeploai_khoi_A1 = 2
            elif khoiA1 >= 12 and khoiA1 < 18:
                Xeploai_khoi_A1 = 3
            else:
                Xeploai_khoi_A1 = 4

                # Phân loại năng lực học sinh theo khối B
            if khoiB >= 24:
                Xeploai_khoi_B = 1
            elif khoiB >= 18 and khoiB < 24:
                Xeploai_khoi_B = 2
            elif khoiB >= 12 and khoiB < 18:
                Xeploai_khoi_B = 3
            else:
                Xeploai_khoi_B = 4

                # Phân loại năng lực học sinh theo khối C
            if khoiC >= 21:
                Xeploai_khoi_C = 1
            elif khoiC >= 15 and khoiC < 21:
                Xeploai_khoi_C = 2
            elif khoiC >= 12 and khoiC < 15:
                Xeploai_khoi_C = 3
            else:
                Xeploai_khoi_C = 4
                # Phân loại năng lực học sinh theo khối D
            if khoiD >= 32:
                Xeploai_khoi_D = 1
            elif khoiD >= 24 and khoiD < 32:
                Xeploai_khoi_D = 2
            elif khoiD >= 20 and khoiD < 24:
                Xeploai_khoi_D = 3
            else:
                Xeploai_khoi_D = 4

                # Xếp loại năng lực của từng học sinh theo các khối
            xep_loai = [Xeploai_khoi_A, Xeploai_khoi_A1, Xeploai_khoi_B,
                            Xeploai_khoi_C, Xeploai_khoi_D]
            xeploai_thidaihoc[Ma_HS] = xep_loai
        return xeploai_thidaihoc
    rec.close()


def luudiem_trungbinh(filename):
    file1 = open(filename, "w")
    file1.write("Ma HS" + ", " + "xeploai_TB chuan" + ", " + "Xeploai_A" + ", " + "xeploai_A1"
                + ", " + "xeploai_B" + ", " + "xeploai_C" + ", " + "xeploai_D" + "\n")
    num = 1
    for i in diemtk:
        file1.write(i)
        xeploaitb = diemtk[i]
        file1.write("; " + str(xeploaitb) + '; ')
        num_str = str(num)
        list =xeploai_thidaihoc.get(num_str)
        string = '; '.join(str(e) for e in list)
        file1.write(string)
        num = int(num_str)
        num += 1
        file1.write("\n")
    file1.close()
    print("Luu file thanh cong!")


def main():
    print("-------------BAI TOAN PHAN TICH DIEM: CHUONG TRINH TINH DIEM TRUNG BINH-------------")
    # tinh_toan_diem_tong_ket.txt
    print("Nhap ten file de xep loai hoc sinh: ")
    file = input()
    print(xeploai_hocsinh(file))
    print(xeploai_thidaihoc_hocsinh(file))
    # danhgia_hocsinh.txt
    print("Nhap ten file luu ket qua bang diem cua hoc sinh: ")
    filename2 = input()
    luudiem_trungbinh(filename2)
main()