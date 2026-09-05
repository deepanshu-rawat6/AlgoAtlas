import { useState, useRef, useEffect } from 'react';

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
  const kTimerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [kPlaying, setKPlaying] = useState(false);
  const [kSpeed, setKSpeed] = useState(3);
  const kMountedRef = useRef(false);
  const kNextRef = useRef(() => {});

  // Z state
  const [zText, setZText] = useState('AABAABAAA');
  const [zPattern, setZPattern] = useState('AABA');
  const [zFrames, setZFrames] = useState<ZFrame[]>([]);
  const [zStep, setZStep] = useState(0);
  const [zStarted, setZStarted] = useState(false);
  const zTimerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [zPlaying, setZPlaying] = useState(false);
  const [zSpeed, setZSpeed] = useState(3);
  const zMountedRef = useRef(false);
  const zNextRef = useRef(() => {});

  function kStopPlay() {
    if (kTimerRef.current) { clearInterval(kTimerRef.current); kTimerRef.current = null; }
    setKPlaying(false);
  }
  function zStopPlay() {
    if (zTimerRef.current) { clearInterval(zTimerRef.current); zTimerRef.current = null; }
    setZPlaying(false);
  }

  function startKmp() { kStopPlay(); setKFrames(buildFrames(kText, kPattern)); setKStep(0); setKStarted(true); }
  function startZ() { zStopPlay(); setZFrames(buildZFrames(zText, zPattern)); setZStep(0); setZStarted(true); }

  function kNextStep() {
    if (kStep >= kFrames.length - 1) { kStopPlay(); return; }
    setKStep(s => s + 1);
  }
  function kStepBack() { if (kPlaying) kStopPlay(); setKStep(s => Math.max(0, s - 1)); }
  function kTogglePlay() {
    if (kPlaying) { kStopPlay(); return; }
    setKPlaying(true);
    kTimerRef.current = setInterval(() => { kNextRef.current(); }, 1100 - kSpeed * 200);
  }

  function zNextStep() {
    if (zStep >= zFrames.length - 1) { zStopPlay(); return; }
    setZStep(s => s + 1);
  }
  function zStepBack() { if (zPlaying) zStopPlay(); setZStep(s => Math.max(0, s - 1)); }
  function zTogglePlay() {
    if (zPlaying) { zStopPlay(); return; }
    setZPlaying(true);
    zTimerRef.current = setInterval(() => { zNextRef.current(); }, 1100 - zSpeed * 200);
  }

  useEffect(() => { kNextRef.current = kNextStep; });
  useEffect(() => { zNextRef.current = zNextStep; });

  useEffect(() => () => {
    if (kTimerRef.current) clearInterval(kTimerRef.current);
    if (zTimerRef.current) clearInterval(zTimerRef.current);
  }, []);

  // Stop play on tab switch
  useEffect(() => { kStopPlay(); zStopPlay(); }, [tab]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (!kMountedRef.current) { kMountedRef.current = true; return; }
    if (!kPlaying) return;
    kStopPlay();
    setKPlaying(true);
    kTimerRef.current = setInterval(() => { kNextRef.current(); }, 1100 - kSpeed * 200);
  }, [kSpeed]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (!zMountedRef.current) { zMountedRef.current = true; return; }
    if (!zPlaying) return;
    zStopPlay();
    setZPlaying(true);
    zTimerRef.current = setInterval(() => { zNextRef.current(); }, 1100 - zSpeed * 200);
  }, [zSpeed]); // eslint-disable-line react-hooks/exhaustive-deps

  const kFrame = kFrames[kStep];
  const lps = buildLPS(kPattern);
  const kDone = kStarted && kStep >= kFrames.length - 1;

  const zFrame = zFrames[zStep];
  const combined = zPattern + '#' + zText;
  const zDone = zStarted && zStep >= zFrames.length - 1;

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
            <div className="flex flex-wrap items-center gap-3">
              <button onClick={kNextStep} disabled={kDone}
                className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
                Next Step
              </button>
              <button onClick={kStepBack} disabled={kStep === 0}
                className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
                ← Back
              </button>
              <button onClick={kTogglePlay} disabled={kDone}
                className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
                {kPlaying ? 'Pause' : '▶ Play'}
              </button>
              <div className="flex items-center gap-2">
                <span className="text-xs text-slate-500">Speed</span>
                <input type="range" min={1} max={5} value={kSpeed} onChange={e => setKSpeed(Number(e.target.value))}
                  className="w-24" />
                <span className="text-xs text-slate-400">{kSpeed}x</span>
              </div>
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
            <div className="flex flex-wrap items-center gap-3">
              <button onClick={zNextStep} disabled={zDone}
                className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
                Next Step
              </button>
              <button onClick={zStepBack} disabled={zStep === 0}
                className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
                ← Back
              </button>
              <button onClick={zTogglePlay} disabled={zDone}
                className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
                {zPlaying ? 'Pause' : '▶ Play'}
              </button>
              <div className="flex items-center gap-2">
                <span className="text-xs text-slate-500">Speed</span>
                <input type="range" min={1} max={5} value={zSpeed} onChange={e => setZSpeed(Number(e.target.value))}
                  className="w-24" />
                <span className="text-xs text-slate-400">{zSpeed}x</span>
              </div>
              <span className="text-xs text-slate-500 self-center">{zStep + 1}/{zFrames.length}</span>
            </div>
          )}
        </>
      )}
    </div>
  );
}
