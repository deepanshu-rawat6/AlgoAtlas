import { useState, useRef, useEffect } from 'react';

const DEFAULT_MERGE: [number, number][] = [[1,3],[2,6],[8,10],[15,18]];
const DEFAULT_INSERT_INTERVALS: [number,number][] = [[1,3],[6,9]];
const DEFAULT_NEW_INTERVAL: [number,number] = [2,5];

const TAB_BTN = (active: boolean) => active ? 'viz-btn viz-btn--primary' : 'viz-btn';

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
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Merge Intervals</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Sort by start, merge overlapping intervals greedily</p>
      </div>
      <div className="rounded-lg p-4 overflow-x-auto" style={{background:'var(--surface-sunken)'}}>
        <svg width="100%" viewBox={`0 0 500 ${(intervals.length + merged.length + 2) * 28 + 10}`} style={{ minWidth: 320 }}>
          <line x1="10" y1="5" x2={max * scale + 10} y2="5" stroke="var(--border)" strokeWidth="1" />
          {Array.from({ length: max + 1 }, (_, i) => (
            <g key={i}>
              <line x1={i * scale + 10} y1="3" x2={i * scale + 10} y2="7" stroke="var(--border)" strokeWidth="1" />
              <text x={i * scale + 10} y="18" textAnchor="middle" fill="var(--text-faint)" fontSize="9">{i}</text>
            </g>
          ))}
          {sorted.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + i * 28} width={(e - s) * scale} height="18"
                fill={i < step ? 'var(--surface-raised)' : i === step ? 'var(--accent-soft)' : 'var(--surface-sunken)'}
                stroke={i < step ? 'var(--border)' : i === step ? 'var(--accent)' : 'var(--border-soft)'} strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + i * 28 + 13} fill="var(--text-dim)" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
          <line x1="10" y1={28 + sorted.length * 28 + 8} x2={max * scale + 10} y2={28 + sorted.length * 28 + 8} stroke="var(--border)" strokeWidth="1" strokeDasharray="4" />
          <text x="12" y={28 + sorted.length * 28 + 20} fill="var(--text-faint)" fontSize="9">merged:</text>
          {merged.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + sorted.length * 28 + 24 + i * 28} width={(e - s) * scale} height="18"
                fill="color-mix(in srgb, var(--tier-3) 20%, transparent)" stroke="var(--tier-3)" strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + sorted.length * 28 + 24 + i * 28 + 13} fill="var(--tier-3)" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
        </svg>
      </div>
      <div className="viz-info">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          Next Step
        </button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">
          Reset
        </button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
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

  while (i < n && intervals[i][1] < ni[0]) {
    result.push([...intervals[i]]);
    frames.push({ idx: i, phase: 'before', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `[${intervals[i]}] ends before new interval starts → add to result` });
    i++;
  }
  while (i < n && intervals[i][0] <= ni[1]) {
    const merged: [number,number] = [Math.min(ni[0], intervals[i][0]), Math.max(ni[1], intervals[i][1])];
    frames.push({ idx: i, phase: 'overlap', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `[${intervals[i]}] overlaps → merge: [${ni}] ∪ [${intervals[i]}] = [${merged}]` });
    ni = merged;
    i++;
  }
  result.push([...ni]);
  frames.push({ idx: i - 1, phase: 'overlap', result: result.map(x => [...x] as [number,number]), newInterval: [...ni], msg: `Merged interval [${ni}] added to result` });

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

  function cellColor(phase: InsertPhase) {
    if (phase === 'done') return { fill: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', stroke: 'var(--tier-3)' };
    if (phase === 'before') return { fill: 'var(--surface-raised)', stroke: 'var(--border)' };
    if (phase === 'overlap') return { fill: 'var(--accent-soft)', stroke: 'var(--accent)' };
    return { fill: 'var(--surface-sunken)', stroke: 'var(--border-soft)' };
  }

  return (
    <div className="space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Insert Interval</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Insert into sorted non-overlapping intervals and merge</p>
      </div>

      <div className="flex flex-wrap gap-4 text-xs" style={{color:'var(--text-dim)'}}>
        <span>Intervals: <span style={{color:'var(--text)',fontFamily:'var(--mono)'}}>{intervals.map(i => `[${i}]`).join(', ')}</span></span>
        <span>New: <span style={{color:'var(--accent)',fontFamily:'var(--mono)'}}>[{newInterval.join(',')}]</span></span>
      </div>

      <div className="rounded-lg p-4 overflow-x-auto" style={{background:'var(--surface-sunken)'}}>
        <svg width="100%" viewBox={`0 0 460 ${(intervals.length + 4) * 28 + 10}`} style={{ minWidth: 300 }}>
          {/* Axis */}
          {Array.from({ length: max + 1 }, (_, i) => (
            <g key={i}>
              <line x1={i * scale + 10} y1="3" x2={i * scale + 10} y2="7" stroke="var(--border)" strokeWidth="1" />
              <text x={i * scale + 10} y="18" textAnchor="middle" fill="var(--text-faint)" fontSize="9">{i}</text>
            </g>
          ))}
          {/* New interval */}
          <rect x={newInterval[0] * scale + 10} y={28} width={(newInterval[1] - newInterval[0]) * scale} height="18"
            fill="var(--accent-soft)" stroke="var(--accent)" strokeWidth="1.5" rx="3" strokeDasharray="4" />
          <text x={newInterval[0] * scale + 15} y={28 + 13} fill="var(--accent)" fontSize="10">new [{newInterval.join(',')}]</text>

          {/* Original intervals */}
          {intervals.map(([s, e], i) => {
            const isCurr = frame && i === frame.idx;
            const color = isCurr ? cellColor(frame.phase) : { fill: 'var(--surface-sunken)', stroke: 'var(--border-soft)' };
            return (
              <g key={i}>
                <rect x={s * scale + 10} y={56 + i * 28} width={(e - s) * scale} height="18"
                  fill={color.fill} stroke={color.stroke} strokeWidth="1.5" rx="3" />
                <text x={s * scale + 15} y={56 + i * 28 + 13} fill="var(--text-dim)" fontSize="10">[{s},{e}]</text>
              </g>
            );
          })}

          {/* Separator */}
          <line x1="10" y1={56 + intervals.length * 28 + 8} x2={max * scale + 10} y2={56 + intervals.length * 28 + 8} stroke="var(--border)" strokeWidth="1" strokeDasharray="4" />
          <text x="12" y={56 + intervals.length * 28 + 20} fill="var(--text-faint)" fontSize="9">result:</text>

          {/* Result */}
          {frame && frame.result.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={56 + intervals.length * 28 + 24 + i * 28} width={(e - s) * scale} height="18"
                fill="color-mix(in srgb, var(--tier-3) 20%, transparent)" stroke="var(--tier-3)" strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={56 + intervals.length * 28 + 24 + i * 28 + 13} fill="var(--tier-3)" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
        </svg>
      </div>

      {frame && (
        <div className={frame.phase === 'done' ? '' : 'viz-info'}
          style={frame.phase === 'done' ? {background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'} : undefined}>
          {frame.msg}
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          Next Step
        </button>
        <button onClick={stepBack} disabled={step === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={() => { stopPlay(); setStep(0); }} className="viz-btn">
          Reset
        </button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
        <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}} className="self-center">{step + 1}/{frames.length}</span>
      </div>
    </div>
  );
}

// ── Main ─────────────────────────────────────────────────────────────────────
export default function IntervalsViz() {
  const [tab, setTab] = useState<'merge' | 'insert'>('merge');
  return (
    <div className="panel p-6 space-y-6">
      <div className="flex gap-2">
        <button className={TAB_BTN(tab === 'merge')} onClick={() => setTab('merge')}>Merge Intervals</button>
        <button className={TAB_BTN(tab === 'insert')} onClick={() => setTab('insert')}>Insert Interval</button>
      </div>
      {tab === 'merge' ? <MergeTab /> : <InsertTab />}
    </div>
  );
}
