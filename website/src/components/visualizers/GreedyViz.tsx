import { useState, useRef, useEffect } from 'react';

const TAB_BTN = (active: boolean) => active ? 'viz-btn viz-btn--primary' : 'viz-btn';

// ── Jump Game ────────────────────────────────────────────────────────────────

const DEFAULT_JUMP = [2, 3, 1, 1, 4];

interface JumpSnap { i: number; maxReach: number; started: boolean; done: boolean; canJump: boolean | null; msg: string; }

function JumpGame() {
  const [arrInput, setArrInput] = useState(DEFAULT_JUMP.join(', '));
  const [i, setI] = useState(-1);
  const [maxReach, setMaxReach] = useState(0);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [canJump, setCanJump] = useState<boolean | null>(null);
  const [msg, setMsg] = useState('Jump Game: can you reach the last index? Press "Start".');
  const [history, setHistory] = useState<JumpSnap[]>([]);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const nextRef = useRef<() => void>(() => {});

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));

  function start() {
    setPlaying(false);
    setHistory([]);
    setI(0); setMaxReach(arr[0] ?? 0); setStarted(true); setDone(false); setCanJump(null);
    setMsg(`Start at i=0, maxReach = arr[0] = ${arr[0]}. Press "Next Step".`);
  }

  function reset() {
    setPlaying(false);
    setHistory([]);
    setI(-1); setMaxReach(0); setStarted(false); setDone(false); setCanJump(null);
    setMsg('Jump Game: can you reach the last index? Press "Start".');
  }

  function next() {
    if (!started || done) return;
    setHistory(h => [...h, { i, maxReach, started, done, canJump, msg }]);
    const ni = i + 1;
    if (ni >= arr.length) {
      setDone(true); setCanJump(maxReach >= arr.length - 1);
      setMsg(`✓ Reached end! maxReach=${maxReach} ≥ lastIndex=${arr.length - 1}`);
      return;
    }
    if (ni > maxReach) {
      setDone(true); setCanJump(false);
      setMsg(`✗ i=${ni} > maxReach=${maxReach} — can't reach here! Return false.`);
      setI(ni); return;
    }
    const newReach = Math.max(maxReach, ni + arr[ni]);
    setI(ni); setMaxReach(newReach);
    setMsg(`i=${ni}, arr[${ni}]=${arr[ni]} → maxReach = max(${maxReach}, ${ni}+${arr[ni]}) = ${newReach}`);
    if (newReach >= arr.length - 1) {
      setDone(true); setCanJump(true);
      setMsg(`i=${ni}, arr[${ni}]=${arr[ni]} → maxReach=${newReach} ≥ lastIndex=${arr.length - 1} — Can reach! ✓`);
    }
  }

  useEffect(() => { nextRef.current = next; });

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
      setI(s.i); setMaxReach(s.maxReach); setStarted(s.started);
      setDone(s.done); setCanJump(s.canJump); setMsg(s.msg);
      return prev;
    });
  }

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Track farthest reachable index greedily</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array (max jump from each index)</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={arrInput} onChange={e => { setArrInput(e.target.value); reset(); }} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>
      <div className="flex gap-2 flex-wrap">
        {arr.map((v, idx) => {
          const isCurr = idx === i;
          const isReachable = idx <= maxReach && started;
          const isBlocked = done && !canJump && idx > maxReach;
          const isResult = idx === arr.length - 1 && canJump;
          const cellStyle = isCurr
            ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
            : isResult
              ? {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'}
              : isBlocked
                ? {background:'color-mix(in srgb, #ef4444 15%, transparent)',borderColor:'#ef4444',color:'var(--text)'}
                : isReachable
                  ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
                  : {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
          return (
            <div key={idx} className="flex flex-col items-center gap-1">
              <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg" style={cellStyle}>{v}</div>
              <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{idx}]</div>
            </div>
          );
        })}
      </div>
      {started && (
        <div className="flex items-center gap-3 text-sm">
          <span style={{color:'var(--text-dim)',fontFamily:'var(--mono)'}}>maxReach:</span>
          <span style={{background:'var(--surface-raised)',border:'1px solid var(--border)',padding:'0.25rem 0.75rem',borderRadius:'0.25rem',color:'var(--accent)',fontFamily:'var(--mono)',fontWeight:'bold'}}>{maxReach}</span>
        </div>
      )}
      <div className={canJump === true || canJump === false ? '' : 'viz-info'}
        style={canJump === true
          ? {background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}
          : canJump === false
            ? {background:'color-mix(in srgb, #ef4444 15%, transparent)',border:'1px solid #ef4444',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'#ef4444',fontSize:'0.875rem',fontFamily:'var(--mono)'}
            : undefined}>{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={!started || done}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={!started || done}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Merge Intervals ──────────────────────────────────────────────────────────

type Interval = [number, number];

interface MergeStep {
  current: Interval;
  merged: Interval[];
  remaining: Interval[];
  msg: string;
}

function parseIntervals(s: string): Interval[] {
  return s.trim().split(/\s+/).map(p => {
    const [a, b] = p.split(',').map(Number);
    return [a, b] as Interval;
  }).filter(([a, b]) => !isNaN(a) && !isNaN(b));
}

function buildMergeSteps(raw: Interval[]): MergeStep[] {
  const sorted = [...raw].sort((a, b) => a[0] - b[0]);
  const steps: MergeStep[] = [];
  const merged: Interval[] = [];

  for (let i = 0; i < sorted.length; i++) {
    const cur = sorted[i];
    const remaining = sorted.slice(i + 1);
    if (merged.length === 0) {
      merged.push([...cur] as Interval);
      steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `Init merged with [${cur}]` });
    } else {
      const last = merged[merged.length - 1];
      if (cur[0] <= last[1]) {
        const prev = [...last] as Interval;
        last[1] = Math.max(last[1], cur[1]);
        steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `[${cur}] overlaps with [${prev}] (${cur[0]}≤${prev[1]}) → merge to [${last}]` });
      } else {
        merged.push([...cur] as Interval);
        steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `[${cur}] no overlap with [${merged[merged.length - 2]}] → add as new` });
      }
    }
  }
  return steps;
}

function MergeIntervalsViz() {
  const [input, setInput] = useState('1,3 2,6 8,10 15,18');
  const [steps, setSteps] = useState<MergeStep[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  useEffect(() => {
    if (!playing || steps.length === 0) return;
    const id = setInterval(() => {
      setStepIdx(s => {
        if (s >= steps.length - 1) { setPlaying(false); return s; }
        return s + 1;
      });
    }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed, steps.length]);

  function start() {
    setPlaying(false);
    const ivs = parseIntervals(input);
    if (ivs.length === 0) return;
    const s = buildMergeSteps(ivs);
    setSteps(s);
    setStepIdx(0);
  }

  function reset() { setPlaying(false); setSteps([]); setStepIdx(-1); }

  const step = steps[stepIdx] ?? null;
  const allIntervals = parseIntervals(input).sort((a, b) => a[0] - b[0]);
  const maxVal = allIntervals.reduce((m, [, e]) => Math.max(m, e), 0) || 1;
  const isDone = stepIdx >= steps.length - 1 && steps.length > 0;

  const SVG_W = 340, SVG_H = 20, PAD = 10;
  function bar(iv: Interval, color: string, y: number, key: string) {
    const x1 = PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD);
    const x2 = PAD + (iv[1] / maxVal) * (SVG_W - 2 * PAD);
    return <rect key={key} x={x1} y={y} width={Math.max(x2 - x1, 4)} height={14} rx={3} fill={color} opacity={0.85} />;
  }

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Sort intervals by start, then merge overlapping pairs</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Intervals (format: "1,3 2,6 8,10")</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={input} onChange={e => { setInput(e.target.value); reset(); }} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>

      {/* Timeline SVG */}
      <div className="rounded-lg p-4 space-y-3" style={{background:'var(--surface-sunken)'}}>
        <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Timeline (0 → {maxVal})</div>
        <svg width={SVG_W} height={16}>
          <line x1={PAD} y1={8} x2={SVG_W - PAD} y2={8} stroke="var(--border)" strokeWidth={1} />
          {[0, 0.25, 0.5, 0.75, 1].map(t => {
            const x = PAD + t * (SVG_W - 2 * PAD);
            return <g key={t}><line x1={x} y1={4} x2={x} y2={12} stroke="var(--border)" strokeWidth={1} /><text x={x} y={16} textAnchor="middle" fontSize={8} fill="var(--text-faint)">{Math.round(t * maxVal)}</text></g>;
          })}
        </svg>

        <div>
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Input (sorted):</div>
          <svg width={SVG_W} height={allIntervals.length * 20 + 4}>
            {allIntervals.map((iv, i) => {
              const isCurr = step && iv[0] === step.current[0] && iv[1] === step.current[1];
              const isInRemaining = step?.remaining.some(r => r[0] === iv[0] && r[1] === iv[1]);
              const color = isCurr ? 'var(--accent)' : isInRemaining ? 'var(--border)' : 'var(--surface-raised)';
              return <g key={i}>{bar(iv, color, i * 20, `in-${i}`)}<text x={PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD)} y={i * 20 + 11} fontSize={9} fill="var(--text)">{`[${iv}]`}</text></g>;
            })}
          </svg>
        </div>

        {step && step.merged.length > 0 && (
          <div>
            <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Merged so far:</div>
            <svg width={SVG_W} height={step.merged.length * 20 + 4}>
              {step.merged.map((iv, i) => (
                <g key={i}>{bar(iv, 'var(--tier-3)', i * 20, `mg-${i}`)}<text x={PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD)} y={i * 20 + 11} fontSize={9} fill="var(--text)">{`[${iv}]`}</text></g>
              ))}
            </svg>
          </div>
        )}
      </div>

      {step && <div className="viz-info">{step.msg}</div>}

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStepIdx(s => Math.min(steps.length - 1, s + 1))} disabled={stepIdx < 0 || isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
        <button onClick={() => { setPlaying(false); setStepIdx(s => Math.max(0, s - 1)); }} disabled={stepIdx <= 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={stepIdx < 0 || isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
        {steps.length > 0 && <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>{stepIdx + 1} / {steps.length}</span>}
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────

export default function GreedyViz() {
  const [tab, setTab] = useState<'jump' | 'merge'>('jump');
  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>Greedy</h3>
        <div className="flex gap-2">
          <button className={TAB_BTN(tab === 'jump')} onClick={() => setTab('jump')}>Jump Game</button>
          <button className={TAB_BTN(tab === 'merge')} onClick={() => setTab('merge')}>Merge Intervals</button>
        </div>
      </div>
      {tab === 'jump' ? <JumpGame /> : <MergeIntervalsViz />}
    </div>
  );
}
