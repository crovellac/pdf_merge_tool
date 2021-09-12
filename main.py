import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger
import os


window = tk.Tk()
window.title("PDF Merger")
window.geometry('500x200')

title_frame = tk.Frame(window)
title_frame.pack()
title_label = tk.Label(title_frame, text='PDF Merger', font=("TkDefaultFont","30"))
title_label.pack()

work_frame = tk.Frame(window)
work_frame.pack()

render_frame = tk.Frame(window)
render_frame.pack()

#--------Input for Document 1-----------------
input1_label = tk.Label(work_frame, text='Document 1:')
input1_label.grid(column=0, row=0)
input1_file_text = tk.Text(work_frame, state='disabled', width=30, height=1)
input1_file_text.grid(column=1, row=0)


def clicked_input1():
    pdf1_name = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("Document","*.pdf")])
    input1_file_text.configure(state='normal')
    input1_file_text.delete('end')
    input1_file_text.insert('end',pdf1_name)
    input1_file_text.configure(state='disabled')
input1_browse_btn = tk.Button(work_frame, text='Browse', command=clicked_input1)
input1_browse_btn.grid(column=2, row=0)

#----------Input for Document 2------------------
input2_label = tk.Label(work_frame, text='Document 2:')
input2_label.grid(column=0, row=1)
input2_file_text = tk.Text(work_frame, state='disabled', width=30, height=1)
input2_file_text.grid(column=1, row=1)


def clicked_input2():
    pdf2_name = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("Document","*.pdf")])
    input2_file_text.configure(state='normal')
    input2_file_text.delete('end')
    input2_file_text.insert('end',pdf2_name)
    input2_file_text.configure(state='disabled')
input2_browse_btn = tk.Button(work_frame, text='Browse', command=clicked_input2)
input2_browse_btn.grid(column=2, row=1)

output_name_label = tk.Label(work_frame, text='Output filename:')
output_name_label.grid(column=0, row=2)
output_name_text = tk.Text(work_frame, width=30, height=1)
output_name_text.grid(column=1, row=2)
output_filetype_label = tk.Label(work_frame, text='.pdf')
output_filetype_label.grid(column=2,row=2)

#---------Merging the PDFs-----------------

status_text1 = tk.Label(render_frame, text='')
status_text2 = tk.Label(render_frame, text='')

def clicked_mergebutton():
    pdf1_name = input1_file_text.get('1.0', 'end-1c')
    pdf2_name = input2_file_text.get('1.0', 'end-1c')
    output_filename = output_name_text.get("1.0", "end-1c")
    if pdf1_name and pdf2_name and output_filename:
        pdf_merger = PdfFileMerger()
        pdf_merger.append(pdf1_name)
        pdf_merger.append(pdf2_name)
        pdf_merger.write("./"+output_filename+'.pdf')
        status_text1['text'] = "Wrote "+output_filename+".pdf to"
        status_text2['text'] = os.getcwd()
merge_button = tk.Button(render_frame, text='Merge', command=clicked_mergebutton)
merge_button.pack()
status_text1.pack()
status_text2.pack()

window.mainloop()
