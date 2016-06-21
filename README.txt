-------------------------------------------------------------------------------------------
# Merging two PDFs

If you need to merge two PDFs named 1.pdf and 2.pdf, just double-click the merge_two_pdfs.sh script and a PDF named merged.pdf will be produced as output.

-------------------------------------------------------------------------------------------
# Merging all PDFs in a folder

If you need to merge all PDFs in a folder, name the PDFs in such a way that order is maintained (i.e., 01.pdf, 02.pdf, 03.pdf, etc. or A.pdf, B.pdf, C.pdf, etc.) and double-click the merge_all_pdfs.sh script and a PDF named merged.pdf will be produced as output.

-------------------------------------------------------------------------------------------
# Reverse Collation and Merging

If you need to collate two PDFs representing the even and odd numbered pages of a single document aptly named even.pdf and odd.pdf (where even.pdf is in reverse order), just double-click the reverse_collate_and_merge_pdfs.sh script and a PDF named merged.pdf will be produced as output.

To produce the two pdfs, simply scan all of one side of a stack of documents and then flip the stack of documents over and scan the opposite side of the stack of documents. You'll name the first set even.pdf and the second set odd.pdf. You'll notice that even.pdf has the documents in reverse order. By running reverse_collate_and_merge_pdfs.sh, the even.pdf documents get added in reverse order before collation, so the script will handle that use case.

-------------------------------------------------------------------------------------------