import { useState, useRef, useEffect } from 'react';

// ── Classic Binary Search tab ─────────────────────────────────────────────────

const DEFAULT_ARRAY = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 89, 95];
const DEFAULT_TARGET = 23;

type Phase = 'idle' | 'found' | 'done';

interface BSState {
  array: number[];
  target: number;
  lo: number;
  hi: number;
  mid: number | null;
  phase: Phase;
  message: string;
}

function initBS(array: number[], target: number): BSState {
  const sorted = [...array].sort((a, b) => a - b);
  return { array: sorted, target, lo: 0, hi: sorted.length - 1, mid: null, phase: 'idle',
    message: `Sorted array ready. Searching for ${target}. Press "Next Step".` };
}

function stepBS(s: BSState): BSState {
  const { array, target, lo, hi } = s;
  if (lo > hi) return { ...s, phase: 'done', mid: null,
    message: `Not found. lo (${lo}) > hi (${hi}). ${target} is not in the array.` };
  const mid = Math.floor((lo + hi) / 2);
  const val = array[mid];
  if (val === target) return { ...s, mid, phase: 'found', message: `Found! arr[${mid}] = ${val} = target ${target} ✓` };
  if (val < target) return { ...s, mid, lo: mid + 1, message: `arr[${mid}]=${val} < ${target} → search right half. New lo = ${mid + 1}` };
  return { ...s, mid, hi: mid - 1, message: `arr[${mid}]=${val} > ${target} → search left half. New hi = ${mid - 1}` };
}

const inputStyle: React.CSSProperties = {
  background: 'var(--surface-raised)', border: '1px solid var(--border)',
  borderRadius: '0.375rem', padding: '0.375rem 0.75rem',
  color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%',
};

function ClassicBSTab() {
  const [arrayInput, setArrayInput] = useState(DEFAULT_ARRAY.join(', '));
  const [targetInput, setTargetInput] = useState(String(DEFAULT_TARGET));
  const [state, setState] = useState<BSState>(() => initBS(DEFAULT_ARRAY, DEFAULT_TARGET));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<BSState[]>([]);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay(); setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setState(initBS(arr.length ? arr : DEFAULT_ARRAY, parseInt(targetInput) || DEFAULT_TARGET));
  }

  function nextStep() {
    if (done) return;
    setHistory(h => [...h, state]);
    setState(stepBS(state));
  }

  function stepBack() {
    if (playing) stopPlay();
    if (history.length === 0) return;
    const prev = [...history]; const s = prev.pop()!;
    setState(s); setHistory(prev);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => {
        if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; }
        setHistory(h => [...h, prev]);
        return stepBS(prev);
      });
    }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const mountedRef = useRef(false);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => {
      setState(prev => {
        if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; }
        setHistory(h => [...h, prev]);
        return stepBS(prev);
      });
    }, 1100 - speed * 200);
  }, [speed]);

  const { array, lo, hi, mid, phase, message } = state;
  const done = phase === 'found' || phase === 'done';

  function cellStyle(i: number): React.CSSProperties {
    const isFound = phase === 'found' && i === mid;
    const isMid = i === mid;
    const inRange = i >= lo && i <= hi;
    if (isFound) return { background: 'color-mix(in srgb, var(--tier-3) 25%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' };
    if (phase === 'done' && !inRange) return { background: 'var(--surface-sunken)', borderColor: 'var(--border-soft)', color: 'var(--text-faint)' };
    if (isMid) return { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' };
    if (inRange) return { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' };
    return { background: 'var(--surface-sunken)', borderColor: 'var(--border-soft)', color: 'var(--text-faint)' };
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ color: 'var(--text-faint)', fontSize: '0.75rem', display: 'block', marginBottom: '0.25rem' }}>Array (will be sorted)</label>
          <input style={inputStyle} value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label style={{ color: 'var(--text-faint)', fontSize: '0.75rem', display: 'block', marginBottom: '0.25rem' }}>Target</label>
          <input style={inputStyle} value={targetInput} onChange={e => setTargetInput(e.target.value)} />
        </div>
      </div>

      <div className="overflow-x-auto pb-6">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLo = i === lo, isHi = i === hi, isMid = i === mid;
            const isFound = phase === 'found' && i === mid;
            return (
              <div key={i} className="flex flex-col items-center">
                <div style={{ ...cellStyle(i), width: '2.75rem', height: '2.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: 'var(--mono)', fontWeight: 700, border: '2px solid', borderRadius: '0.5rem', fontSize: '0.875rem', transition: 'background 0.2s, border-color 0.2s' }}>{val}</div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.7rem', marginTop: '0.25rem', height: '1rem', textAlign: 'center', minWidth: '2.75rem' }}>
                  {isFound ? '✓' : isMid ? 'mid' : isLo && isHi ? 'lo/hi' : isLo ? 'lo' : isHi ? 'hi' : ''}
                </div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.65rem' }}>{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="viz-info" style={phase === 'found' ? { color: 'var(--tier-3)' } : phase === 'done' ? { color: 'var(--bad, #ef4444)' } : {}}>
        {message}
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className="viz-btn viz-btn--primary">{playing ? 'Pause' : '▶ Play'}</button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── BS on Answer — Koko Eating Bananas tab ────────────────────────────────────

const PILES = [3, 6, 7, 11];
const H = 8;
const MAX_K = Math.max(...PILES);

function hoursNeeded(k: number): number {
  return PILES.reduce((sum, p) => sum + Math.ceil(p / k), 0);
}

interface KokoStep {
  lo: number; hi: number; mid: number | null;
  hours: number | null; feasible: boolean | null;
  msg: string; done: boolean;
}

function buildKokoSteps(): KokoStep[] {
  const steps: KokoStep[] = [];
  steps.push({ lo: 1, hi: MAX_K, mid: null, hours: null, feasible: null, done: false,
    msg: `Koko Eating Bananas: piles=[${PILES}], h=${H}. Search k in [1..${MAX_K}]. lo=1, hi=${MAX_K}.` });
  let lo = 1, hi = MAX_K;
  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);
    const hours = hoursNeeded(mid);
    const feasible = hours <= H;
    const breakdown = PILES.map(p => `⌈${p}/${mid}⌉=${Math.ceil(p / mid)}`).join(' + ');
    const msg = `mid=${mid}, hours(${mid}) = ${breakdown} = ${hours}. h=${H}. ${hours}≤${H} → ${feasible ? `hi=${mid} (feasible, try smaller k)` : `lo=${mid + 1} (too slow)`}`;
    if (feasible) hi = mid; else lo = mid + 1;
    steps.push({ lo, hi, mid, hours, feasible, done: lo === hi, msg });
  }
  const last = steps[steps.length - 1];
  if (!last.done) steps.push({ ...last, done: true, msg: `lo = hi = ${lo}. Answer: k = ${lo}.` });
  else steps[steps.length - 1] = { ...last, msg: last.msg + ` → lo=hi=${lo}. Answer: k=${lo}.` };
  return steps;
}

const KOKO_STEPS = buildKokoSteps();

function KokoTab() {
  const [stepIdx, setStepIdx] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setStepIdx(s => { if (s >= KOKO_STEPS.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const mountedRef = useRef(false);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => {
      setStepIdx(s => { if (s >= KOKO_STEPS.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }, [speed]);

  const step = KOKO_STEPS[stepIdx];

  function kCellStyle(k: number): React.CSSProperties {
    const isAnswer = step.done && k === step.lo;
    const isMid = k === step.mid;
    const inRange = k >= step.lo && k <= step.hi;
    if (isAnswer) return { background: 'color-mix(in srgb, var(--tier-3) 25%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' };
    if (isMid) return { background: 'var(--accent-soft)', borderColor: 'var(--accent)', color: 'var(--text)' };
    if (inRange) return { background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' };
    return { background: 'var(--surface-sunken)', borderColor: 'var(--border-soft)', color: 'var(--text-faint)' };
  }

  return (
    <div className="space-y-6">
      <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>
        piles = [{PILES.join(', ')}], h = {H} — Find minimum k so Koko finishes in ≤ h hours.
      </p>

      <div>
        <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.5rem' }}>Search space: k ∈ [1 .. {MAX_K}]</div>
        <div className="overflow-x-auto">
          <div className="flex gap-1 min-w-max">
            {Array.from({ length: MAX_K }, (_, i) => i + 1).map(k => {
              const isLo = k === step.lo, isHi = k === step.hi, isMid = k === step.mid;
              const isAnswer = step.done && k === step.lo;
              return (
                <div key={k} className="flex flex-col items-center">
                  <div style={{ ...kCellStyle(k), width: '2.5rem', height: '2.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: 'var(--mono)', fontWeight: 700, border: '2px solid', borderRadius: '0.5rem', fontSize: '0.875rem', transition: 'background 0.2s, border-color 0.2s' }}>{k}</div>
                  <div style={{ color: 'var(--text-faint)', fontSize: '0.65rem', marginTop: '0.25rem', height: '1rem', textAlign: 'center', minWidth: '2.5rem' }}>
                    {isAnswer ? 'ans' : isMid ? 'mid' : isLo && isHi ? 'lo/hi' : isLo ? 'lo' : isHi ? 'hi' : ''}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {step.mid !== null && (
        <div style={{ background: 'var(--surface-sunken)', border: '1px solid var(--border-soft)', borderRadius: '0.5rem', padding: '0.75rem 1rem' }}>
          <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.5rem' }}>Feasibility check for k = {step.mid}:</div>
          <div className="flex flex-wrap gap-3">
            {PILES.map((p, i) => (
              <span key={i} style={{ fontFamily: 'var(--mono)', fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                ⌈{p}/{step.mid}⌉ = <span style={{ color: 'var(--accent)' }}>{Math.ceil(p / step.mid!)}</span>
              </span>
            ))}
            <span style={{ fontFamily: 'var(--mono)', fontSize: '0.875rem', color: step.feasible ? 'var(--tier-3)' : 'var(--text-dim)' }}>
              → total = {step.hours} hrs {step.feasible ? '≤' : '>'} {H}
            </span>
          </div>
        </div>
      )}

      <div className="viz-info" style={step.done ? { color: 'var(--tier-3)' } : {}}>
        {step.msg}
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStepIdx(s => Math.min(KOKO_STEPS.length - 1, s + 1))} disabled={stepIdx === KOKO_STEPS.length - 1} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={() => { if (playing) stopPlay(); setStepIdx(s => Math.max(0, s - 1)); }} disabled={stepIdx === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={stepIdx === KOKO_STEPS.length - 1} className="viz-btn viz-btn--primary">{playing ? 'Pause' : '▶ Play'}</button>
        <button onClick={() => { stopPlay(); setStepIdx(0); }} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ───────────────────────────────────────────────────────────────────────

type Tab = 'Classic BS' | 'BS on Answer';
const TABS: Tab[] = ['Classic BS', 'BS on Answer'];

export default function BinarySearchViz() {
  const [tab, setTab] = useState<Tab>('Classic BS');
  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Binary Search</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Classic binary search · Binary search on answer space</p>
      </div>
      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`viz-btn ${tab === t ? 'viz-btn--primary' : ''}`}>
            {t}
          </button>
        ))}
      </div>
      {tab === 'Classic BS' ? <ClassicBSTab /> : <KokoTab />}
    </div>
  );
}
