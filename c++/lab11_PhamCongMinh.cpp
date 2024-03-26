#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class SinhVien {
public:
    string maSo;
    string hoTenDem;
    string ten;

    SinhVien(string maSo, string hoTenDem, string ten) {
        this->maSo = maSo;
        this->hoTenDem = hoTenDem;
        this->ten = ten;
    }

    bool operator < (const SinhVien &other) const {
        if (this->ten != other.ten) {
            return this->ten < other.ten;
        } else {
            return this->hoTenDem < other.hoTenDem;
        }
    }
};

void inSinhVien(const SinhVien &sinhVien) {
    cout << sinhVien.ten << " " << sinhVien.hoTenDem << " (" << sinhVien.maSo << ")" << endl;
}

int timKiemNhiPhan(const vector<SinhVien> &danhSachSinhVien, string ten) {
    int trai = 0, phai = danhSachSinhVien.size() - 1;

    while (trai <= phai) {
        int giua = (trai + phai) / 2;
        if (danhSachSinhVien[giua].ten == ten) {
            return giua;
        } else if (danhSachSinhVien[giua].ten < ten) {
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }

    return -1;
}

void timKiemSinhVienTheoMaSo(const vector<SinhVien> &danhSachSinhVien, string maSo) {
    for (auto sinhVien : danhSachSinhVien) {
        if (sinhVien.maSo == maSo) {
            inSinhVien(sinhVien);
            return;
        }
    }

    cout << "Khong tim thay sinh vien voi ma so " << maSo << "." << endl;
}

void timKiemSinhVienTheoHoTen(const vector<SinhVien> &danhSachSinhVien, string ten) {
    int index = timKiemNhiPhan(danhSachSinhVien, ten);
    if (index == -1) {
        cout << "Khong tim thay sinh vien voi ten " << ten << "." << endl;
        return;
    }

    while (index > 0 && danhSachSinhVien[index - 1].ten == ten) {
        index--;
    }

    while (index < danhSachSinhVien.size() && danhSachSinhVien[index].ten == ten) {
        inSinhVien(danhSachSinhVien[index]);
        index++;
    }
}

void themSinhVien(vector<SinhVien> &danhSachSinhVien) {
    string maSo, hoTenDem, ten;
    cout << "Nhap ma so sinh vien: ";
    cin >> maSo;
    cout << "Nhap ho ten dem: ";
    cin >> hoTenDem;
    cout << "Nhap ten: ";
    cin >> ten;

    SinhVien sinhVienMoi(maSo, hoTenDem, ten);
    auto it = upper_bound(danhSachSinhVien.begin(), danhSachSinhVien.end(), sinhVienMoi);
    danhSachSinhVien.insert(it, sinhVienMoi);
}

void capNhatSinhVienTheoMaSo(vector<SinhVien> &danhSachSinhVien, string maSo) {
    auto it = find_if(danhSachSinhVien.begin(), danhSachSinhVien.end(), [maSo](const SinhVien &sinhVien) { return sinhVien.maSo == maSo; });
    if (it == danhSachSinhVien.end()) {
        cout << "Khong tim thay sinh vien voi ma so " << maSo << "." << endl;
        return;
    }

    string hoTenDem, ten;
    cout << "Nhap ho ten dem moi: ";
    cin >> hoTenDem;
    cout << "Nhap ten moi: ";
    cin >> ten;

    it->hoTenDem = hoTenDem;
    it->ten = ten;

    sort(danhSachSinhVien.begin(), danhSachSinhVien.end());
}
void inDanhSachSinhVien(const vector<SinhVien> &danhSachSinhVien) {
cout << "Danh sach sinh vien" << endl;
for (auto sinhVien : danhSachSinhVien) {
inSinhVien(sinhVien);
}
}
int main() {
vector<SinhVien> danhSachSinhVien;
while (true) {
    cout << "Chon chuc nang:" << endl;
    cout << "1. Them sinh vien" << endl;
    cout << "2. Cap nhat sinh vien theo ma sinh vien" << endl;
    cout << "3. Tim kiem theo ma sinh vien" << endl;
    cout << "4. Tim kiem theo ho va ten" << endl;
    cout << "5. In danh sach sinh vien" << endl;
    cout << "6. Thoat chuong trinh" << endl;
    cout << "Nhap lua chon: ";
    int chon;
    cin >> chon;

    switch (chon) {
        case 1:
            themSinhVien(danhSachSinhVien);
            break;
        case 2: {
            string maSo;
            cout << "Nhap ma sinh vien can cap nhat: ";
            cin >> maSo;
            capNhatSinhVienTheoMaSo(danhSachSinhVien, maSo);
            break;
        }
        case 3: {
            string maSo;
            cout << "Nhap ma sinh vien can tim kiem: ";
            cin >> maSo;
            timKiemSinhVienTheoMaSo(danhSachSinhVien, maSo);
            break;
        }
        case 4: {
            string ten;
            cout << "Nhap ho ten sinh vien can tim kiem: ";
            cin >> ten;
            timKiemSinhVienTheoHoTen(danhSachSinhVien, ten);
            break;
        }
        case 5:
            inDanhSachSinhVien(danhSachSinhVien);
            break;
        case 6:
            return 0;
        default:
            cout << "Vui long chon chuc nang hop le" << endl;
            break;
    }

    cout << endl;
}
return 0;
}