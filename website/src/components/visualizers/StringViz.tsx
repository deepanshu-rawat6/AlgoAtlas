import { useState } from 'react';

function buildLPS(pattern: string): number[] {
  const lps = Array(pattern.length).fill(0);
  let len = 0, i = 1;
  while (i < pattern.length) {
    if (pattern[i] === pattern[len]) { lps[i++] = ++len; }
    else if (len) { len = lps[len - 1]; }
    else { lps[i++] = 0; }
  }
  return lps;
}

interface Frame { ti: number; pi: number; match: boolean; found: number | null; msg: string; }

function buildFrames(text: string, pattern: string): Frame[] {
  const frames: Frame[] = [];
  const lps = buildLPS(pattern);
  let ti = 0, pi = 0;
  while (ti < text.length) {
    if (text[ti] === pattern[pi]) {
      frames.push({ ti, pi, match: true, found: null, msg: `Match: text[${ti}]='${text[ti]}' == pattern[${pi}]` });
      ti++; pi++;
      if (pi === pattern.length) {
        frames.push({ ti: ti - 1, pi: pi - 1, match: true, found: ti - pi, msg: `✓ Pattern found at index ${ti - pi}!` });
        pi = lps[pi - 1];
      }
    } else {
      frames.push({ ti, pi, match: false, found: null, msg: `Mismatch: text[${ti}]='${text[ti]}' ≠ pattern[${pi}]${pi > 0 ? ` → use LPS, pi=${lps[pi-1]}` : ', advance ti'}` });
      if (pi) pi = lps[pi - 1]; else ti++;
    }
  }
  frames.push({ ti, pi, match: false, found: null, msg: pi === 0 ? 'Search complete.' : 'Pattern not found.' });
  return frames;
}

// Z-Function
interface ZFrame { i: number; z: number[]; l: number; r: number; matchEnd: number; msg: string; }

function buildZFrames(text: string, pattern: string): ZFrame[] {
  const s = pattern + '#' + text;
  const n = s.length;
  const z = Array(n).fill(0);
  z[0] = n;
  const frames: ZFrame[] = [];
  let l = 0, r = 0;
  for (let i = 1; i < n; i++) {
    if (i < r) z[i] = Math.min(r - i, z[i - l]);
    while (i + z[i] < n && s[z[i]] === s[i + z[i]]) z[i]++;
    if (i + z[i] > r) { l = i; r = i + z[i]; }
    const pLen = pattern.length;
    const found = z[i] === pLen ? i - pLen - 1 : -1;
    const zSnap = [...z];
    frames.push({
      i, z: zSnap, l, r,
      matchEnd: i + z[i],
      msg: found >= 0
        ? `✓ Z[${i}]=${z[i]} == pattern.length → match at text index ${found}`
        : `Z[${i}]=${z[i]}${z[i] > 0 ? ` (matches first ${z[i]} chars of combined string)` : ''}`,
    });
  }
  frames.push({ i: n, z: [...z], l, r, matchEnd: 0, msg: 'Z-array complete.' });
  return frames;
}

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

export default function StringViz() {
  const [tab, setTab] = useState<'kmp' | 'z'>('kmp');

  // KMP state
  const [kText, setKText] = useState('AABAABAAA');
  const [kPattern, setKPattern] = useState('AABA');
  const [kFrames, setKFrames] = useState<Frame[]>([]);
  const [kStep, setKStep] = useState(0);
  const [kStarted, setKStarted] = useState(false);

  // Z state
  const [zText, setZText] = useState('AABAABAAA');
  const [zPattern, setZPattern] = useState('AABA');
  const [zFrames, setZFrames] = useState<ZFrame[]>([]);
  const [zStep, setZStep] = useState(0);
  const [zStarted, setZStarted] = useState(false);

  function startKmp() { setKFrames(buildFrames(kText, kPattern)); setKStep(0); setKStarted(true); }
  function startZ() { setZFrames(buildZFrames(zText, zPattern)); setZStep(0); setZStarted(true); }

  const kFrame = kFrames[kStep];
  const lps = buildLPS(kPattern);

  const zFrame = zFrames[zStep];
  const combined = zPattern + '#' + zText;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      {/* Tab bar */}
      <div className="flex gap-2">
        <button className={TAB_BTN(tab === 'kmp')} onClick={() => setTab('kmp')}>KMP</button>
        <button className={TAB_BTN(tab === 'z')} onClick={() => setTab('z')}>Z-Function</button>
      </div>

      {tab === 'kmp' && (
        <>
          <div>
            <h3 className="text-lg font-semibold text-slate-100 mb-1">KMP Pattern Matching</h3>
            <p className="text-sm text-slate-400">O(n+m) using LPS (failure function) to avoid backtracking</p>
          </div>
          <div className="flex flex-wrap gap-3">
            {([['Text', kText, setKText], ['Pattern', kPattern, setKPattern]] as const).map(([label, val, set]) => (
              <div key={label} className="flex-1 min-w-28">
                <label className="block text-xs text-slate-400 mb-1">{label}</label>
                <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 font-mono"
                  value={val} onChange={e => set(e.target.value.toUpperCase())} />
              </div>
            ))}
            <div className="flex items-end"><button onClick={startKmp} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button></div>
          </div>

          <div className="flex gap-2 items-center flex-wrap">
            <span className="text-xs text-slate-500 font-mono">LPS:</span>
            {kPattern.split('').map((c, i) => (
              <div key={i} className="flex flex-col items-center">
                <span className="text-xs font-mono text-slate-400 w-7 text-center">{c}</span>
                <span className="text-xs font-mono bg-slate-700 border border-slate-600 w-7 h-7 flex items-center justify-center rounded text-blue-300">{lps[i]}</span>
              </div>
            ))}
          </div>

          {kStarted && kFrame && (
            <div className="space-y-2">
              <div className="flex gap-1 flex-wrap">
                {kText.split('').map((c, i) => {
                  const isTi = i === kFrame.ti;
                  const isFound = kFrame.found !== null && i >= kFrame.found && i < kFrame.found + kPattern.length;
                  let bg = 'bg-slate-700 border-slate-600 text-slate-300';
                  if (isFound) bg = 'bg-green-800 border-green-400 text-white';
                  else if (isTi) bg = `${kFrame.match ? 'bg-blue-800 border-blue-400' : 'bg-red-800 border-red-400'} text-white`;
                  return (
                    <div key={i} className="flex flex-col items-center">
                      <div className={`w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm ${bg}`}>{c}</div>
                      <span className="text-xs text-slate-600">{i}</span>
                    </div>
                  );
                })}
              </div>
              <div className="flex gap-1 flex-wrap items-center">
                <span className="text-xs text-slate-500">Pattern:</span>
                {kPattern.split('').map((c, i) => (
                  <div key={i} className={`w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm ${i === kFrame.pi ? 'bg-purple-800 border-purple-400 text-white' : 'bg-slate-700 border-slate-600 text-slate-400'}`}>{c}</div>
                ))}
              </div>
            </div>
          )}

          {kFrame && <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${kFrame.found !== null ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{kFrame.msg}</div>}

          {kStarted && (
            <div className="flex gap-3">
              <button onClick={() => setKStep(s => Math.max(0, s - 1))} disabled={kStep === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
              <button onClick={() => setKStep(s => Math.min(kFrames.length - 1, s + 1))} disabled={kStep >= kFrames.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
              <span className="text-xs text-slate-500 self-center">{kStep + 1}/{kFrames.length}</span>
            </div>
          )}
        </>
      )}

      {tab === 'z' && (
        <>
          <div>
            <h3 className="text-lg font-semibold text-slate-100 mb-1">Z-Function Pattern Matching</h3>
            <p className="text-sm text-slate-400">Build Z-array on pattern+'#'+text; match where Z[i] == pattern.length</p>
          </div>
          <div className="flex flex-wrap gap-3">
            {([['Text', zText, setZText], ['Pattern', zPattern, setZPattern]] as const).map(([label, val, set]) => (
              <div key={label} className="flex-1 min-w-28">
                <label className="block text-xs text-slate-400 mb-1">{label}</label>
                <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 font-mono"
                  value={val} onChange={e => set(e.target.value.toUpperCase())} />
              </div>
            ))}
            <div className="flex items-end"><button onClick={startZ} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button></div>
          </div>

          {/* Combined string + Z-array */}
          {zStarted && zFrame && (
            <div className="space-y-3">
              <p className="text-xs text-slate-500 font-mono">Combined: <span className="text-slate-300">{combined}</span></p>
              <div className="flex gap-1 flex-wrap">
                {combined.split('').map((c, i) => {
                  const isCurr = i === zFrame.i;
                  const inMatchExtent = i >= zFrame.i && i < zFrame.matchEnd;
                  const inZBox = zFrame.l > 0 && i >= zFrame.l && i < zFrame.r;
                  let bg = 'bg-slate-700 border-slate-600 text-slate-300';
                  if (isCurr) bg = 'bg-yellow-800 border-yellow-400 text-white';
                  else if (inMatchExtent) bg = 'bg-blue-800 border-blue-500 text-white';
                  else if (inZBox) bg = 'bg-green-900 border-green-600 text-green-200';
                  return (
                    <div key={i} className="flex flex-col items-center">
                      <div className={`w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm ${bg}`}>{c}</div>
                      <span className="text-xs text-slate-600">{i}</span>
                    </div>
                  );
                })}
              </div>
              {/* Z-array values */}
              <div className="flex gap-2 items-center flex-wrap">
                <span className="text-xs text-slate-500 font-mono">Z:</span>
                {zFrame.z.slice(1).map((v, i) => {
                  const realI = i + 1;
                  const isMatch = v === zPattern.length;
                  return (
                    <div key={realI} className="flex flex-col items-center">
                      <span className="text-xs font-mono text-slate-500 w-7 text-center">{realI}</span>
                      <span className={`text-xs font-mono w-7 h-7 flex items-center justify-center rounded border ${realI === zFrame.i ? 'bg-yellow-800 border-yellow-400 text-white' : isMatch ? 'bg-green-800 border-green-400 text-green-200' : 'bg-slate-700 border-slate-600 text-blue-300'}`}>{v}</span>
                    </div>
                  );
                })}
              </div>
              <p className="text-xs text-slate-500">Z-box: <span className="text-green-400 font-mono">[{zFrame.l}, {zFrame.r})</span></p>
            </div>
          )}

          {zFrame && <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${zFrame.msg.startsWith('✓') ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{zFrame.msg}</div>}

          {zStarted && (
            <div className="flex gap-3">
              <button onClick={() => setZStep(s => Math.max(0, s - 1))} disabled={zStep === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
              <button onClick={() => setZStep(s => Math.min(zFrames.length - 1, s + 1))} disabled={zStep >= zFrames.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
              <span className="text-xs text-slate-500 self-center">{zStep + 1}/{zFrames.length}</span>
            </div>
          )}
        </>
      )}
    </div>
  );
}
