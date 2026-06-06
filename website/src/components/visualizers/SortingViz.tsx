import { useState, useRef, useEffect } from 'react';

const DEFAULT = [38, 27, 43, 3, 9, 82, 10];

interface Frame { array: number[]; comparing: number[]; swapping: number[]; msg: string; }

function buildMergeSortFrames(input: number[]): Frame[] {
  const frames: Frame[] = [];
  const arr = [...input];

  function merge(arr: number[], l: number, m: number, r: number) {
    const left = arr.slice(l, m + 1);
    const right = arr.slice(m + 1, r + 1);
    let i = 0, j = 0, k = l;
    while (i < left.length && j < right.length) {
      frames.push({ array: [...arr], comparing: [l + i, m + 1 + j], swapping: [], msg: `Compare left[${i}]=${left[i]} vs right[${j}]=${right[j]}` });
      if (left[i] <= right[j]) { arr[k++] = left[i++]; }
      else { arr[k++] = right[j++]; }
      frames.push({ array: [...arr], comparing: [], swapping: [k - 1], msg: `Place ${arr[k-1]} at index ${k-1}` });
    }
    while (i < left.length) { arr[k++] = left[i++]; frames.push({ array: [...arr], comparing: [], swapping: [k-1], msg: `Copy remaining left: ${arr[k-1]}` }); }
    while (j < right.length) { arr[k++] = right[j++]; frames.push({ array: [...arr], comparing: [], swapping: [k-1], msg: `Copy remaining right: ${arr[k-1]}` }); }
  }

  function mergeSort(arr: number[], l: number, r: number) {
    if (l >= r) return;
    const m = Math.floor((l + r) / 2);
    frames.push({ array: [...arr], comparing: [l, r], swapping: [], msg: `Split [${l}..${r}] at mid=${m}` });
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
  }

  mergeSort(arr, 0, arr.length - 1);
  frames.push({ array: [...arr], comparing: [], swapping: [], msg: '✓ Sort complete!' });
  return frames;
}

export default function SortingViz() {
  const [input, setInput] = useState(DEFAULT.join(', '));
  const [frames, setFrames] = useState<Frame[]>([]);
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  function start() {
    const arr = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setFrames(buildMergeSortFrames(arr.length ? arr : DEFAULT));
    setStep(0); setPlaying(false);
  }

  function stopPlay() { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } setPlaying(false); }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setStep(s => { if (s >= frames.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 300);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const frame = frames[step];
  const done = step >= frames.length - 1;
  const maxVal = frame ? Math.max(...frame.array) : 1;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Merge Sort</h3>
        <p className="text-sm text-slate-400">Divide and conquer — O(n log n)</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded">Start</button>
        </div>
      </div>

      {frame && (
        <div className="flex gap-1 items-end h-32">
          {frame.array.map((v, i) => {
            const isCompare = frame.comparing.includes(i);
            const isSwap = frame.swapping.includes(i);
            const height = Math.max(8, Math.round((v / maxVal) * 100));
            return (
              <div key={i} className="flex flex-col items-center gap-1 flex-1">
                <span className="text-xs font-mono text-slate-500">{v}</span>
                <div className={`w-full rounded-t transition-all duration-150 ${isSwap ? 'bg-green-500' : isCompare ? 'bg-yellow-500' : 'bg-blue-600'}`}
                  style={{ height: `${height}%` }} />
              </div>
            );
          })}
        </div>
      )}

      {frame && <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300 min-h-10">{frame.msg}</div>}

      {frames.length > 0 && (
        <div className="flex gap-3 items-center">
          <button onClick={() => setStep(s => Math.max(0, s - 1))} disabled={step === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={done} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
          <button onClick={togglePlay} disabled={done} className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 text-white text-sm rounded-lg">{playing ? 'Pause' : 'Play'}</button>
          <span className="text-xs text-slate-500">{step + 1}/{frames.length}</span>
        </div>
      )}
    </div>
  );
}
