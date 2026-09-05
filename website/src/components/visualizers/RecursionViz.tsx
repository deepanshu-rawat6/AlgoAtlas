import { useState, useEffect, useRef } from 'react';

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

// ── Fibonacci ────────────────────────────────────────────────────────────────

interface FibCall { id: string; n: number; result: number | null; parentId: string | null; depth: number; }

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

function FibonacciViz() {
  const [n, setN] = useState(5);
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
    const c = buildCalls(Math.min(n, 7));
    callsRef.current = c;
    setCalls(c); setStep(0); setStarted(true);
  }

  function reset() {
    stopPlay();
    setCalls([]); callsRef.current = []; setStep(-1); setStarted(false);
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

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">Visualize overlapping subproblems (why memoization helps)</p>
      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block text-xs text-slate-400 mb-1">n (max 7)</label>
          <input type="number" min="1" max="7"
            className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={n} onChange={e => setN(Math.min(7, Math.max(1, parseInt(e.target.value) || 1)))} />
        </div>
        <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Build Tree</button>
      </div>
      {started && (
        <div className="bg-slate-900/60 rounded-lg p-4 space-y-3 max-h-72 overflow-y-auto">
          {Object.entries(byDepth).map(([depth, depthCalls]) => (
            <div key={depth} className="flex gap-2 flex-wrap items-center">
              <span className="text-xs text-slate-600 font-mono w-12">d={depth}:</span>
              {depthCalls.map(c => {
                const isCurr = c.id === current?.id;
                const memoHit = depthCalls.filter(x => x.n === c.n && x.id < c.id).length > 0;
                return (
                  <div key={c.id} className={`flex flex-col items-center px-2 py-1 rounded border text-xs font-mono ${isCurr ? 'bg-yellow-800 border-yellow-500 text-yellow-100' : memoHit ? 'bg-red-900/40 border-red-800 text-red-400' : c.result !== null ? 'bg-blue-900/40 border-blue-700 text-blue-200' : 'bg-slate-700 border-slate-600 text-slate-400'}`}>
                    <span>fib({c.n})</span>
                    {c.result !== null && <span className="text-green-400">={c.result}</span>}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}
      {started && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300">
          {current ? `Call ${step + 1}/${calls.length}: fib(${current.n})${current.result !== null ? ` = ${current.result}` : ' (computing...)'}` : ''}
          {step === calls.length - 1 && ` | Total calls: ${calls.length} (naive)`}
        </div>
      )}
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={!started || isDone}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={!started || step <= 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={!started || isDone}
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
      <p className="text-sm text-slate-400">Classic recursion: move n disks from A to C using B as auxiliary</p>
      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block text-xs text-slate-400 mb-1">Disks (1–5)</label>
          <input type="number" min="1" max="5"
            className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={n} onChange={e => setN(Math.min(5, Math.max(1, parseInt(e.target.value) || 1)))} />
        </div>
        <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
      </div>

      {allStates.length > 0 && (
        <>
          <div className="bg-slate-900/60 rounded-lg p-4">
            <svg width={SVG_W} height={SVG_H}>
              {/* Base line */}
              <line x1={10} y1={SVG_H - 10} x2={SVG_W - 10} y2={SVG_H - 10} stroke="#475569" strokeWidth={2} />
              {PEG_POSITIONS.map((px, pi) => {
                const label = PEG_LABELS[pi];
                const stack = pegState[label] ?? [];
                const pegH = maxDisk * (diskH + diskGap) + 10;
                return (
                  <g key={label}>
                    {/* Peg pole */}
                    <rect x={px - 3} y={SVG_H - 10 - pegH} width={6} height={pegH} rx={2} fill="#64748b" />
                    {/* Label */}
                    <text x={px} y={SVG_H - 1} textAnchor="middle" fontSize={10} fill="#94a3b8">{label}</text>
                    {/* Disks */}
                    {stack.map((disk, di) => {
                      const w = (disk / maxDisk) * maxDiskW;
                      const y = SVG_H - 10 - (di + 1) * (diskH + diskGap);
                      const isMoving = move && (move.from === label || move.to === label) && disk === move.disk;
                      return (
                        <rect key={disk} x={px - w / 2} y={y} width={w} height={diskH} rx={3}
                          fill={DISK_COLORS[(disk - 1) % DISK_COLORS.length]}
                          stroke={isMoving ? '#fbbf24' : 'transparent'} strokeWidth={2} opacity={0.9} />
                      );
                    })}
                  </g>
                );
              })}
            </svg>
          </div>

          <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300">
            {stepIdx === 0
              ? `Initial state: ${n} disks on peg A. Total moves: ${moves.length}`
              : move
                ? `Move ${stepIdx}/${moves.length}: Move disk ${move.disk}: ${move.from} → ${move.to}`
                : ''}
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <button onClick={() => goTo(stepIdx + 1)} disabled={isDone}
              className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
            <button onClick={() => { setPlaying(false); goTo(stepIdx - 1); }} disabled={stepIdx <= 0}
              className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
            <button onClick={() => setPlaying(p => !p)} disabled={isDone}
              className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
              {playing ? 'Pause' : '▶ Play'}
            </button>
            <button onClick={start}
              className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">Reset</button>
            <div className="flex items-center gap-2">
              <span className="text-xs text-slate-500">Speed</span>
              <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
              <span className="text-xs text-slate-400">{speed}x</span>
            </div>
            <span className="text-xs text-slate-500">{stepIdx} / {moves.length} moves</span>
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
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">Recursion</h3>
        <div className="flex gap-2">
          <button className={TAB_BTN(tab === 'fib')} onClick={() => setTab('fib')}>Fibonacci</button>
          <button className={TAB_BTN(tab === 'hanoi')} onClick={() => setTab('hanoi')}>Tower of Hanoi</button>
        </div>
      </div>
      {tab === 'fib' ? <FibonacciViz /> : <HanoiViz />}
    </div>
  );
}
