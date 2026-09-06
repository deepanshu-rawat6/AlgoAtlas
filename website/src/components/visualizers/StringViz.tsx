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

  const inputStyle = { background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' };
  const labelStyle = { display: 'block' as const, color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' };
  const foundMsgStyle = { background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)', minHeight: '2.5rem' };

  return (
    <div className="panel p-6 space-y-6">
      {/* Tab bar */}
      <div className="flex gap-2">
        <button className={tab === 'kmp' ? 'viz-btn viz-btn--primary' : 'viz-btn'} onClick={() => setTab('kmp')}>KMP</button>
        <button className={tab === 'z' ? 'viz-btn viz-btn--primary' : 'viz-btn'} onClick={() => setTab('z')}>Z-Function</button>
      </div>

      {tab === 'kmp' && (
        <>
          <div>
            <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>KMP Pattern Matching</h3>
            <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>O(n+m) using LPS (failure function) to avoid backtracking</p>
          </div>
          <div className="flex flex-wrap gap-3">
            {([['Text', kText, setKText], ['Pattern', kPattern, setKPattern]] as const).map(([label, val, set]) => (
              <div key={label} className="flex-1 min-w-28">
                <label style={labelStyle}>{label}</label>
                <input style={{ ...inputStyle, fontFamily: 'var(--mono)' }}
                  value={val} onChange={e => set(e.target.value.toUpperCase())} />
              </div>
            ))}
            <div className="flex items-end"><button onClick={startKmp} className="viz-btn viz-btn--primary">Start</button></div>
          </div>

          <div className="flex gap-2 items-center flex-wrap">
            <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem', fontFamily: 'var(--mono)' }}>LPS:</span>
            {kPattern.split('').map((c, i) => (
              <div key={i} className="flex flex-col items-center">
                <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem', fontFamily: 'var(--mono)', width: '1.75rem', textAlign: 'center' }}>{c}</span>
                <span style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', width: '1.75rem', height: '1.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '0.25rem', color: 'var(--accent)', fontFamily: 'var(--mono)', fontSize: '0.75rem' }}>{lps[i]}</span>
              </div>
            ))}
          </div>

          {kStarted && kFrame && (
            <div className="space-y-2">
              <div className="flex gap-1 flex-wrap">
                {kText.split('').map((c, i) => {
                  const isTi = i === kFrame.ti;
                  const isFound = kFrame.found !== null && i >= kFrame.found && i < kFrame.found + kPattern.length;
                  let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' };
                  if (isFound) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' };
                  else if (isTi) cellStyle = kFrame.match
                    ? { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' }
                    : { background: 'color-mix(in srgb, #ef4444 15%, transparent)', borderColor: '#ef4444', color: 'var(--text)' };
                  return (
                    <div key={i} className="flex flex-col items-center">
                      <div style={cellStyle} className="w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm">{c}</div>
                      <span style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{i}</span>
                    </div>
                  );
                })}
              </div>
              <div className="flex gap-1 flex-wrap items-center">
                <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Pattern:</span>
                {kPattern.split('').map((c, i) => {
                  const pStyle = i === kFrame.pi
                    ? { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' }
                    : { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-faint)' };
                  return (
                    <div key={i} style={pStyle} className="w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm">{c}</div>
                  );
                })}
              </div>
            </div>
          )}

          {kFrame && (
            kFrame.found !== null
              ? <div style={foundMsgStyle}>{kFrame.msg}</div>
              : <div className="viz-info">{kFrame.msg}</div>
          )}

          {kStarted && (
            <div className="flex flex-wrap items-center gap-3">
              <button onClick={kNextStep} disabled={kDone} className="viz-btn viz-btn--primary">Next Step</button>
              <button onClick={kStepBack} disabled={kStep === 0} className="viz-btn">← Back</button>
              <button onClick={kTogglePlay} disabled={kDone} className={kPlaying ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
                {kPlaying ? 'Pause' : '▶ Play'}
              </button>
              <div className="flex items-center gap-2">
                <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
                <input type="range" min={1} max={5} value={kSpeed} onChange={e => setKSpeed(Number(e.target.value))}
                  className="speed-slider w-24" />
                <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{kSpeed}x</span>
              </div>
              <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>{kStep + 1}/{kFrames.length}</span>
            </div>
          )}
        </>
      )}

      {tab === 'z' && (
        <>
          <div>
            <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Z-Function Pattern Matching</h3>
            <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Build Z-array on pattern+'#'+text; match where Z[i] == pattern.length</p>
          </div>
          <div className="flex flex-wrap gap-3">
            {([['Text', zText, setZText], ['Pattern', zPattern, setZPattern]] as const).map(([label, val, set]) => (
              <div key={label} className="flex-1 min-w-28">
                <label style={labelStyle}>{label}</label>
                <input style={{ ...inputStyle, fontFamily: 'var(--mono)' }}
                  value={val} onChange={e => set(e.target.value.toUpperCase())} />
              </div>
            ))}
            <div className="flex items-end"><button onClick={startZ} className="viz-btn viz-btn--primary">Start</button></div>
          </div>

          {/* Combined string + Z-array */}
          {zStarted && zFrame && (
            <div className="space-y-3">
              <p style={{ color: 'var(--text-faint)', fontSize: '0.75rem', fontFamily: 'var(--mono)' }}>Combined: <span style={{ color: 'var(--text)' }}>{combined}</span></p>
              <div className="flex gap-1 flex-wrap">
                {combined.split('').map((c, i) => {
                  const isCurr = i === zFrame.i;
                  const inMatchExtent = i >= zFrame.i && i < zFrame.matchEnd;
                  const inZBox = zFrame.l > 0 && i >= zFrame.l && i < zFrame.r;
                  let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' };
                  if (isCurr) cellStyle = { background: 'color-mix(in srgb, #eab308 20%, transparent)', borderColor: '#eab308', color: 'var(--text)' };
                  else if (inMatchExtent) cellStyle = { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' };
                  else if (inZBox) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' };
                  return (
                    <div key={i} className="flex flex-col items-center">
                      <div style={cellStyle} className="w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm">{c}</div>
                      <span style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{i}</span>
                    </div>
                  );
                })}
              </div>
              {/* Z-array values */}
              <div className="flex gap-2 items-center flex-wrap">
                <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem', fontFamily: 'var(--mono)' }}>Z:</span>
                {zFrame.z.slice(1).map((v, i) => {
                  const realI = i + 1;
                  const isMatch = v === zPattern.length;
                  const zValStyle = realI === zFrame.i
                    ? { background: 'color-mix(in srgb, #eab308 20%, transparent)', borderColor: '#eab308', color: 'var(--text)' }
                    : isMatch
                    ? { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' }
                    : { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--accent)' };
                  return (
                    <div key={realI} className="flex flex-col items-center">
                      <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem', fontFamily: 'var(--mono)', width: '1.75rem', textAlign: 'center' }}>{realI}</span>
                      <span style={{ ...zValStyle, width: '1.75rem', height: '1.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: '0.25rem', border: '1px solid', fontFamily: 'var(--mono)', fontSize: '0.75rem' }}>{v}</span>
                    </div>
                  );
                })}
              </div>
              <p style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Z-box: <span style={{ color: 'var(--tier-3)', fontFamily: 'var(--mono)' }}>[{zFrame.l}, {zFrame.r})</span></p>
            </div>
          )}

          {zFrame && (
            zFrame.msg.startsWith('✓')
              ? <div style={foundMsgStyle}>{zFrame.msg}</div>
              : <div className="viz-info">{zFrame.msg}</div>
          )}

          {zStarted && (
            <div className="flex flex-wrap items-center gap-3">
              <button onClick={zNextStep} disabled={zDone} className="viz-btn viz-btn--primary">Next Step</button>
              <button onClick={zStepBack} disabled={zStep === 0} className="viz-btn">← Back</button>
              <button onClick={zTogglePlay} disabled={zDone} className={zPlaying ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
                {zPlaying ? 'Pause' : '▶ Play'}
              </button>
              <div className="flex items-center gap-2">
                <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
                <input type="range" min={1} max={5} value={zSpeed} onChange={e => setZSpeed(Number(e.target.value))}
                  className="speed-slider w-24" />
                <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{zSpeed}x</span>
              </div>
              <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>{zStep + 1}/{zFrames.length}</span>
            </div>
          )}
        </>
      )}
    </div>
  );
}
