# -*- coding: utf-8 -*-
"""assets/data/*.json → assets/js/data-bundle.js 생성
JSON을 수정한 뒤 이 스크립트를 한 번 실행하세요:  python build-data.py
(파일을 더블클릭해 file://로 열어도 뉴스·제품·FAQ가 보이도록 데이터를 스크립트로 묶습니다)"""
import json, glob, os
here = os.path.dirname(os.path.abspath(__file__))
data = {}
for f in sorted(glob.glob(os.path.join(here, 'assets', 'data', '*.json'))):
    data[os.path.splitext(os.path.basename(f))[0]] = json.load(open(f, encoding='utf-8'))
js = '''/* 자동 생성 파일: build-data.py 로 다시 만드세요. 직접 수정하지 마세요. */
window.BP_DATA = %s;
(function () {
  var orig = window.fetch ? window.fetch.bind(window) : null;
  window.fetch = function (url, opt) {
    var m = typeof url === 'string' && url.match(/assets\\/data\\/([\\w-]+)\\.json(\\?.*)?$/);
    if (m && window.BP_DATA[m[1]]) {
      var body = window.BP_DATA[m[1]];
      return Promise.resolve({ ok: true, status: 200, json: function () { return Promise.resolve(JSON.parse(JSON.stringify(body))); }, text: function () { return Promise.resolve(JSON.stringify(body)); } });
    }
    return orig ? orig(url, opt) : Promise.reject(new Error('fetch unavailable'));
  };
})();
''' % json.dumps(data, ensure_ascii=False, separators=(',', ':'))
open(os.path.join(here, 'assets', 'js', 'data-bundle.js'), 'w', encoding='utf-8').write(js)
print('data-bundle.js:', ', '.join(data), '(%d KB)' % (len(js.encode()) // 1024))
