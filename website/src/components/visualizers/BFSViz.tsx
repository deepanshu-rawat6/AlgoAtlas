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

// ── Union-Find ───────────────────────────────────────────────────────────────
const UF_N = 8;
const NODE_X = [28, 83, 138, 193, 248, 303, 358, 413];
const NODE_Y = 90;
const UF_R = 20;
const COMP_COLORS = ['#3b82f6','#22c55e','#f97316','#a855f7','#ec4899','#06b6d4','#eab308','#ef4444'];

type UFStep = { parent: number[]; rank: number[]; highlight: number[]; msg: string };

function ufGetRoot(p: number[], i: number): number {
  let cur = i; while (p[cur] !== cur) cur = p[cur]; return cur;
}

function buildUnionSteps(par: number[], rnk: number[], a: number, b: number): UFStep[] {
  const steps: UFStep[] = [];
  const p = [...par], r = [...rnk];

  function findRoot(arr: number[], start: number) {
    const path: number[] = [];
    let cur = start;
    while (arr[cur] !== cur) { path.push(cur); cur = arr[cur]; }
    path.push(cur);
    return { root: cur, path };
  }

  const { root: rootA, path: pathA } = findRoot(p, a);
  steps.push({ parent: [...p], rank: [...r], highlight: pathA, msg: `Find root of ${a}: path [${pathA.join('→')}], root = ${rootA}` });
  for (const n of pathA) p[n] = rootA;
  steps.push({ parent: [...p], rank: [...r], highlight: pathA, msg: `Path compression: all nodes in [${pathA.join('→')}] now point directly to ${rootA}` });

  const { root: rootB, path: pathB } = findRoot(p, b);
  steps.push({ parent: [...p], rank: [...r], highlight: pathB, msg: `Find root of ${b}: path [${pathB.join('→')}], root = ${rootB}` });
  for (const n of pathB) p[n] = rootB;
  if (pathB.length > 2) steps.push({ parent: [...p], rank: [...r], highlight: pathB, msg: `Path compression: all nodes in [${pathB.join('→')}] now point directly to ${rootB}` });

  if (rootA === rootB) {
    steps.push({ parent: [...p], rank: [...r], highlight: [rootA], msg: `${a} and ${b} already in same component (root=${rootA}). No union needed.` });
    return steps;
  }

  if (r[rootA] < r[rootB]) {
    p[rootA] = rootB;
    steps.push({ parent: [...p], rank: [...r], highlight: [rootA, rootB], msg: `Union by rank: rank[${rootA}]=${r[rootA]} < rank[${rootB}]=${r[rootB]} → attach ${rootA} under ${rootB}` });
  } else if (r[rootA] > r[rootB]) {
    p[rootB] = rootA;
    steps.push({ parent: [...p], rank: [...r], highlight: [rootA, rootB], msg: `Union by rank: rank[${rootA}]=${r[rootA]} > rank[${rootB}]=${r[rootB]} → attach ${rootB} under ${rootA}` });
  } else {
    p[rootB] = rootA; r[rootA]++;
    steps.push({ parent: [...p], rank: [...r], highlight: [rootA, rootB], msg: `Equal ranks → attach ${rootB} under ${rootA}, rank[${rootA}] → ${r[rootA]}` });
  }
  steps.push({ parent: [...p], rank: [...r], highlight: [], msg: `Done! ${a} and ${b} are now connected.` });
  return steps;
}

function UnionFindTab() {
  const [parent, setParent] = useState<number[]>(() => Array.from({ length: UF_N }, (_, i) => i));
  const [rank,   setRank]   = useState<number[]>(() => Array(UF_N).fill(0));
  const [nodeA,  setNodeA]  = useState('0');
  const [nodeB,  setNodeB]  = useState('1');
  const [steps,  setSteps]  = useState<UFStep[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);
  const [playing, setPlaying] = useState(false);
  const [speed,  setSpeed]  = useState(3);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const nextStepRef = useRef<() => void>(() => {});

  const inProgress = stepIdx >= 0 && steps.length > 0;
  const cur = inProgress ? steps[stepIdx] : null;
  const dispParent = cur ? cur.parent : parent;
  const dispRank   = cur ? cur.rank   : rank;
  const dispHL     = cur ? cur.highlight : [];
  const dispMsg    = cur ? cur.msg : 'Enter two nodes (0–7) and click Union.';

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function doNextStep() {
    if (!inProgress) return;
    if (stepIdx >= steps.length - 1) {
      // commit last step's state
      setParent(steps[steps.length - 1].parent);
      setRank(steps[steps.length - 1].rank);
      setSteps([]); setStepIdx(-1); stopPlay();
    } else {
      setStepIdx(s => s + 1);
    }
  }

  useEffect(() => { nextStepRef.current = doNextStep; });

  useEffect(() => {
    if (!playing) {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
      return;
    }
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
    return () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
  }, [playing, speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  function startUnion() {
    const a = parseInt(nodeA), b = parseInt(nodeB);
    if (isNaN(a) || isNaN(b) || a < 0 || a >= UF_N || b < 0 || b >= UF_N) return;
    stopPlay();
    const s = buildUnionSteps(parent, rank, a, b);
    setSteps(s); setStepIdx(0);
  }

  function stepBack() {
    stopPlay();
    if (stepIdx <= 0) { setSteps([]); setStepIdx(-1); }
    else setStepIdx(s => s - 1);
  }

  function reset() {
    stopPlay();
    setParent(Array.from({ length: UF_N }, (_, i) => i));
    setRank(Array(UF_N).fill(0));
    setSteps([]); setStepIdx(-1);
  }

  const inputStyle: React.CSSProperties = {
    background: 'var(--surface-raised)', border: '1px solid var(--border)',
    borderRadius: '0.375rem', padding: '0.375rem 0.5rem', width: '3.5rem',
    color: 'var(--text)', fontSize: '0.875rem', outline: 'none', textAlign: 'center',
  };

  return (
    <div className="space-y-5">
      <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>
        Union-Find groups nodes into components. Find uses <strong>path compression</strong>; Union uses <strong>rank</strong> to keep trees shallow.
      </p>

      {/* SVG */}
      <div className="panel p-2">
        <svg viewBox="0 0 440 140" className="w-full" style={{ maxHeight: 150 }}>
          <defs>
            <marker id="uf-arr" markerWidth="7" markerHeight="5" refX="5" refY="2.5" orient="auto">
              <polygon points="0 0, 7 2.5, 0 5" fill="var(--text-faint)" />
            </marker>
          </defs>
          {/* Parent arrows */}
          {dispParent.map((p, i) => {
            if (p === i) return null;
            const x1 = NODE_X[i], x2 = NODE_X[p], y = NODE_Y;
            const mx = (x1 + x2) / 2;
            const my = y - Math.abs(x2 - x1) * 0.45 - UF_R - 5;
            const dx = x2 - x1, dy = 0;
            const len = Math.sqrt(dx * dx + dy * dy) || 1;
            const ex = x2 - (dx / len) * (UF_R + 7), ey = y;
            return (
              <path key={i}
                d={`M ${x1} ${y - UF_R} Q ${mx} ${my} ${ex} ${ey - UF_R}`}
                fill="none" stroke="var(--text-faint)" strokeWidth="1.5"
                markerEnd="url(#uf-arr)" />
            );
          })}
          {/* Nodes */}
          {Array.from({ length: UF_N }, (_, i) => {
            const isHL = dispHL.includes(i);
            const color = COMP_COLORS[ufGetRoot(dispParent, i) % COMP_COLORS.length];
            return (
              <g key={i}>
                <circle cx={NODE_X[i]} cy={NODE_Y} r={UF_R}
                  fill={isHL ? color : `${color}33`}
                  stroke={color} strokeWidth={isHL ? 3 : 1.5} />
                <text x={NODE_X[i]} y={NODE_Y + 5} textAnchor="middle"
                  fill="var(--text)" fontSize="13" fontWeight="bold">{i}</text>
                <text x={NODE_X[i]} y={NODE_Y + UF_R + 14} textAnchor="middle"
                  fill="var(--text-faint)" fontSize="10">p:{dispParent[i]}</text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* rank row */}
      <div className="flex gap-1 items-center flex-wrap">
        <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem', fontFamily: 'var(--mono)', minWidth: '3rem' }}>rank:</span>
        {dispRank.map((v, i) => (
          <span key={i} className="px-2 py-0.5 rounded border text-xs font-mono"
            style={{ background: 'var(--surface-raised)', borderColor: 'var(--border)', color: 'var(--text-secondary)' }}>{v}</span>
        ))}
      </div>

      <div className="viz-info">{dispMsg}</div>

      {/* Controls */}
      {!inProgress ? (
        <div className="flex gap-3 items-end flex-wrap">
          <div>
            <label style={{ display: 'block', fontSize: '0.7rem', color: 'var(--text-faint)', marginBottom: '0.2rem' }}>Node A</label>
            <input style={inputStyle} value={nodeA} onChange={e => setNodeA(e.target.value)} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.7rem', color: 'var(--text-faint)', marginBottom: '0.2rem' }}>Node B</label>
            <input style={inputStyle} value={nodeB} onChange={e => setNodeB(e.target.value)} />
          </div>
          <button onClick={startUnion} className="viz-btn viz-btn--primary">Union</button>
          <button onClick={reset} className="viz-btn">Reset</button>
        </div>
      ) : (
        <div className="flex flex-wrap items-center gap-3">
          <button onClick={doNextStep} className="viz-btn viz-btn--primary">
            {stepIdx >= steps.length - 1 ? 'Commit' : 'Next Step'}
          </button>
          <button onClick={stepBack} className="viz-btn">← Back</button>
          <button onClick={() => setPlaying(p => !p)} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
            {playing ? 'Pause' : '▶ Play'}
          </button>
          <button onClick={() => { stopPlay(); setSteps([]); setStepIdx(-1); }} className="viz-btn">Cancel</button>
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>{stepIdx + 1}/{steps.length}</span>
          <div className="flex items-center gap-2">
            <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
            <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
            <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
          </div>
        </div>
      )}
    </div>
  );
}

// ── Main component ───────────────────────────────────────────────────────────
type Tab = 'grid' | 'dijkstra' | 'unionfind';
const TABS: { id: Tab; label: string }[] = [
  { id: 'grid', label: 'Grid BFS/DFS' },
  { id: 'dijkstra', label: 'Dijkstra' },
  { id: 'unionfind', label: 'Union-Find' },
];

export default function BFSViz() {
  const [tab, setTab] = useState<Tab>('grid');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Graph Traversal</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>BFS, DFS, Dijkstra's shortest path, and Union-Find</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2 flex-wrap">
        {TABS.map(t => (
          <button key={t.id} onClick={() => setTab(t.id)}
            className={tab === t.id ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t.label}
          </button>
        ))}
      </div>

      {tab === 'grid' ? <GridTab /> : tab === 'dijkstra' ? <DijkstraTab /> : <UnionFindTab />}
    </div>
  );
}
