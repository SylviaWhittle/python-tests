import yaml
from pathlib import Path

with open('config.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data['v1'])
    
basepath = Path('./')
path = Path(basepath / 'test' / 'test.txt')
Path.mkdir(path, parents=True, exist_ok=True)

