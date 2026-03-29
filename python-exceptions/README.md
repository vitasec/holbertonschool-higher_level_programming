# Python - Exceptions 🐍

## Təsvir
Bu layihə Python proqramlaşdırma dilində xətaların idarə edilməsi (**Exception Handling**) mövzusunu əhatə edir. Proqramın icrası zamanı yaranan gözlənilməz halları (məsələn: sıfıra bölmə, yanlış tip daxil etmə və s.) necə düzgün qarşılamağı və proqramın "çökmədən" işinə davam etməsini təmin etməyi öyrənirik.

## Öyrənilən Əsas Mövzular
* **Exceptions nədir:** Proqramın icrası zamanı baş verən xətalar.
* **Try / Except:** Xətanı "yaxalamaq" və idarə etmək.
* **Else:** Xəta baş vermədikdə icra olunacaq kod bloku.
* **Finally:** Xəta olub-olmamasından asılı olmayaraq həmişə icra olunan hissə.
* **Raise:** Süni şəkildə xəta yaratmaq (məsələn, daxil edilən rəqəm mənfi olarsa).
* **Traceback:** Xətanın haradan və niyə qaynaqlandığını anlamaq.

## Faylların Strukturu
| Fayl Adı | Təsviri |
| :--- | :--- |
| `0-safe_print_list.py` | Siyahının elementlərini təhlükəsiz (try/except ilə) çap edir. |
| `1-safe_print_integer.py` | Yalnız tam ədədləri (integer) çap edən funksiya. |
| `2-safe_print_list_integers.py` | Siyahıdakı yalnız tam ədədləri çap edir. |
| `3-safe_print_division.py` | İki rəqəmin bölünməsini `finally` bloku ilə icra edir. |
| `4-list_division.py` | İki siyahını element-element bölür və xətaları idarə edir. |
| `5-raise_exception.py` | Tip xətası (`TypeError`) yaradan funksiya. |
| `6-raise_exception_msg.py` | Mesajla birlikdə ad xətası (`NameError`) yaradır. |

## İstifadə Qaydaları
Bütün Python faylları `python3` (versiya 3.8.5) ilə test edilmişdir.
Kodun keyfiyyəti `pycodestyle` (versiya 2.8.*) standartlarına uyğundur.

Örnək işə salma:
```bash
$ ./0-main.py
