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

  * djvulibre, 
  * [tesseract](https://en.wikipedia.org/wiki/Tesseract)

Say, in Fedora Linux you can install them with

```bash
$ sudo dnf install -y djvulibre tesseract
$ sudo dnf install -y tesseract-langpack-fra
```

(and whatever other languages you need)


**Remark**

You do not need this script if your DjVu file already contains a text 
layer.  In this case all you have to do is to run 

```bash
$  djvused <DjVu document>  -e 'print-pure-txt' > <text file>
``` 

for example
```bash
$  djvused paper.djvu 'print-pure-txt' > paper.txt
``` 

where djvused is a part of the standard library djvulibre.)
