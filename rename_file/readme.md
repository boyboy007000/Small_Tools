"## Giới thiệu chương trình đổi tên tệp theo tên thư mục

**Mục đích:**

Chương trình này được viết bằng Python với mục đích đổi tên các tệp trong một thư mục được chỉ định theo tên của thư mục đó.

**Thư viện:**

* `os`: Truy cập hệ thống tệp
* `shutil`: Sao chép tệp

**Chức năng chính:**

1. **Đổi tên tệp:** Duyệt qua từng thư mục con trong thư mục gốc và xử lý từng tệp.
2. **Lọc tệp:** Bỏ qua các tệp có tên chứa "Shop_", "Blog Khoa Hoc" hoặc "donate".
3. **Tạo tên tệp mới:** Kết hợp tên thư mục con hiện tại với tên tệp gốc và phần mở rộng.
4. **Sao chép tệp:** Thay vì đổi tên trực tiếp, sao chép tệp gốc sang một thư mục đích với tên tệp mới.

**Cách sử dụng:**

1. **Chỉnh sửa đường dẫn thư mục:** Thay đổi biến `folder_path` thành đường dẫn đến thư mục chứa các tệp bạn muốn xử lý.
2. **Lưu và chạy tệp:** Lưu tệp Python (ví dụ: `rename_files.py`) và chạy nó bằng lệnh `python rename_files.py`.

**Lưu ý:**

* Chương trình hiện tại sao chép tệp thay vì đổi tên trực tiếp. Bạn có thể thay đổi dòng `# os.rename(...)` để thực hiện đổi tên nếu cần thiết.
* Chương trình bỏ qua các tệp có tên chứa "Shop_", "Blog Khoa Hoc" hoặc "donate". Bạn có thể điều chỉnh điều kiện lọc này theo nhu cầu của bạn.

**Lợi ích:**

* Tự động đổi tên nhiều tệp theo quy tắc nhất quán.
* Sắp xếp tệp logic và dễ quản lý hơn.

**Ví dụ:**

Giả sử bạn có một thư mục `/home/annguyen/temp/` chứa các thư mục con và tệp như sau:

```
/home/annguyen/temp/
├── Thư mục 1
│   ├── File 1.txt
│   └── File 2.docx
└── Thư mục 2
    ├── File 3.pdf
    └── File 4.jpg
```

Sau khi chạy chương trình, các tệp sẽ được đổi tên như sau:

```
/home/annguyen/temp/
├── Thư mục 1
│   ├── Thư mục 1_File 1.txt
│   └── Thư mục 1_File 2.docx
└── Thư mục 2
    ├── Thư mục 2_File 3.pdf
    └── Thư mục 2_File 4.jpg
```

**Kết luận:**

Chương trình này cung cấp một giải pháp đơn giản để đổi tên tệp theo tên thư mục trong Python. Bạn có thể tùy chỉnh chương trình để phù hợp với nhu cầu cụ thể của bạn bằng cách thay đổi đường dẫn thư mục, điều kiện lọc tệp và hành động đổi tên/sao chép.
"