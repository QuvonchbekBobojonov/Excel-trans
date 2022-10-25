# Excel_Trans 2022

Developed by Quvonchbek Bobojonov (c) 2022

## Examples of How To Use (Buggy Alpha Version)

### install
```terminal
pip install excel-trans==1.22.1
```

### Uzbek Translate

```python

from Excel_Trans import Translator

trans = Translator()

#Uzbek Translate

trans.UzbekTranslate(file='test.xlsx', to_variant='latin', save_file='test1.xlsx')

# get supported variants

print(trans.variant())

```

### Global Translate
```python

from Excel_Trans import Translator
trans = Translator()

#Global Translate

trans.GlobalTranslate(file='test.xlsx', target='ru', save_file='test1.xlsx')

#get supported languages

trans.get_supported_languages(as_dict=True)

```
