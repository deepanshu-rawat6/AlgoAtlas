import { useState, useRef, useEffect } from 'react';

const DEFAULT = [38, 27, 43, 3, 9, 82, 10];

interface Frame { array: number[]; comparing: number[]; swapping: number[]; pivot: number[]; msg: string; }

// ── Merge Sort ───────────────────────────────────────────────────────────────
function buildMergeSortFrames(input: number[]): Frame[] {
  const frames: Frame[] = [];
  const arr = [...input];

  function merge(arr: number[], l: number, m: number, r: number) {
    const left = arr.slice(l, m + 1), right = arr.slice(m + 1, r + 1);
    let i = 0, j = 0, k = l;
    while (i < left.length && j < right.length) {
      frames.push({ array: [...arr], comparing: [l+i, m+1+j], swapping: [], pivot: [], msg: `Compare ${left[i]} vs ${right[j]}` });
      if (left[i] <= right[j]) arr[k++] = left[i++]; else arr[k++] = right[j++];
      frames.push({ array: [...arr], comparing: [], swapping: [k-1], pivot: [], msg: `Place ${arr[k-1]} at [${k-1}]` });
    }
    while (i < left.length) { arr[k++] = left[i++]; frames.push({ array: [...arr], comparing: [], swapping: [k-1], pivot: [], msg: `Copy left: ${arr[k-1]}` }); }
    while (j < right.length) { arr[k++] = right[j++]; frames.push({ array: [...arr], comparing: [], swapping: [k-1], pivot: [], msg: `Copy right: ${arr[k-1]}` }); }
  }

  function mergeSort(arr: number[], l: number, r: number) {
    if (l >= r) return;
    const m = Math.floor((l + r) / 2);
    frames.push({ array: [...arr], comparing: [l, r], swapping: [], pivot: [], msg: `Split [${l}..${r}] at mid=${m}` });
    mergeSort(arr, l, m); mergeSort(arr, m+1, r);
    merge(arr, l, m, r);
  }

  mergeSort(arr, 0, arr.length - 1);
  frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [], msg: '✓ Sort complete!' });
  return frames;
}

// ── Quick Sort (Lomuto) ──────────────────────────────────────────────────────
function buildQuickSortFrames(input: number[]): Frame[] {
  const frames: Frame[] = [];
  const arr = [...input];

  function partition(arr: number[], lo: number, hi: number): number {
    const pivotVal = arr[hi];
    frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [hi], msg: `Pivot = ${pivotVal} (index ${hi})` });
    let i = lo - 1;
    for (let j = lo; j < hi; j++) {
      frames.push({ array: [...arr], comparing: [j], swapping: [], pivot: [hi], msg: `Compare arr[${j}]=${arr[j]} with pivot=${pivotVal}` });
      if (arr[j] <= pivotVal) {
        i++;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        if (i !== j) frames.push({ array: [...arr], comparing: [], swapping: [i, j], pivot: [hi], msg: `Swap ${arr[i]} ↔ ${arr[j]} (i=${i}, j=${j})` });
      }
    }
    [arr[i+1], arr[hi]] = [arr[hi], arr[i+1]];
    frames.push({ array: [...arr], comparing: [], swapping: [i+1, hi], pivot: [i+1], msg: `Place pivot ${pivotVal} at index ${i+1}` });
    return i + 1;
  }

  function quickSort(arr: number[], lo: number, hi: number) {
    if (lo >= hi) return;
    const p = partition(arr, lo, hi);
    quickSort(arr, lo, p - 1);
    quickSort(arr, p + 1, hi);
  }

  quickSort(arr, 0, arr.length - 1);
  frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [], msg: '✓ Sort complete!' });
  return frames;
}

// ── Heap Sort ────────────────────────────────────────────────────────────────
function buildHeapSortFrames(input: number[]): Frame[] {
  const frames: Frame[] = [];
  const arr = [...input];
  const n = arr.length;

  function heapify(arr: number[], n: number, i: number) {
    let largest = i, l = 2*i+1, r = 2*i+2;
    if (l < n) frames.push({ array: [...arr], comparing: [i, l], swapping: [], pivot: [], msg: `Heapify: compare arr[${i}]=${arr[i]} with left arr[${l}]=${arr[l]}` });
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n) frames.push({ array: [...arr], comparing: [i, r], swapping: [], pivot: [], msg: `Heapify: compare arr[${i}]=${arr[i]} with right arr[${r}]=${arr[r]}` });
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      frames.push({ array: [...arr], comparing: [], swapping: [i, largest], pivot: [], msg: `Swap ${arr[largest]} ↔ ${arr[i]} (index ${i} ↔ ${largest})` });
      heapify(arr, n, largest);
    }
  }

  // Build max-heap
  frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [], msg: 'Phase 1: Build max-heap (heapify from n/2 down to 0)' });
  for (let i = Math.floor(n/2) - 1; i >= 0; i--) heapify(arr, n, i);
  frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [], msg: 'Max-heap built! Phase 2: Extract max repeatedly.' });

  // Extract elements
  for (let i = n - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];
    frames.push({ array: [...arr], comparing: [], swapping: [0, i], pivot: [], msg: `Extract max ${arr[i]}: swap root with arr[${i}]` });
    heapify(arr, i, 0);
  }
  frames.push({ array: [...arr], comparing: [], swapping: [], pivot: [], msg: '✓ Sort complete!' });
  return frames;
}

// ── Main component ───────────────────────────────────────────────────────────
type Algo = 'merge' | 'quick' | 'heap';
const TABS: { id: Algo; label: string }[] = [
  { id: 'merge', label: 'Merge Sort' },
  { id: 'quick', label: 'Quick Sort' },
  { id: 'heap',  label: 'Heap Sort' },
];
const BUILDERS: Record<Algo, (arr: number[]) => Frame[]> = {
  merge: buildMergeSortFrames,
  quick: buildQuickSortFrames,
  heap:  buildHeapSortFrames,
};

export default function SortingViz() {
  const [algo, setAlgo] = useState<Algo>('merge');
  const [input, setInput] = useState(DEFAULT.join(', '));
  const [frames, setFrames] = useState<Frame[]>([]);
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function switchAlgo(a: Algo) {
    stopPlay(); setAlgo(a); setFrames([]); setStep(0);
  }

  function start() {
    stopPlay();
    const arr = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setFrames(BUILDERS[algo](arr.length ? arr : DEFAULT));
    setStep(0);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setStep(s => {
        if (s >= frames.length - 1) { stopPlay(); return s; }
        return s + 1;
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
      setStep(s => { if (s >= frames.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }, [speed]);

  const frame = frames[step];
  const done = step >= frames.length - 1;
  const maxVal = frame ? Math.max(...frame.array) : 1;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Sorting Algorithms</h3>
        <p className="text-sm text-slate-400">Step through Merge Sort, Quick Sort, and Heap Sort</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t.id} onClick={() => switchAlgo(t.id)}
            className={`px-3 py-1.5 text-xs font-medium rounded border transition-colors ${algo === t.id ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600 hover:bg-slate-600'}`}>
            {t.label}
          </button>
        ))}
      </div>

      {/* Input + Start */}
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded">Start</button>
        </div>
      </div>

      {/* Bar chart */}
      {frame && (
        <div className="flex gap-1 items-end h-32">
          {frame.array.map((v, i) => {
            const isCompare = frame.comparing.includes(i);
            const isSwap    = frame.swapping.includes(i);
            const isPivot   = frame.pivot.includes(i);
            const height = Math.max(8, Math.round((v / maxVal) * 100));
            const color = isPivot ? 'bg-orange-500' : isSwap ? 'bg-green-500' : isCompare ? 'bg-yellow-500' : 'bg-blue-600';
            return (
              <div key={i} className="flex flex-col items-center gap-1 flex-1">
                <span className="text-xs font-mono text-slate-500">{v}</span>
                <div className={`w-full rounded-t transition-all duration-150 ${color}`} style={{ height: `${height}%` }} />
              </div>
            );
          })}
        </div>
      )}

      {/* Legend (quick/heap only) */}
      {(algo === 'quick' || algo === 'heap') && (
        <div className="flex gap-4 text-xs text-slate-400">
          {algo === 'quick' && <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-orange-500 inline-block"></span>Pivot</span>}
          <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-yellow-500 inline-block"></span>Comparing</span>
          <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-green-500 inline-block"></span>Swapped</span>
          <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-blue-600 inline-block"></span>Default</span>
        </div>
      )}

      {frame && <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300 min-h-10">{frame.msg}</div>}

      {frames.length > 0 && (
        <div className="flex flex-wrap items-center gap-3">
          <button onClick={() => setStep(s => Math.min(frames.length-1, s+1))} disabled={done}
            className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">Next Step</button>
          <button onClick={() => { if (playing) stopPlay(); setStep(s => Math.max(0, s-1)); }} disabled={step===0}
            className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm font-medium rounded-lg">← Back</button>
          <button onClick={togglePlay} disabled={done}
            className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">{playing ? 'Pause' : '▶ Play'}</button>
          <span className="text-xs text-slate-500">{step+1}/{frames.length}</span>
          <div className="flex items-center gap-2">
            <span className="text-xs text-slate-500">Speed</span>
            <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
            <span className="text-xs text-slate-400">{speed}x</span>
          </div>
        </div>
      )}
    </div>
  );
}
