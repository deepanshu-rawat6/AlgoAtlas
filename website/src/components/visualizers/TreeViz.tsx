import { useState } from 'react';

// Tree: [3, 9, 20, null, null, 15, 7]
// Index:  0   1   2     3     4   5   6
const TREE = [3, 9, 20, null, null, 15, 7];

const W = 500, H = 200, R = 18;

// Absolute x,y positions for each node index in a 500×200 viewBox
const POS: Record<number, [number, number]> = {
  0: [250, 30],
  1: [120, 90],  2: [380, 90],
  3: [55,  160], 4: [185, 160], 5: [315, 160], 6: [445, 160],
};

// Only draw edges where both parent and child have non-null values
const EDGES = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]].filter(
  ([a, b]) => TREE[a] !== null && TREE[b] !== null
);

export default function TreeViz() {
  const [mode, setMode] = useState<'bfs'|'dfs'>('bfs');
  const [visited, setVisited] = useState<number[]>([]);
  const [queue, setQueue] = useState<number[]>([]);
  const [levels, setLevels] = useState<number[][]>([]);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [msg, setMsg] = useState('Select BFS or DFS, then press "Start".');

  function reset() {
    setVisited([]); setQueue([]); setLevels([]); setStarted(false); setDone(false);
    setMsg('Select BFS or DFS, then press "Start".');
  }

  function start() {
    setVisited([]); setLevels([]); setStarted(true); setDone(false);
    if (mode === 'bfs') {
      setQueue([0]);
      setMsg('BFS: enqueue root(3). Press "Next Step".');
    } else {
      setQueue([0]);
      setMsg('DFS preorder: push root(3) onto stack. Press "Next Step".');
    }
  }

  function nextStep() {
    if (!started || done || queue.length === 0) return;

    if (mode === 'bfs') {
      const nextQ: number[] = [];
      const levelNodes: number[] = [];
      for (const idx of queue) {
        if (TREE[idx] == null) continue;
        levelNodes.push(idx);
        const l = 2*idx+1, r = 2*idx+2;
        if (l < TREE.length && TREE[l] != null) nextQ.push(l);
        if (r < TREE.length && TREE[r] != null) nextQ.push(r);
      }
      const newVisited = [...visited, ...levelNodes];
      setVisited(newVisited);
      setLevels(prev => [...prev, levelNodes]);
      setQueue(nextQ);
      const vals = levelNodes.map(i => TREE[i]).join(', ');
      if (nextQ.length === 0) {
        setDone(true);
        setMsg(`Level ${levels.length}: [${vals}] — BFS complete! Order: [${newVisited.map(i => TREE[i]).join(', ')}]`);
      } else {
        setMsg(`Level ${levels.length}: [${vals}] → enqueue [${nextQ.map(i => TREE[i]).join(', ')}]`);
      }
    } else {
      const stack = [...queue];
      const idx = stack.pop()!;
      const newVisited = [...visited, idx];
      setVisited(newVisited);
      // Push right then left so left is processed first
      const r = 2*idx+2, l = 2*idx+1;
      if (r < TREE.length && TREE[r] != null) stack.push(r);
      if (l < TREE.length && TREE[l] != null) stack.push(l);
      setQueue(stack);
      if (stack.length === 0) {
        setDone(true);
        setMsg(`Visit ${TREE[idx]} — DFS complete! Preorder: [${newVisited.map(i => TREE[i]).join(', ')}]`);
      } else {
        setMsg(`Visit ${TREE[idx]} → stack: [${stack.map(i => TREE[i]).join(', ')}]`);
      }
    }
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Tree Traversal</h3>
        <p className="text-sm text-slate-400">BFS level-order or DFS preorder on a binary tree</p>
      </div>

      <div className="flex gap-3 items-center">
        {(['bfs','dfs'] as const).map(m => (
          <button key={m} onClick={() => { setMode(m); reset(); }}
            className={`px-4 py-2 rounded-lg text-sm font-medium border ${mode === m ? 'bg-blue-700 border-blue-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>
            {m.toUpperCase()}
          </button>
        ))}
        {!started
          ? <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm font-medium rounded-lg">Start</button>
          : <button onClick={reset} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded-lg">Reset</button>
        }
      </div>

      {/* SVG Tree — all absolute coords in a 500×200 viewBox */}
      <div className="bg-slate-900/60 rounded-lg p-3">
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" style={{ maxHeight: 220 }}>
          {/* Edges first so they render behind nodes */}
          {EDGES.map(([a, b]) => (
            <line key={`${a}-${b}`}
              x1={POS[a][0]} y1={POS[a][1] + R}
              x2={POS[b][0]} y2={POS[b][1] - R}
              stroke="#334155" strokeWidth="2" />
          ))}

          {/* Nodes */}
          {TREE.map((val, i) => {
            if (val == null || !POS[i]) return null;
            const isVisited = visited.includes(i);
            const inQueue  = queue.includes(i);
            const fill   = isVisited ? '#1d4ed8' : inQueue ? '#854d0e' : '#1e293b';
            const stroke = isVisited ? '#60a5fa' : inQueue ? '#fbbf24' : '#475569';
            return (
              <g key={i}>
                <circle cx={POS[i][0]} cy={POS[i][1]} r={R} fill={fill} stroke={stroke} strokeWidth="2" />
                <text x={POS[i][0]} y={POS[i][1] + 5} textAnchor="middle" fill="white" fontSize="13" fontWeight="bold">{val}</text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* Visit order */}
      {visited.length > 0 && (
        <div className="flex gap-2 flex-wrap items-center">
          <span className="text-xs text-slate-500">Visited:</span>
          {visited.map((i, idx) => (
            <span key={idx} className="bg-blue-900/50 border border-blue-700 px-2 py-0.5 rounded text-sm font-mono text-blue-300">{TREE[i]}</span>
          ))}
        </div>
      )}

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>

      <button onClick={nextStep} disabled={!started || done}
        className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
        Next Step
      </button>
    </div>
  );
}
