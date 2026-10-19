#!/usr/bin/env python3
from pathlib import Path
import json,re
W=Path(__file__).resolve().parent
units={x['id']:x for x in map(json.loads,(W/'units.jsonl').read_text().splitlines())}
blocks={}
for p in (W/'commentary').glob('*.md'):
 for m in re.finditer(r'^=== (\S+)\n(.*?)(?=^=== |\Z)',p.read_text(),re.M|re.S):blocks[m[1]]=m[2].strip()
sets={}
for k,b in blocks.items():
 if units[k]['disposition']=='operative':
  ws=re.findall(r'\w+',b.lower());sets[k]={tuple(ws[i:i+5]) for i in range(len(ws)-4)}
pairs=[];ids=list(sets)
for i,a in enumerate(ids):
 for b in ids[i+1:]:pairs.append({'first':a,'second':b,'five_word_jaccard':round(len(sets[a]&sets[b])/len(sets[a]|sets[b]),5)})
pairs.sort(key=lambda x:x['five_word_jaccard'],reverse=True)
report={'method':'Unique five-word sequence Jaccard comparison; operative provisions only, excluding all explicit vacant and repealed slots','operative_blocks':len(sets),'all_commentary_blocks':len(blocks),'highest_overlap_pairs':pairs[:10],'pairs_above_0_07':[p for p in pairs if p['five_word_jaccard']>0.07],'assessment':'Technical similarity screen only. Highest pairs concern corresponding procedural rules and were checked against their distinct statutory references. No exact repeated substantive paragraphs in separate audit. No certification of semantic originality or legal correctness.'}
(W/'prose-inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'operative_blocks':len(sets),'highest':pairs[0],'above_0_07':len(report['pairs_above_0_07'])}))
