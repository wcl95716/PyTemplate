import uuid
import requests
import pandas as pd
from io import BytesIO

import os
from typing import Optional
import hashlib
import os


def download_excel_and_read(excel_url: str) -> pd.DataFrame:
    try:
        # 使用requests库下载Excel文件
        response = requests.get(excel_url)

        if response.status_code == 200:
            # 使用BytesIO对象包装字节数据
            content = BytesIO(response.content)

            # 使用pandas库读取Excel文件内容
            df = pd.read_excel(content, engine='openpyxl')
            return df
        else:
            print("Failed to download Excel file")
            return pd.DataFrame()  # Return an empty DataFrame instead of None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return pd.DataFrame()
        raise


def download_file_to_folder(file_url: str, folder_path: str = './data/files') -> Optional[str]:
    try:
        # 发起GET请求以下载文件
        response = requests.get(file_url, stream=True)
            # Ensure directory exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 检查响应状态码，确保请求成功
        if response.status_code == 200:
            # 获取文件名
            original_file_name = os.path.basename(file_url)

            # 生成唯一的文件名
            file_name = str(uuid.uuid4()) + '_' + original_file_name

            # file_name = os.path.basename(file_url)

            # 构造文件的本地路径
            local_path = os.path.join(folder_path, file_name)

            # 以二进制方式写入文件
            with open(local_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            return local_path
        else:
            print(f"Failed to download file from {file_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while downloading the file: {str(e)}")
        return None


def calculate_file_size(file_path: str) -> int:
    """Calculate the size of a file."""
    return os.path.getsize(file_path)

def calculate_file_hash(file_path: str, hash_algorithm: str = "sha256") -> str:
    """Calculate the hash value of a file."""
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # Read in 64K chunks
            if not data:
                break
            hash_func.update(data)
    return hash_func.hexdigest()


def test1() -> None:
    # 调用函数下载文件到指定文件夹
    file_url = 'http://127.0.0.1:8001/test/uploads/c2faed2d0ed641f59cb8b46fe236a7eb_-.xlsx'  # 替换为实际的文件URL
    file_path = download_file_to_folder(file_url)
    if file_path:
        print(f"File downloaded successfully to {file_path}")
    else:
        print("File download failed")


def test2()-> None:
    
    file_path = "data/upload_file/20240119002330Clash.for.Windows-0.20.39-arm64.dmg"
    print("file_path :", file_path)
    print("File size:", calculate_file_size(file_path))
    print("File hash (SHA256):", calculate_file_hash(file_path))
    
    pass

if __name__ == "__main__":
    
    print("File hash ")
    test2()
    
    pass
    
