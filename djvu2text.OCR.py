#! /usr/bin/python

# by Maxim Leyenson, <leyenson@gmail.com>
# under the GNU license


import os
import sys
import commands


try:
    filename   = sys.argv[1];
    output     = sys.argv[2];
    language   = sys.argv[3];
except:
    print 'Usage: %s <input.djvu> <output.txt> <lang> ' % sys.argv[0]; 
             #--  sys.argv[0] = "0'th argument" = filename
    print  'example: .. input.djvu output.txt eng '
    print  'Partial list of languages known to Tesseract: '
    print  '  English: eng '
    print  '  German:  deu'
    print  '  French:  fra'
    print  '  Italian: ita'
    print  '  Russian: rus'
    sys.exit(1);


# ---------------------------------------------------------------
# The following function computes the number of pages in a DjVu file
# ---------------------------------------------------------------

def numberOfPagesInDjvuFile(filename):

# returns number of pages in DjVu file
# djvudump output contains the string "5 pages" if document has more than 1 page, 
#    or does not contain the word "pages" for a document with one page

   command ="djvudump " + filename + " | grep -c pages "
   count = commands.getoutput(command) 
   count = int(count)
   # print "count = ", count
   if (count == 0):
      pages = 1
   else:
      command ="djvudump " + filename + " | grep pages | sed 's/.*files//g;' | sed 's/pages.*//g;' "
      pages = commands.getoutput(command)
      pages = int(pages)
      # print "has", pages, "pages"
   return pages

# remarks
#    $djvudump a.djvu  | grep pages returns, f.e.,
#        "DIRM [325]        Document directory (bundled, 34 files 34 pages)"
#
#    $  |  sed 's/.*files//g;'
#            returns "34 pages)"
# 
#    $  |  sed 's/pages.*//g;'
#            returns 34

# --------------------- end of the function ------------------------

number_of_pages_in_book = \
   numberOfPagesInDjvuFile(filename)
print '[ ', number_of_pages_in_book, ' pages in file ]'

firstpage = 1
lastpage = number_of_pages_in_book 
# lastpage = 3

# creating empty output file
print '[ creating epty output file ]'
cmd = 'echo > ' + output
print '> ' + cmd
os.system(cmd)

for i in range (firstpage,lastpage + 1):   # 1-(n-1)
    print " [ page", str(i), "/", lastpage, " ]"
    cmd = 'ddjvu -format=tiff -scale=300 '
    # cmd = cmd + ' -verbose '
    cmd = cmd + '-page=' + str(i) + ' '
    cmd = cmd + filename + ' ' + 'page.tif'
    print '> ' + cmd
    os.system(cmd)
    print ' [running tesseract... ] '
    cmd = 'tesseract ' + 'page.tif' + ' '
    cmd = cmd +  'page.text' 
    cmd = cmd + ' -l ' + language         # specifying language
    cmd = cmd + ' -psm 4 '                # specifying page layout for TOC
    print '> ' + cmd
    os.system(cmd)
    cmd = 'cat page.text.txt >> ' + output
    print '> ' + cmd
    os.system(cmd)
    cmd = 'rm -vf page.tif '
    os.system(cmd)
    cmd = 'rm -vf page.text.txt '
    os.system(cmd)

    
# djvu -> tif example:     

#   ddjvu -format=tiff -page=1 -scale=300 -verbose a.djvu page1.tif   # or PBM;

# tesseract example: 
#   tesseract a.tif text(.txt)  -l eng

