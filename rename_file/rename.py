import os
import shutil
import sys

def rename_files(folder_path, dest_folder):
  """
  Hàm này đổi tên tệp trong thư mục được chỉ định theo tên thư mục.

  Args:
    folder_path: Đường dẫn đến thư mục chứa các tệp cần đổi tên.
  """
  for root, _, files in os.walk(folder_path):
    for file in files:
      # Lấy tên tệp và phần mở rộng
      filename, extension = os.path.splitext(file)
      if "Shop_" in filename or "Blog Khoa Hoc" in filename or "donate" in filename:
        continue
      # Tạo tên tệp mới bằng cách kết hợp tên thư mục và tên tệp gốc
      new_filename = f"{os.path.basename(root)}_{filename}{extension}"
      # Đổi tên tệp
      # os.rename(os.path.join(root, file), os.path.join(root, new_filename))
      # print(new_filename)
      # Tạo đường dẫn đến tệp nguồn và tệp đích
      source_filepath = os.path.join(root, file)
      # dest_folder = "folder"
      dest_filepath = os.path.join(dest_folder, new_filename)
      # Sao chép tệp
      shutil.copyfile(source_filepath, dest_filepath)


arguments = sys.argv[1:]
# Thay đổi đường dẫn thư mục theo thư mục bạn muốn xử lý
# folder_path = "folder"
folder_path = arguments[0]
dest_folder = arguments[1]

rename_files(folder_path, dest_folder)