from pathlib import Path
import json,re,html
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether,Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor,Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

ROOT=Path(__file__).parent
SITE=ROOT.parent
OUT=SITE/'src/roi/pdfs'; OUT.mkdir(parents=True,exist_ok=True)
guides=json.loads((SITE/'src/roi/catalog.json').read_text(encoding='utf8'))
pdfmetrics.registerFont(TTFont('Inter','C:/Windows/Fonts/Inter-Regular.ttf'))
pdfmetrics.registerFontFamily('Inter',normal='Inter',bold='Inter',italic='Inter',boldItalic='Inter')
NAVY=HexColor('#0D1526'); STEEL=HexColor('#7B96B2'); ROSE=HexColor('#D6B0A0'); PAPER=HexColor('#F6F2ED'); INK=HexColor('#172036')
W,H=A4
styles={
 'body':ParagraphStyle('body',fontName='Inter',fontSize=9.7,leading=15,textColor=INK,spaceAfter=9),
 'heading':ParagraphStyle('heading',fontName='Inter',fontSize=17,leading=21,textColor=NAVY,spaceBefore=13,spaceAfter=9,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='Inter',fontSize=27,leading=33,textColor=NAVY,spaceAfter=16),
 'small':ParagraphStyle('small',fontName='Inter',fontSize=8.2,leading=12,textColor=INK,spaceAfter=6),
 'cell':ParagraphStyle('cell',fontName='Inter',fontSize=8.2,leading=12,textColor=INK),
 'white':ParagraphStyle('white',fontName='Inter',fontSize=8.6,leading=12,textColor=PAPER),
 'bullet':ParagraphStyle('bullet',fontName='Inter',fontSize=9.5,leading=14,textColor=INK,leftIndent=10,firstLineIndent=-9,spaceAfter=3),
 'formula':ParagraphStyle('formula',fontName='Inter',fontSize=9,leading=15,textColor=INK,backColor=HexColor('#E9E2DA'),borderPadding=10,spaceBefore=9,spaceAfter=12)
}
def markup(s):
    s=html.escape(s.replace('–','-').replace('—','-').replace('\u2011','-'))
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'\1',s)
    return s.replace('\n','<br/>')
def p(s,style='body'): return Paragraph(markup(s),styles[style])
def table(rows,widths=None,blank=False):
    data=[[p(v,'white' if ri==0 else 'cell') for v in row] for ri,row in enumerate(rows)]
    t=Table(data,colWidths=widths or [150,165,184],repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[PAPER,HexColor('#EDE7DF')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),1,ROSE),('LINEBELOW',(0,1),(-1,-1),.4,HexColor('#D0BEB0'))]))
    return t
def make_cover(g):
    def draw(c,doc):
        c.drawImage(str(SITE/'src/roi/cover-master.png'),0,0,width=W,height=H)
        c.setFillColor(ROSE); c.setFont('Inter',14.5)
        y=H*.343
        for line in g['coverLines']:
            size=14.5
            while pdfmetrics.stringWidth(line,'Inter',size)>W*.405: size-=.25
            c.setFont('Inter',size); c.drawString(W*.086,y,line); y-=23
        c.setTitle('The ROI of Smart Living - '+g['title']);c.setAuthor('LuxSync')
    return draw
def pages(g):
    def draw(c,doc):
        c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
        c.setFillColor(NAVY); c.rect(0,H-42,W,42,fill=1,stroke=0)
        c.setFont('Inter',9); c.setFillColor(ROSE); c.drawString(48,H-26,'LUXSYNC  /  THE ROI OF SMART LIVING')
        c.setStrokeColor(ROSE);c.setLineWidth(.8);c.line(48,44,W-48,44)
        c.setFillColor(INK);c.setFont('Inter',8);c.drawString(48,30,g['title']);c.drawRightString(W-48,30,f'{doc.page-1}')
    return draw
for g in guides:
    story=[Spacer(1,1),PageBreak(),p(g['title'],'title'),Image(str(SITE/'src/heroes'/(g['hero']+'-1600.webp')),width=499,height=180,kind='proportional'),Spacer(1,18)]
    heading_index=0
    for block in g['blocks']:
        kind=block['type']
        if kind=='heading':
            if heading_index in (1,3): story.append(PageBreak())
            story.append(p(block['text'],'heading'))
            heading_index+=1
        elif kind=='paragraph': story.append(p(block['text']))
        elif kind=='list':
            story.append(KeepTogether([p('- '+v,'bullet') for v in block['items']]))
            story.append(Spacer(1,5))
        elif kind=='formula':
            story.append(p('Reference method - enter and review values manually. Automated calculations are not included in this edition.','small'))
            story.append(p(block['text'],'formula'))
        elif kind=='table':
            rows=block['rows']
            if rows[0][0]=='Input':
                rows=[['Input','Your value / unit','Reference method']]+[[r[0],'________________\n'+r[1],r[2]] for r in rows[1:]]
            story.append(table(rows))
    story += [PageBreak(),p('Your measurement log','title'),p('Record observations before and after a change. Use comparable periods, consistent units, and your own measured data. Keep estimates and scenario values clearly labeled.'),p('Property / project: __________________________________________________'),p('Period: __________________  Recorded by: __________________________'),p('Phase:  Baseline / Pilot / Follow-up'),p('Record your observations','heading')]
    log=[['Value area','Measurement / unit','Notes / evidence']]+[[m['label'],'________________\n________________','________________\n________________'] for m in g['metrics']]
    story += [table(log),Spacer(1,14),p('Context: occupancy, weather, schedule, or equipment changes','heading'),p('______________________________________________________________________\n\n______________________________________________________________________'),PageBreak(),p('Compare two periods','title'),p('Copy recorded values side by side. This worksheet makes no automatic ROI, savings, or payback calculation. Explain differences in context before drawing conclusions.'),p('Period A: __________________  Period B: __________________'),table([['Value area','Period A / unit','Period B / unit']]+[[m['label'],'________________','________________'] for m in g['metrics']]),Spacer(1,16),p('What changed? What needs another measurement?','heading'),p('______________________________________________________________________\n\n______________________________________________________________________'),p('Continue online','heading'),p('Open this guide in the LuxSync ROI Guide Library to keep an editable worksheet, save measurement periods, and compare your recorded observations in your account.'),p('Where Luxury Lives Intelligently','small')]
    file=OUT/(g['id']+'.pdf')
    doc=SimpleDocTemplate(str(file),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=62,bottomMargin=60)
    doc.build(story,onFirstPage=make_cover(g),onLaterPages=pages(g))
    reader=PdfReader(file)
    text='\n'.join(x.extract_text() or '' for x in reader.pages)
    assert 'YOUR SUBTITLE' not in text
    assert 'Your measurement log' in text and 'Compare two periods' in text
    print(g['id'],len(reader.pages),'pages',file.stat().st_size,'bytes')

