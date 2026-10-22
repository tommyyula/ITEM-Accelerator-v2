#!/usr/bin/env python3
"""封装既有简版和详版 HTML，不改写各页内容。Python 标准库即可。

运行 python3 build.py 生成 index.html（会前简版默认）和
presentation.html（会上详版默认）。两文件都独立包含两个版本，
可以按同一 MD 章节切换，无须后台、API 或网络组件。
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CHAPTERS=['Why · 为什么现在','总体架构','七个案例','能力底座','业务工具','Ontology','合作计划','决策收敛']


def load_deck(metadata: str, folder: str, expected: int) -> dict:
    plan=json.loads((ROOT/metadata).read_text(encoding='utf-8'))
    pages=[]
    for n,item in enumerate(plan,1):
        source=ROOT/folder/(item['id']+'.html')
        html=source.read_text(encoding='utf-8')
        if '<!doctype html>' not in html.lower() or not html.rstrip().lower().endswith('</html>'):
            raise ValueError(f'页面不完整：{source}')
        pages.append({**item,'n':n,'html':html})
    if len(pages)!=expected:
        raise ValueError(f'{folder} 应有 {expected} 页，实际 {len(pages)} 页')
    if len({p['id'] for p in pages})!=len(pages):
        raise ValueError(f'{folder} 页面 ID 重复')
    return {'pages':pages}


def main() -> None:
    payload={
        'version':2,
        'chapters':CHAPTERS,
        'decks':{
            'summary':load_deck('summary-deck.json','summary-slides',10),
            'detail':load_deck('deck.json','slides',40),
        },
        'videos':json.loads((ROOT/'videos.json').read_text(encoding='utf-8')),
        'markdown':(ROOT/'docs'/'meeting.md').read_text(encoding='utf-8'),
    }
    encoded=json.dumps(payload,ensure_ascii=False,separators=(',',':'))
    encoded=encoded.replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    template=(ROOT/'template.html').read_text(encoding='utf-8')
    for token in ['__DECK_DATA__','__DEFAULT_MODE__']:
        if template.count(token)!=1:
            raise ValueError(f'模板必须恰好含一个 {token}')
    for filename,mode in [('index.html','summary'),('presentation.html','detail')]:
        html=template.replace('__DECK_DATA__',encoded).replace('__DEFAULT_MODE__',mode)
        output=ROOT/filename
        output.write_text(html.rstrip()+'\n',encoding='utf-8')
        print(f'已构建：{output.resolve()}（默认 {mode}，{output.stat().st_size:,} 字节）')
    print('10页会前简版 ↔ 同章40页详版 ↔ 会后MD下载；左侧目录默认显示。')


if __name__=='__main__':
    main()
