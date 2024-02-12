from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 45)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", align="C")
        self.ln(20)
        self.image("shirtificate.png", x=5, y=80, w=200)


name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 240, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
