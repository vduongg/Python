description = '''
Bài tập lớn Python
## Thành viên nhóm
* **A37527 Đỗ Anh Thư**
* **A38322 Trần Văn Tú**
* **A38221 Vũ Thế Dương**
'''

tags = [
    {
        "name" : "Trang chủ",
        "description" : "Thông tin thành viên nhóm"
    },
    {
        "name" : "Anh Thư Numpy",
        "description" : "Thống kê phần trăm điểm tổng kết là 0 và Cập nhật điểm của sinh viên theo môn học."
    },
    {
        "name" : "Anh Thư Pandas",
        "description": "Hiển thị bảng danh sách sinh viên đạt điểm 10 và Hiển thị bảng danh sách các sinh viên có điểm tương tự nhau."
    },
    {
        "name" : "Thế Dương Numpy",
        "description" : "Lấy sĩ số theo mã lớp và Thống kê điểm trung bình môn theo lớp."
    },
    {
        "name" : "Thế Dương Pandas",
        "description" : "Thống kê điểm của môn học theo lớp và cập nhập tên lớp theo mã lớp."
    },
    {
        "name" : "Trần Văn Tú Numpy",
        "description" : "Tính điểm trung bình cuối kì tất cả các môn theo sinh viên và Điểm trung bình cuối kì tất cả các môn theo lớp."
    },
    {
        "name" : "Trần Văn Tú Pandas",
        "description" : "Đếm số học sinh qua môn và Cập nhật tên môn học."
    }
]

des_api = {
    'AnhThuNP': {
        "ThongKeDiem0" : "Trả về phần trăm điểm tổng kết 0 của tất cả các môn.",
        "CapNhatDiemSo" : "Đầu vào là mã sinh viên, mã môn học, điểm giữa kì và cuối kì của sinh viên. Mã sinh viên và mã môn học mang giá trị nguyên dương. 2 đầu điểm mang giá trị thực dương."
    },
    "AnhThuPD": {
        "DanhSachDiem10" : "Hiện bảng danh sách các sinh viên được điểm tổng kết 10.",
        "DanhSachGiongNhau" :"Đầu vào là điểm giữa kì và điểm cuối kì có giá trị là số thực dương. Hiển thị danh sách các sinh viên có điểm số giống như đầu vào."

    },
    "TheDuongNP": {
        "SiSoLop": "Đầu vào là mã lớp có giá trị nguyên dương. Trả về sĩ số của lớp học",
        "TrungBinhMon" : "Đầu vào là mã lớp và  mã môn học có giá trị nguyên dương. Trả về Điểm trung bình môn học theo lớp. "
    },
    "TheDuongPD": {
        "ThongKeDiemTheoMonHoc" : "Nhập vào mã môn học có giá trị nguyên dương. Trả về danh sách điểm của môn học theo lớp.",
        "CapNhatTenLop" : "Đầu vào là mã lớp có giá trị nguyên dương, tên lớp để thay có kiểu string."
    },

    "TranTuNP" : {
        "TrungBinhCuoiKi" : "Nhập vào mã sinh viên mang giá trị nguyên dương, hiển thị điểm cuối kì trung bình của sinh viên đó.",
        "TrungBinhCuoiKiLop" : "Đầu vào là mã lớp mang giá trị nguyên dương, hiển thị điểm trung bình cuối kì các môn của lớp."
    },

    "TranTuPD" : {
        "QuaMon" : "Nhập vào mã môn có giá trị nguyên dương, trả về số học sinh qua môn học.",
        "CapNhatTenMon" : "Đầu vào mã môn có giá trị nguyên dương và tên môn học mới."
    }
}