# Uzbek_Trans 2022

Developed by Quvonchbek Bobojonov (c) 2022

## Examples of How To Use (Buggy Alpha Version)

Uzbek Translate

```js
pip install Uzbek-Trans==1.22
```

```python
from Uzbek_Trans import transliterate, to_cyrillic, to_latin, test

text = transliterate(text='salom', to_variant="cyrillic")

print(text)

print(to_cyrillic(text="salom"))
print(to_latin(text="салом"))

# Uzbek_Trans test
if __name__ == "__main__":
    test()
```
 Uzbek_Trans test consul

```js 
1: latin, 2: cyrillic
Turni kiriting:2
матн киритинг:salom
салом
```

