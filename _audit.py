#!/usr/bin/env python3
"""Independent coverage and XML character audit, then manuscript/link checks."""
from pathlib import Path
from collections import Counter,defaultdict
import re,json,hashlib,xml.etree.ElementTree as E,sys,urllib.parse
W=Path(__file__).resolve().parent
xml=W/'sources/arbgg.xml';root=E.parse(xml).getroot()
units=[json.loads(l) for l in (W/'units.jsonl').read_text().splitlines() if l]
expected=[];raw={};headings=[];unclassified=[]
for n in root.findall('norm'):
 m=n.find('metadaten');lab=m.findtext('enbez')
 if lab:
  assert re.fullmatch(r'§ \d+[a-z]?',lab),lab
  ident='p'+lab.split()[1];expected.append(ident);raw[ident]=n
 elif m.find('gliederungseinheit') is not None:headings.append(n.attrib['doknr'])
 elif m.findtext('jurabk')=='ArbGG' and m.findtext('langue')=='Arbeitsgerichtsgesetz':pass
 else:unclassified.append(n.attrib['doknr'])
parsed=[u['id'] for u in units]
# Independent index-HTML enumeration, not copied from parser output.
html_ids=list(dict.fromkeys('p'+x for x in re.findall(r'href="__([0-9]+[a-z]?)\.html"',(W/'sources/index.html').read_text(encoding='iso-8859-1'))))
missing=sorted(set(expected)-set(parsed));extra=sorted(set(parsed)-set(expected));dupes=[k for k,v in Counter(parsed).items() if v>1]
def chars(s):return re.sub(r'\s+','',s)
text_errors=[];note_errors=[];empty=[];note_count=0
for u in units:
 n=raw[u['id']];body=n.find('textdaten/text/Content');t=''.join(body.itertext()) if body is not None else ''
 if not t.strip():
  title=n.findtext('metadaten/titel','');empty.append({'id':u['id'],'official_body':'empty','official_title':title,'rendering':'Wegfallvermerk aus amtlicher Überschrift'});t=title
 elif t.strip()=='-':empty.append({'id':u['id'],'official_body':'-','rendering':'Unveränderte ausdrückliche Leerstelle'})
 if chars(t)!=chars(u['text']):text_errors.append(u['id'])
 note=n.find('textdaten/fussnoten');nt=''.join(note.itertext()) if note is not None else ''
 if nt.strip():note_count+=1
 if chars(nt)!=chars(''.join(u.get('notes',[]))):note_errors.append(u['id'])
report={'official_source':'https://www.gesetze-im-internet.de/arbgg/xml.zip','xml_path':'sources/arbgg.xml','xml_sha256':hashlib.sha256(xml.read_bytes()).hexdigest(),'official_builddate':root.attrib['builddate'],'expected_ids':expected,'parsed_ids':parsed,'index_html_ids':html_ids,'counts':{'xml_norm_records':len(root.findall('norm')),'numbered_provisions':len(expected),'structural_headings':len(headings),'header_records':1,'intake_units_including_headings':166,'numbered_notes':note_count},'missing_ids':missing,'extra_ids':extra,'duplicate_ids':dupes,'index_discrepancies':sorted(set(html_ids)^set(expected)),'xml_nonwhitespace_character_mismatches':text_errors,'footnote_mismatches':note_errors,'empty_and_repealed_slots':empty,'unclassified_records':unclassified,'annex_disposition':[{'identifier':'Anhang EV','disposition':'Nicht als operativer Normdatensatz im amtlichen Gesamt-XML oder Inhaltsverzeichnis vorhanden. Allgemeiner amtlicher Hinweis erklärt die Einigungsvertrags-Maßgaben ausdrücklich für nicht mehr anzuwenden. Hinweis vollständig in structure.json und Einleitung erhalten; kein historischer Anhang als aktuelles Recht ergänzt.'}],'scope':'Alle im amtlichen Gesamt-XML enthaltenen nummerierten Vorschriften; Gliederungen und Hinweise getrennt erhalten. Keine Zusammenfügung historischer Fassungen.'}
report['ok']=not any([missing,extra,dupes,text_errors,note_errors,unclassified,report['index_discrepancies']]) and expected==parsed
(W/'completeness-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Commentary identifiers, lengths, exact repetitions; length is not legal-quality proof.
blocks={};duplicates=[];delimiters=Counter()
for p in sorted((W/'commentary').glob('*.md')):
 for m in re.finditer(r'^=== (\S+)\n(.*?)(?=^=== |\Z)',p.read_text(),re.M|re.S):
  k,b=m[1],m[2].strip();delimiters[k]+=1;blocks[k]=b
repeated=defaultdict(list)
for k,b in blocks.items():
 for para in re.split(r'\n\s*\n',b):
  if len(para)>150:repeated[para].append(k)
repeats=[{'ids':v,'text':k} for k,v in repeated.items() if len(v)>1]
meta=json.loads((W/'meta.json').read_text());out=Path(meta['repo_dir']);bad_links=[]
for p in out.rglob('*.md') if out.exists() else []:
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
  if target.startswith(('http:','https:','mailto:','#')):continue
  q=target.split('#')[0].strip('<>')
  if q and not (p.parent/urllib.parse.unquote(q)).exists():bad_links.append({'file':str(p.relative_to(out)),'target':target})
audit={'units':len(units),'commented_units':len(blocks),'commentary_chars':sum(map(len,blocks.values())),'missing_comments':sorted(set(parsed)-set(blocks)),'extra_comments':sorted(set(blocks)-set(parsed)),'duplicate_delimiters':{k:v for k,v in delimiters.items() if v>1},'ordinary_units_below_700_chars':[u['id'] for u in units if len(u['text'])>160 and len(blocks.get(u['id'],''))<700],'exact_repeated_substantive_paragraphs':repeats,'broken_local_links':bad_links,'minimum_length_is_quality_proof':False,'legal_review':'Author source-based drafting checks only; independent second pass outstanding.'}
audit['ok']=report['ok'] and not any([audit['missing_comments'],audit['extra_comments'],audit['duplicate_delimiters'],repeats,bad_links])
(W/'audit-report.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'completeness_ok':report['ok'],'expected':len(expected),'parsed':len(parsed),'commented':len(blocks),'xml_text_mismatches':text_errors,'footnote_mismatches':note_errors,'broken_links':bad_links,'repeated_paragraphs':len(repeats),'audit_ok':audit['ok']},ensure_ascii=False))
sys.exit(0 if audit['ok'] else 1)
