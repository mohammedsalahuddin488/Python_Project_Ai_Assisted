import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

os.chdir(os.path.dirname(__file__))

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x400")
        self.pdf_list = []
        
        # Title
        title_label = tk.Label(root, text="PDF Merger", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Add PDF button
        self.add_btn = tk.Button(button_frame, text="Add PDF", command=self.add_pdf, bg="#4CAF50", fg="white", padx=10)
        self.add_btn.pack(side=tk.LEFT, padx=5)
        
        # Remove PDF button
        self.remove_btn = tk.Button(button_frame, text="Remove Selected", command=self.remove_pdf, bg="#f44336", fg="white", padx=10)
        self.remove_btn.pack(side=tk.LEFT, padx=5)
        
        # Listbox for PDFs
        list_label = tk.Label(root, text="Selected PDFs:", font=("Arial", 10, "bold"))
        list_label.pack(anchor=tk.W, padx=20, pady=(10, 0))
        
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.pack(padx=20, pady=10)
        
        # Merge button
        self.merge_btn = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, bg="#2196F3", fg="white", padx=20, pady=10, font=("Arial", 12))
        self.merge_btn.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(root, text="Ready", fg="green")
        self.status_label.pack(pady=5)
    
    def add_pdf(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        for file in files:
            if file not in self.pdf_list:
                self.pdf_list.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))
    
    def remove_pdf(self):
        selected = self.listbox.curselection()
        if selected:
            for index in reversed(selected):
                self.pdf_list.pop(index)
                self.listbox.delete(index)
    
    def merge_pdfs(self):
        if not self.pdf_list:
            messagebox.showwarning("Warning", "Please add PDF files first!")
            return
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged.pdf"
        )
        
        if not output_file:
            return
        
        try:
            self.status_label.config(text="Merging...", fg="orange")
            self.root.update()
            
            writer = PdfWriter()
            for pdf in self.pdf_list:
                writer.append(pdf)
            
            writer.write(output_file)
            writer.close()
            
            self.status_label.config(text="Merged successfully!", fg="green")
            messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved as: {os.path.basename(output_file)}")
        except Exception as e:
            self.status_label.config(text="Error!", fg="red")
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = PDFMergerGUI(root)
    root.mainloop()