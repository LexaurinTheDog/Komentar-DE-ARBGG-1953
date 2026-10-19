"""Run in assigned WORK: compare freshly fetched XML, manuscript and rendered book.

The OUTPUT copy documents this verification algorithm; authoring fragments remain
in WORK because their relative links target the assembled book's root.
"""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
from collections import Counter
W=Path(__file__).resolve().parent
meta=json.loads((W/'meta.json').read_text());O=Path(meta['repo_dir'])
units=[json.loads(x) for x in (W/'units.jsonl').read_text().splitlines()]
root=ET.parse(W/'sources/second-pass/arbgg-current.xml').getroot()
assert root.findtext('norm/metadaten/jurabk')=='ArbGG'
expected=[];raw={}
for n in root.findall('norm'):
 label=n.findtext('metadaten/enbez','')
 if label:
  assert re.fullmatch(r'§ \d+[a-z]?',label)
  k='p'+label.split()[1];expected.append(k);raw[k]=n
parsed=[u['id'] for u in units]
ledger=json.loads((W/'second-pass-unit-review.json').read_text())
reviewed={x['id']:x for x in ledger['units']}
blocks={}
for p in (W/'commentary').glob('*.md'):
 for m in re.finditer(r'^=== (\S+)\n(.*?)(?=^=== |\Z)',p.read_text(),re.M|re.S):
  assert m[1] not in blocks;blocks[m[1]]=m[2].strip()
def compact(x):return re.sub(r'\s+','',x)
statutory_errors=[];render_errors=[];ledger_errors=[]
for u in units:
 n=raw[u['id']];el=n.find('textdaten/text/Content')
 actual=''.join(el.itertext()) if el is not None else ''
 if not actual.strip():actual=n.findtext('metadaten/titel','')
 if compact(actual)!=compact(u['text']):statutory_errors.append(u['id'])
 chapter=next(c for c in meta['chapters'] if c['n']==u['chapter'])
 book=(O/f"{chapter['n']:02}-{chapter['slug']}.md").read_text()
 sections=re.split(r'^### ',book,flags=re.M)[1:]
 section=next(s for s in sections if s.splitlines()[0].split(' — ')[0]==u['label'])
 quote='\n'.join(line[2:] if line.startswith('> ') else '' for line in section.splitlines() if line.startswith('>'))
 if compact(quote)!=compact(u['text']) or blocks[u['id']] not in section:render_errors.append(u['id'])
 if not reviewed[u['id']]['reviewed'] or reviewed[u['id']]['commentary_sha256']!=hashlib.sha256(blocks[u['id']].encode()).hexdigest():ledger_errors.append(u['id'])
casechecks=json.loads((W/'cases/second-pass-text-check.json').read_text())
case_errors=[f"{r['case']}:{p['rn']}" for r in casechecks for p in r['paragraphs'] if not p['normalized_full_paragraph_in_fresh_official_html']]
corrected=json.loads((W/'second-pass-corrections.json').read_text())
report={'expected_ids_from_fresh_official_xml':expected,'parsed_ids':parsed,'units_reviewed':len(reviewed),'commented_units':len(blocks),'missing_ids':sorted(set(expected)-set(parsed)),'extra_ids':sorted(set(parsed)-set(expected)),'duplicate_ids':[k for k,v in Counter(parsed).items() if v>1],'statutory_nonwhitespace_mismatches':statutory_errors,'render_or_commentary_mismatches':render_errors,'review_hash_mismatches':ledger_errors,'case_paragraphs_checked':sum(len(r['paragraphs']) for r in casechecks),'case_paragraph_mismatches':case_errors,'corrections':len(corrected),'source_sha256':hashlib.sha256((W/'sources/second-pass/arbgg-current.xml').read_bytes()).hexdigest(),'annex_disposition':'No operative annex record in current official XML/index; general Anhang EV nonapplication note preserved in structure.json and introduction.','independent_external_professional_approval':False}
report['ok']=expected==parsed and set(reviewed)==set(parsed)==set(blocks) and not any([statutory_errors,render_errors,ledger_errors,case_errors])
(W/'second-pass-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['units_reviewed','commented_units','case_paragraphs_checked','corrections','statutory_nonwhitespace_mismatches','render_or_commentary_mismatches','review_hash_mismatches','ok']}))
raise SystemExit(0 if report['ok'] else 1)
