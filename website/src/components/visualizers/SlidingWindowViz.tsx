import { useState, useRef, useEffect } from 'react';

// ── Min Subarray Sum tab ─────────────────────────────────────────────────────
const MSS_DEFAULT = [2, 1, 5, 1, 3, 2];
const MSS_TARGET = 7;

type MSSPhase = 'idle' | 'running' | 'found' | 'done';
interface MSSState {
  array: number[]; target: number;
  left: number; right: number; sum: number;
  minLen: number; minLeft: number; minRight: number;
  phase: MSSPhase; message: string;
}

function mssInit(array: number[], target: number): MSSState {
  return { array, target, left: 0, right: -1, sum: 0, minLen: Infinity, minLeft: -1, minRight: -1, phase: 'idle',
    message: 'Press "Next Step" to start. Finding minimum subarray with sum ≥ target.' };
}

function mssStep(s: MSSState): MSSState {
  const { array, target, left, right, sum, minLen, minLeft, minRight } = s;
  const n = array.length;
  if (right + 1 < n && sum < target) {
    const nr = right + 1;
    const ns = sum + array[nr];
    return { ...s, right: nr, sum: ns, message: `Expand right → include arr[${nr}]=${array[nr]}, window sum = ${ns}` };
  }
  if (sum >= target) {
    const len = right - left + 1;
    const newMin = len < minLen;
    return { ...s, minLen: newMin ? len : minLen, minLeft: newMin ? left : minLeft, minRight: newMin ? right : minRight,
      sum: sum - array[left], left: left + 1,
      message: `Window sum ${sum} ≥ ${target}! Window [${left}..${right}] len=${len}${newMin ? ' ← new minimum' : ''}. Shrink left.` };
  }
  return { ...s, phase: 'done', message: minLen === Infinity ? 'No valid subarray found.'
    : `Done! Minimum subarray: indices [${minLeft}..${minRight}], length ${minLen}.` };
}

function MinSubarrayTab() {
  const [arrayInput, setArrayInput] = useState(MSS_DEFAULT.join(', '));
  const [targetInput, setTargetInput] = useState(String(MSS_TARGET));
  const [state, setState] = useState<MSSState>(() => mssInit(MSS_DEFAULT, MSS_TARGET));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<MSSState[]>([]);
  const mountedMSSRef = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || MSS_TARGET;
    setState(mssInit(arr.length ? arr : MSS_DEFAULT, tgt));
  }

  function nextStep() {
    setState(prev => {
      if (prev.phase === 'done') return prev;
      setHistory(h => [...h, prev]);
      return mssStep(prev);
    });
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'done') { stopPlay(); return prev; } return mssStep(prev); });
    }, 1100 - speed * 200);
  }

  useEffect(() => {
    if (!mountedMSSRef.current) { mountedMSSRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'done') { stopPlay(); return prev; } return mssStep(prev); });
    }, 1100 - speed * 200);
  }, [speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, minLeft, minRight, phase, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Array (comma-separated)</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Target</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={targetInput} onChange={e => setTargetInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const inWindow = i >= left && i <= right;
            const isMin = phase === 'done' && i >= minLeft && i <= minRight;
            let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)' };
            if (isMin) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)' };
            else if (inWindow) cellStyle = { background: 'var(--accent-soft)', borderColor: 'var(--accent)' };
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div style={cellStyle} className="w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg" >
                  <span style={{ color: 'var(--text)' }}>{val}</span>
                </div>
                <div style={{ color: 'var(--text-dim)', fontSize: '0.75rem', height: '1rem' }}>{i === left && i === right ? 'L R' : i === left ? 'L' : i === right ? 'R' : ''}</div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      {phase === 'done'
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)', minHeight: '3rem' }}>{message}</div>
        : <div className="viz-info">{message}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={phase === 'done'} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={phase === 'done'} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Longest No Repeat tab ────────────────────────────────────────────────────
const LNR_DEFAULT = 'abcabcbb';

interface LNRState {
  s: string; left: number; right: number;
  windowSet: Set<string>; maxLen: number; maxLeft: number;
  done: boolean; message: string;
}

function lnrInit(s: string): LNRState {
  return { s, left: 0, right: -1, windowSet: new Set(), maxLen: 0, maxLeft: 0, done: false,
    message: 'Press "Next Step" to start. Finding longest substring without repeating characters.' };
}

function lnrStep(st: LNRState): LNRState {
  const { s, left, right, windowSet, maxLen, maxLeft } = st;

  // Try expanding right
  const nr = right + 1;
  if (nr >= s.length) {
    return { ...st, done: true, message: `Done! Longest substring has length ${maxLen}, starting at index ${maxLeft}.` };
  }

  const ch = s[nr];
  if (!windowSet.has(ch)) {
    // expand
    const newSet = new Set(windowSet);
    newSet.add(ch);
    const len = nr - left + 1;
    const newMax = len > maxLen;
    return { ...st, right: nr, windowSet: newSet,
      maxLen: newMax ? len : maxLen, maxLeft: newMax ? left : maxLeft,
      message: `right='${ch}', window={${[...newSet].join(',')}}, len=${len}${newMax ? ' ← new max!' : ''}` };
  } else {
    // shrink: remove left char
    const newSet = new Set(windowSet);
    const removedChar = s[left];
    newSet.delete(removedChar);
    return { ...st, left: left + 1, windowSet: newSet,
      message: `right='${ch}' duplicate! shrink left: remove '${removedChar}', left=${left + 1}` };
  }
}

function LongestNoRepeatTab() {
  const [strInput, setStrInput] = useState(LNR_DEFAULT);
  const [state, setState] = useState<LNRState>(() => lnrInit(LNR_DEFAULT));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<LNRState[]>([]);
  const mountedLNRRef = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setHistory([]);
    setState(lnrInit(strInput || LNR_DEFAULT));
  }

  function nextStep() {
    setState(prev => {
      if (prev.done) return prev;
      setHistory(h => [...h, prev]);
      return lnrStep(prev);
    });
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return lnrStep(prev); });
    }, 1100 - speed * 200);
  }

  useEffect(() => {
    if (!mountedLNRRef.current) { mountedLNRRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return lnrStep(prev); });
    }, 1100 - speed * 200);
  }, [speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { s, left, right, windowSet, maxLen, done, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>String</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={strInput} onChange={e => setStrInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {s.split('').map((ch, i) => {
            const isRight = i === right + 1; // next to expand (yellow)
            const inWindow = i >= left && i <= right;
            let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' };
            if (isRight && !done) cellStyle = { background: 'color-mix(in srgb, #eab308 20%, transparent)', borderColor: '#eab308', color: 'var(--text)' };
            else if (inWindow) cellStyle = { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' };
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div style={cellStyle} className="w-10 h-10 flex items-center justify-center font-mono font-bold border-2 rounded-lg">{ch}</div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="viz-info space-y-2">
        <div style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>Window set: <span style={{ fontFamily: 'var(--mono)', color: 'var(--accent)' }}>{'{'}  {[...windowSet].join(', ')}  {'}'}</span></div>
        <div style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>Max length so far: <span style={{ fontFamily: 'var(--mono)', color: 'var(--tier-3)', fontWeight: 700 }}>{maxLen}</span></div>
      </div>

      {done
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>{message}</div>
        : <div className="viz-info">{message}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────
export default function SlidingWindowViz() {
  const [tab, setTab] = useState<'min' | 'norepeat'>('min');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Sliding Window</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Avoid nested loops by maintaining a dynamic window</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('min')} className={tab === 'min' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Min Subarray Sum</button>
        <button onClick={() => setTab('norepeat')} className={tab === 'norepeat' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Longest No Repeat</button>
      </div>

      {tab === 'min' ? <MinSubarrayTab /> : <LongestNoRepeatTab />}
    </div>
  );
}
