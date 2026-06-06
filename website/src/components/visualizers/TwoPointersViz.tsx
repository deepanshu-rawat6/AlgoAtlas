import { useState, useRef, useEffect } from 'react';

const DEFAULT_ARRAY = [1, 2, 4, 6, 8, 9, 14, 15];
const DEFAULT_TARGET = 13;

type Phase = 'idle' | 'found' | 'done';

interface State {
  array: number[];
  target: number;
  left: number;
  right: number;
  phase: Phase;
  foundLeft: number;
  foundRight: number;
  message: string;
}

function initState(array: number[], target: number): State {
  const sorted = [...array].sort((a, b) => a - b);
  return {
    array: sorted, target,
    left: 0, right: sorted.length - 1,
    phase: 'idle', foundLeft: -1, foundRight: -1,
    message: `Array sorted. Find two numbers summing to ${target}. Press "Next Step".`,
  };
}

function step(s: State): State {
  const { array, target, left, right } = s;
  if (left >= right) {
    return { ...s, phase: 'done', message: `No pair found that sums to ${target}.` };
  }
  const sum = array[left] + array[right];
  if (sum === target) {
    return { ...s, phase: 'found', foundLeft: left, foundRight: right,
      message: `Found! arr[${left}]=${array[left]} + arr[${right}]=${array[right]} = ${sum} ✓` };
  }
  if (sum < target) {
    return { ...s, left: left + 1,
      message: `Sum ${sum} < ${target} → move left pointer right (need larger values)` };
  }
  return { ...s, right: right - 1,
    message: `Sum ${sum} > ${target} → move right pointer left (need smaller values)` };
}

export default function TwoPointersViz() {
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
    setState(prev => (prev.phase === 'found' || prev.phase === 'done') ? prev : step(prev));
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
        if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; }
        return step(prev);
      });
    }, 700);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, phase, foundLeft, foundRight, message } = state;
  const done = phase === 'found' || phase === 'done';

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Two Pointers</h3>
        <p className="text-sm text-slate-400">Two Sum II — sorted array, find pair summing to target</p>
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
      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLeft = i === left;
            const isRight = i === right;
            const isFound = phase === 'found' && (i === foundLeft || i === foundRight);
            let bg = 'bg-slate-700 border-slate-600';
            if (isFound) bg = 'bg-green-800 border-green-400';
            else if (isLeft) bg = 'bg-emerald-800 border-emerald-400';
            else if (isRight) bg = 'bg-red-800 border-red-400';
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg ${bg} text-slate-100`}>
                  {val}
                </div>
                <div className="text-xs h-4" style={{ color: isLeft ? '#4ade80' : isRight ? '#f87171' : 'transparent' }}>
                  {isLeft ? 'L' : isRight ? 'R' : '.'}
                </div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Message */}
      <div className={`rounded-lg px-4 py-3 text-sm min-h-12 font-mono ${phase === 'found' ? 'bg-green-900/40 text-green-300' : phase === 'done' ? 'bg-red-900/40 text-red-300' : 'bg-slate-900/60 text-slate-300'}`}>
        {message}
      </div>

      {/* Controls */}
      <div className="flex gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={togglePlay} disabled={done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : 'Auto Play'}
        </button>
      </div>
    </div>
  );
}
