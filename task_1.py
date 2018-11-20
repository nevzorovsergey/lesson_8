s = "papjsdhlsdjhgsjhlwkjkdlgj lieukjlskgj iwetuldkj"
l = len(s)
finded = set()

for size in range(1, l):
    for i in range(l - size + 1):
        substr = s[i:i+size]
        sub_hash = hash(substr)
        if sub_hash not in finded:
            finded.add(sub_hash)

print(f'Найдено {len(finded)} подстрок')
