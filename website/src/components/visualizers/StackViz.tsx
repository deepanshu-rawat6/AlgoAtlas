import { useState } from 'react';

const DEFAULT = [73, 74, 75, 71, 69, 72, 76, 73];

export default function StackViz() {
  const [arrInput, setArrInput] = useState(DEFAULT.join(', '));
  const [i, setI] = useState(-1);
  const [stack, setStack] = useState<number[]>([]);
  const [result, setResult] = useState<number[]>([]);
  const [msg, setMsg] = useState('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const done = i >= arr.length - 1 && stack.length === 0 || (i >= arr.length);

  function reset() {
    setI(-1); setStack([]); setResult([]); 
    setMsg('Monotonic Decreasing Stack — Daily Temperatures. Press "Next Step".');
  }

  function next() {
    let ni = i, ns = [...stack], nr = [...result];
    const n = arr.length;

    // First pop all smaller from stack
    if (ns.length > 0 && ni >= 0 && ni < n && arr[ni + 1] !== undefined) {
      // If we just added current element and stack has elements to pop
    }

    ni = i + 1;
    if (ni >= n) return;

    const msgs: string[] = [];

    // Pop all indices from stack where arr[idx] < arr[ni]
    while (ns.length > 0 && arr[ns[ns.length - 1]] < arr[ni]) {
      const idx = ns.pop()!;
      if (!nr[idx]) nr[idx] = 0;
      nr[idx] = ni - idx;
      msgs.push(`Pop idx ${idx} (temp ${arr[idx]} < ${arr[ni]}), wait = ${ni - idx} days`);
    }

    ns.push(ni);
    msgs.push(`Push idx ${ni} (temp ${arr[ni]}) onto stack`);

    setI(ni);
    setStack(ns);
    setResult(nr);
    setMsg(msgs.join(' → '));
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Monotonic Stack — Daily Temperatures</h3>
        <p className="text-sm text-slate-400">Track next greater element using a decreasing stack of indices</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Temperatures</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => setArrInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      {/* Temperatures array */}
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

      {/* Stack visualization */}
      <div className="flex items-end gap-2">
        <span className="text-xs text-slate-500 font-mono">Stack (indices):</span>
        <div className="flex gap-1">
          {stack.length === 0
            ? <span className="text-slate-600 text-sm">[ empty ]</span>
            : stack.map((idx, si) => (
                <span key={si} className="bg-blue-900/50 border border-blue-700 px-2 py-1 rounded text-sm font-mono text-blue-300">
                  {idx}({arr[idx]})
                </span>
              ))
          }
        </div>
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>

      <div className="flex gap-3">
        <button onClick={next} disabled={i >= arr.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
      </div>
    </div>
  );
}
