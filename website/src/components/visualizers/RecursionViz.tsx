import { useState, useEffect, useRef } from 'react';

// ── Fibonacci ────────────────────────────────────────────────────────────────

interface FibCall { id: string; n: number; result: number | null; parentId: string | null; depth: number; isMemoHit?: boolean; }

function buildCalls(n: number): FibCall[] {
  const calls: FibCall[] = [];
  let id = 0;
  function fib(n: number, parentId: string | null, depth: number): number {
    const cid = String(id++);
    calls.push({ id: cid, n, result: null, parentId, depth });
    if (n <= 1) { calls[calls.length - 1].result = n; return n; }
    const l = fib(n - 1, cid, depth + 1);
    const r = fib(n - 2, cid, depth + 1);
    const res = l + r;
    calls.find(c => c.id === cid)!.result = res;
    return res;
  }
  fib(n, null, 0);
  return calls;
}

function buildMemoCalls(n: number): FibCall[] {
  const calls: FibCall[] = [];
  const memoCache = new Map<number, number>();
  let id = 0;
  function fib(n: number, parentId: string | null, depth: number): number {
    const cid = String(id++);
    if (memoCache.has(n)) {
      const memoResult = memoCache.get(n)!;
      calls.push({ id: cid, n, result: memoResult, parentId, depth, isMemoHit: true });
      return memoResult;
    }
    calls.push({ id: cid, n, result: null, parentId, depth, isMemoHit: false });
    if (n <= 1) {
      calls[calls.length - 1].result = n;
      memoCache.set(n, n);
      return n;
    }
    const l = fib(n - 1, cid, depth + 1);
    const r = fib(n - 2, cid, depth + 1);
    const res = l + r;
    calls.find(c => c.id === cid)!.result = res;
    memoCache.set(n, res);
    return res;
  }
  fib(n, null, 0);
  return calls;
}

function FibonacciViz() {
  const [n, setN] = useState(5);
  const [memo, setMemo] = useState(false);
  const [calls, setCalls] = useState<FibCall[]>([]);
  const [step, setStep] = useState(-1);
  const [started, setStarted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const callsRef = useRef<FibCall[]>([]);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function startInterval(spd: number) {
    timerRef.current = setInterval(() => {
      setStep(s => {
        const next = s + 1;
        if (next >= callsRef.current.length) { stopPlay(); return s; }
        return next;
      });
    }, 1100 - spd * 200);
  }

  function start() {
    stopPlay();
    const c = memo ? buildMemoCalls(Math.min(n, 7)) : buildCalls(Math.min(n, 7));
    callsRef.current = c;
    setCalls(c); setStep(0); setStarted(true);
  }

  function reset() {
    stopPlay();
    setCalls([]); callsRef.current = []; setStep(-1); setStarted(false);
  }

  function toggleMemo() {
    reset();
    setMemo(m => !m);
  }

  const isDone = started && step >= calls.length - 1;

  function nextStep() {
    if (isDone) return;
    setStep(s => Math.min(calls.length - 1, s + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setStep(s => Math.max(0, s - 1));
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    if (isDone) return;
    setPlaying(true);
    startInterval(speed);
  }

  const mountedRef = useRef(false);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    startInterval(speed);
  }, [speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const visible = calls.slice(0, step + 1);
  const current = calls[step];
  const byDepth: Record<number, FibCall[]> = {};
  for (const c of visible) { byDepth[c.depth] = byDepth[c.depth] || []; byDepth[c.depth].push(c); }

  const naiveCount = buildCalls(Math.min(n, 7)).length;
  const memoCount = memo ? calls.length : null;

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Visualize overlapping subproblems (why memoization helps)</p>
      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>n (max 7)</label>
          <input type="number" min="1" max="7"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'5rem'}}
            value={n} onChange={e => setN(Math.min(7, Math.max(1, parseInt(e.target.value) || 1)))} />
        </div>
        <button onClick={start} className="viz-btn viz-btn--primary">Build Tree</button>
        <button onClick={toggleMemo}
          className={memo ? 'viz-btn viz-btn--primary' : 'viz-btn'}
          title="Toggle memoization">
          {memo ? 'With Memo' : 'Naive'}
        </button>
        {memo && (
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem',alignSelf:'center'}}>
            Naive: {naiveCount} calls → Memo: {buildMemoCalls(Math.min(n, 7)).length} calls
          </span>
        )}
      </div>
      {started && (
        <div style={{background:'var(--surface-sunken)',borderRadius:'0.5rem',padding:'1rem'}} className="space-y-3 max-h-72 overflow-y-auto">
          {Object.entries(byDepth).map(([depth, depthCalls]) => (
            <div key={depth} className="flex gap-2 flex-wrap items-center">
              <span style={{color:'var(--text-faint)',fontFamily:'var(--mono)',fontSize:'0.75rem',width:'3rem'}}>d={depth}:</span>
              {depthCalls.map(c => {
                const isCurr = c.id === current?.id;
                let cellStyle: React.CSSProperties;
                if (isCurr) {
                  cellStyle = {background:'var(--accent-soft)',border:'1px solid var(--accent)',color:'var(--text)'};
                } else if (memo && c.isMemoHit) {
                  cellStyle = {background:'var(--surface-raised)',border:'1px solid var(--border)',color:'var(--text-faint)'};
                } else if (!memo) {
                  const memoHit = depthCalls.filter(x => x.n === c.n && x.id < c.id).length > 0;
                  if (memoHit) {
                    cellStyle = {background:'color-mix(in srgb, #ef4444 15%, transparent)',border:'1px solid #ef4444',color:'var(--text)'};
                  } else if (c.result !== null) {
                    cellStyle = {background:'var(--surface-raised)',border:'1px solid var(--border)',color:'var(--text-secondary)'};
                  } else {
                    cellStyle = {background:'var(--surface-sunken)',border:'1px solid var(--border-soft)',color:'var(--text-faint)'};
                  }
                } else if (c.result !== null) {
                  cellStyle = {background:'var(--surface-raised)',border:'1px solid var(--border)',color:'var(--text-secondary)'};
                } else {
                  cellStyle = {background:'var(--surface-sunken)',border:'1px solid var(--border-soft)',color:'var(--text-faint)'};
                }
                return (
                  <div key={c.id} className="flex flex-col items-center px-2 py-1 rounded text-xs font-mono" style={cellStyle}>
                    <span>fib({c.n})</span>
                    {memo && c.isMemoHit
                      ? <span style={{color:'var(--text-faint)'}}>cache</span>
                      : c.result !== null && <span style={{color:'var(--tier-3)'}}>={c.result}</span>}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}
      {started && (
        <div className="viz-info">
          {current ? `Call ${step + 1}/${calls.length}: fib(${current.n})${current.isMemoHit ? ' (cache hit)' : current.result !== null ? ` = ${current.result}` : ' (computing...)'}` : ''}
          {step === calls.length - 1 && memo && memoCount !== null && ` | Memo: ${memoCount} calls (naive would need ${naiveCount})`}
          {step === calls.length - 1 && !memo && ` | Total calls: ${calls.length} (naive)`}
        </div>
      )}
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={!started || isDone} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={!started || step <= 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={!started || isDone} className="viz-btn viz-btn--primary">
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

// ── Tower of Hanoi ───────────────────────────────────────────────────────────

interface HanoiMove { disk: number; from: string; to: string; }

function computeHanoi(n: number, from: string, to: string, aux: string, moves: HanoiMove[]) {
  if (n === 0) return;
  computeHanoi(n - 1, from, aux, to, moves);
  moves.push({ disk: n, from, to });
  computeHanoi(n - 1, aux, to, from, moves);
}

type Pegs = Record<string, number[]>;

function applyMove(pegs: Pegs, move: HanoiMove): Pegs {
  const next: Pegs = { A: [...pegs.A], B: [...pegs.B], C: [...pegs.C] };
  const disk = next[move.from].pop()!;
  next[move.to].push(disk);
  return next;
}

function HanoiViz() {
  const [n, setN] = useState(3);
  const [moves, setMoves] = useState<HanoiMove[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);
  const [pegState, setPegState] = useState<Pegs>({ A: [], B: [], C: [] });
  const [allStates, setAllStates] = useState<Pegs[]>([]);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  function start() {
    const disks = Math.min(Math.max(n, 1), 5);
    const ms: HanoiMove[] = [];
    computeHanoi(disks, 'A', 'C', 'B', ms);
    const initial: Pegs = { A: Array.from({ length: disks }, (_, i) => disks - i), B: [], C: [] };
    const states: Pegs[] = [initial];
    let cur = initial;
    for (const m of ms) { cur = applyMove(cur, m); states.push(cur); }
    setMoves(ms); setAllStates(states); setStepIdx(0); setPegState(initial);
    setPlaying(false);
  }

  function goTo(idx: number, states: Pegs[] = allStates) {
    if (idx < 0 || idx >= states.length) return;
    setStepIdx(idx); setPegState(states[idx]);
  }

  useEffect(() => {
    if (playing) {
      timerRef.current = setInterval(() => {
        setStepIdx(s => {
          const next = s + 1;
          if (next >= allStates.length) { setPlaying(false); clearInterval(timerRef.current!); return s; }
          setPegState(allStates[next]);
          return next;
        });
      }, 1100 - speed * 200);
    } else {
      if (timerRef.current) clearInterval(timerRef.current);
    }
    return () => { if (timerRef.current) clearInterval(timerRef.current); };
  }, [playing, allStates, speed]);

  const SVG_W = 300, SVG_H = 140;
  const PEG_POSITIONS = [50, 150, 250];
  const PEG_LABELS = ['A', 'B', 'C'];
  const maxDisk = n;
  const diskH = 14, diskGap = 2;
  const maxDiskW = 60;
  const DISK_COLORS = ['#3b82f6', '#8b5cf6', '#ec4899', '#f97316', '#22c55e'];
  const move = moves[stepIdx - 1] ?? null;
  const isDone = allStates.length > 0 && stepIdx >= allStates.length - 1;

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Classic recursion: move n disks from A to C using B as auxiliary</p>
      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Disks (1–5)</label>
          <input type="number" min="1" max="5"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'5rem'}}
            value={n} onChange={e => setN(Math.min(5, Math.max(1, parseInt(e.target.value) || 1)))} />
        </div>
        <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
      </div>

      {allStates.length > 0 && (
        <>
          <div style={{background:'var(--surface-sunken)',borderRadius:'0.5rem',padding:'1rem'}}>
            <svg width={SVG_W} height={SVG_H}>
              {/* Base line */}
              <line x1={10} y1={SVG_H - 10} x2={SVG_W - 10} y2={SVG_H - 10} stroke="var(--border)" strokeWidth={2} />
              {PEG_POSITIONS.map((px, pi) => {
                const label = PEG_LABELS[pi];
                const stack = pegState[label] ?? [];
                const pegH = maxDisk * (diskH + diskGap) + 10;
                return (
                  <g key={label}>
                    {/* Peg pole */}
                    <rect x={px - 3} y={SVG_H - 10 - pegH} width={6} height={pegH} rx={2} fill="var(--border)" />
                    {/* Label */}
                    <text x={px} y={SVG_H - 1} textAnchor="middle" fontSize={10} fill="var(--text-faint)">{label}</text>
                    {/* Disks */}
                    {stack.map((disk, di) => {
                      const w = (disk / maxDisk) * maxDiskW;
                      const y = SVG_H - 10 - (di + 1) * (diskH + diskGap);
                      const isMoving = move && (move.from === label || move.to === label) && disk === move.disk;
                      return (
                        <rect key={disk} x={px - w / 2} y={y} width={w} height={diskH} rx={3}
                          fill={DISK_COLORS[(disk - 1) % DISK_COLORS.length]}
                          stroke={isMoving ? 'var(--accent)' : 'transparent'} strokeWidth={2} opacity={0.9} />
                      );
                    })}
                  </g>
                );
              })}
            </svg>
          </div>

          <div className="viz-info">
            {stepIdx === 0
              ? `Initial state: ${n} disks on peg A. Total moves: ${moves.length}`
              : move
                ? `Move ${stepIdx}/${moves.length}: Move disk ${move.disk}: ${move.from} → ${move.to}`
                : ''}
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <button onClick={() => goTo(stepIdx + 1)} disabled={isDone} className="viz-btn viz-btn--primary">Next Step</button>
            <button onClick={() => { setPlaying(false); goTo(stepIdx - 1); }} disabled={stepIdx <= 0} className="viz-btn">← Back</button>
            <button onClick={() => setPlaying(p => !p)} disabled={isDone} className="viz-btn viz-btn--primary">
              {playing ? 'Pause' : '▶ Play'}
            </button>
            <button onClick={start} className="viz-btn">Reset</button>
            <div className="flex items-center gap-2">
              <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
              <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
              <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
            </div>
            <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>{stepIdx} / {moves.length} moves</span>
          </div>
        </>
      )}
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────

export default function RecursionViz() {
  const [tab, setTab] = useState<'fib' | 'hanoi'>('fib');
  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>Recursion</h3>
        <div className="flex gap-2">
          <button className={`viz-btn${tab === 'fib' ? ' viz-btn--primary' : ''}`} onClick={() => setTab('fib')}>Fibonacci</button>
          <button className={`viz-btn${tab === 'hanoi' ? ' viz-btn--primary' : ''}`} onClick={() => setTab('hanoi')}>Tower of Hanoi</button>
        </div>
      </div>
      {tab === 'fib' ? <FibonacciViz /> : <HanoiViz />}
    </div>
  );
}
