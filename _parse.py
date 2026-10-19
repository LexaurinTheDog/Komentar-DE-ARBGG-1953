#!/usr/bin/env python3
"""Reproducible ArbGG extraction from the preserved GII XML; no network."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json,re,hashlib,difflib
W=Path(__file__).resolve().parent
R=ET.parse(W/'sources/arbgg.xml').getroot()
assert R.attrib['doknr']=='BJNR012670953'
assert R.findtext('norm/metadaten/jurabk')=='ArbGG'
def clean(s):
 return re.sub(r'\s+',' ',s).strip()
def render(el,depth=0):
 if el is None:return ''
 s=el.text or ''
 for c in el:
  if c.tag=='BR': s+='\n'
  elif c.tag=='DL':s+='\n'+render(c,depth+1)+'\n'
  elif c.tag=='DT':s+='  '*max(0,depth-1)+render(c,depth)+' '
  elif c.tag=='DD':s+=render(c,depth)+'\n'
  elif c.tag in ('P','LA','pre'):s+=render(c,depth)+'\n'
  else:s+=render(c,depth)
  s+=c.tail or ''
 return s

def content(el):
 if el is None:return ''
 return '\n\n'.join('\n'.join(line.rstrip() for line in render(c).strip().splitlines()) for c in el if render(c).strip())
chapters=[(1,'grundlagen','Allgemeine Vorschriften (§§ 1–13a)'),(2,'arbeitsgerichte','Arbeitsgerichte (§§ 14–32)'),(3,'obergerichte','Landesarbeitsgerichte und Bundesarbeitsgericht (§§ 33–45)'),(4,'elektronischer-prozess','Verfahrensgrundlagen und elektronischer Rechtsverkehr (§§ 46–50a)'),(5,'erste-instanz','Urteilsverfahren erster Instanz (§§ 51–63)'),(6,'rechtsmittel','Berufung, Revision und Beschwerden (§§ 64–79)'),(7,'beschlussverfahren','Beschlussverfahren (§§ 80–100)'),(8,'schiedsverfahren','Schiedsvertrag in Arbeitsstreitigkeiten (§§ 101–110)'),(9,'schlussvorschriften','Übergangs- und Schlussvorschriften (§§ 111–122)')]
def chapter(num):
 return 1 if num<14 else 2 if num<33 else 3 if num<46 else 4 if num<51 else 5 if num<64 else 6 if num<80 else 7 if num<101 else 8 if num<111 else 9
units=[];structure=[];heads=[];global_notes=[]
for n in R.findall('norm'):
 m=n.find('metadaten'); label=clean(m.findtext('enbez',''));g=m.find('gliederungseinheit')
 if g is not None:
  key=g.findtext('gliederungskennzahl');h=clean(g.findtext('gliederungsbez','')+' — '+g.findtext('gliederungstitel',''))
  level=len(key)//3;structure=structure[:level-1]+[h];heads.append({'key':key,'heading':h,'doknr':n.attrib['doknr']})
 if not label:
  notes=content(n.find('textdaten/fussnoten/Content'))
  if notes:global_notes.append(notes)
  continue
 assert re.fullmatch(r'§ \d+[a-z]?',label),label
 no=label[2:];title=clean(''.join(m.find('titel').itertext())) if m.find('titel') is not None else ''
 txt=content(n.find('textdaten/text/Content'))
 disposition='operative'
 if not txt:
  assert title=='(weggefallen)',(label,title)
  txt=title;disposition='repealed-empty-body-title-preserved'
 elif txt.strip()=='-':disposition='explicit-empty-slot'
 notes=content(n.find('textdaten/fussnoten/Content'))
 units.append({'id':'p'+no,'label':label,'title':title,'chapter':chapter(int(re.match(r'\d+',no)[0])),'structure':structure.copy(),'text':txt,'notes':[notes] if notes else [],'official_doknr':n.attrib['doknr'],'disposition':disposition})
(W/'units.jsonl').write_text(''.join(json.dumps(u,ensure_ascii=False)+'\n' for u in units))
meta={'cc':'de','lang':'de','repo':W.name,'repo_dir':'/Volumes/LaCie/open-commentary/de/'+W.name,'title':'Kommentar zum Arbeitsgerichtsgesetz','source_path':str(W/'sources/arbgg-canonical.md'),'intro_file':'00-einleitung.md','intro_desc':'Rechtsstand, Methode und Benutzung','labels':{'text':'Wortlaut der Vorschrift','chapter':'Kommentarkapitel','notes':'Amtlicher Hinweis'},'chapters':[{'n':n,'slug':s,'title':t} for n,s,t in chapters],'authoring_date':'2026-10-19','source_url':'https://www.gesetze-im-internet.de/arbgg/','legal_version':'Art. 7 G vom 20.05.2026, BGBl. 2026 I Nr. 152; seit 01.10.2026'}
(W/'meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
canon=['# Arbeitsgerichtsgesetz','Amtliche XML-Fassung: '+R.attrib['builddate']]+[x.findtext('standkommentar','') for x in R.findall('norm/metadaten/standangabe')]+global_notes
for u in units:canon+=['## '+u['label']+' '+u['title'],u['text']]+u['notes']
(W/'sources/arbgg-canonical.md').write_text('\n\n'.join(canon)+'\n')
(W/'sources/structure.json').write_text(json.dumps({'headings':heads,'general_editorial_notes':global_notes},ensure_ascii=False,indent=2))
# Original intake retained byte-for-byte; compare each numbered text independently.
old=(W/'sources/intake-original.md').read_text(); matches=list(re.finditer(r'^#### (§ \d+[a-z]?)(?: (.*))?$',old,re.M));changes=[]
for i,mt in enumerate(matches):
 label=mt[1];body=old[mt.end():matches[i+1].start() if i+1<len(matches) else len(old)]
 body=re.split(r'^### ',body,flags=re.M)[0].strip();u=next((u for u in units if u['label']==label),None)
 if u and re.sub(r'\s+',' ',body)!=re.sub(r'\s+',' ',u['text']):changes.append({'id':u['id'],'label':label,'old_body':body,'current_body':u['text'],'diff':list(difflib.unified_diff(body.splitlines(),u['text'].splitlines(),fromfile='intake',tofile='official-2026-10-19',lineterm=''))})
(W/'sources/change-map.json').write_text(json.dumps({'original_sha256':hashlib.sha256((W/'sources/intake-original.md').read_bytes()).hexdigest(),'current_xml_sha256':hashlib.sha256((W/'sources/arbgg.xml').read_bytes()).hexdigest(),'intake_numbered_units':len(matches),'changes_including_editorial_or_layout':changes},ensure_ascii=False,indent=2))
print(len(units),'provisions;',len(heads),'structural headings;',len(changes),'comparison differences')
