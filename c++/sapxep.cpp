#include<bits/stdc++.h>
using namespace std;



void bubbleSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (a[j] > a[j+1]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}


void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j = j-1;
        }

        a[j + 1] = key;
    }
}
void interchangeSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            if (a[i] > a[j]) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}
void selectionSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        int min = i;
        for (int j = i+1; j < n; j++) {
            if (a[j] < a[min]) {
                min= j;
            }
        }
        
        int temp = a[min];
        a[min] = a[i];
        a[i] = temp;
    }
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int a[], int low, int high) {
    int pivot = a[high]; 
    int i = (low - 1); 

    for (int j = low; j <= high - 1; j++) {
        if (a[j] <= pivot) {
            i++; 
            swap(&a[i], &a[j]);
        }
    }
    swap(&a[i + 1], &a[high]);
    return (i + 1);
}

void quickSort(int a[], int low, int high) {
    if (low < high) {
        int pi = partition(a, low, high);

        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}
void merge(int a[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = a[l + i];
    for (j = 0; j < n2; j++)
        R[j] = a[m + 1 + j];

    i = 0; 
    j = 0; 
    k = l; 
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            a[k] = L[i];
            i++;
        } else {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        a[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        a[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int a[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(a, l, m);
        mergeSort(a, m + 1, r);

        merge(a, l, m, r);
    }
}

void inmang(int a[], int size) {
    for (int i = 0; i < size; i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
int main()
{
	int lc,n;
	cout<<"1.bubbleSort: "<<endl;
	cout<<"2.insertionSort: "<<endl;
	cout<<"3.interchangeSort: "<<endl;
	cout<<"4.selectionSort: "<<endl;
	cout<<"5.quickSort: "<<endl;
	cout<<"6. mergeSort: "<<endl;
	
	
	cout<<"Nhap lua chon: ";
	cin>>lc;
	
	
	if(lc == 1)
	{
    cout << "Nhap so phan tu trong mang: ";
    cin >> n;
    
    int a[n];
    cout << "Nhap cac phan tu cua mang:\n";
	for (int i = 0; i < n; i++) {
    	cout<<"a["<<i<<"] = ";
        cin >> a[i];
        }
        
    cout << "Mang ban dau: ";
    inmang(a, n);
    
    bubbleSort(a, n);
    
    cout << "Mang sau khi sap xep: ";
    inmang(a, n);
    }
    
    
    if(lc == 2)
    {
    	cout << "Nhap so phan tu trong mang: ";
    cin >> n;
    
    int a[n];
    cout << "Nhap cac phan tu cua mang:\n";
	for (int i = 0; i < n; i++) {
    	cout<<"a["<<i<<"] = ";
        cin >> a[i];
    	}
    	cout << "Mang ban dau: ";
    	inmang(a, n);
    
    	insertionSort(a, n);
    
    	cout << "Mang sau khi sap xep: ";
    	inmang(a, n);
    }
    
    if(lc == 3)
    {
    	cout << "Nhap so phan tu trong mang: ";
    cin >> n;
    
    int a[n];
    cout << "Nhap cac phan tu cua mang:\n";
	for (int i = 0; i < n; i++) {
    	cout<<"a["<<i<<"] = ";
        cin >> a[i];
    	}
    	cout << "Mang ban dau: ";
    	inmang(a, n);
    
    	interchangeSort(a, n);
    
    	cout << "Mang sau khi sap xep: ";
    	inmang(a, n);
    }
    
    if(lc == 4)
    {
    	cout << "Nhap so phan tu trong mang: ";
    cin >> n;
    
    	int a[n];
   	 	cout << "Nhap cac phan tu cua mang:\n";
		for (int i = 0; i < n; i++) {
    		cout<<"a["<<i<<"] = ";
        	cin >> a[i];
        }
    	cout << "Mang ban dau: ";
    	inmang(a, n);
    
    	selectionSort(a, n);
    
   	 	cout << "Mang sau khi sep xep: ";
    	inmang(a, n);
    }
    
    
    if(lc == 5)
    {		
		cout << "Nhap so phan tu trong mang: ";
    	cin >> n;
    
    	int a[n];
    	cout << "Nhap cac phan tu cua mang:\n";
		for (int i = 0; i < n; i++) {
    		cout<<"a["<<i<<"] = ";
        	cin >> a[i];
    		}
    	cout << "Mang ban dau: ";
    	inmang(a, n);

    	quickSort(a, 0, n - 1);

    	cout << "Mang sau khi sap xep: ";
   	 	inmang(a, n);
   	}
   	
   	
   	if(lc == 6)
   	{
    	cout << "Nhap so phan tu trong mang: ";
    	cin >> n;
    
    	int a[n];
    	cout << "Nhap cac phan tu cua mang:\n";
		for (int i = 0; i < n; i++) {
    		cout<<"a["<<i<<"] = ";
        	cin >> a[i];
    		}
    	cout << "Mang ban dau: ";
    	inmang(a, n);
    
    	mergeSort(a,0, n-1);
    
    	cout<<"Mang sau khi sap xep: ";
    	inmang(a, n);
    }
    return 0;
}
    
	