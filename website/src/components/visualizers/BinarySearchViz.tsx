import { useState } from 'react';

const DEFAULT_ARRAY = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 89, 95];
const DEFAULT_TARGET = 23;

type Phase = 'idle' | 'found' | 'done';

interface State {
  array: number[];
  target: number;
  lo: number;
  hi: number;
  mid: number | null;
  phase: Phase;
  message: string;
}

function initState(array: number[], target: number): State {
  const sorted = [...array].sort((a, b) => a - b);
  return {
    array: sorted, target,
    lo: 0, hi: sorted.length - 1, mid: null,
    phase: 'idle',
    message: `Sorted array ready. Searching for ${target}. Press "Next Step".`,
  };
}

function step(s: State): State {
  const { array, target, lo, hi } = s;
  if (lo > hi) {
    return { ...s, phase: 'done', mid: null,
      message: `Not found. lo (${lo}) > hi (${hi}). ${target} is not in the array.` };
  }
  const mid = Math.floor((lo + hi) / 2);
  const val = array[mid];
  if (val === target) {
    return { ...s, mid, phase: 'found',
      message: `Found! arr[${mid}] = ${val} = target ${target} ✓` };
  }
  if (val < target) {
    return { ...s, mid, lo: mid + 1,
      message: `arr[${mid}]=${val} < ${target} → search right half. New lo = ${mid + 1}` };
  }
  return { ...s, mid, hi: mid - 1,
    message: `arr[${mid}]=${val} > ${target} → search left half. New hi = ${mid - 1}` };
}

export default function BinarySearchViz() {
  const [arrayInput, setArrayInput] = useState(DEFAULT_ARRAY.join(', '));
  const [targetInput, setTargetInput] = useState(String(DEFAULT_TARGET));
  const [state, setState] = useState<State>(() => initState(DEFAULT_ARRAY, DEFAULT_TARGET));

  function reset() {
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || DEFAULT_TARGET;
    setState(initState(arr.length ? arr : DEFAULT_ARRAY, tgt));
  }

  function nextStep() {
    setState(prev => (prev.phase === 'found' || prev.phase === 'done') ? prev : step(prev));
  }

  const { array, lo, hi, mid, phase, message } = state;
  const done = phase === 'found' || phase === 'done';

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Binary Search</h3>
        <p className="text-sm text-slate-400">Watch lo/mid/hi converge on the target</p>
      </div>

      {/* Inputs */}
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (will be sorted)</label>
          <input
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrayInput}
            onChange={e => setArrayInput(e.target.value)}
          />
        </div>
        <div className="w-24">
          <label className="block text-xs text-slate-400 mb-1">Target</label>
          <input
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={targetInput}
            onChange={e => setTargetInput(e.target.value)}
          />
        </div>
        <div className="flex items-end">
          <button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button>
        </div>
      </div>

      {/* Array visualization */}
      <div className="overflow-x-auto pb-6">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLo = i === lo;
            const isHi = i === hi;
            const isMid = i === mid;
            const inRange = i >= lo && i <= hi;
            const isFound = phase === 'found' && i === mid;
            let bg = 'bg-slate-700 border-slate-600 text-slate-500';
            if (isFound) bg = 'bg-green-700 border-green-400 text-white';
            else if (phase === 'done' && !inRange) bg = 'bg-slate-800 border-slate-700 text-slate-600';
            else if (isMid) bg = 'bg-yellow-700 border-yellow-400 text-white';
            else if (inRange) bg = 'bg-slate-600 border-slate-500 text-slate-200';
            return (
              <div key={i} className="flex flex-col items-center">
                <div className={`w-11 h-11 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>
                  {val}
                </div>
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

      {/* Message */}
      <div className={`rounded-lg px-4 py-3 text-sm min-h-12 font-mono ${
        phase === 'found' ? 'bg-green-900/40 text-green-300' :
        phase === 'done' ? 'bg-red-900/40 text-red-300' :
        'bg-slate-900/60 text-slate-300'
      }`}>
        {message}
      </div>

      {/* Controls */}
      <div className="flex gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
      </div>
    </div>
  );
}
