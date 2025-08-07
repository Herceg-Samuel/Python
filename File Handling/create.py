from pathlib import Path

path = Path("emails")
#print(path.mkdir())
#print(path.rmdir())


for file in path.glob('*'):
    print(file)