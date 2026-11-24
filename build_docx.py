import sys, copy
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION_START
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TITLE = "Respon Arugula terhadap Media Tanam dan Interval Irigasi Tetes di Licin, Banyuwangi"

doc = Document('reference.docx')

def para(text='', bold=False, center=False, size=12, space_after=6, italic=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    if text:
        r = p.add_run(text)
        r.bold = bold; r.italic = italic
        r.font.name = 'Times New Roman'; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0,0,0)
    return p

def blank(n=1):
    for _ in range(n):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0

def set_cell(cell, text, bold=False, center=False, size=12):
    cell.text = ''
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.bold = bold
    r.font.name = 'Times New Roman'; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0,0,0)

# ================= COVER =================
para('UNIVERSITAS 17 AGUSTUS 1945 BANYUWANGI', bold=True, center=True, size=14, space_after=0)
para('FAKULTAS PERTANIAN DAN PERIKANAN', bold=True, center=True, size=12, space_after=0)
para('PROGRAM STUDI S1 AGROTEKNOLOGI', bold=True, center=True, size=12, space_after=24)
blank(3)
para('PROPOSAL TUGAS AKHIR', bold=True, center=True, size=14, space_after=12)
para(TITLE, bold=True, center=True, size=13, space_after=36)
para('Disusun oleh:', center=True, space_after=6)
para('[Nama Mahasiswa]', bold=True, center=True, space_after=0)
para('NIM. [NIM]', center=True, space_after=24)
para('PROGRAM STUDI S1 AGROTEKNOLOGI', center=True, space_after=24)
para('Dibimbing oleh:', center=True, space_after=6)
para('[Nama Pembimbing 1]', center=True, space_after=0)
para('[Nama Pembimbing 2]', center=True, space_after=36)
para('BANYUWANGI, [Bulan Tahun]', bold=True, center=True, size=12)

doc.add_page_break()

# ================= LEMBAR PENGESAHAN =================
para('LEMBAR PENGESAHAN', bold=True, center=True, size=14, space_after=12)
para('Proposal Tugas Akhir', center=True, space_after=0)
para(TITLE, center=True, italic=True, space_after=18)
para('Disusun oleh:', bold=True, space_after=6)

t = doc.add_table(rows=3, cols=2)
try:
    t.style = 'Table Grid'
except Exception:
    pass
for i, (k, v) in enumerate([
    ('Nama', '[Nama Mahasiswa]'),
    ('NIM', '[NIM]'),
    ('Program Studi', 'S1 Agroteknologi'),
]):
    set_cell(t.rows[i].cells[0], k, bold=True)
    set_cell(t.rows[i].cells[1], v)
doc.add_paragraph().paragraph_format.space_after = Pt(6)
para('Proposal Tugas Akhir ini telah disetujui dan dinyatakan memenuhi syarat akademik.', space_after=18)

def sig_block(title, name):
    tb = doc.add_table(rows=1, cols=2)
    tb.autofit = True
    return tb

def fill_sig(cell, role_title, name):
    cell.text = ''
    p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(role_title + '\n')
    r.bold = True; r.font.name = 'Times New Roman'; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0,0,0)
    for _ in range(3):
        cell.add_paragraph()
    p2 = cell.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p2.add_run(name + '\n'); r.bold = True
    r.font.name = 'Times New Roman'; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0,0,0)
    p3 = cell.add_paragraph(); p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p3.add_run('[NIP].'); r.font.name = 'Times New Roman'; r.font.size = Pt(12)

tb1 = sig_block('', '')
fill_sig(tb1.rows[0].cells[0], 'Koordinator Program Studi', '[Nama Koordinator]')
fill_sig(tb1.rows[0].cells[1], 'Pembimbing I', '[Nama Pembimbing 1]')
doc.add_paragraph().paragraph_format.space_after = Pt(12)
tb2 = sig_block('', '')
fill_sig(tb2.rows[0].cells[0], 'Pembimbing II', '[Nama Pembimbing 2]')
fill_sig(tb2.rows[0].cells[1], 'Dekan Fakultas Pertanian dan Perikanan', '[Nama Dekan]')
para('Banyuwangi, [Bulan Tahun]', center=True, space_after=0)

# ================= PERNYATAAN =================
doc.add_page_break()
para('PERNYATAAN KEASLIAN KARYA TULIS', bold=True, center=True, size=14, space_after=18)
for t_ in [
    'Yang bertanda tangan di bawah ini:',
    'Nama          : [Nama Mahasiswa]',
    'NIM           : [NIM]',
    'Program Studi : S1 Agroteknologi',
    'Judul Proposal Tugas Akhir : ' + TITLE,
]:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.first_line_indent = Cm(0)
    r = p.add_run(t_); r.font.name = 'Times New Roman'; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0,0,0)
para('Menyatakan dengan sesungguhnya bahwa Proposal Tugas Akhir ini adalah karya ilmiah saya sendiri, bukan hasil plagiat, duplikasi, atau penyalahgunaan karya orang lain. Jika dikemudian hari terbukti terdapat pelanggaran terhadap etika ilmiah, saya bersedia menerima sanksi akademik sesuai ketentuan yang berlaku.', space_after=18)

pt = doc.add_table(rows=1, cols=2)
pt.autofit = True
cellL = pt.rows[0].cells[0]; cellL.text = ''
cellR = pt.rows[0].cells[1]
p = cellR.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
r = p.add_run('Banyuwangi, [Bulan Tahun]\n\n\n\n'); r.font.name = 'Times New Roman'; r.font.size = Pt(12)
p2 = cellR.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p2.add_run('[Nama Mahasiswa]\n'); r.bold = True
r.font.name = 'Times New Roman'; r.font.size = Pt(12)
p3 = cellR.add_paragraph(); p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p3.add_run('NIM. [NIM]'); r.font.name = 'Times New Roman'; r.font.size = Pt(12)

# ================= SECTION 2: DAFTAR ISI =================
sec2 = doc.add_section(WD_SECTION_START.NEW_PAGE)
sec2.footer.is_linked_to_previous = False
fp = sec2.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = fp.add_run()
fld1 = OxmlElement('w:fldChar'); fld1.set(qn('w:fldCharType'), 'begin')
instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve'); instr.text = ' PAGE '
fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'), 'end')
run._r.append(fld1); run._r.append(instr); run._r.append(fld2)
run.font.name = 'Times New Roman'; run.font.size = Pt(12)
sectPr = sec2._sectPr
pg = OxmlElement('w:pgNumType'); pg.set(qn('w:fmt'), 'lowerRoman'); pg.set(qn('w:start'), '1')
sectPr.insert(0, pg)
sec2.top_margin, sec2.bottom_margin = Cm(3), Cm(3)
sec2.left_margin, sec2.right_margin = Cm(4), Cm(3)
sec2.page_width, sec2.page_height = Cm(21.0), Cm(29.7)

para('DAFTAR ISI', bold=True, center=True, size=14, space_after=18)
p = doc.add_paragraph()
r = p.add_run()
f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin'); r._r.append(f1)
it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = ' TOC \\o "1-2" \\h \\z \\u '
r._r.append(it)
f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'separate'); r._r.append(f2)
r2 = p.add_run('(Daftar isi akan terisi otomatis setelah field diperbarui: klik kanan field → Update Field, atau tekan Ctrl+A lalu F9)')
r2.font.size = Pt(10); r2.italic = True
f3 = OxmlElement('w:fldChar'); f3.set(qn('w:fldCharType'), 'end'); r2._r.append(f3)

# ================= SECTION 3: ISI =================
sec3 = doc.add_section(WD_SECTION_START.NEW_PAGE)
sec3.footer.is_linked_to_previous = False
fp3 = sec3.footer.paragraphs[0]; fp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
run3 = fp3.add_run()
fd1 = OxmlElement('w:fldChar'); fd1.set(qn('w:fldCharType'), 'begin')
it3 = OxmlElement('w:instrText'); it3.set(qn('xml:space'), 'preserve'); it3.text = ' PAGE '
fd2 = OxmlElement('w:fldChar'); fd2.set(qn('w:fldCharType'), 'end')
run3._r.append(fd1); run3._r.append(it3); run3._r.append(fd2)
run3.font.name = 'Times New Roman'; run3.font.size = Pt(12)
sectPr3 = sec3._sectPr
pg3 = OxmlElement('w:pgNumType'); pg3.set(qn('w:fmt'), 'decimal'); pg3.set(qn('w:start'), '1')
sectPr3.insert(0, pg3)
sec3.top_margin, sec3.bottom_margin = Cm(3), Cm(3)
sec3.left_margin, sec3.right_margin = Cm(4), Cm(3)
sec3.page_width, sec3.page_height = Cm(21.0), Cm(29.7)

# ================= MERGE body.docx =================
body_doc = Document('body.docx')
body_el = body_doc.element.body
# cari posisi sectPr terakhir di dokumen tujuan
sectPr_target = doc.element.body.find(qn('w:sectPr'))
for child in list(body_el):
    if child.tag == qn('w:sectPr'):
        continue
    doc.element.body.insert(list(doc.element.body).index(sectPr_target), copy.deepcopy(child))
    sectPr_target = doc.element.body.find(qn('w:sectPr'))

doc.save('Proposal Tugas Akhir - Arugula (UNTAG).docx')
print('saved Proposal Tugas Akhir - Arugula (UNTAG).docx')
