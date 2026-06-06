import { useState, useRef, useEffect } from 'react';

const DEFAULT_ARRAY = [2, 1, 5, 1, 3, 2];
const DEFAULT_TARGET = 7;

type Phase = 'idle' | 'running' | 'found' | 'done';

interface State {
  array: number[];
  target: number;
  left: number;
  right: number;
  sum: number;
  minLen: number;
  minLeft: number;
  minRight: number;
  phase: Phase;
  message: string;
}

function initState(array: number[], target: number): State {
  return {
    array, target,
    left: 0, right: -1, sum: 0,
    minLen: Infinity, minLeft: -1, minRight: -1,
    phase: 'idle',
    message: 'Press "Next Step" to start. Finding minimum subarray with sum ≥ target.',
  };
}

function step(s: State): State {
  const { array, target, left, right, sum, minLen, minLeft, minRight } = s;
  const n = array.length;

  // If right hasn't reached end, expand right first
  if (right + 1 < n && sum < target) {
    const nr = right + 1;
    const ns = sum + array[nr];
    return {
      ...s, right: nr, sum: ns,
      message: `Expand right → include arr[${nr}]=${array[nr]}, window sum = ${ns}`,
    };
  }

  // If sum >= target, try shrinking left
  if (sum >= target) {
    const len = right - left + 1;
    const newMin = len < minLen;
    const ns: State = {
      ...s,
      minLen: newMin ? len : minLen,
      minLeft: newMin ? left : minLeft,
      minRight: newMin ? right : minRight,
      sum: sum - array[left],
      left: left + 1,
      message: `Window sum ${sum} ≥ ${target}! Window [${left}..${right}] len=${len}${newMin ? ' ← new minimum' : ''}. Shrink left.`,
    };
    return ns;
  }

  // Done
  return {
    ...s,
    phase: 'done',
    message: minLen === Infinity
      ? 'No valid subarray found.'
      : `Done! Minimum subarray: indices [${minLeft}..${minRight}], length ${minLen}.`,
  };
}

export default function SlidingWindowViz() {
  const [arrayInput, setArrayInput] = useState(DEFAULT_ARRAY.join(', '));
  const [targetInput, setTargetInput] = useState(String(DEFAULT_TARGET));
  const [state, setState] = useState<State>(() => initState(DEFAULT_ARRAY, DEFAULT_TARGET));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);

  function reset() {
    stopPlay();
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || DEFAULT_TARGET;
    setState(initState(arr.length ? arr : DEFAULT_ARRAY, tgt));
  }

  function nextStep() {
    setState(prev => prev.phase === 'done' ? prev : step(prev));
  }

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => {
        if (prev.phase === 'done') { stopPlay(); return prev; }
        return step(prev);
      });
    }, 600);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, minLeft, minRight, phase, message } = state;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Sliding Window</h3>
        <p className="text-sm text-slate-400">Minimum subarray with sum ≥ target</p>
      </div>

      {/* Inputs */}
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (comma-separated)</label>
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
      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const inWindow = i >= left && i <= right;
            const isMin = phase === 'done' && i >= minLeft && i <= minRight;
            const isLeft = i === left;
            const isRight = i === right;
            let bg = 'bg-slate-700 border-slate-600';
            if (isMin) bg = 'bg-green-800 border-green-500';
            else if (inWindow) bg = 'bg-blue-800 border-blue-500';
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg ${bg} text-slate-100`}>
                  {val}
                </div>
                <div className="text-xs text-slate-500 h-4">
                  {isLeft && isRight ? 'L R' : isLeft ? 'L' : isRight ? 'R' : ''}
                </div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Message */}
      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm text-slate-300 min-h-12 font-mono">
        {message}
      </div>

      {/* Controls */}
      <div className="flex gap-3">
        <button
          onClick={nextStep}
          disabled={phase === 'done'}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg"
        >
          Next Step
        </button>
        <button
          onClick={togglePlay}
          disabled={phase === 'done'}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg"
        >
          {playing ? 'Pause' : 'Auto Play'}
        </button>
      </div>
    </div>
  );
}
