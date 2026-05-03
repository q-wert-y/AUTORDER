import shutil
from pathlib import Path

def mover(filefolder, filenamee):
    desktop = Path.home() / "Desktop"
    source_path = desktop / filenamee
    target_folder = Path("C:\\") / filefolder
    target_folder.mkdir(parents=True, exist_ok=True)
    
    target_path = target_folder / filenamee
    
    if target_path.exists():
        stem = target_path.stem
        suffix = target_path.suffix
        counter = 1
        while target_path.exists():
            new_name = f"{stem}({counter}){suffix}"
            target_path = target_folder / new_name
            counter += 1
    
    shutil.move(str(source_path), str(target_path))
