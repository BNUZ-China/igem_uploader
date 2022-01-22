import os
import hashlib

def calcFileMD5_8digit(base_dir, filepath):
    file = open(os.path.join(base_dir, filepath), 'rb')
    content = file.read()
    md5 = hashlib.md5(content)
    file.close()
    return md5.hexdigest()[:8]


def getFileList(base_dir):
    result = []
    for curDir, dirs, files in os.walk(base_dir):
        for file in files:
            all_path = os.path.join(curDir, file)
            relative_path = curDir.replace('D:/Code/iGem/Wiki/src/assets\\', '').replace('D:/Code/iGem/Wiki/src/assets', '')
            file_name = file
            name = '.'.join(file_name.split('.')[:-1])
            ext  = file_name.split('.')[-1]

            file_md5_name = f'{name}.{calcFileMD5_8digit(base_dir, all_path)}.{ext}'
            result.append({
                'all_path': all_path,
                'relative_path': relative_path,
                'file_name': file_name,
                'file_md5_name': file_md5_name
            })
    return result

print(getFileList('D:/Code/iGem/Wiki/src/assets'))