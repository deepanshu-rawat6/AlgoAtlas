import { useState, useRef, useEffect } from 'react';

// ── Monotonic Stack tab ───────────────────────────────────────────────────────

const DEFAULT_TEMPS = [73, 74, 75, 71, 69, 72, 76, 73];

interface MonoSnap { i: number; stack: number[]; result: number[]; msg: string; }

function MonotonicStackTab() {
  const [arrInput, setArrInput] = useState(DEFAULT_TEMPS.join(', '));
  const [i, setI] = useState(-1);
  const [stack, setStack] = useState<number[]>([]);
  const [result, setResult] = useState<number[]>([]);
  const [msg, setMsg] = useState('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');
  const [history, setHistory] = useState<MonoSnap[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const isDone = i >= arr.length - 1;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setI(-1); setStack([]); setResult([]); setHistory([]);
    setMsg('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');
  }

  function nextStep() {
    const ni = i + 1;
    if (ni >= arr.length) { stopPlay(); return; }
    const ns = [...stack], nr = [...result];
    const msgs: string[] = [];
    while (ns.length > 0 && arr[ns[ns.length - 1]] < arr[ni]) {
      const idx = ns.pop()!;
      nr[idx] = ni - idx;
      msgs.push(`Pop idx ${idx} (temp ${arr[idx]} < ${arr[ni]}), wait = ${ni - idx} days`);
    }
    ns.push(ni);
    msgs.push(`Push idx ${ni} (temp ${arr[ni]}) onto stack`);
    setHistory(h => [...h, { i, stack, result, msg }]);
    setI(ni); setStack(ns); setResult(nr); setMsg(msgs.join(' → '));
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setI(s.i); setStack(s.stack); setResult(s.result); setMsg(s.msg);
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
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Temperatures</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={arrInput} onChange={e => setArrInput(e.target.value)} />
        </div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, idx) => {
          const isCurrent = idx === i;
          const inStack = stack.includes(idx);
          const isDoneIdx = result[idx] !== undefined;
          const cellStyle = isCurrent
            ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
            : inStack
              ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
              : isDoneIdx
                ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
                : {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
          return (
            <div key={idx} className="flex flex-col items-center gap-1">
              <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>{v}</div>
              <div className="text-xs text-center" style={{ minWidth: '3rem' }}>
                {result[idx] !== undefined
                  ? <span style={{color:'var(--tier-3)'}}>{result[idx]}d</span>
                  : <span style={{color:'var(--text-faint)'}}>?</span>}
              </div>
              <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{idx}]</div>
            </div>
          );
        })}
      </div>

      <div className="flex items-end gap-2">
        <span style={{color:'var(--text-faint)',fontSize:'0.75rem',fontFamily:'var(--mono)'}}>Stack (indices):</span>
        <div className="flex gap-1">
          {stack.length === 0
            ? <span style={{color:'var(--text-faint)',fontSize:'0.875rem'}}>[ empty ]</span>
            : stack.map((idx, si) => (
                <span key={si} style={{background:'var(--surface-raised)',border:'1px solid var(--border)',padding:'0.25rem 0.5rem',borderRadius:'0.25rem',fontSize:'0.875rem',fontFamily:'var(--mono)',color:'var(--accent)'}}>
                  {idx}({arr[idx]})
                </span>
              ))}
        </div>
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

// ── Min Stack tab ─────────────────────────────────────────────────────────────

type MinOp = { type: 'push'; val: number } | { type: 'pop' } | { type: 'getmin' };

const MIN_OPS: MinOp[] = [
  { type: 'push', val: 5 }, { type: 'push', val: 3 }, { type: 'push', val: 7 },
  { type: 'push', val: 1 }, { type: 'getmin' }, { type: 'pop' },
  { type: 'getmin' }, { type: 'push', val: 2 }, { type: 'getmin' },
];

function opLabel(op: MinOp) {
  if (op.type === 'push') return `Push(${op.val})`;
  if (op.type === 'pop') return 'Pop';
  return 'GetMin';
}

interface MinStackState {
  main: number[];
  minStack: number[];
  getMinResult: number | null;
  msg: string;
}

function buildMinSteps() {
  const steps: (MinStackState & { opIdx: number })[] = [];
  let main: number[] = [], minStack: number[] = [];

  steps.push({ opIdx: -1, main: [], minStack: [], getMinResult: null, msg: 'Initial state. main stack and min-stack are both empty.' });

  MIN_OPS.forEach((op, opIdx) => {
    main = [...main]; minStack = [...minStack];
    let getMinResult: number | null = null;
    let msg = '';
    if (op.type === 'push') {
      main.push(op.val);
      const newMin = minStack.length === 0 ? op.val : Math.min(op.val, minStack[minStack.length - 1]);
      minStack.push(newMin);
      msg = `Push(${op.val}): add ${op.val} to main. min-stack top = min(${op.val}, ${minStack.length > 1 ? minStack[minStack.length - 2] : '∞'}) = ${newMin}. min-stack[top] always = current minimum.`;
    } else if (op.type === 'pop') {
      const popped = main.pop();
      minStack.pop();
      msg = `Pop: removed ${popped} from main. Also pop min-stack. min-stack[top] always = current minimum.`;
    } else {
      getMinResult = minStack[minStack.length - 1] ?? null;
      msg = `GetMin → ${getMinResult}. min-stack[top] always = current minimum. O(1) lookup!`;
    }
    steps.push({ opIdx, main: [...main], minStack: [...minStack], getMinResult, msg });
  });

  return steps;
}

const MIN_STEPS = buildMinSteps();

function MinStackTab() {
  const [stepIdx, setStepIdx] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const step = MIN_STEPS[stepIdx];
  const isDone = stepIdx === MIN_STEPS.length - 1;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    setStepIdx(s => Math.min(MIN_STEPS.length - 1, s + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setStepIdx(s => Math.max(0, s - 1));
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
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Auxiliary min-stack tracks current minimum at each level — O(1) getMin.</p>

      {/* Operations list */}
      <div className="flex flex-wrap gap-2">
        {MIN_OPS.map((op, i) => {
          const si = i + 1;
          const isActive = stepIdx === si;
          const isDoneOp = stepIdx > si;
          const opStyle = isActive
            ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
            : isDoneOp
              ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
              : {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
          return (
            <span key={i} className="px-2 py-1 text-xs font-mono border rounded" style={opStyle}>{opLabel(op)}</span>
          );
        })}
      </div>

      {/* Stacks side by side */}
      <div className="flex gap-8">
        {/* Main stack */}
        <div className="flex-1">
          <div style={{color:'var(--text-dim)',fontSize:'0.75rem',marginBottom:'0.5rem',fontFamily:'var(--mono)'}}>Main Stack</div>
          <div className="flex flex-col-reverse gap-1 min-h-16">
            {step.main.length === 0
              ? <span style={{color:'var(--text-faint)',fontSize:'0.75rem',fontFamily:'var(--mono)'}}>[ empty ]</span>
              : step.main.map((v, i) => {
                  const isTop = i === step.main.length - 1;
                  return (
                    <div key={i} className="flex items-center justify-between px-3 py-1.5 rounded border font-mono text-sm"
                      style={isTop
                        ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
                        : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}}>
                      <span>{v}</span>
                      {isTop && <span style={{color:'var(--accent)',fontSize:'0.75rem',marginLeft:'0.5rem'}}>← top</span>}
                    </div>
                  );
                })}
          </div>
        </div>

        {/* Min stack */}
        <div className="flex-1">
          <div style={{color:'var(--text-dim)',fontSize:'0.75rem',marginBottom:'0.5rem',fontFamily:'var(--mono)'}}>Min-Stack</div>
          <div className="flex flex-col-reverse gap-1 min-h-16">
            {step.minStack.length === 0
              ? <span style={{color:'var(--text-faint)',fontSize:'0.75rem',fontFamily:'var(--mono)'}}>[ empty ]</span>
              : step.minStack.map((v, i) => {
                  const isTop = i === step.minStack.length - 1;
                  return (
                    <div key={i} className="flex items-center justify-between px-3 py-1.5 rounded border font-mono text-sm"
                      style={isTop
                        ? {background:'color-mix(in srgb, var(--accent) 20%, transparent)',borderColor:'var(--accent)',color:'var(--text)'}
                        : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}}>
                      <span>{v}</span>
                      {isTop && <span style={{color:'var(--accent)',fontSize:'0.75rem',marginLeft:'0.5rem'}}>= min</span>}
                    </div>
                  );
                })}
          </div>
        </div>
      </div>

      {/* GetMin result */}
      {step.getMinResult !== null && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          GetMin → {step.getMinResult}
        </div>
      )}

      <div className="viz-info">{step.msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          Next Step
        </button>
        <button onClick={stepBack} disabled={stepIdx === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
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

// ── Valid Parentheses tab ─────────────────────────────────────────────────────

type ParenAction = 'push' | 'pop' | 'mismatch' | 'exhausted' | 'done';
interface ParenStep { charIdx: number; stack: string[]; action: ParenAction; msg: string; }

const MATCHES: Record<string, string> = { ')': '(', ']': '[', '}': '{' };
const OPENS = new Set(['(', '[', '{']);

function buildParenSteps(input: string): ParenStep[] {
  const steps: ParenStep[] = [];
  const stack: string[] = [];
  let valid = true;
  for (let i = 0; i < input.length; i++) {
    const ch = input[i];
    if (OPENS.has(ch)) {
      stack.push(ch);
      steps.push({ charIdx: i, stack: [...stack], action: 'push', msg: `Push '${ch}' onto stack` });
    } else if (MATCHES[ch]) {
      if (stack.length === 0) {
        steps.push({ charIdx: i, stack: [], action: 'exhausted', msg: `Stack empty! No matching bracket for '${ch}' at pos ${i} → Invalid` });
        valid = false; break;
      } else if (stack[stack.length - 1] !== MATCHES[ch]) {
        steps.push({ charIdx: i, stack: [...stack], action: 'mismatch', msg: `Mismatch: top='${stack[stack.length - 1]}', expected '${MATCHES[ch]}' for '${ch}' → Invalid` });
        valid = false; break;
      } else {
        const popped = stack.pop()!;
        steps.push({ charIdx: i, stack: [...stack], action: 'pop', msg: `Match! Pop '${popped}' ← closed by '${ch}'` });
      }
    }
  }
  if (valid) {
    steps.push(stack.length === 0
      ? { charIdx: input.length, stack: [], action: 'done', msg: 'Stack empty → Valid ✓' }
      : { charIdx: input.length, stack: [...stack], action: 'exhausted', msg: 'Unclosed brackets remain → Invalid ✗' });
  }
  return steps;
}

function ValidParensTab() {
  const [input, setInput] = useState('({[]})');
  const [steps, setSteps] = useState<ParenStep[]>(() => buildParenSteps('({[]})'));
  const [stepIdx, setStepIdx] = useState(-1);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const step = stepIdx >= 0 ? steps[stepIdx] : null;
  const isDone = stepIdx === steps.length - 1 && stepIdx >= 0;
  const isInvalid = step && (step.action === 'mismatch' || step.action === 'exhausted');
  const isValid = step && step.action === 'done';

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setSteps(buildParenSteps(input));
    setStepIdx(-1);
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    setStepIdx(s => Math.min(steps.length - 1, s + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setStepIdx(s => Math.max(-1, s - 1));
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
    stopPlay(); setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }, [speed]); // eslint-disable-line react-hooks/exhaustive-deps

  const charIdx = step?.charIdx ?? -1;
  const stack = step?.stack ?? [];

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Input string</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={input} onChange={e => { setInput(e.target.value); setStepIdx(-1); setSteps(buildParenSteps(e.target.value)); }} />
        </div>
      </div>

      {/* Input character boxes */}
      <div className="flex flex-wrap gap-1">
        {input.split('').map((ch, idx) => {
          const isCurr = idx === charIdx;
          const isPast = stepIdx >= 0 && idx < charIdx;
          let cellStyle: React.CSSProperties;
          if (isCurr && isInvalid) cellStyle = {background:'color-mix(in srgb, #ef4444 20%, transparent)',borderColor:'#ef4444',color:'var(--text)'};
          else if (isCurr) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
          else if (isPast) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
          else cellStyle = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
          return (
            <div key={idx} className="w-10 h-10 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg" style={cellStyle}>{ch}</div>
          );
        })}
      </div>

      {/* Stack */}
      <div>
        <div style={{color:'var(--text-dim)',fontSize:'0.75rem',marginBottom:'0.5rem',fontFamily:'var(--mono)'}}>Stack (top on left)</div>
        <div className="flex gap-1">
          {stack.length === 0
            ? <span style={{color:'var(--text-faint)',fontSize:'0.875rem'}}>[ empty ]</span>
            : [...stack].reverse().map((ch, si) => {
                const isTop = si === 0;
                const topStyle: React.CSSProperties = isTop
                  ? (step?.action === 'pop' ? {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'}
                    : step?.action === 'push' ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
                    : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text)'})
                  : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
                return (
                  <div key={si} className="w-10 h-10 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg" style={topStyle}>{ch}</div>
                );
              })}
        </div>
      </div>

      {isValid && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          Valid ✓
        </div>
      )}
      {isInvalid && (
        <div style={{background:'color-mix(in srgb, #ef4444 15%, transparent)',border:'1px solid #ef4444',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'#ef4444',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          Invalid ✗
        </div>
      )}

      <div className="viz-info">{step?.msg ?? 'Press "Next Step" or "▶ Play" to start.'}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          Next Step
        </button>
        <button onClick={stepBack} disabled={stepIdx < 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">
          ← Back
        </button>
        <button onClick={togglePlay} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
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

// ── Root component ─────────────────────────────────────────────────────────────

type Tab = 'Monotonic Stack' | 'Min Stack' | 'Valid Parens';
const TABS: Tab[] = ['Monotonic Stack', 'Min Stack', 'Valid Parens'];

export default function StackViz() {
  const [tab, setTab] = useState<Tab>('Monotonic Stack');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Stack</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Monotonic stack · Min stack O(1) getMin · Valid parentheses matching</p>
      </div>

      <div className="flex gap-2 flex-wrap">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={tab === t ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t}
          </button>
        ))}
      </div>

      {tab === 'Monotonic Stack' ? <MonotonicStackTab /> : tab === 'Min Stack' ? <MinStackTab /> : <ValidParensTab />}
    </div>
  );
}
