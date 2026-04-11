from pathlib import Path
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')