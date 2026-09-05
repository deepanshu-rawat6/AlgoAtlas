import { useState, useRef, useEffect } from 'react';

// ── Reversal tab ──────────────────────────────────────────────────────────────

const DEFAULT = [1, 2, 3, 4, 5];

interface NodeState { val: number; next: number | null; }

function buildList(vals: number[]): NodeState[] {
  return vals.map((val, i) => ({ val, next: i < vals.length - 1 ? i + 1 : null }));
}

interface RevState {
  nodes: NodeState[];
  prev: number | null;
  curr: number | null;
  done: boolean;
  msg: string;
}

function initRev(vals: number[]): RevState {
  const nodes = buildList(vals);
  return { nodes, prev: null, curr: 0, done: false, msg: 'prev=null, curr=head(0). Press "Next Step" to reverse.' };
}

function revStep(s: RevState): RevState {
  if (s.done || s.curr === null) return s;
  const nodes = s.nodes.map(n => ({ ...n }));
  const curr = s.curr;
  const nextNode = nodes[curr].next;
  nodes[curr].next = s.prev;
  return {
    nodes, prev: curr, curr: nextNode,
    done: nextNode === null,
    msg: nextNode === null
      ? `✓ Done! Reversed. New head = node(${curr}).`
      : `next=nodes[${nextNode}], nodes[${curr}].next → ${s.prev === null ? 'null' : `nodes[${s.prev}]`}, prev=nodes[${curr}], curr=nodes[${nextNode}]`,
  };
}

function ReversalTab() {
  const [input, setInput] = useState(DEFAULT.join(' → '));
  const [state, setState] = useState<RevState>(() => initRev(DEFAULT));
  const [history, setHistory] = useState<RevState[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const { nodes, prev: prevIdx, curr: currIdx, done, msg } = state;
  const n = nodes.length;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    const vals = input.split(/[→,\s]+/).map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setState(initRev(vals.length ? vals : DEFAULT));
    setHistory([]);
  }

  function nextStep() {
    if (done) { stopPlay(); return; }
    setHistory(h => [...h, state]);
    setState(revStep(state));
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
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
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Values (space or → separated)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex items-center gap-0 min-w-max">
          {nodes.map((node, i) => {
            const isCurr = i === currIdx;
            const isPrev = i === prevIdx;
            const pointsTo = node.next;
            let bg = 'bg-slate-700 border-slate-600';
            if (isCurr) bg = 'bg-yellow-800 border-yellow-400';
            else if (isPrev) bg = 'bg-blue-800 border-blue-500';
            return (
              <div key={i} className="flex items-center">
                <div className="flex flex-col items-center gap-1">
                  <div className={`w-14 h-12 flex flex-col items-center justify-center border-2 rounded-lg text-sm ${bg}`}>
                    <span className="font-mono font-bold text-slate-100">{node.val}</span>
                    <span className="text-xs text-slate-400">→{pointsTo !== null ? `[${pointsTo}]` : 'null'}</span>
                  </div>
                  <div className="text-xs h-4 text-center" style={{ minWidth: '3.5rem' }}>
                    {isCurr ? <span className="text-yellow-400">curr</span> : isPrev ? <span className="text-blue-400">prev</span> : null}
                  </div>
                </div>
                {i < n - 1 && <div className="text-slate-500 text-lg mx-0.5 mb-5">→</div>}
              </div>
            );
          })}
          <div className="text-slate-500 font-mono text-sm mb-5 ml-1">→ null</div>
        </div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${done ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={done}
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

// ── Floyd's Cycle Detection tab ───────────────────────────────────────────────

// Fixed list: 0→1→2→3→4→2 (cycle: node 4 points back to node 2)
const CYCLE_NODES = [0, 1, 2, 3, 4];
const CYCLE_NEXT = [1, 2, 3, 4, 2]; // next[i] = index of next node

interface CycleState {
  slow: number;
  fast: number;
  step: number;
  done: boolean;
  msg: string;
}

function initCycle(): CycleState {
  return { slow: 0, fast: 0, step: 0, done: false, msg: '🐢 slow=0, 🐇 fast=0. Both start at head. Press "Next Step".' };
}

function cycleStep(prev: CycleState): CycleState {
  if (prev.done) return prev;
  const newSlow = CYCLE_NEXT[prev.slow];
  const newFast = CYCLE_NEXT[CYCLE_NEXT[prev.fast]];
  const step = prev.step + 1;
  if (newSlow === newFast) {
    return { slow: newSlow, fast: newFast, step, done: true,
      msg: `🎯 Cycle detected! 🐢 slow and 🐇 fast both at node ${newSlow}. Meeting point = node ${newSlow}.` };
  }
  return { slow: newSlow, fast: newFast, step, done: false,
    msg: `Step ${step}: 🐢 slow moved 1 step → node ${newSlow}. 🐇 fast moved 2 steps → node ${newFast}.` };
}

function CycleDetectionTab() {
  const [state, setState] = useState<CycleState>(initCycle);
  const [history, setHistory] = useState<CycleState[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const { slow, fast, done } = state;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setState(initCycle());
    setHistory([]);
  }

  function nextStep() {
    if (done) { stopPlay(); return; }
    setHistory(h => [...h, state]);
    setState(cycleStep(state));
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
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
      <p className="text-sm text-slate-400">
        Floyd's algorithm: slow moves 1 step, fast moves 2. If they meet, there's a cycle.
      </p>

      {/* Node row */}
      <div className="overflow-x-auto pb-4">
        <div className="flex items-start gap-0 min-w-max">
          {CYCLE_NODES.map((val, i) => {
            const isSlow = i === slow;
            const isFast = i === fast;
            const isBoth = isSlow && isFast;
            let bg = 'bg-slate-700 border-slate-600';
            if (done && isBoth) bg = 'bg-green-700 border-green-400';
            else if (isBoth) bg = 'bg-purple-700 border-purple-400';
            else if (isSlow) bg = 'bg-blue-800 border-blue-400';
            else if (isFast) bg = 'bg-orange-800 border-orange-400';
            return (
              <div key={i} className="flex items-center">
                <div className="flex flex-col items-center gap-1">
                  <div className="text-xs h-5 text-center font-mono" style={{ minWidth: '3.5rem' }}>
                    {isBoth ? <span className={done ? 'text-green-400' : 'text-purple-400'}>🐢🐇</span>
                      : isSlow ? <span className="text-blue-400">🐢</span>
                      : isFast ? <span className="text-orange-400">🐇</span>
                      : null}
                  </div>
                  <div className={`w-14 h-12 flex flex-col items-center justify-center border-2 rounded-lg text-sm ${bg}`}>
                    <span className="font-mono font-bold text-slate-100">{val}</span>
                    <span className="text-xs text-slate-400">→{CYCLE_NEXT[i]}</span>
                  </div>
                  <div className="text-xs text-slate-500 text-center" style={{ minWidth: '3.5rem' }}>[{i}]</div>
                </div>
                {i < CYCLE_NODES.length - 1 && (
                  <div className="text-slate-500 text-lg mx-0.5 mt-5">→</div>
                )}
              </div>
            );
          })}
          {/* Cycle back arrow label */}
          <div className="flex flex-col justify-center ml-2 mt-5">
            <div className="text-orange-400 text-sm font-mono">↩ cycle to node 2</div>
          </div>
        </div>

        {/* SVG curve arrow from node 4 back to node 2 */}
        <div className="relative mt-1" style={{ height: '36px', minWidth: '420px' }}>
          <svg width="420" height="36" className="absolute left-0 top-0">
            {/* Node positions: each node cell ~62px wide (w-14=56 + 6px gap) */}
            {/* Node 2 center ≈ 2*62+28 = 152, Node 4 center ≈ 4*62+28 = 276 */}
            <path d="M 276 4 C 276 30, 152 30, 152 4" stroke="#fb923c" strokeWidth="2" fill="none" markerEnd="url(#arr)" />
            <defs>
              <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
                <path d="M0,0 L0,6 L8,3 z" fill="#fb923c" />
              </marker>
            </defs>
          </svg>
        </div>
      </div>

      {/* Legend */}
      <div className="flex gap-4 text-xs">
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-blue-700 inline-block" /> 🐢 slow</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-orange-700 inline-block" /> 🐇 fast</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-green-700 inline-block" /> meeting point</span>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${done ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>
        {state.msg}
      </div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={done}
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

// ── Root component ─────────────────────────────────────────────────────────────

type Tab = 'Reversal' | 'Cycle Detection';
const TABS: Tab[] = ['Reversal', 'Cycle Detection'];

export default function LinkedListViz() {
  const [tab, setTab] = useState<Tab>('Reversal');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Linked List</h3>
        <p className="text-sm text-slate-400">Three-pointer reversal · Floyd's cycle detection</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-3 py-1.5 text-xs font-medium rounded border transition-colors ${tab === t ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`}>
            {t}
          </button>
        ))}
      </div>

      {tab === 'Reversal' ? <ReversalTab /> : <CycleDetectionTab />}
    </div>
  );
}
