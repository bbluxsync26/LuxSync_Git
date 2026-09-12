import pathlib, re, json, shutil
ROOT=pathlib.Path(__file__).parent
SITE=ROOT.parent
SOURCE=SITE/'src/roi/source'
definitions=[
 ('commercial-offices','Commercial Offices','Commercial & care','plush-drift-commercial',['COMMERCIAL','OFFICES']),
 ('nursing-homes','Nursing Homes','Commercial & care','plush-drift-care',['NURSING HOMES']),
 ('senior-living-communities','Senior Living Communities','Commercial & care','aging-in-place',['SENIOR LIVING','COMMUNITIES']),
 ('str-owners','Short-Term Rental Owners','Short-term rentals','plush-drift-rental',['SHORT-TERM RENTAL','OWNERS']),
 ('str-operators','Short-Term Rental Operators','Short-term rentals','solutions',['SHORT-TERM RENTAL','OPERATORS']),
 ('str-managers','Short-Term Rental Managers','Short-term rentals','professionals',['SHORT-TERM RENTAL','MANAGERS']),
 ('residential-homeowners','Residential Homeowners','Residential','plush-drift-residential',['RESIDENTIAL','HOMEOWNERS']),
 ('residential-busy-professionals','Busy Professionals','Residential','professionals',['BUSY','PROFESSIONALS']),
 ('residential-intentional-parents','Intentional Parents & Families','Residential','families',['INTENTIONAL PARENTS','& FAMILIES']),
 ('residential-seniors-caregivers','Seniors, Caregivers & Aging in Place','Residential','plush-drift-care',['SENIORS & CAREGIVERS','AGING IN PLACE'])]
def parse(md):
    lines=md.splitlines(); result=[]; i=0
    while i<len(lines):
        s=lines[i].strip()
        if not s: i+=1; continue
        if s.startswith('# '): i+=1; continue
        if s=='## Where Luxury Lives Intelligently': i+=1; continue
        if s.startswith('## '): result.append({'type':'heading','text':s[3:]}); i+=1; continue
        if s.startswith('```'):
            i+=1; code=[]
            while i<len(lines) and not lines[i].startswith('```'): code.append(lines[i]); i+=1
            result.append({'type':'formula','text':'\n'.join(code)}); i+=1; continue
        if s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.match(r'^[-: ]+$',x) for x in cells): rows.append(cells)
                i+=1
            result.append({'type':'table','rows':rows}); continue
        if s.startswith('- ') or re.match(r'^\d+\. ',s):
            items=[]
            while i<len(lines) and (lines[i].strip().startswith('- ') or re.match(r'^\d+\. ',lines[i].strip())):
                items.append(re.sub(r'^(?:- |\d+\. )','',lines[i].strip())); i+=1
            result.append({'type':'list','items':items}); continue
        paras=[s]; i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||-|```)',lines[i]): paras.append(lines[i].strip()); i+=1
        result.append({'type':'paragraph','text':' '.join(paras)})
    return result
guides=[]
for slug,title,group,hero,cover in definitions:
    md=(SOURCE/(slug+'.md')).read_text(encoding='utf-8-sig'); blocks=parse(md)
    tables=[x['rows'] for x in blocks if x['type']=='table']
    guides.append({'id':slug,'title':title,'group':group,'hero':hero,'coverLines':cover,'audience':re.sub(r'\*\*','',blocks[0]['text']),'intro':blocks[1]['text'],'blocks':blocks,'metrics':[{'id':f'metric-{i}','label':row[0],'hint':row[1]} for i,row in enumerate(tables[0][1:])],'worksheet':[{'id':f'input-{i}','label':row[0],'unit':row[1],'method':row[2]} for i,row in enumerate(tables[1][1:])]})
(SITE/'src/roi').mkdir(exist_ok=True)
(SITE/'src/roi/catalog.json').write_text(json.dumps(guides,indent=2,ensure_ascii=False),encoding='utf8')

print(f'Prepared {len(guides)} complete guides from supplied Markdown.')

