import { useState } from 'react';

interface Call { id: string; n: number; result: number | null; parentId: string | null; depth: number; }

function buildCalls(n: number): Call[] {
  const calls: Call[] = [];
  let idCounter = 0;
  function fib(n: number, parentId: string | null, depth: number): number {
    const id = String(idCounter++);
    calls.push({ id, n, result: null, parentId, depth });
    if (n <= 1) { calls[calls.length - 1].result = n; return n; }
    const l = fib(n - 1, id, depth + 1);
    const r = fib(n - 2, id, depth + 1);
    const res = l + r;
    calls.find(c => c.id === id)!.result = res;
    return res;
  }
  fib(n, null, 0);
  return calls;
}

export default function RecursionViz() {
  const [n, setN] = useState(5);
  const [calls, setCalls] = useState<Call[]>([]);
  const [step, setStep] = useState(-1);
  const [started, setStarted] = useState(false);

  function start() {
    const c = buildCalls(Math.min(n, 7));
    setCalls(c); setStep(0); setStarted(true);
  }

  function next() { if (step < calls.length - 1) setStep(s => s + 1); }
  function prev() { if (step > 0) setStep(s => s - 1); }

  const visible = calls.slice(0, step + 1);
  const current = calls[step];

  const byDepth: Record<number, Call[]> = {};
  for (const c of visible) {
    byDepth[c.depth] = byDepth[c.depth] || [];
    byDepth[c.depth].push(c);
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Recursion Tree — Fibonacci</h3>
        <p className="text-sm text-slate-400">Visualize overlapping subproblems (why memoization helps)</p>
      </div>

      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block text-xs text-slate-400 mb-1">n (max 7)</label>
          <input type="number" min="1" max="7"
            className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={n} onChange={e => setN(Math.min(7, Math.max(1, parseInt(e.target.value) || 1)))} />
        </div>
        <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Build Tree</button>
      </div>

      {/* Recursion calls by depth */}
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

      <div className="flex gap-3">
        <button onClick={prev} disabled={!started || step <= 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
        <button onClick={next} disabled={!started || step >= calls.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
      </div>
    </div>
  );
}
