import { useState } from 'react';

interface Node { path: number[]; idx: number; id: string; parentId: string | null; }

function generateSteps(nums: number[]): Node[] {
  const steps: Node[] = [];
  function bt(path: number[], idx: number, parentId: string | null) {
    const id = path.join(',') + '@' + idx;
    steps.push({ path: [...path], idx, id, parentId });
    for (let i = idx; i < nums.length; i++) {
      path.push(nums[i]);
      bt(path, i + 1, id);
      path.pop();
    }
  }
  bt([], 0, null);
  return steps;
}

export default function BacktrackingViz() {
  const [input, setInput] = useState('1, 2, 3');
  const [steps, setSteps] = useState<Node[]>([]);
  const [curr, setCurr] = useState(-1);
  const [started, setStarted] = useState(false);

  const nums = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n)).slice(0, 4);

  function start() {
    const s = generateSteps(nums);
    setSteps(s); setCurr(0); setStarted(true);
  }

  function next() { if (curr < steps.length - 1) setCurr(c => c + 1); }
  function prev() { if (curr > 0) setCurr(c => c - 1); }

  const visible = steps.slice(0, curr + 1);
  const current = steps[curr];
  const leaves = visible.filter(n => {
    const isLeaf = !visible.some(m => m.parentId === n.id);
    return isLeaf;
  });

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Backtracking — Subsets</h3>
        <p className="text-sm text-slate-400">Choose / Explore / Unchoose recursion tree</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (max 4 elements)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
        </div>
      </div>

      {/* Recursion tree as cards */}
      {started && (
        <div className="overflow-y-auto max-h-80 space-y-1">
          {visible.map((node, idx) => {
            const isCurr = node.id === current?.id;
            const depth = node.path.length;
            return (
              <div key={node.id} className={`flex items-center gap-2 py-1 px-2 rounded ${isCurr ? 'bg-yellow-900/50 border border-yellow-700' : 'bg-slate-800/40'}`}
                style={{ marginLeft: depth * 20 }}>
                <span className="font-mono text-sm text-slate-300">
                  [{node.path.join(', ')}]
                </span>
                {depth === nums.length && <span className="text-xs text-green-400 ml-1">← leaf subset ✓</span>}
                {isCurr && <span className="text-xs text-yellow-400 ml-auto">← current</span>}
              </div>
            );
          })}
        </div>
      )}

      {/* Collected subsets */}
      {leaves.length > 0 && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3">
          <div className="text-xs text-slate-500 mb-2">Subsets found so far:</div>
          <div className="flex flex-wrap gap-2">
            {leaves.map(n => (
              <span key={n.id} className="bg-green-900/40 border border-green-800 px-2 py-1 rounded text-sm font-mono text-green-300">
                [{n.path.join(', ') || '∅'}]
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="flex gap-3">
        <button onClick={prev} disabled={!started || curr <= 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm font-medium rounded-lg">← Prev</button>
        <button onClick={next} disabled={!started || curr >= steps.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">Next →</button>
        {started && <span className="text-xs text-slate-500 self-center">{curr + 1} / {steps.length} nodes</span>}
      </div>
    </div>
  );
}
