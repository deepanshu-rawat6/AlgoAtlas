import { useState, useRef, useEffect } from 'react';

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

// ── Two Sum II tab ───────────────────────────────────────────────────────────
const TS2_DEFAULT = [1, 2, 4, 6, 8, 9, 14, 15];
const TS2_TARGET = 13;

type TS2Phase = 'idle' | 'found' | 'done';
interface TS2State {
  array: number[]; target: number;
  left: number; right: number; phase: TS2Phase;
  foundLeft: number; foundRight: number; message: string;
}

function ts2Init(array: number[], target: number): TS2State {
  const sorted = [...array].sort((a, b) => a - b);
  return { array: sorted, target, left: 0, right: sorted.length - 1, phase: 'idle', foundLeft: -1, foundRight: -1,
    message: `Array sorted. Find two numbers summing to ${target}. Press "Next Step".` };
}

function ts2Step(s: TS2State): TS2State {
  const { array, target, left, right } = s;
  if (left >= right) return { ...s, phase: 'done', message: `No pair found that sums to ${target}.` };
  const sum = array[left] + array[right];
  if (sum === target) return { ...s, phase: 'found', foundLeft: left, foundRight: right,
    message: `Found! arr[${left}]=${array[left]} + arr[${right}]=${array[right]} = ${sum} ✓` };
  if (sum < target) return { ...s, left: left + 1,
    message: `Sum ${sum} < ${target} → move left pointer right (need larger values)` };
  return { ...s, right: right - 1,
    message: `Sum ${sum} > ${target} → move right pointer left (need smaller values)` };
}

function TwoSumIITab() {
  const [arrayInput, setArrayInput] = useState(TS2_DEFAULT.join(', '));
  const [targetInput, setTargetInput] = useState(String(TS2_TARGET));
  const [state, setState] = useState<TS2State>(() => ts2Init(TS2_DEFAULT, TS2_TARGET));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<TS2State[]>([]);
  const mountedTS2Ref = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }
  function reset() {
    stopPlay();
    setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || TS2_TARGET;
    setState(ts2Init(arr.length ? arr : TS2_DEFAULT, tgt));
  }
  function nextStep() {
    setState(prev => {
      if (prev.phase === 'found' || prev.phase === 'done') return prev;
      setHistory(h => [...h, prev]);
      return ts2Step(prev);
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
      setState(prev => { if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; } return ts2Step(prev); });
    }, 1100 - speed * 200);
  }
  useEffect(() => {
    if (!mountedTS2Ref.current) { mountedTS2Ref.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; } return ts2Step(prev); });
    }, 1100 - speed * 200);
  }, [speed]);
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, phase, foundLeft, foundRight, message } = state;
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
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLeft = i === left, isRight = i === right;
            const isFound = phase === 'found' && (i === foundLeft || i === foundRight);
            let bg = 'bg-slate-700 border-slate-600';
            if (isFound) bg = 'bg-green-800 border-green-400';
            else if (isLeft) bg = 'bg-emerald-800 border-emerald-400';
            else if (isRight) bg = 'bg-red-800 border-red-400';
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg ${bg} text-slate-100`}>{val}</div>
                <div className="text-xs h-4" style={{ color: isLeft ? '#4ade80' : isRight ? '#f87171' : 'transparent' }}>
                  {isLeft ? 'L' : isRight ? 'R' : '.'}
                </div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm min-h-12 font-mono ${phase === 'found' ? 'bg-green-900/40 text-green-300' : phase === 'done' ? 'bg-red-900/40 text-red-300' : 'bg-slate-900/60 text-slate-300'}`}>{message}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── 3Sum tab ─────────────────────────────────────────────────────────────────
const TS3_DEFAULT = [-1, 0, 1, 2, -1, -4];

interface TS3State {
  array: number[];        // sorted
  i: number;              // outer pointer
  left: number;
  right: number;
  triplets: [number, number, number][];
  done: boolean;
  message: string;
}

function ts3Init(raw: number[]): TS3State {
  const array = [...raw].sort((a, b) => a - b);
  return { array, i: 0, left: 1, right: array.length - 1, triplets: [], done: array.length < 3,
    message: `Sorted: [${array.join(', ')}]. Fix i=0 (val=${array[0]}), L=1, R=${array.length - 1}. Press "Next Step".` };
}

function ts3Step(s: TS3State): TS3State {
  const { array, triplets } = s;
  const n = array.length;
  let { i, left, right } = s;

  // Skip duplicate i
  if (i > 0 && array[i] === array[i - 1]) {
    i++;
    if (i >= n - 2) return { ...s, done: true, message: `Done! Found ${triplets.length} triplet(s).` };
    left = i + 1; right = n - 1;
    return { ...s, i, left, right, message: `Skip duplicate i=${i} (val=${array[i]}). L=${left}, R=${right}.` };
  }

  if (left >= right) {
    // advance i
    const ni = i + 1;
    if (ni >= n - 2) return { ...s, done: true, message: `Done! Found ${triplets.length} triplet(s).` };
    // skip duplicate ni
    let nii = ni;
    while (nii < n - 2 && array[nii] === array[nii - 1] && nii > 0) nii++;
    return { ...s, i: nii, left: nii + 1, right: n - 1,
      message: `L≥R, advance i → Fix i=${nii} (val=${array[nii]}), L=${nii + 1}, R=${n - 1}.` };
  }

  const sum = array[i] + array[left] + array[right];

  if (sum === 0) {
    const triplet: [number, number, number] = [array[i], array[left], array[right]];
    const newTriplets = [...triplets, triplet];
    // skip duplicates at left and right
    let nl = left + 1, nr = right - 1;
    while (nl < nr && array[nl] === array[nl - 1]) nl++;
    while (nl < nr && array[nr] === array[nr + 1]) nr--;
    return { ...s, triplets: newTriplets, left: nl, right: nr,
      message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${array[i]}+(${array[left]})+(${array[right]})=0 → triplet found! [${triplet.join(',')}]` };
  }

  if (sum < 0) {
    return { ...s, left: left + 1, message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${sum}<0 → move L right.` };
  }

  return { ...s, right: right - 1, message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${sum}>0 → move R left.` };
}

function ThreeSumTab() {
  const [arrayInput, setArrayInput] = useState(TS3_DEFAULT.join(', '));
  const [state, setState] = useState<TS3State>(() => ts3Init(TS3_DEFAULT));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<TS3State[]>([]);
  const mountedTS3Ref = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setState(ts3Init(arr.length >= 3 ? arr : TS3_DEFAULT));
  }

  function nextStep() {
    setState(prev => {
      if (prev.done) return prev;
      setHistory(h => [...h, prev]);
      return ts3Step(prev);
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
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return ts3Step(prev); });
    }, 1100 - speed * 200);
  }

  useEffect(() => {
    if (!mountedTS3Ref.current) { mountedTS3Ref.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return ts3Step(prev); });
    }, 1100 - speed * 200);
  }, [speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, i, left, right, triplets, done, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (will be sorted)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, idx) => {
            const isI = idx === i;
            const isLeft = idx === left;
            const isRight = idx === right;
            let bg = 'bg-slate-700 border-slate-600';
            if (isI) bg = 'bg-orange-800 border-orange-400';
            else if (isLeft) bg = 'bg-green-800 border-green-400';
            else if (isRight) bg = 'bg-red-800 border-red-400';
            const label = isI ? 'i' : isLeft ? 'L' : isRight ? 'R' : '';
            const labelColor = isI ? '#fb923c' : isLeft ? '#4ade80' : '#f87171';
            return (
              <div key={idx} className="flex flex-col items-center gap-1">
                <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg ${bg} text-slate-100`}>{val}</div>
                <div className="text-xs h-4 font-medium" style={{ color: label ? labelColor : 'transparent' }}>{label || '.'}</div>
                <div className="text-xs text-slate-600">{idx}</div>
              </div>
            );
          })}
        </div>
      </div>

      {triplets.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {triplets.map((t, idx) => (
            <span key={idx} className="text-xs font-mono bg-green-900/40 border border-green-700 px-2 py-1 rounded text-green-300">
              [{t.join(', ')}]
            </span>
          ))}
        </div>
      )}

      <div className={`rounded-lg px-4 py-3 text-sm min-h-12 font-mono ${done ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{message}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────
export default function TwoPointersViz() {
  const [tab, setTab] = useState<'twosum2' | 'threesum'>('twosum2');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Two Pointers</h3>
        <p className="text-sm text-slate-400">Two boundaries that move toward each other on sorted input</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('twosum2')} className={`${TAB_BTN} ${tab === 'twosum2' ? ACTIVE : INACTIVE}`}>Two Sum II</button>
        <button onClick={() => setTab('threesum')} className={`${TAB_BTN} ${tab === 'threesum' ? ACTIVE : INACTIVE}`}>3Sum</button>
      </div>

      {tab === 'twosum2' ? <TwoSumIITab /> : <ThreeSumTab />}
    </div>
  );
}
