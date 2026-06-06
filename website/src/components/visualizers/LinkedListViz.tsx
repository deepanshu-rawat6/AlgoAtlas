import { useState } from 'react';

const DEFAULT = [1, 2, 3, 4, 5];

interface NodeState { val: number; next: number | null; }

function buildList(vals: number[]): NodeState[] {
  return vals.map((val, i) => ({ val, next: i < vals.length - 1 ? i + 1 : null }));
}

interface State {
  nodes: NodeState[];
  prev: number | null;
  curr: number | null;
  step: number;
  done: boolean;
  msg: string;
}

function init(vals: number[]): State {
  const nodes = buildList(vals);
  return { nodes, prev: null, curr: 0, step: 0, done: false, msg: 'prev=null, curr=head(0). Press "Next Step" to reverse.' };
}

export default function LinkedListViz() {
  const [input, setInput] = useState(DEFAULT.join(' → '));
  const [state, setState] = useState<State>(() => init(DEFAULT));

  function reset() {
    const vals = input.split(/[→,\s]+/).map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setState(init(vals.length ? vals : DEFAULT));
  }

  function next() {
    setState(prev => {
      if (prev.done || prev.curr === null) return prev;
      const nodes = prev.nodes.map(n => ({ ...n }));
      const curr = prev.curr;
      const nextNode = nodes[curr].next;
      nodes[curr].next = prev.prev;
      return {
        nodes,
        prev: curr,
        curr: nextNode,
        step: prev.step + 1,
        done: nextNode === null,
        msg: nextNode === null
          ? `✓ Done! Reversed. New head = node(${curr}).`
          : `next=nodes[${nextNode}], nodes[${curr}].next → ${prev.prev === null ? 'null' : `nodes[${prev.prev}]`}, prev=nodes[${curr}], curr=nodes[${nextNode}]`,
      };
    });
  }

  const { nodes, prev: prevIdx, curr: currIdx, done, msg } = state;
  const n = nodes.length;
  const headIdx = done ? prevIdx : 0;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Linked List Reversal</h3>
        <p className="text-sm text-slate-400">Three pointers: prev, curr, next — O(n) in-place</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Values (space or → separated)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      {/* Node visualization */}
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
                    <span className="text-xs text-slate-400">→{pointsTo === null ? 'null' : node.val > 0 ? '' : ''}{pointsTo !== null ? `[${pointsTo}]` : 'null'}</span>
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

      <div className="flex gap-3">
        <button onClick={next} disabled={done} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
      </div>
    </div>
  );
}
