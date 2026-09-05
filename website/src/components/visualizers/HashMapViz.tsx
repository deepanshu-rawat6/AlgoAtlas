import { useState, useRef, useEffect } from 'react';

const TS_DEFAULT = [2, 7, 11, 15];
const TS_TARGET = 9;
const PS_DEFAULT = [1, 1, 1, 2, 3];
const PS_K = 3;

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

// ── Two Sum tab ──────────────────────────────────────────────────────────────
interface TSSnap { step: number; map: Record<number, number>; found: [number, number] | null; msg: string; }

function TwoSumTab() {
  const [arrInput, setArrInput] = useState(TS_DEFAULT.join(', '));
  const [tgtInput, setTgtInput] = useState(String(TS_TARGET));
  const [step, setStep] = useState(-1);
  const [map, setMap] = useState<Record<number, number>>({});
  const [found, setFound] = useState<[number, number] | null>(null);
  const [msg, setMsg] = useState('Press "Next Step" to walk through Two Sum hash map lookup.');
  const [history, setHistory] = useState<TSSnap[]>([]);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const nextRef = useRef<() => void>(() => {});

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const target = parseInt(tgtInput) || TS_TARGET;

  function reset() {
    setPlaying(false);
    setHistory([]);
    setStep(-1); setMap({}); setFound(null);
    setMsg('Press "Next Step" to walk through Two Sum hash map lookup.');
  }

  function next() {
    if (found || step >= arr.length - 1) return;
    const ni = step + 1;
    const complement = target - arr[ni];
    // snapshot before advancing
    setHistory(h => [...h, { step, map, found, msg }]);
    if (map[complement] !== undefined) {
      setFound([map[complement], ni]);
      setMsg(`✓ Found! arr[${map[complement]}]=${complement} + arr[${ni}]=${arr[ni]} = ${target}`);
    } else {
      setMap(prev => ({ ...prev, [arr[ni]]: ni }));
      setMsg(`i=${ni}: arr[${ni}]=${arr[ni]}, complement=${complement} not in map → store {${arr[ni]}: ${ni}}`);
    }
    setStep(ni);
  }

  useEffect(() => { nextRef.current = next; });

  const done = found !== null || (step >= arr.length - 1 && step >= 0);

  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed]);

  useEffect(() => { if (done) setPlaying(false); }, [done]);

  function stepBack() {
    setPlaying(false);
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setStep(s.step); setMap(s.map); setFound(s.found); setMsg(s.msg);
      return prev;
    });
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => { setArrInput(e.target.value); reset(); }} />
        </div>
        <div className="w-24">
          <label className="block text-xs text-slate-400 mb-1">Target</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={tgtInput} onChange={e => { setTgtInput(e.target.value); reset(); }} />
        </div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, i) => {
          const isFound = found && (i === found[0] || i === found[1]);
          const isActive = i === step && !isFound;
          let bg = 'bg-slate-700 border-slate-600 text-slate-300';
          if (isFound) bg = 'bg-green-800 border-green-400 text-white';
          else if (isActive) bg = 'bg-yellow-800 border-yellow-400 text-white';
          return (
            <div key={i} className="flex flex-col items-center gap-1">
              <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg ${bg}`}>{v}</div>
              <div className="text-xs text-slate-500">[{i}]</div>
            </div>
          );
        })}
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4">
        <div className="text-xs text-slate-500 mb-2 font-mono">HashMap: seen = {'{'}</div>
        <div className="flex flex-wrap gap-2 ml-4">
          {Object.entries(map).length === 0
            ? <span className="text-slate-600 text-sm font-mono">empty</span>
            : Object.entries(map).map(([k, v]) => (
                <span key={k} className="text-sm font-mono bg-blue-900/40 border border-blue-700 px-2 py-1 rounded text-blue-300">{k}: {v}</span>
              ))}
        </div>
        <div className="text-xs text-slate-500 mt-2 font-mono">{'}'}</div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${found ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={done}
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

// ── Prefix Sum tab ───────────────────────────────────────────────────────────
interface PSStep {
  index: number;          // current i being processed
  currSum: number;
  prefixMap: Record<number, number>;
  count: number;
  foundRanges: [number, number][];  // list of [start, end] inclusive
  done: boolean;
  msg: string;
}

function buildPSSteps(arr: number[], k: number): PSStep[] {
  const steps: PSStep[] = [];
  let currSum = 0;
  let count = 0;
  const prefixMap: Record<number, number> = { 0: 1 };
  const foundRanges: [number, number][] = [];

  // initial state (before processing any element)
  steps.push({ index: -1, currSum: 0, prefixMap: { 0: 1 }, count: 0, foundRanges: [], done: false,
    msg: 'Initial: prefix_map={0:1}, curr_sum=0. Press "Next Step".' });

  for (let i = 0; i < arr.length; i++) {
    currSum += arr[i];
    const need = currSum - k;
    const snapMap = { ...prefixMap };
    let newCount = count;
    const newRanges = [...foundRanges];

    if (snapMap[need] !== undefined) {
      newCount += snapMap[need];
      // find start index (where prefix sum == need) — rough: last occurrence
      // For display, mark all possible subarrays ending at i
      newRanges.push([i - (snapMap[need] > 0 ? 1 : 0), i]);
      steps.push({
        index: i, currSum, prefixMap: { ...snapMap, [currSum]: (snapMap[currSum] ?? 0) + 1 },
        count: newCount, foundRanges: newRanges, done: false,
        msg: `i=${i}: prefix=${currSum}, check ${currSum}-${k}=${need} in map → found! count+=map[${need}]=${snapMap[need]}. Total subarrays=${newCount}`,
      });
    } else {
      steps.push({
        index: i, currSum, prefixMap: { ...snapMap, [currSum]: (snapMap[currSum] ?? 0) + 1 },
        count: newCount, foundRanges: newRanges, done: false,
        msg: `i=${i}: prefix=${currSum}, check ${currSum}-${k}=${need} not in map. Store prefix ${currSum}.`,
      });
    }

    prefixMap[currSum] = (prefixMap[currSum] ?? 0) + 1;
    count = newCount;
    foundRanges.length = 0;
    newRanges.forEach(r => foundRanges.push(r));
  }

  // mark last step done
  steps[steps.length - 1] = { ...steps[steps.length - 1], done: true,
    msg: steps[steps.length - 1].msg + ` — Done! Total = ${count}.` };
  return steps;
}

function PrefixSumTab() {
  const [arrInput, setArrInput] = useState(PS_DEFAULT.join(', '));
  const [kInput, setKInput] = useState(String(PS_K));
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const k = parseInt(kInput) || PS_K;
  const steps = buildPSSteps(arr.length ? arr : PS_DEFAULT, k);

  const [stepIdx, setStepIdx] = useState(0);

  function reset() { setPlaying(false); setStepIdx(0); }

  const s = steps[stepIdx];
  const isDone = s.done;

  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => {
      setStepIdx(i => {
        if (i >= steps.length - 1) { setPlaying(false); return i; }
        return i + 1;
      });
    }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed, steps.length]);

  useEffect(() => { if (isDone) setPlaying(false); }, [isDone]);

  // determine per-element highlight: current=yellow, in a found range=green
  function getBoxClass(i: number) {
    if (i === s.index) return 'bg-yellow-800 border-yellow-400 text-white';
    // check if i is in any found range
    for (const [lo, hi] of s.foundRanges) {
      if (i >= lo && i <= hi) return 'bg-green-800 border-green-400 text-white';
    }
    return 'bg-slate-700 border-slate-600 text-slate-300';
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => { setArrInput(e.target.value); setStepIdx(0); }} />
        </div>
        <div className="w-20">
          <label className="block text-xs text-slate-400 mb-1">K</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={kInput} onChange={e => { setKInput(e.target.value); setStepIdx(0); }} />
        </div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, i) => (
          <div key={i} className="flex flex-col items-center gap-1">
            <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg ${getBoxClass(i)}`}>{v}</div>
            <div className="text-xs text-slate-500">[{i}]</div>
          </div>
        ))}
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4">
        <div className="text-xs text-slate-500 mb-2 font-mono">prefix_map = {'{'}</div>
        <div className="flex flex-wrap gap-2 ml-4">
          {Object.entries(s.prefixMap).length === 0
            ? <span className="text-slate-600 text-sm font-mono">empty</span>
            : Object.entries(s.prefixMap).map(([pk, pv]) => (
                <span key={pk} className="text-sm font-mono bg-blue-900/40 border border-blue-700 px-2 py-1 rounded text-blue-300">{pk}: {pv}</span>
              ))}
        </div>
        <div className="text-xs text-slate-500 mt-2 font-mono">{'}'}</div>
        <div className="text-xs text-slate-400 mt-2">Subarrays found: <span className="text-green-400 font-mono font-bold">{s.count}</span></div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${s.count > 0 ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{s.msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStepIdx(i => Math.min(i + 1, steps.length - 1))} disabled={isDone}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={() => { setPlaying(false); setStepIdx(i => Math.max(0, i - 1)); }} disabled={stepIdx === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone}
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

// ── Root ─────────────────────────────────────────────────────────────────────
export default function HashMapViz() {
  const [tab, setTab] = useState<'twosum' | 'prefixsum'>('twosum');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Hash Map</h3>
        <p className="text-sm text-slate-400">Trade space for time with complement / prefix lookups</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('twosum')} className={`${TAB_BTN} ${tab === 'twosum' ? ACTIVE : INACTIVE}`}>Two Sum</button>
        <button onClick={() => setTab('prefixsum')} className={`${TAB_BTN} ${tab === 'prefixsum' ? ACTIVE : INACTIVE}`}>Prefix Sum</button>
      </div>

      {tab === 'twosum' ? <TwoSumTab /> : <PrefixSumTab />}
    </div>
  );
}
