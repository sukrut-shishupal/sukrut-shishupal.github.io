# Editable PDF source. Install: python -m pip install reportlab
# Set font/fontb below to installed DejaVu Sans font paths on your machine.
# The supplied paths are for Linux; Windows users can install DejaVu Sans and
# point these two variables at its .ttf files. Then run: python resume_source.py
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fontb='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DV',font));pdfmetrics.registerFont(TTFont('DVB',fontb));pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB')
ink=colors.HexColor('#172b2a');green=colors.HexColor('#153f3c');muted=colors.HexColor('#465650')
st={
'name':ParagraphStyle('name',fontName='DVB',fontSize=23,leading=27,textColor=ink,spaceAfter=6),
'position':ParagraphStyle('position',fontName='DV',fontSize=10,leading=14,textColor=green,spaceAfter=7),
'contact':ParagraphStyle('contact',fontName='DV',fontSize=8,leading=12,textColor=muted,spaceAfter=9),
'section':ParagraphStyle('section',fontName='DVB',fontSize=9,leading=12,textColor=green,spaceBefore=11,spaceAfter=5),
'role':ParagraphStyle('role',fontName='DVB',fontSize=8.8,leading=12,textColor=ink,spaceBefore=5,spaceAfter=2),
'body':ParagraphStyle('body',fontName='DV',fontSize=8.3,leading=11.9,textColor=ink,spaceAfter=4),
'bullet':ParagraphStyle('bullet',fontName='DV',fontSize=8.3,leading=11.9,textColor=ink,leftIndent=9,firstLineIndent=-7,spaceAfter=3),
'cite':ParagraphStyle('cite',fontName='DV',fontSize=7.7,leading=10.7,textColor=ink,spaceAfter=4),
}
out=Path(__file__).resolve().parent/'UPLOAD_THESE_FILES/files/Sukrut_Shishupal_Resume.pdf'
doc=SimpleDocTemplate(str(out),pagesize=letter,rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=30,title='Sukrut Shishupal, PhD | Machine Learning and Health Data Science',author='Sukrut Shishupal')
flow=[]
def p(t,k='body'): flow.append(Paragraph(t,st[k]))
def section(t):p(t.upper(),'section')
def bullet(t):p('• '+t,'bullet')
p('Sukrut Shishupal, PhD','name')
p('Machine Learning | Health Data Science | Biomedical Informatics','position')
p('Salt Lake City, Utah · <link href="mailto:sukrut.shishupal@gmail.com">sukrut.shishupal@gmail.com</link><br/><link href="https://sukrut-shishupal.github.io">sukrut-shishupal.github.io</link> · <link href="https://github.com/sukrut-shishupal">github.com/sukrut-shishupal</link> · <link href="https://www.linkedin.com/in/sukrutshishupal/">linkedin.com/in/sukrutshishupal</link>','contact')
flow.append(HRFlowable(width='100%',thickness=.7,color=colors.HexColor('#b9c9be')))
section('Profile')
p('Biomedical informatics researcher with a PhD, developing interpretable time-series methods for environmental and healthcare data. Experience in scientific data pipelines, geospatial analysis, machine learning, and collaborative health research.')
section('Technical strengths')
p('<b>Programming:</b> Python, R, SQL, Java<br/><b>Methods:</b> Time-series analysis, shapelet methods, feature engineering, clustering, statistical modeling<br/><b>Research workflows:</b> Large-scale data preparation, geospatial analysis, high-performance computing')
section('Experience')
p('Graduate Research Assistant | University of Utah | Nov 2022-present','role')
bullet('Develop temporal pattern extraction and reusable exposure representations for the SMARTER project.')
bullet('First author of an IEEE ICHI 2026 paper on a reusable exposure-pattern library derived from EPA data spanning 2004-2024, with 7- and 30-day windows.')
bullet('Contribute to telemedicine analysis and visualization, with co-authored publications in JMIR and JAMIA Open.')
p('Graduate Teaching Assistant | University of Utah | Aug 2023-present','role')
bullet('Co-developed materials and delivered lectures for Introduction to Programming (Fall 2023) and Biomedical Data Wrangling (Spring 2024 and Spring 2026).')
p('Trainee Software Developer | Automation Teknix | Nov 2020-May 2021','role')
p('Software development experience in the automation industry.')
section('Selected research')
p('<b>Nursing EHR activity:</b> Investigate local temporal patterns using 30-minute windows of activity recorded in 5-minute bins. Ongoing research.')
p('<b>Protein binding affinity:</b> Investigated graph-based features and machine learning in a thesis study of 101 heterodimeric protein complexes, comparing network representations with cross-validation.')
section('Education')
p('<b>PhD, Biomedical Informatics</b> | University of Utah | 2026<br/>Advisors: Dr. Kathy Sward and Dr. Ramkiran Gouripeddi')
p('<b>MS, Biomedical Informatics, Data Science Track</b> | University of Utah | 2024<br/><b>Integrated BS-MS, Bioinformatics &amp; Biotechnology</b> | Savitribai Phule Pune University | 2020')
section('Selected publications')
p('<b>First author.</b> A Reusable Library of Exposure Health Machine Learning Primitives. <i>IEEE ICHI</i>. 2026;481-489. <link href="https://doi.org/10.1109/ICHI69079.2026.00272">doi:10.1109/ICHI69079.2026.00272</link>','cite')
p('<b>Co-author.</b> Social vulnerability, lower broadband internet access, and rurality associated with lower telemedicine use in U.S. Counties. <i>JAMIA Open</i>. 2025;8(4):ooaf056. <link href="https://doi.org/10.1093/jamiaopen/ooaf056">doi:10.1093/jamiaopen/ooaf056</link>','cite')
p('<b>Second author.</b> Travel Distance Between Participants in US Telemedicine Sessions With Estimates of Emissions Savings: Observational Study. <i>JMIR</i>. 2024;26:e53437. <link href="https://doi.org/10.2196/53437">doi:10.2196/53437</link>','cite')
doc.build(flow)
print(out)
