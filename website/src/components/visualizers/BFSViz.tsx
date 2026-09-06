import { useState, useRef, useEffect } from 'react';

// ── Grid BFS/DFS ────────────────────────────────────────────────────────────
const ROWS = 6, COLS = 6;
const DIRS = [[0,1],[0,-1],[1,0],[-1,0]];
const LEVEL_COLORS_CSS = [
  '#eab308','#f97316','#ef4444','#ec4899',
  '#a855f7','#6366f1','#3b82f6','#06b6d4',
  '#14b8a6','#22c55e',
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
            className={mode === m ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {m.toUpperCase()}
          </button>
        ))}
        <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}} className="self-center ml-2">
          {mode === 'bfs' ? 'Queue — expands level by level' : 'Stack — goes deep before wide'}
        </span>
      </div>
      <div className="inline-block">
        {grid.map((row, r) => (
          <div key={r} className="flex gap-1 mb-1">
            {row.map((cell, c) => {
              const inFrontier = frontier.some(([fr, fc]) => fr === r && fc === c);
              let cellBg = 'var(--surface-sunken)';
              if (cell.visited) {
                cellBg = mode === 'bfs'
                  ? LEVEL_COLORS_CSS[cell.level % LEVEL_COLORS_CSS.length]
                  : cell.order >= 0 ? 'var(--accent)' : '#ca8a04';
              }
              return (
                <button key={c} onClick={() => handleCellClick(r, c)}
                  className={`w-12 h-12 rounded-lg border-2 text-xs font-bold transition-all ${inFrontier ? 'scale-105' : ''} ${!started ? 'cursor-pointer' : 'cursor-default'}`}
                  style={{background:cellBg, borderColor:inFrontier?'var(--text)':'transparent', color:cell.visited?'var(--text)':'var(--text-faint)'}}>
                  {cell.visited && cell.order >= 0 ? cell.order : ''}
                </button>
              );
            })}
          </div>
        ))}
      </div>
      <div className="flex gap-4 flex-wrap text-xs" style={{color:'var(--text-dim)'}}>
        {mode === 'bfs' ? (
          <>
            {LEVEL_COLORS_CSS.slice(0, 4).map((c, i) => (
              <span key={i} className="flex items-center gap-1">
                <span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'0.25rem',background:c}}></span> Level {i}
              </span>
            ))}
            <span style={{color:'var(--text-faint)'}}>number = visit order within level</span>
          </>
        ) : (
          <>
            <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'0.25rem',background:'#ca8a04'}}></span> In stack</span>
            <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'0.25rem',background:'var(--accent)'}}></span> Processed</span>
            <span style={{color:'var(--text-faint)'}}>number = visit order</span>
          </>
        )}
      </div>
      <div className="viz-info">{message}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={!started || done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={gridHistory.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={!started || done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
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
    if (s.current === i) return 'var(--accent-soft)';
    if (s.visited[i])   return 'var(--accent)';
    if (s.updated.includes(i)) return 'var(--tier-3)';
    return 'var(--surface-raised)';
  }
  function nodeStroke(i: number) {
    if (s.current === i) return 'var(--accent)';
    if (s.visited[i])   return 'var(--accent)';
    if (s.updated.includes(i)) return 'var(--tier-3)';
    return 'var(--border)';
  }

  return (
    <div className="space-y-6">
      <div className="panel p-3">
        <svg viewBox="0 0 320 210" className="w-full" style={{ maxHeight: 220 }}>
          {/* Edges */}
          {WEIGHTED_EDGES.map(([u,v,w], idx) => {
            const [x1,y1] = NODE_POS[u], [x2,y2] = NODE_POS[v];
            const mx = (x1+x2)/2, my = (y1+y2)/2;
            return (
              <g key={idx}>
                <line x1={x1} y1={y1} x2={x2} y2={y2} stroke="var(--border)" strokeWidth="2" />
                <text x={mx} y={my-4} textAnchor="middle" fill="var(--text-faint)" fontSize="11">{w}</text>
              </g>
            );
          })}
          {/* Nodes */}
          {LABELS.map((lbl, i) => (
            <g key={i}>
              <circle cx={NODE_POS[i][0]} cy={NODE_POS[i][1]} r={18} fill={nodeColor(i)} stroke={nodeStroke(i)} strokeWidth="2.5" />
              <text x={NODE_POS[i][0]} y={NODE_POS[i][1]+5} textAnchor="middle" fill="var(--text)" fontSize="13" fontWeight="bold">{lbl}</text>
            </g>
          ))}
        </svg>
      </div>

      {/* Distance table */}
      <div className="flex gap-2 flex-wrap">
        {LABELS.map((lbl, i) => (
          <div key={i} className="flex flex-col items-center rounded-lg border px-3 py-2 min-w-12"
            style={s.current===i ? {borderColor:'var(--accent)',background:'var(--accent-soft)'} : s.visited[i] ? {borderColor:'var(--accent)',background:'color-mix(in srgb, var(--accent) 15%, transparent)'} : s.updated.includes(i) ? {borderColor:'var(--tier-3)',background:'color-mix(in srgb, var(--tier-3) 15%, transparent)'} : {borderColor:'var(--border)',background:'var(--surface-raised)'}}>
            <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>{lbl}</span>
            <span style={{color:'var(--text)',fontSize:'0.875rem',fontWeight:700}}>{s.dist[i] === INF ? '∞' : s.dist[i]}</span>
          </div>
        ))}
      </div>

      {/* Legend */}
      <div className="flex gap-4 flex-wrap text-xs" style={{color:'var(--text-dim)'}}>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--accent-soft)',border:'2px solid var(--accent)'}}></span>Current</span>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--accent)'}}></span>Visited</span>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--tier-3)'}}></span>Updated</span>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--surface-raised)',border:'2px solid var(--border)'}}></span>Unvisited</span>
      </div>

      <div className="viz-info">{s.msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStep(s => Math.min(DIJKSTRA_STEPS.length-1, s+1))} disabled={step===DIJKSTRA_STEPS.length-1}
          className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={() => { if (playing) stopPlay(); setStep(s => Math.max(0, s-1)); }} disabled={step===0}
          className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={step===DIJKSTRA_STEPS.length-1}
          className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={() => { stopPlay(); setStep(0); }} className="viz-btn">Reset</button>
        <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>{step+1}/{DIJKSTRA_STEPS.length}</span>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
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
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Graph Traversal</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>BFS, DFS, and Dijkstra's shortest path</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2">
        {TABS.map(t => (
          <button key={t.id} onClick={() => setTab(t.id)}
            className={tab === t.id ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t.label}
          </button>
        ))}
      </div>

      {tab === 'grid' ? <GridTab /> : <DijkstraTab />}
    </div>
  );
}
