import { useState, useRef, useEffect } from 'react';

const DEFAULT_MERGE: [number, number][] = [[1,3],[2,6],[8,10],[15,18]];
const DEFAULT_INSERT_INTERVALS: [number,number][] = [[1,3],[6,9]];
const DEFAULT_NEW_INTERVAL: [number,number] = [2,5];

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

// ── Merge Intervals ──────────────────────────────────────────────────────────

interface MergeSnap { step: number; merged: [number,number][]; msg: string; }

function MergeTab() {
  const [intervals] = useState<[number,number][]>(DEFAULT_MERGE);
  const [step, setStep] = useState(0);
  const [merged, setMerged] = useState<[number,number][]>([]);
  const [msg, setMsg] = useState('Intervals sorted by start. Press "Next Step" to merge.');
  const [history, setHistory] = useState<MergeSnap[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const sorted = [...intervals].sort((a, b) => a[0] - b[0]);
  const max = Math.max(...intervals.map(i => i[1])) + 1;
  const scale = 480 / (max + 1);
  const isDone = step >= sorted.length;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setStep(0); setMerged([]); setHistory([]);
    setMsg('Intervals sorted by start. Press "Next Step" to merge.');
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    const curr = sorted[step];
    const m = [...merged];
    let newMsg = '';
    if (m.length === 0 || m[m.length - 1][1] < curr[0]) {
      m.push([...curr]);
      newMsg = `[${curr}] does NOT overlap with last merged → push as new interval.`;
    } else {
      const last = m[m.length - 1];
      const newEnd = Math.max(last[1], curr[1]);
      newMsg = `[${curr}] overlaps with [${last}] → merge: end = max(${last[1]}, ${curr[1]}) = ${newEnd}`;
      m[m.length - 1] = [last[0], newEnd];
    }
    const newStep = step + 1;
    if (newStep >= sorted.length) newMsg += `. Done! ${m.length} merged interval(s).`;
    setHistory(h => [...h, { step, merged, msg }]);
    setMerged(m); setStep(newStep); setMsg(newMsg);
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setStep(s.step); setMerged(s.merged); setMsg(s.msg);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => { nextRef.current = nextStep; });
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }, [speed]); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Merge Intervals</h3>
        <p className="text-sm text-slate-400">Sort by start, merge overlapping intervals greedily</p>
      </div>
      <div className="bg-slate-900/60 rounded-lg p-4 overflow-x-auto">
        <svg width="100%" viewBox={`0 0 500 ${(intervals.length + merged.length + 2) * 28 + 10}`} style={{ minWidth: 320 }}>
          <line x1="10" y1="5" x2={max * scale + 10} y2="5" stroke="#334155" strokeWidth="1" />
          {Array.from({ length: max + 1 }, (_, i) => (
            <g key={i}>
              <line x1={i * scale + 10} y1="3" x2={i * scale + 10} y2="7" stroke="#475569" strokeWidth="1" />
              <text x={i * scale + 10} y="18" textAnchor="middle" fill="#64748b" fontSize="9">{i}</text>
            </g>
          ))}
          {sorted.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + i * 28} width={(e - s) * scale} height="18"
                fill={i < step ? '#1e3a5f' : i === step ? '#1d4ed8' : '#1e293b'}
                stroke={i < step ? '#334155' : i === step ? '#60a5fa' : '#475569'} strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + i * 28 + 13} fill="#94a3b8" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
          <line x1="10" y1={28 + sorted.length * 28 + 8} x2={max * scale + 10} y2={28 + sorted.length * 28 + 8} stroke="#334155" strokeWidth="1" strokeDasharray="4" />
          <text x="12" y={28 + sorted.length * 28 + 20} fill="#64748b" fontSize="9">merged:</text>
          {merged.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + sorted.length * 28 + 24 + i * 28} width={(e - s) * scale} height="18"
                fill="#14532d" stroke="#22c55e" strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + sorted.length * 28 + 24 + i * 28 + 13} fill="#86efac" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
        </svg>
      </div>
      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset}
          className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">
          Reset
        </button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Insert Interval ──────────────────────────────────────────────────────────
type InsertPhase = 'before' | 'overlap' | 'after' | 'done';

interface InsertFrame {
  idx: number;
  phase: InsertPhase;
  result: [number,number][];
  newInterval: [number,number];
  msg: string;
}

function buildInsertFrames(intervals: [number,number][], newInterval: [number,number]): InsertFrame[] {
  const frames: InsertFrame[] = [];
  const result: [number,number][] = [];
  let ni: [number,number] = [...newInterval];
  let i = 0;
  const n = intervals.length;

  // Phase 1: before
  while (i < n && intervals[i][1] < ni[0]) {
    result.push([...intervals[i]]);
    frames.push({ idx: i, phase: 'before', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `[${intervals[i]}] ends before new interval starts → add to result` });
    i++;
  }
  // Phase 2: overlap
  while (i < n && intervals[i][0] <= ni[1]) {
    const merged: [number,number] = [Math.min(ni[0], intervals[i][0]), Math.max(ni[1], intervals[i][1])];
    frames.push({ idx: i, phase: 'overlap', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `[${intervals[i]}] overlaps → merge: [${ni}] ∪ [${intervals[i]}] = [${merged}]` });
    ni = merged;
    i++;
  }
  result.push([...ni]);
  frames.push({ idx: i - 1, phase: 'overlap', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `Merged interval [${ni}] added to result` });

  // Phase 3: after
  while (i < n) {
    result.push([...intervals[i]]);
    frames.push({ idx: i, phase: 'after', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `[${intervals[i]}] starts after merged end ${ni[1]} → add to result` });
    i++;
  }
  frames.push({ idx: i, phase: 'done', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `Done! Result: ${result.map(r => `[${r}]`).join(', ')}` });
  return frames;
}

function InsertTab() {
  const [intervals] = useState<[number,number][]>(DEFAULT_INSERT_INTERVALS);
  const [newInterval] = useState<[number,number]>(DEFAULT_NEW_INTERVAL);
  const [frames] = useState(() => buildInsertFrames(intervals, newInterval));
  const [step, setStep] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const frame = frames[step];
  const max = Math.max(...intervals.map(i => i[1]), newInterval[1]) + 2;
  const scale = 420 / (max + 1);
  const isDone = step >= frames.length - 1;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    setStep(s => Math.min(frames.length - 1, s + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setStep(s => Math.max(0, s - 1));
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => { nextRef.current = nextStep; });
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }, [speed]); // eslint-disable-line react-hooks/exhaustive-deps

  function cellColor(idx: number, phase: InsertPhase) {
    if (phase === 'done') return { fill: '#14532d', stroke: '#22c55e' };
    if (phase === 'before') return { fill: '#1e3a5f', stroke: '#3b82f6' };
    if (phase === 'overlap') return { fill: '#713f12', stroke: '#eab308' };
    return { fill: '#1e293b', stroke: '#475569' };
  }

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Insert Interval</h3>
        <p className="text-sm text-slate-400">Insert into sorted non-overlapping intervals and merge</p>
      </div>

      <div className="flex flex-wrap gap-4 text-xs text-slate-400">
        <span>Intervals: <span className="text-slate-200 font-mono">{intervals.map(i => `[${i}]`).join(', ')}</span></span>
        <span>New: <span className="text-yellow-300 font-mono">[{newInterval.join(',')}]</span></span>
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4 overflow-x-auto">
        <svg width="100%" viewBox={`0 0 460 ${(intervals.length + 4) * 28 + 10}`} style={{ minWidth: 300 }}>
          {/* Axis */}
          {Array.from({ length: max + 1 }, (_, i) => (
            <g key={i}>
              <line x1={i * scale + 10} y1="3" x2={i * scale + 10} y2="7" stroke="#475569" strokeWidth="1" />
              <text x={i * scale + 10} y="18" textAnchor="middle" fill="#64748b" fontSize="9">{i}</text>
            </g>
          ))}
          {/* New interval */}
          <rect x={newInterval[0] * scale + 10} y={28} width={(newInterval[1] - newInterval[0]) * scale} height="18"
            fill="#422006" stroke="#f59e0b" strokeWidth="1.5" rx="3" strokeDasharray="4" />
          <text x={newInterval[0] * scale + 15} y={28 + 13} fill="#fcd34d" fontSize="10">new [{newInterval.join(',')}]</text>

          {/* Original intervals */}
          {intervals.map(([s, e], i) => {
            const isCurr = frame && i === frame.idx;
            const color = isCurr ? cellColor(i, frame.phase) : { fill: '#1e293b', stroke: '#475569' };
            return (
              <g key={i}>
                <rect x={s * scale + 10} y={56 + i * 28} width={(e - s) * scale} height="18"
                  fill={color.fill} stroke={color.stroke} strokeWidth="1.5" rx="3" />
                <text x={s * scale + 15} y={56 + i * 28 + 13} fill="#94a3b8" fontSize="10">[{s},{e}]</text>
              </g>
            );
          })}

          {/* Separator */}
          <line x1="10" y1={56 + intervals.length * 28 + 8} x2={max * scale + 10} y2={56 + intervals.length * 28 + 8} stroke="#334155" strokeWidth="1" strokeDasharray="4" />
          <text x="12" y={56 + intervals.length * 28 + 20} fill="#64748b" fontSize="9">result:</text>

          {/* Result */}
          {frame && frame.result.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={56 + intervals.length * 28 + 24 + i * 28} width={(e - s) * scale} height="18"
                fill="#14532d" stroke="#22c55e" strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={56 + intervals.length * 28 + 24 + i * 28 + 13} fill="#86efac" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
        </svg>
      </div>

      {frame && (
        <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${frame.phase === 'done' ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>
          {frame.msg}
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={step === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={() => { stopPlay(); setStep(0); }}
          className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">
          Reset
        </button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
        <span className="text-xs text-slate-500 self-center">{step + 1}/{frames.length}</span>
      </div>
    </div>
  );
}

// ── Main ─────────────────────────────────────────────────────────────────────
export default function IntervalsViz() {
  const [tab, setTab] = useState<'merge' | 'insert'>('merge');
  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div className="flex gap-2">
        <button className={TAB_BTN(tab === 'merge')} onClick={() => setTab('merge')}>Merge Intervals</button>
        <button className={TAB_BTN(tab === 'insert')} onClick={() => setTab('insert')}>Insert Interval</button>
      </div>
      {tab === 'merge' ? <MergeTab /> : <InsertTab />}
    </div>
  );
}
