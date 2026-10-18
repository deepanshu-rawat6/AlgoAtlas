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
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Values (space or → separated)</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex items-center gap-0 min-w-max">
          {nodes.map((node, i) => {
            const isCurr = i === currIdx;
            const isPrev = i === prevIdx;
            const pointsTo = node.next;
            let nodeStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)' };
            if (isCurr) nodeStyle = { background: 'color-mix(in srgb, #eab308 20%, transparent)', borderColor: '#eab308' };
            else if (isPrev) nodeStyle = { background: 'var(--accent-soft)', borderColor: 'var(--accent)' };
            return (
              <div key={i} className="flex items-center">
                <div className="flex flex-col items-center gap-1">
                  <div style={nodeStyle} className="w-14 h-12 flex flex-col items-center justify-center border-2 rounded-lg text-sm">
                    <span style={{ color: 'var(--text)', fontFamily: 'var(--mono)', fontWeight: 700 }}>{node.val}</span>
                    <span style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>→{pointsTo !== null ? `[${pointsTo}]` : 'null'}</span>
                  </div>
                  <div className="text-xs h-4 text-center" style={{ minWidth: '3.5rem' }}>
                    {isCurr ? <span className="text-yellow-400">curr</span> : isPrev ? <span style={{ color: 'var(--accent)' }}>prev</span> : null}
                  </div>
                </div>
                {i < n - 1 && <div style={{ color: 'var(--text-faint)', fontSize: '1.125rem' }} className="mx-0.5 mb-5">→</div>}
              </div>
            );
          })}
          <div style={{ color: 'var(--text-faint)', fontFamily: 'var(--mono)', fontSize: '0.875rem' }} className="mb-5 ml-1">→ null</div>
        </div>
      </div>

      {done
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>{msg}</div>
        : <div className="viz-info">{msg}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
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
      <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>
        Floyd's algorithm: slow moves 1 step, fast moves 2. If they meet, there's a cycle.
      </p>

      {/* Node row */}
      <div className="overflow-x-auto pb-4">
        <div className="flex items-start gap-0 min-w-max">
          {CYCLE_NODES.map((val, i) => {
            const isSlow = i === slow;
            const isFast = i === fast;
            const isBoth = isSlow && isFast;
            let nodeStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)' };
            if (done && isBoth) nodeStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)' };
            else if (isBoth) nodeStyle = { background: 'color-mix(in srgb, #a855f7 20%, transparent)', borderColor: '#a855f7' };
            else if (isSlow) nodeStyle = { background: 'var(--accent-soft)', borderColor: 'var(--accent)' };
            else if (isFast) nodeStyle = { background: 'color-mix(in srgb, #f97316 20%, transparent)', borderColor: '#f97316' };
            return (
              <div key={i} className="flex items-center">
                <div className="flex flex-col items-center gap-1">
                  <div className="text-xs h-5 text-center font-mono" style={{ minWidth: '3.5rem' }}>
                    {isBoth ? <span style={{ color: done ? 'var(--tier-3)' : '#a855f7' }}>🐢🐇</span>
                      : isSlow ? <span style={{ color: 'var(--accent)' }}>🐢</span>
                      : isFast ? <span style={{ color: '#f97316' }}>🐇</span>
                      : null}
                  </div>
                  <div style={nodeStyle} className="w-14 h-12 flex flex-col items-center justify-center border-2 rounded-lg text-sm">
                    <span style={{ color: 'var(--text)', fontFamily: 'var(--mono)', fontWeight: 700 }}>{val}</span>
                    <span style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>→{CYCLE_NEXT[i]}</span>
                  </div>
                  <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', textAlign: 'center', minWidth: '3.5rem' }}>[{i}]</div>
                </div>
                {i < CYCLE_NODES.length - 1 && (
                  <div style={{ color: 'var(--text-faint)', fontSize: '1.125rem' }} className="mx-0.5 mt-5">→</div>
                )}
              </div>
            );
          })}
          {/* Cycle back arrow label */}
          <div className="flex flex-col justify-center ml-2 mt-5">
            <div style={{ color: '#f97316', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>↩ cycle to node 2</div>
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
        <span className="flex items-center gap-1"><span style={{ width: '0.75rem', height: '0.75rem', borderRadius: '0.25rem', background: 'var(--accent)', display: 'inline-block' }} /> 🐢 slow</span>
        <span className="flex items-center gap-1"><span style={{ width: '0.75rem', height: '0.75rem', borderRadius: '0.25rem', background: '#f97316', display: 'inline-block' }} /> 🐇 fast</span>
        <span className="flex items-center gap-1"><span style={{ width: '0.75rem', height: '0.75rem', borderRadius: '0.25rem', background: 'var(--tier-3)', display: 'inline-block' }} /> meeting point</span>
      </div>

      {done
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>{state.msg}</div>
        : <div className="viz-info">{state.msg}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Merge Two Sorted Lists tab ─────────────────────────────────────────────────

interface MergeStep {
  p1: number;      // index into list1, -1 = exhausted
  p2: number;      // index into list2, -1 = exhausted
  result: number[];
  msg: string;
}

function buildMergeSteps(list1: number[], list2: number[]): MergeStep[] {
  const steps: MergeStep[] = [];
  const push = (p1: number, p2: number, result: number[], msg: string) =>
    steps.push({ p1, p2, result: [...result], msg });

  push(0, 0, [], `Start: p1 at list1[0]=${list1[0]}, p2 at list2[0]=${list2[0]}. Compare and take smaller.`);

  let p1 = 0, p2 = 0;
  const result: number[] = [];

  while (p1 < list1.length && p2 < list2.length) {
    if (list1[p1] <= list2[p2]) {
      result.push(list1[p1]);
      push(p1 + 1 < list1.length ? p1 + 1 : -1, p2,
        result, `list1[${p1}]=${list1[p1]} ≤ list2[${p2}]=${list2[p2]} → take ${list1[p1]} from list1, advance p1`);
      p1++;
    } else {
      result.push(list2[p2]);
      push(p1, p2 + 1 < list2.length ? p2 + 1 : -1,
        result, `list1[${p1}]=${list1[p1]} > list2[${p2}]=${list2[p2]} → take ${list2[p2]} from list2, advance p2`);
      p2++;
    }
  }

  while (p1 < list1.length) {
    result.push(list1[p1]);
    push(p1 + 1 < list1.length ? p1 + 1 : -1, -1,
      result, `list2 exhausted. Append list1[${p1}]=${list1[p1]}`);
    p1++;
  }

  while (p2 < list2.length) {
    result.push(list2[p2]);
    push(-1, p2 + 1 < list2.length ? p2 + 1 : -1,
      result, `list1 exhausted. Append list2[${p2}]=${list2[p2]}`);
    p2++;
  }

  push(-1, -1, result, `Merged! Result: [${result.join(', ')}]`);
  return steps;
}

const DEFAULT_L1 = [1, 3, 5];
const DEFAULT_L2 = [2, 4, 6];

function MergeListsTab() {
  const [input1, setInput1] = useState(DEFAULT_L1.join(', '));
  const [input2, setInput2] = useState(DEFAULT_L2.join(', '));
  const [list1, setList1] = useState(DEFAULT_L1);
  const [list2, setList2] = useState(DEFAULT_L2);
  const [steps, setSteps] = useState<MergeStep[]>(() => buildMergeSteps(DEFAULT_L1, DEFAULT_L2));
  const [stepIdx, setStepIdx] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const isDone = stepIdx >= steps.length - 1;
  const step = steps[stepIdx];

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    const l1 = input1.split(',').map(v => parseInt(v.trim())).filter(v => !isNaN(v));
    const l2 = input2.split(',').map(v => parseInt(v.trim())).filter(v => !isNaN(v));
    const nl1 = l1.length ? l1 : DEFAULT_L1;
    const nl2 = l2.length ? l2 : DEFAULT_L2;
    setList1(nl1); setList2(nl2);
    setSteps(buildMergeSteps(nl1, nl2));
    setStepIdx(0);
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    setStepIdx(i => Math.min(steps.length - 1, i + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setStepIdx(i => Math.max(0, i - 1));
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

  const nodeBox = (val: number, highlight: 'p1' | 'p2' | 'done' | 'none') => {
    const styles: Record<typeof highlight, React.CSSProperties> = {
      p1: { background: 'var(--accent-soft)', borderColor: 'var(--accent)' },
      p2: { background: 'color-mix(in srgb, #eab308 20%, transparent)', borderColor: '#eab308' },
      done: { background: 'var(--surface-sunken)', borderColor: 'var(--border)', opacity: 0.4 },
      none: { background: 'var(--surface-raised)', borderColor: 'var(--border)' },
    };
    return (
      <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm"
        style={{ color: 'var(--text)', ...styles[highlight] }}>
        {val}
      </div>
    );
  };

  return (
    <div className="space-y-6">
      <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>
        Dummy head + two pointers. Compare heads, attach smaller, advance that pointer.
      </p>

      <div className="flex flex-wrap gap-3">
        {[['List 1', input1, setInput1], ['List 2', input2, setInput2]].map(([label, val, set]) => (
          <div key={label as string} className="flex-1 min-w-32">
            <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>{label as string} (comma separated)</label>
            <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
              value={val as string} onChange={e => (set as (v: string) => void)(e.target.value)} />
          </div>
        ))}
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      {/* List 1 */}
      <div>
        <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem', fontFamily: 'var(--mono)' }}>
          List 1 <span style={{ color: 'var(--accent)' }}>(p1{step.p1 === -1 ? '=exhausted' : `→[${step.p1}]`})</span>
        </div>
        <div className="flex items-center gap-1 flex-wrap">
          {list1.map((v, i) => {
            const highlight = step.p1 === i ? 'p1' : step.p1 === -1 || i < step.p1 ? 'done' : 'none';
            return (
              <div key={i} className="flex items-center">
                {nodeBox(v, highlight)}
                {i < list1.length - 1 && <span style={{ color: 'var(--text-faint)', margin: '0 2px' }}>→</span>}
              </div>
            );
          })}
          <span style={{ color: 'var(--text-faint)', fontFamily: 'var(--mono)', fontSize: '0.875rem', marginLeft: '4px' }}>→ null</span>
        </div>
      </div>

      {/* List 2 */}
      <div>
        <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem', fontFamily: 'var(--mono)' }}>
          List 2 <span style={{ color: '#eab308' }}>(p2{step.p2 === -1 ? '=exhausted' : `→[${step.p2}]`})</span>
        </div>
        <div className="flex items-center gap-1 flex-wrap">
          {list2.map((v, i) => {
            const highlight = step.p2 === i ? 'p2' : step.p2 === -1 || i < step.p2 ? 'done' : 'none';
            return (
              <div key={i} className="flex items-center">
                {nodeBox(v, highlight)}
                {i < list2.length - 1 && <span style={{ color: 'var(--text-faint)', margin: '0 2px' }}>→</span>}
              </div>
            );
          })}
          <span style={{ color: 'var(--text-faint)', fontFamily: 'var(--mono)', fontSize: '0.875rem', marginLeft: '4px' }}>→ null</span>
        </div>
      </div>

      {/* Result */}
      <div>
        <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem', fontFamily: 'var(--mono)' }}>Result</div>
        <div className="flex items-center gap-1 flex-wrap min-h-12">
          {step.result.length === 0
            ? <span style={{ color: 'var(--text-faint)', fontFamily: 'var(--mono)', fontSize: '0.875rem' }}>[ empty ]</span>
            : step.result.map((v, i) => (
                <div key={i} className="flex items-center">
                  <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm"
                    style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', borderColor: 'var(--tier-3)', color: 'var(--text)' }}>
                    {v}
                  </div>
                  {i < step.result.length - 1 && <span style={{ color: 'var(--text-faint)', margin: '0 2px' }}>→</span>}
                </div>
              ))}
        </div>
      </div>

      {isDone
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>{step.msg}</div>
        : <div className="viz-info">{step.msg}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={stepIdx === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={isDone} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root component ─────────────────────────────────────────────────────────────

type Tab = 'Reversal' | 'Cycle Detection' | 'Merge Lists';
const TABS: Tab[] = ['Reversal', 'Cycle Detection', 'Merge Lists'];

export default function LinkedListViz() {
  const [tab, setTab] = useState<Tab>('Reversal');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Linked List</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Three-pointer reversal · Floyd's cycle detection · Merge two sorted lists</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2 flex-wrap">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={tab === t ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t}
          </button>
        ))}
      </div>

      {tab === 'Reversal' ? <ReversalTab /> : tab === 'Cycle Detection' ? <CycleDetectionTab /> : <MergeListsTab />}
    </div>
  );
}
