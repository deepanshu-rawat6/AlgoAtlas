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
    stopPlay();
    setHistory([]);
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
    const prev = [...history];
    const s = prev.pop()!;
    setState(s);
    setHistory(prev);
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

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (will be sorted)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label className="block text-xs text-slate-400 mb-1">Target</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={targetInput} onChange={e => setTargetInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button>
        </div>
      </div>

      <div className="overflow-x-auto pb-6">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLo = i === lo, isHi = i === hi, isMid = i === mid;
            const inRange = i >= lo && i <= hi;
            const isFound = phase === 'found' && i === mid;
            let bg = 'bg-slate-700 border-slate-600 text-slate-500';
            if (isFound) bg = 'bg-green-700 border-green-400 text-white';
            else if (phase === 'done' && !inRange) bg = 'bg-slate-800 border-slate-700 text-slate-600';
            else if (isMid) bg = 'bg-yellow-700 border-yellow-400 text-white';
            else if (inRange) bg = 'bg-slate-600 border-slate-500 text-slate-200';
            return (
              <div key={i} className="flex flex-col items-center">
                <div className={`w-11 h-11 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>{val}</div>
                <div className="text-xs mt-1 h-4 text-center leading-none" style={{ minWidth: '2.75rem' }}>
                  {isFound ? <span className="text-green-400">✓</span>
                    : isMid ? <span className="text-yellow-400">mid</span>
                    : isLo && isHi ? <span className="text-slate-400">lo/hi</span>
                    : isLo ? <span className="text-blue-400">lo</span>
                    : isHi ? <span className="text-red-400">hi</span>
                    : null}
                </div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm min-h-12 font-mono ${
        phase === 'found' ? 'bg-green-900/40 text-green-300' :
        phase === 'done' ? 'bg-red-900/40 text-red-300' : 'bg-slate-900/60 text-slate-300'}`}>
        {message}
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset}
          className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">Reset</button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── BS on Answer — Koko Eating Bananas tab ────────────────────────────────────

const PILES = [3, 6, 7, 11];
const H = 8;
const MAX_K = Math.max(...PILES); // 11

function hoursNeeded(k: number): number {
  return PILES.reduce((sum, p) => sum + Math.ceil(p / k), 0);
}

interface KokoStep {
  lo: number;
  hi: number;
  mid: number | null;
  hours: number | null;
  feasible: boolean | null;
  msg: string;
  done: boolean;
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
    const pilesBreakdown = PILES.map(p => `⌈${p}/${mid}⌉=${Math.ceil(p / mid)}`).join(' + ');
    const msg = `mid=${mid}, hours(${mid}) = ${pilesBreakdown} = ${hours}. h=${H}. ${hours}≤${H} → ${feasible ? `hi=${mid} (feasible, try smaller k)` : `lo=${mid + 1} (too slow, need faster k)`}`;
    if (feasible) hi = mid; else lo = mid + 1;
    steps.push({ lo, hi, mid, hours, feasible, done: lo === hi, msg });
  }
  // Final step
  const last = steps[steps.length - 1];
  if (!last.done) {
    steps.push({ ...last, done: true, msg: `lo = hi = ${lo}. Answer: k = ${lo}. Koko eats ${lo} bananas/hour.` });
  } else {
    steps[steps.length - 1] = { ...last, msg: last.msg + ` → lo=hi=${lo}. Answer: k=${lo}.` };
  }

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

  const kokoMountedRef = useRef(false);
  useEffect(() => {
    if (!kokoMountedRef.current) { kokoMountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => {
      setStepIdx(s => { if (s >= KOKO_STEPS.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }, [speed]);

  const step = KOKO_STEPS[stepIdx];

  return (
    <div className="space-y-6">
      <div className="text-sm text-slate-400 space-y-1">
        <div>piles = [{PILES.join(', ')}], h = {H}</div>
        <div>Find minimum k (bananas/hr) such that Koko finishes in ≤ h hours.</div>
      </div>

      {/* Number line 1..11 */}
      <div>
        <div className="text-xs text-slate-400 mb-2">Search space: k ∈ [1 .. {MAX_K}]</div>
        <div className="overflow-x-auto">
          <div className="flex gap-1 min-w-max">
            {Array.from({ length: MAX_K }, (_, i) => i + 1).map(k => {
              const isLo = k === step.lo, isHi = k === step.hi, isMid = k === step.mid;
              const isAnswer = step.done && k === step.lo;
              let bg = 'bg-slate-700 border-slate-600 text-slate-500';
              if (isAnswer) bg = 'bg-green-700 border-green-400 text-white';
              else if (isMid) bg = 'bg-yellow-700 border-yellow-400 text-white';
              else if (k >= step.lo && k <= step.hi) bg = 'bg-slate-600 border-slate-500 text-slate-200';
              return (
                <div key={k} className="flex flex-col items-center">
                  <div className={`w-10 h-10 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>{k}</div>
                  <div className="text-xs mt-1 h-4 text-center leading-none" style={{ minWidth: '2.5rem' }}>
                    {isAnswer ? <span className="text-green-400">ans</span>
                      : isMid ? <span className="text-yellow-400">mid</span>
                      : isLo && isHi ? <span className="text-slate-400">lo/hi</span>
                      : isLo ? <span className="text-blue-400">lo</span>
                      : isHi ? <span className="text-red-400">hi</span>
                      : null}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Feasibility breakdown */}
      {step.mid !== null && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3 space-y-1">
          <div className="text-xs text-slate-400 mb-1">Feasibility check for k = {step.mid}:</div>
          <div className="flex flex-wrap gap-3">
            {PILES.map((p, i) => (
              <span key={i} className="font-mono text-sm text-slate-300">
                ⌈{p}/{step.mid}⌉ = <span className="text-yellow-300">{Math.ceil(p / step.mid!)}</span>
              </span>
            ))}
            <span className="font-mono text-sm">
              → total = <span className={step.feasible ? 'text-green-400' : 'text-red-400'}>{step.hours}</span> hrs
              {step.feasible ? ' ≤' : ' >'} {H}
            </span>
          </div>
        </div>
      )}

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${
        step.done ? 'bg-green-900/40 text-green-300' :
        step.feasible === true ? 'bg-blue-900/40 text-blue-300' :
        step.feasible === false ? 'bg-orange-900/40 text-orange-300' :
        'bg-slate-900/60 text-slate-300'}`}>
        {step.msg}
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStepIdx(s => Math.min(KOKO_STEPS.length - 1, s + 1))} disabled={stepIdx === KOKO_STEPS.length - 1}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={() => { if (playing) stopPlay(); setStepIdx(s => Math.max(0, s - 1)); }} disabled={stepIdx === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={stepIdx === KOKO_STEPS.length - 1}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={() => { stopPlay(); setStepIdx(0); }}
          className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">Reset</button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root component ─────────────────────────────────────────────────────────────

type Tab = 'Classic BS' | 'BS on Answer';
const TABS: Tab[] = ['Classic BS', 'BS on Answer'];

export default function BinarySearchViz() {
  const [tab, setTab] = useState<Tab>('Classic BS');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Binary Search</h3>
        <p className="text-sm text-slate-400">Classic binary search · Binary search on answer space</p>
      </div>

      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-3 py-1.5 text-xs font-medium rounded border transition-colors ${tab === t ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`}>
            {t}
          </button>
        ))}
      </div>

      {tab === 'Classic BS' ? <ClassicBSTab /> : <KokoTab />}
    </div>
  );
}
