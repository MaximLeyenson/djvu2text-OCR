# djvu2text-OCR

This simple script performs an OCR (optical character recognition) on a DjVu 
document  via Tesseract and produces a plain text file.


**Usage**

```bash
   $ djvu2text-OCR.py <input.djvu> <output.txt> <lang>
```

For example,
```bash
   $ djvu2text-OCR.py paper.djvu  OCR.txt eng
```

**Requirements**  

djvulibre, [tesseract](https://en.wikipedia.org/wiki/Tesseract)

Say, in Fedora Linux you can install them with

```bash
$ sudo dnf install -y djvulibre tesseract
$ sudo dnf install -y tesseract-langpack-fra
```

(and whatever other languages you need)


**Remark**

[to be written]
