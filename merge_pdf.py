import os
from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = "C:\Users\Neophile\Desktop\share\scan"
merged_file = 'notes'
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()

for filename in pdf_files:
	print "Adding {filename} to the file.".format(filename=filename)
	merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(files_dir, merged_file+".pdf"))