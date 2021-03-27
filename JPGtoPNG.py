import sys
import os
from PIL import Image


def JPG_to_PNG(source_path, target_path):
    """
    Give two directories as entries and it will convert all pictures in the first directory from JPG to PNG and save
    them in the second directory
    """
    count = 0
    if not source_path.endswith('/'):
        source_path = source_path + '/'

    if not target_path.endswith('/'):
        target_path = target_path + '/'

    for file_name in os.listdir(source_path):
        if file_name.lower().endswith(".jpg"):
            img_path = source_path + file_name
            img = Image.open(img_path)
            if not os.path.exists(target_path):
                os.mkdir(target_path)

            file_name = file_name[:-4]
            file_name = file_name + '.png'
            img_path = target_path + file_name
            img.save(img_path, 'png')
            count += 1

    print(f"[+] {count} pictures converted.")


def main():
    JPG_to_PNG(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
