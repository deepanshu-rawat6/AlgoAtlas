import { useState } from 'react';

// ── Monotonic Stack tab ───────────────────────────────────────────────────────

const DEFAULT_TEMPS = [73, 74, 75, 71, 69, 72, 76, 73];

function MonotonicStackTab() {
  const [arrInput, setArrInput] = useState(DEFAULT_TEMPS.join(', '));
  const [i, setI] = useState(-1);
  const [stack, setStack] = useState<number[]>([]);
  const [result, setResult] = useState<number[]>([]);
  const [msg, setMsg] = useState('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));

  function reset() {
    setI(-1); setStack([]); setResult([]);
    setMsg('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');
  }

  function next() {
    const ni = i + 1;
    if (ni >= arr.length) return;
    const ns = [...stack], nr = [...result];
    const msgs: string[] = [];
    while (ns.length > 0 && arr[ns[ns.length - 1]] < arr[ni]) {
      const idx = ns.pop()!;
      nr[idx] = ni - idx;
      msgs.push(`Pop idx ${idx} (temp ${arr[idx]} < ${arr[ni]}), wait = ${ni - idx} days`);
    }
    ns.push(ni);
    msgs.push(`Push idx ${ni} (temp ${arr[ni]}) onto stack`);
    setI(ni); setStack(ns); setResult(nr); setMsg(msgs.join(' → '));
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Temperatures</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => setArrInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, idx) => {
          const isCurrent = idx === i;
          const inStack = stack.includes(idx);
          const isDone = result[idx] !== undefined;
          let bg = 'bg-slate-700 border-slate-600 text-slate-400';
          if (isCurrent) bg = 'bg-yellow-800 border-yellow-400 text-white';
          else if (inStack) bg = 'bg-blue-800 border-blue-500 text-white';
          else if (isDone) bg = 'bg-slate-600 border-slate-500 text-slate-300';
          return (
            <div key={idx} className="flex flex-col items-center gap-1">
              <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>{v}</div>
              <div className="text-xs text-center" style={{ minWidth: '3rem' }}>
                {result[idx] !== undefined ? <span className="text-green-400">{result[idx]}d</span> : <span className="text-slate-600">?</span>}
              </div>
              <div className="text-xs text-slate-600">[{idx}]</div>
            </div>
          );
        })}
      </div>

      <div className="flex items-end gap-2">
        <span className="text-xs text-slate-500 font-mono">Stack (indices):</span>
        <div className="flex gap-1">
          {stack.length === 0
            ? <span className="text-slate-600 text-sm">[ empty ]</span>
            : stack.map((idx, si) => (
                <span key={si} className="bg-blue-900/50 border border-blue-700 px-2 py-1 rounded text-sm font-mono text-blue-300">
                  {idx}({arr[idx]})
                </span>
              ))}
        </div>
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>

      <button onClick={next} disabled={i >= arr.length - 1}
        className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
        Next Step
      </button>
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
  const step = MIN_STEPS[stepIdx];

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">Auxiliary min-stack tracks current minimum at each level — O(1) getMin.</p>

      {/* Operations list */}
      <div className="flex flex-wrap gap-2">
        {MIN_OPS.map((op, i) => {
          const si = i + 1;
          const isActive = stepIdx === si;
          const isDone = stepIdx > si;
          let cls = 'bg-slate-700 border-slate-600 text-slate-400';
          if (isActive) cls = 'bg-yellow-800 border-yellow-400 text-white';
          else if (isDone) cls = 'bg-slate-600 border-slate-500 text-slate-300';
          return (
            <span key={i} className={`px-2 py-1 text-xs font-mono border rounded ${cls}`}>{opLabel(op)}</span>
          );
        })}
      </div>

      {/* Stacks side by side */}
      <div className="flex gap-8">
        {/* Main stack */}
        <div className="flex-1">
          <div className="text-xs text-slate-400 mb-2 font-mono">Main Stack</div>
          <div className="flex flex-col-reverse gap-1 min-h-16">
            {step.main.length === 0
              ? <span className="text-slate-600 text-xs font-mono">[ empty ]</span>
              : step.main.map((v, i) => {
                  const isTop = i === step.main.length - 1;
                  return (
                    <div key={i} className={`flex items-center justify-between px-3 py-1.5 rounded border font-mono text-sm ${isTop ? 'bg-blue-800 border-blue-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>
                      <span>{v}</span>
                      {isTop && <span className="text-xs text-blue-300 ml-2">← top</span>}
                    </div>
                  );
                })}
          </div>
        </div>

        {/* Min stack */}
        <div className="flex-1">
          <div className="text-xs text-slate-400 mb-2 font-mono">Min-Stack</div>
          <div className="flex flex-col-reverse gap-1 min-h-16">
            {step.minStack.length === 0
              ? <span className="text-slate-600 text-xs font-mono">[ empty ]</span>
              : step.minStack.map((v, i) => {
                  const isTop = i === step.minStack.length - 1;
                  return (
                    <div key={i} className={`flex items-center justify-between px-3 py-1.5 rounded border font-mono text-sm ${isTop ? 'bg-orange-800 border-orange-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>
                      <span>{v}</span>
                      {isTop && <span className="text-xs text-orange-300 ml-2">= min</span>}
                    </div>
                  );
                })}
          </div>
        </div>
      </div>

      {/* GetMin result */}
      {step.getMinResult !== null && (
        <div className="bg-green-900/40 border border-green-700 rounded-lg px-4 py-2 text-sm font-mono text-green-300">
          GetMin → {step.getMinResult}
        </div>
      )}

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{step.msg}</div>

      <div className="flex gap-3">
        <button onClick={() => setStepIdx(s => Math.max(0, s - 1))} disabled={stepIdx === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          ← Prev
        </button>
        <button onClick={() => setStepIdx(s => Math.min(MIN_STEPS.length - 1, s + 1))} disabled={stepIdx === MIN_STEPS.length - 1}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next →
        </button>
      </div>
    </div>
  );
}

// ── Root component ─────────────────────────────────────────────────────────────

type Tab = 'Monotonic Stack' | 'Min Stack';
const TABS: Tab[] = ['Monotonic Stack', 'Min Stack'];

export default function StackViz() {
  const [tab, setTab] = useState<Tab>('Monotonic Stack');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Stack</h3>
        <p className="text-sm text-slate-400">Monotonic stack · Min stack O(1) getMin</p>
      </div>

      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)}
            className={`px-3 py-1.5 text-xs font-medium rounded border transition-colors ${tab === t ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`}>
            {t}
          </button>
        ))}
      </div>

      {tab === 'Monotonic Stack' ? <MonotonicStackTab /> : <MinStackTab />}
    </div>
  );
}
