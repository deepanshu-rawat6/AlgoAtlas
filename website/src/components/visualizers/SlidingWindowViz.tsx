import { useState, useRef, useEffect } from 'react';

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

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

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || MSS_TARGET;
    setState(mssInit(arr.length ? arr : MSS_DEFAULT, tgt));
  }

  function nextStep() { setState(prev => prev.phase === 'done' ? prev : mssStep(prev)); }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'done') { stopPlay(); return prev; } return mssStep(prev); });
    }, 600);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, minLeft, minRight, phase, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (comma-separated)</label>
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
            const inWindow = i >= left && i <= right;
            const isMin = phase === 'done' && i >= minLeft && i <= minRight;
            let bg = 'bg-slate-700 border-slate-600';
            if (isMin) bg = 'bg-green-800 border-green-500';
            else if (inWindow) bg = 'bg-blue-800 border-blue-500';
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg ${bg} text-slate-100`}>{val}</div>
                <div className="text-xs text-slate-500 h-4">{i === left && i === right ? 'L R' : i === left ? 'L' : i === right ? 'R' : ''}</div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm text-slate-300 min-h-12 font-mono">{message}</div>

      <div className="flex gap-3">
        <button onClick={nextStep} disabled={phase === 'done'}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={togglePlay} disabled={phase === 'done'}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : 'Auto Play'}
        </button>
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

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setState(lnrInit(strInput || LNR_DEFAULT));
  }

  function nextStep() { setState(prev => prev.done ? prev : lnrStep(prev)); }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return lnrStep(prev); });
    }, 600);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { s, left, right, windowSet, maxLen, done, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">String</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={strInput} onChange={e => setStrInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {s.split('').map((ch, i) => {
            const isRight = i === right + 1; // next to expand (yellow)
            const inWindow = i >= left && i <= right;
            let bg = 'bg-slate-700 border-slate-600 text-slate-300';
            if (isRight && !done) bg = 'bg-yellow-800 border-yellow-400 text-white';
            else if (inWindow) bg = 'bg-blue-800 border-blue-500 text-white';
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div className={`w-10 h-10 flex items-center justify-center font-mono font-bold border-2 rounded-lg ${bg}`}>{ch}</div>
                <div className="text-xs text-slate-600">{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4 space-y-2">
        <div className="text-xs text-slate-400">Window set: <span className="font-mono text-blue-300">{'{'}  {[...windowSet].join(', ')}  {'}'}</span></div>
        <div className="text-xs text-slate-400">Max length so far: <span className="font-mono text-green-400 font-bold">{maxLen}</span></div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${done ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{message}</div>

      <div className="flex gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={togglePlay} disabled={done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : 'Auto Play'}
        </button>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────
export default function SlidingWindowViz() {
  const [tab, setTab] = useState<'min' | 'norepeat'>('min');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Sliding Window</h3>
        <p className="text-sm text-slate-400">Avoid nested loops by maintaining a dynamic window</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('min')} className={`${TAB_BTN} ${tab === 'min' ? ACTIVE : INACTIVE}`}>Min Subarray Sum</button>
        <button onClick={() => setTab('norepeat')} className={`${TAB_BTN} ${tab === 'norepeat' ? ACTIVE : INACTIVE}`}>Longest No Repeat</button>
      </div>

      {tab === 'min' ? <MinSubarrayTab /> : <LongestNoRepeatTab />}
    </div>
  );
}
