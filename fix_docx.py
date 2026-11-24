import sys, copy
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FN = 'Proposal Tugas Akhir - Arugula (UNTAG).docx'
doc = Document(FN)

JUNK_END = 'UNIVERSITAS 17 AGUSTUS 1945 BANYUWANGI'

BLOCK = [
 'Kata kunci: arugula, Eruca sativa, media tanam, irigasi tetes, interval penyiraman, polybag.',
 'Arugula (Eruca sativa Mill.) merupakan sayuran daun bernilai ekonomi tinggi',
 'ABSTRAK',
 'Akhir kata, penulis menyadari',
 'Penulis mengucapkan terima kasih kepada:',
 'Proposal Tugas Akhir dengan judul "Respon Arugula',
 'Puji syukur penulis panjatkan',
 'KATA PENGANTAR',
]

# 1) hapus paragraf sampah di awal (sebelum cover)
removed = 0
for p in list(doc.paragraphs):
    if p.text.strip() == JUNK_END:
        break
    p._p.getparent().remove(p._p); removed += 1
print('junk removed:', removed)

# 2) hapus blok KP/ABSTRAK yang tersebar (semua paragraf yg teksnya cocok)
block_texts = {t for t in BLOCK}
removed2 = 0
for p in list(doc.paragraphs):
    tx = p.text.strip()
    if any(tx == b or tx.startswith(b) for b in BLOCK):
        p._p.getparent().remove(p._p); removed2 += 1
print('block removed:', removed2)

def make_p(text, bold=False, center=False, size=12, page_break=False):
    p = OxmlElement('w:p')
    if page_break or center or bold or size != 12:
        pPr = OxmlElement('w:pPr')
        if page_break:
            pb = OxmlElement('w:pageBreakBefore'); pPr.append(pb)
        if center:
            jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center'); pPr.append(jc)
        p.append(pPr)
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rf = OxmlElement('w:rFonts')
    for a in ('w:ascii','w:hAnsi','w:cs'):
        rf.set(qn(a), 'Times New Roman')
    rPr.append(rf)
    if bold:
        b = OxmlElement('w:b'); rPr.append(b)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(int(size*2))); rPr.append(sz)
    r.append(rPr)
    t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text
    r.append(t); p.append(r)
    return p

NEW_BLOCK = [
    ('KATA PENGANTAR', True),
    ('Puji syukur penulis panjatkan ke hadirat Allah SWT yang telah melimpahkan rahmat dan hidayah-Nya, sehingga Proposal Tugas Akhir ini dapat disusun dengan baik.', False),
    ('Proposal Tugas Akhir dengan judul "Respon Arugula terhadap Media Tanam dan Interval Irigasi Tetes di Licin, Banyuwangi" ini disusun untuk memenuhi salah satu syarat kelulusan Program Studi S1 Agroteknologi, Fakultas Pertanian dan Perikanan, Universitas 17 Agustus 1945 Banyuwangi.', False),
    ('Penulis mengucapkan terima kasih kepada: (1) Orang tua/wali yang senantiasa memberikan dukungan; (2) Dosen pembimbing yang telah memberikan bimbingan dan arahan; (3) Koordinator Program Studi S1 Agroteknologi; (4) Rekan-rekan mahasiswa serta seluruh pihak yang telah membantu hingga Proposal Tugas Akhir ini dapat diselesaikan.', False),
    ('Akhir kata, penulis menyadari Proposal Tugas Akhir ini masih memiliki kekurangan. Oleh karena itu, kritik dan saran yang membangun sangat diharapkan demi perbaikan di masa mendatang.', False),
    ('ABSTRAK', True),
    ('Arugula (Eruca sativa Mill.) merupakan sayuran daun bernilai ekonomi tinggi yang cocok dibudidayakan di dataran tinggi seperti Kecamatan Licin, Kabupaten Banyuwangi. Budidaya dalam polybag memerlukan pengelolaan air yang tepat karena arugula berakar dangkal, sedangkan efektivitas irigasi tetes sangat bergantung pada kemampuan media tanam menahan air. Penelitian ini bertujuan mengetahui pengaruh komposisi media tanam dan interval irigasi tetes terhadap pertumbuhan dan hasil arugula, serta interaksi keduanya, melalui Rancangan Acak Lengkap faktorial 2 x 3 dengan 3 ulangan di bawah rain shelter. Faktor media meliputi tanah + kompos (1:1) dan tanah + kompos + sekam bakar (1:1:1); faktor interval meliputi penyiraman setiap hari, 2 hari sekali, dan 3 hari sekali dengan volume air per penyiraman yang sama. Parameter yang diamati meliputi tinggi tanaman, jumlah daun, bobot segar, dan water use efficiency (WUE), didukung data monitoring kelembapan dan suhu media berbasis ESP32. Hasil penelitian diharapkan menjadi dasar rekomendasi paket budidaya arugula polybag yang efisien air.', False),
    ('Kata kunci: arugula, Eruca sativa, media tanam, irigasi tetes, interval penyiraman, polybag.', False),
]

# 3) cari paragraf DAFTAR ISI, sisipkan blok baru sebelumnya
target = None
for p in doc.paragraphs:
    if p.text.strip() == 'DAFTAR ISI':
        target = p; break
assert target is not None

for i,(text,is_title) in enumerate(NEW_BLOCK):
    if is_title:
        el = make_p(text, bold=True, center=True, size=14, page_break=(text=='ABSTRAK'))
    else:
        el = make_p(text)
    target._p.addprevious(el)

# page break before DAFTAR ISI juga
pPr = target._p.find(qn('w:pPr'))
if pPr is None:
    pPr = OxmlElement('w:pPr'); target._p.insert(0, pPr)
if pPr.find(qn('w:pageBreakBefore')) is None:
    pPr.append(OxmlElement('w:pageBreakBefore'))

doc.save(FN)
print('saved')

# verifikasi
doc2 = Document(FN)
for i,p in enumerate(doc2.paragraphs[:75]):
    t=p.text.strip()
    if t and i<70: print(i,'|',t[:60])
PYEOF = None
