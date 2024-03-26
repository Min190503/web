#include <iostream>
#include <vector>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;

class Student {
private:
    string studentID;
    string fullName;
public:
    Student() {}

    Student(string id, string name) : studentID(id), fullName(name) {}

    string getStudentID() const {
        return studentID;
    }

    string getFullName() const {
        return fullName;
    }

    void setStudentID(string id) {
        studentID = id;
    }

    void setFullName(const string& fullName) {
    this->fullName = fullName;
    }   

    bool operator<(const Student& other) const {
        if (fullName == other.fullName) {
            return studentID < other.studentID;
        }
        return fullName < other.fullName;
    }

    bool operator==(const Student& other) const {
        return fullName == other.fullName && studentID == other.studentID;
    }

    friend ostream& operator<<(ostream& os, const Student& student) {
        os << student.fullName << "\t" << student.studentID;
        return os;
    }

    friend istream& operator>>(istream& is, Student& student) {
        is >> student.fullName >> student.studentID;
        return is;
    }
};

void displayStudentList(const vector<Student>& students) {
    cout << "Danh sach sinh vien:\n";
    cout << "----------------------------------------\n";
    cout << "Ho ten\tMa sinh vien\n";
    cout << "----------------------------------------\n";
    for (const Student& student : students) {
        cout << student << endl;
    }
    cout << "----------------------------------------\n";
}

int binarySearch(const vector<Student>& students, const string& fullName) {
    int left = 0;
    int right = students.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (students[mid].getFullName() == fullName) {
            return mid;
        }
        else if (students[mid].getFullName() < fullName) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1;
}

void searchByID(const vector<Student>& students) {
    string studentID;
    cout << "Nhap ma sinh vien: ";
    cin >> studentID;

    for (const Student& student : students) {
        if (student.getStudentID() == studentID) {
            cout << "Da tim thay sinh vien: " << student << endl;
            return;
        }
    }
    cout << "Khong tim thay sinh vien trong danh sach!\n";
}

void searchByName(const vector<Student>& students) {
    string fullName;
    cout << "Ho ten sinh vien: ";
    cin.ignore();
    getline(cin, fullName);

    int index = binarySearch(students, fullName);
    if (index != -1) {
        cout << "Da tim thay sinh vien:\n";
        cout << "----------------------------------------\n";
        cout << "Ho ten\tma sinh vien\n";
        cout << "----------------------------------------\n";
        while (index >= 0 && students[index].getFullName() == fullName) {
            cout << students[index] << endl;
            index--;
        }
        cout << "----------------------------------------\n";
        return;
    }
    cout << "khong tim thay sinh vien!\n";
}

void addStudent(vector<Student>& students) {
    string fullName;
    string studentID;

    cout << "Enter Full Name: ";
    cin.ignore();
    getline(cin, fullName);

    cout << "Enter Student ID: ";
    cin >> studentID;

    Student newStudent(fullName, studentID);
    students.push_back(newStudent);

    // Sắp xếp danh sách sinh viên theo thứ tự tăng dần
    sort(students.begin(), students.end());

    cout << "Da them sinh vien vao danh sach!\n";
}

void updateStudent(vector<Student>& students) {
    string studentID;
    cout << "Nhap ma so sin vien: ";
    cin >> studentID;

    for (Student& student : students) {
        if (student.getStudentID() == studentID) {
            cout << "Ho va ten: ";
            cin.ignore();
            string fullName;
            getline(cin, fullName);
            student.setFullName(fullName);
            cout << "Da cap nhat danh sach sinh vien\n";
            return;
        }
    }
    cout << "Khong tim thay!\n";
}

int main() {
    vector<Student> students;
    int choice;

    while (true) {
        cout << "Menu:\n";
        cout << "1. Tim sinh vien theo ma so\n";
        cout << "2. Tim sinh vien theo ho ten\n";
        cout << "3. Them sinh vien\n";
        cout << "4. Cap nhat sinh vien theo ma so\n";
        cout << "5. In toan bo danh sach sinh vien\n";
        cout << "6. Thoat\n";
        cout << "Nhap lua chon: ";
        cin >> choice;

        switch (choice) {
            case 1:
                searchByID(students);
                break;
            case 2:
                searchByName(students);
                break;
            case 3:
                addStudent(students);
                break;
            case 4:
                updateStudent(students);
                break;
            case 5:
                displayStudentList(students);
                break;
            case 6:
                return 0;
            default:
                cout << "Lua chon khong hop le!.\n";
                break;
        }

        cout << endl;
    }

    return 0;
}
