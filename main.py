from pathlib import Path
from apitest import apitest, apiretry, set_config
from mover import mover
from filereader import filereader

API_URL = "YOUR_API_URL_HERE"
API_KEY = "YOUR_API_KEY_HERE"
API_MODEL = "YOUR_MODEL_NAME_HERE"

if API_URL == "YOUR_API_URL_HERE" or API_KEY == "YOUR_API_KEY_HERE" or API_MODEL == "YOUR_MODEL_NAME_HERE":
    print("请先在 main.py 中配置 API_URL、API_KEY 和 API_MODEL！")
    exit(1)

set_config(API_URL, API_KEY, API_MODEL)

desktop = Path.home() / "Desktop"

for file in desktop.iterdir():
    if file.is_file() and file.suffix.lower() not in ('.lnk', '.url', '.ini', '.exe'):
        filenamee = file.name
        print("Now Processing : "+filenamee)
        try:
            filefolder=apitest(filenamee)
            if filefolder!="无法识别":
                mover(filefolder, filenamee)
                print(f"{filenamee} moved to {filefolder} folder")
            else:
                print(f"{filenamee} cannot be classified,try filereader")
                witfile=filereader(filenamee)
                if witfile=="无法识别":
                    print(f"{filenamee} cannot be read,didn't move to any folder.")
                else:
                    filefolder=apiretry(witfile)
                    if filefolder!="无法识别":
                        mover(filefolder, filenamee)
                        print(f"{filenamee} moved to {filefolder} folder")
                    else:
                        print(f"{filenamee} cannot be classified,didn't move to any folder.")

        except Exception as e:
            print(f"Error processing {filenamee}: {e}")
            continue


print("All Files Processed")
