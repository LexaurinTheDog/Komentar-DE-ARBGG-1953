from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib
W=Path(__file__).resolve().parent
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,data):self.parts.append(data)
def normalized(s):return ''.join(x.lower() for x in s if x.isalnum())
records=[]
for name,n in [('10-azb-18-22',44),('5-azb-23-20',33)]:
 source=W/f'cases/bag-{name}-source.md';live=W/f'sources/second-pass/bag-{name}.html'
 p=Text();p.feed(live.read_text());h=normalized(''.join(p.parts))
 body=source.read_text().split('## Gründe\n')[1]
 paragraphs=list(re.finditer(r'^(\d+) (.*?)(?=^\d+ |\Z)',body,re.M|re.S))
 matches=[]
 for m in paragraphs:
  text=m[2]
  if int(m[1])==n:text=text.rsplit('\n\n',3)[0]
  matches.append({'rn':int(m[1]),'normalized_full_paragraph_in_fresh_official_html':normalized(text) in h})
 assert len(matches)==n
 records.append({'case':name,'paragraphs':matches,'full_text_read_in_second_pass':True,'md_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'fresh_html_sha256':hashlib.sha256(live.read_bytes()).hexdigest(),'method':'Every numbered reasons paragraph of local national corpus checked against the freshly fetched primary BAG HTML after alphanumeric normalization; legal meaning read separately. This normalization comparison is not a substitute for semantic review.'})
(W/'cases/second-pass-text-check.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'case':r['case'],'paragraphs':len(r['paragraphs']),'mismatches':[p['rn'] for p in r['paragraphs'] if not p['normalized_full_paragraph_in_fresh_official_html']]} for r in records]))
