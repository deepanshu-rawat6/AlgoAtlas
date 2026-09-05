import { useState, useRef, useEffect } from 'react';

// ── Grid BFS/DFS ────────────────────────────────────────────────────────────
const ROWS = 6, COLS = 6;
const DIRS = [[0,1],[0,-1],[1,0],[-1,0]];
const LEVEL_COLORS = [
  'bg-yellow-500','bg-orange-500','bg-red-500','bg-pink-500',
  'bg-purple-500','bg-indigo-500','bg-blue-500','bg-cyan-500',
  'bg-teal-500','bg-green-500',
];

type GridMode = 'bfs' | 'dfs';
type CellState = { order: number; level: number; visited: boolean };

function makeGrid(): CellState[][] {
  return Array.from({ length: ROWS }, () =>
    Array.from({ length: COLS }, () => ({ order: -1, level: -1, visited: false }))
  );
}

interface GridSnapshot {
  grid: CellState[][];
  frontier: [number,number][];
  visitOrder: number;
  done: boolean;
  message: string;
  currentLevel: number;
}

function GridTab() {
  const [mode, setMode] = useState<GridMode>('bfs');
  const [grid, setGrid] = useState<CellState[][]>(makeGrid);
  const [frontier, setFrontier] = useState<[number,number][]>([]);
  const [visitOrder, setVisitOrder] = useState(0);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [message, setMessage] = useState('Click a cell to set the start point.');
  const [currentLevel, setCurrentLevel] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [gridHistory, setGridHistory] = useState<GridSnapshot[]>([]);
  const nextStepRef = useRef<() => void>(() => {});

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function handleCellClick(r: number, c: number) {
    if (started) return;
    const g = makeGrid();
    g[r][c] = { order: 0, level: 0, visited: true };
    setGrid(g);
    setFrontier([[r, c]]);
    setStarted(true);
    setDone(false);
    setVisitOrder(1);
    setCurrentLevel(0);
    setGridHistory([]);
    setMessage(`Start: (${r},${c}). Press "Next Step" to expand ${mode.toUpperCase()}.`);
  }

  function nextStep() {
    if (!started || done || frontier.length === 0) return;
    setGridHistory(h => [...h, { grid: grid.map(row => row.map(c => ({ ...c }))), frontier: [...frontier], visitOrder, done, message, currentLevel }]);
    if (mode === 'bfs') {
      const g = grid.map(row => row.map(c => ({ ...c })));
      const nextFrontier: [number,number][] = [];
      const level = currentLevel + 1;
      let order = visitOrder;
      for (const [r, c] of frontier) {
        for (const [dr, dc] of DIRS) {
          const nr = r + dr, nc = c + dc;
          if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && !g[nr][nc].visited) {
            g[nr][nc] = { order: order++, level, visited: true };
            nextFrontier.push([nr, nc]);
          }
        }
      }
      setGrid(g); setCurrentLevel(level); setVisitOrder(order);
      if (nextFrontier.length === 0) {
        setFrontier([]); setDone(true);
        setMessage(`BFS complete! Visited ${order - 1} cells in ${level} levels.`);
      } else {
        setFrontier(nextFrontier);
        setMessage(`Level ${level}: visited ${nextFrontier.length} new cell(s).`);
      }
    } else {
      const stack = [...frontier];
      const [r, c] = stack.pop()!;
      const g = grid.map(row => row.map(cell => ({ ...cell })));
      let order = visitOrder;
      if (!g[r][c].visited || g[r][c].order === -1) {
        g[r][c] = { order: order++, level: 0, visited: true };
      }
      for (const [dr, dc] of [...DIRS].reverse()) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && !g[nr][nc].visited) {
          if (!stack.some(([sr, sc]) => sr === nr && sc === nc)) {
            stack.push([nr, nc]);
            g[nr][nc] = { order: -1, level: 1, visited: true };
          }
        }
      }
      setGrid(g); setFrontier(stack); setVisitOrder(order);
      if (stack.length === 0) {
        setDone(true);
        setMessage(`DFS complete! Visited ${order - 1} cells. Stack empty.`);
      } else {
        setMessage(`DFS: visited (${r},${c}). Stack size: ${stack.length}. Next: (${stack[stack.length-1][0]},${stack[stack.length-1][1]})`);
      }
    }
  }

  function reset() {
    stopPlay();
    setGrid(makeGrid()); setFrontier([]); setStarted(false); setDone(false);
    setVisitOrder(0); setCurrentLevel(0); setGridHistory([]);
    setMessage('Click a cell to set the start point.');
  }

  function stepBack() {
    if (playing) stopPlay();
    if (gridHistory.length === 0) return;
    const prev = [...gridHistory];
    const snap = prev.pop()!;
    setGrid(snap.grid);
    setFrontier(snap.frontier);
    setVisitOrder(snap.visitOrder);
    setDone(snap.done);
    setMessage(snap.message);
    setCurrentLevel(snap.currentLevel);
    setGridHistory(prev);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => { nextStepRef.current = nextStep; });
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const gridMountedRef = useRef(false);
  useEffect(() => {
    if (!gridMountedRef.current) { gridMountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }, [speed]);

  function switchMode(m: GridMode) { setMode(m); reset(); }

  return (
    <div className="space-y-6">
      <div className="flex gap-2">
        {(['bfs', 'dfs'] as GridMode[]).map(m => (
          <button key={m} onClick={() => switchMode(m)}
            className={`px-4 py-2 rounded-lg text-sm font-medium border transition-colors ${mode === m ? 'bg-blue-700 border-blue-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-300 hover:bg-slate-600'}`}>
            {m.toUpperCase()}
          </button>
        ))}
        <span className="text-xs text-slate-500 self-center ml-2">
          {mode === 'bfs' ? 'Queue — expands level by level' : 'Stack — goes deep before wide'}
        </span>
      </div>
      <div className="inline-block">
        {grid.map((row, r) => (
          <div key={r} className="flex gap-1 mb-1">
            {row.map((cell, c) => {
              const inFrontier = frontier.some(([fr, fc]) => fr === r && fc === c);
              let colorClass = 'bg-slate-700';
              if (cell.visited) {
                colorClass = mode === 'bfs'
                  ? LEVEL_COLORS[cell.level % LEVEL_COLORS.length]
                  : cell.order >= 0 ? 'bg-blue-600' : 'bg-yellow-600';
              }
              return (
                <button key={c} onClick={() => handleCellClick(r, c)}
                  className={`w-12 h-12 rounded-lg border-2 text-xs font-bold transition-all ${colorClass} ${inFrontier ? 'border-white scale-105' : 'border-transparent'} ${!started ? 'cursor-pointer hover:bg-slate-600' : 'cursor-default'} ${cell.visited ? 'text-white' : 'text-slate-500'}`}>
                  {cell.visited && cell.order >= 0 ? cell.order : ''}
                </button>
              );
            })}
          </div>
        ))}
      </div>
      <div className="flex gap-4 flex-wrap text-xs text-slate-400">
        {mode === 'bfs' ? (
          <>
            {LEVEL_COLORS.slice(0, 4).map((c, i) => (
              <span key={i} className="flex items-center gap-1">
                <span className={`inline-block w-3 h-3 rounded ${c}`}></span> Level {i}
              </span>
            ))}
            <span className="text-slate-500">number = visit order within level</span>
          </>
        ) : (
          <>
            <span className="flex items-center gap-1"><span className="inline-block w-3 h-3 rounded bg-yellow-600"></span> In stack</span>
            <span className="flex items-center gap-1"><span className="inline-block w-3 h-3 rounded bg-blue-600"></span> Processed</span>
            <span className="text-slate-500">number = visit order</span>
          </>
        )}
      </div>
      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm text-slate-300 font-mono min-h-12">{message}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={!started || done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={stepBack} disabled={gridHistory.length === 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={!started || done}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">Reset</button>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Dijkstra ────────────────────────────────────────────────────────────────
// Nodes: A=0 B=1 C=2 D=3 E=4  (circular layout in 320×200 SVG)
const LABELS = ['A','B','C','D','E'];
const NODE_POS: [number,number][] = [
  [160, 30],  // A - top
  [290, 110], // B - right
  [50,  110], // C - left
  [230, 185], // D - bottom-right
  [90,  185], // E - bottom-left
];
// [from, to, weight]
const WEIGHTED_EDGES: [number,number,number][] = [
  [0,1,4],[0,2,2],[1,2,1],[1,3,5],[2,3,8],[2,4,10],[3,4,2],
];

// Adjacency list
const ADJ: [number,number][][] = LABELS.map(() => []);
for (const [u,v,w] of WEIGHTED_EDGES) { ADJ[u].push([v,w]); ADJ[v].push([u,w]); }

interface DijkStep {
  dist: number[];
  visited: boolean[];
  current: number;
  updated: number[];
  msg: string;
}

function buildDijkstraSteps(): DijkStep[] {
  const INF = Infinity;
  const dist = [0, INF, INF, INF, INF];
  const visited = [false,false,false,false,false];
  const steps: DijkStep[] = [];

  steps.push({ dist: [...dist], visited: [...visited], current: -1, updated: [], msg: 'Start: dist[A]=0, all others=∞. Press Next.' });

  for (let iter = 0; iter < 5; iter++) {
    // Pick unvisited node with min dist
    let u = -1;
    for (let i = 0; i < 5; i++) {
      if (!visited[i] && (u === -1 || dist[i] < dist[u])) u = i;
    }
    if (u === -1 || dist[u] === INF) break;
    visited[u] = true;
    const updated: number[] = [];
    for (const [v, w] of ADJ[u]) {
      if (!visited[v] && dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
        updated.push(v);
      }
    }
    steps.push({
      dist: [...dist], visited: [...visited], current: u, updated,
      msg: `Pick ${LABELS[u]} (dist=${dist[u]}). Update neighbors: ${updated.length ? updated.map(v => `${LABELS[v]}→${dist[v]}`).join(', ') : 'none'}.`,
    });
  }
  steps.push({ dist: [...dist], visited: [...visited], current: -1, updated: [], msg: `Done! Shortest distances from A: ${dist.map((d,i) => `${LABELS[i]}=${d}`).join(', ')}.` });
  return steps;
}

const DIJKSTRA_STEPS = buildDijkstraSteps();

function DijkstraTab() {
  const [step, setStep] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setStep(s => { if (s >= DIJKSTRA_STEPS.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const dijkMountedRef = useRef(false);
  useEffect(() => {
    if (!dijkMountedRef.current) { dijkMountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => {
      setStep(s => { if (s >= DIJKSTRA_STEPS.length - 1) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }, [speed]);

  const s = DIJKSTRA_STEPS[step];
  const INF = Infinity;

  function nodeColor(i: number) {
    if (s.current === i) return '#ca8a04';   // yellow
    if (s.visited[i])   return '#1d4ed8';   // blue
    if (s.updated.includes(i)) return '#16a34a'; // green
    return '#1e293b'; // slate
  }
  function nodeStroke(i: number) {
    if (s.current === i) return '#fbbf24';
    if (s.visited[i])   return '#60a5fa';
    if (s.updated.includes(i)) return '#4ade80';
    return '#475569';
  }

  return (
    <div className="space-y-6">
      <div className="bg-slate-900/60 rounded-lg p-3">
        <svg viewBox="0 0 320 210" className="w-full" style={{ maxHeight: 220 }}>
          {/* Edges */}
          {WEIGHTED_EDGES.map(([u,v,w], idx) => {
            const [x1,y1] = NODE_POS[u], [x2,y2] = NODE_POS[v];
            const mx = (x1+x2)/2, my = (y1+y2)/2;
            return (
              <g key={idx}>
                <line x1={x1} y1={y1} x2={x2} y2={y2} stroke="#334155" strokeWidth="2" />
                <text x={mx} y={my-4} textAnchor="middle" fill="#94a3b8" fontSize="11">{w}</text>
              </g>
            );
          })}
          {/* Nodes */}
          {LABELS.map((lbl, i) => (
            <g key={i}>
              <circle cx={NODE_POS[i][0]} cy={NODE_POS[i][1]} r={18} fill={nodeColor(i)} stroke={nodeStroke(i)} strokeWidth="2.5" />
              <text x={NODE_POS[i][0]} y={NODE_POS[i][1]+5} textAnchor="middle" fill="white" fontSize="13" fontWeight="bold">{lbl}</text>
            </g>
          ))}
        </svg>
      </div>

      {/* Distance table */}
      <div className="flex gap-2 flex-wrap">
        {LABELS.map((lbl, i) => (
          <div key={i} className={`flex flex-col items-center rounded-lg border px-3 py-2 min-w-12 ${s.current===i ? 'border-yellow-500 bg-yellow-900/30' : s.visited[i] ? 'border-blue-600 bg-blue-900/30' : s.updated.includes(i) ? 'border-green-600 bg-green-900/30' : 'border-slate-600 bg-slate-800'}`}>
            <span className="text-xs text-slate-400">{lbl}</span>
            <span className="text-sm font-bold text-slate-100">{s.dist[i] === INF ? '∞' : s.dist[i]}</span>
          </div>
        ))}
      </div>

      {/* Legend */}
      <div className="flex gap-4 text-xs text-slate-400 flex-wrap">
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-yellow-600 inline-block"></span>Current</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-blue-700 inline-block"></span>Visited</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-green-700 inline-block"></span>Updated</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-slate-700 inline-block"></span>Unvisited</span>
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300 min-h-12">{s.msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStep(s => Math.min(DIJKSTRA_STEPS.length-1, s+1))} disabled={step===DIJKSTRA_STEPS.length-1}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={() => { if (playing) stopPlay(); setStep(s => Math.max(0, s-1)); }} disabled={step===0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm font-medium rounded-lg">← Back</button>
        <button onClick={togglePlay} disabled={step===DIJKSTRA_STEPS.length-1}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={() => { stopPlay(); setStep(0); }} className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-slate-200 text-sm font-medium rounded-lg">Reset</button>
        <span className="text-xs text-slate-500">{step+1}/{DIJKSTRA_STEPS.length}</span>
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Main component ───────────────────────────────────────────────────────────
type Tab = 'grid' | 'dijkstra';
const TABS: { id: Tab; label: string }[] = [
  { id: 'grid', label: 'Grid BFS/DFS' },
  { id: 'dijkstra', label: 'Dijkstra' },
];

export default function BFSViz() {
  const [tab, setTab] = useState<Tab>('grid');

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Graph Traversal</h3>
        <p className="text-sm text-slate-400">BFS, DFS, and Dijkstra's shortest path</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t.id} onClick={() => setTab(t.id)}
            className={`px-3 py-1.5 text-xs font-medium rounded border transition-colors ${tab === t.id ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600 hover:bg-slate-600'}`}>
            {t.label}
          </button>
        ))}
      </div>

      {tab === 'grid' ? <GridTab /> : <DijkstraTab />}
    </div>
  );
}
