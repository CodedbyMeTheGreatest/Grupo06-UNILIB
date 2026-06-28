import sys
import os

try:
    import pypdf
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

pdf_path = r"c:\Users\56958\Desktop\Proyectos\UNILIB_RQY1102-008D\EA02\EA_02_G6_Urrutia_Lefiman_Huenchullan_Pinto_informe.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

text_output = []
for idx, page in enumerate(reader.pages):
    text_output.append(f"--- PAGE {idx+1} ---")
    text_output.append(page.extract_text() or "")

with open("pdf_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(text_output))

print("PDF text extracted to pdf_text.txt successfully.")
