import os
import shutil
import datetime
import schedule
import time

src_dir = "C:/Users/Sudhir/Pictures/Screenshots"
des_dir = "D:/manav/New folder"

def copy(src,des):
    today = datetime.date.today()
    dest_dir = os.path.join(des,str(today))

    try:
        shutil.copytree(src,dest_dir)
        print(f"Folder copy to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {des}")

schedule.every().day.at("23:30").do(lambda: copy(src_dir,des_dir))

while True:
    schedule.run_pending()
    time.sleep(60)