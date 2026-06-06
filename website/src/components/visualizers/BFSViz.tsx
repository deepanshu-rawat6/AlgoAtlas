import { useState } from 'react';

const ROWS = 6, COLS = 6;
const DIRS = [[0,1],[0,-1],[1,0],[-1,0]];
const LEVEL_COLORS = [
  'bg-yellow-500','bg-orange-500','bg-red-500','bg-pink-500',
  'bg-purple-500','bg-indigo-500','bg-blue-500','bg-cyan-500',
  'bg-teal-500','bg-green-500',
];

type Mode = 'bfs' | 'dfs';
type CellState = { order: number; level: number; visited: boolean };

function makeGrid(): CellState[][] {
  return Array.from({ length: ROWS }, () =>
    Array.from({ length: COLS }, () => ({ order: -1, level: -1, visited: false }))
  );
}

export default function BFSViz() {
  const [mode, setMode] = useState<Mode>('bfs');
  const [grid, setGrid] = useState<CellState[][]>(makeGrid);
  // BFS: queue of [r,c]; DFS: stack of [r,c]
  const [frontier, setFrontier] = useState<[number,number][]>([]);
  const [visitOrder, setVisitOrder] = useState(0);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [message, setMessage] = useState('Click a cell to set the start point.');
  // For BFS level tracking
  const [currentLevel, setCurrentLevel] = useState(0);

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
    setMessage(`Start: (${r},${c}). Press "Next Step" to expand ${mode.toUpperCase()}.`);
  }

  function nextStep() {
    if (!started || done || frontier.length === 0) return;

    if (mode === 'bfs') {
      // Expand one full BFS level at a time
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

      setGrid(g);
      setCurrentLevel(level);
      setVisitOrder(order);

      if (nextFrontier.length === 0) {
        setFrontier([]);
        setDone(true);
        setMessage(`BFS complete! Visited ${order - 1} cells in ${level} levels.`);
      } else {
        setFrontier(nextFrontier);
        setMessage(`Level ${level}: visited ${nextFrontier.length} new cell(s).`);
      }
    } else {
      // DFS: pop one cell from stack, push unvisited neighbours (right, left, down, up — reversed so up/left explored first)
      const stack = [...frontier];
      const [r, c] = stack.pop()!;
      const g = grid.map(row => row.map(cell => ({ ...cell })));
      let order = visitOrder;

      // Mark current cell (may already be marked on click; only mark here for subsequent steps)
      if (!g[r][c].visited || g[r][c].order === -1) {
        g[r][c] = { order: order++, level: 0, visited: true };
      }

      // Push unvisited neighbours onto stack (reversed DIRS so first dir is explored first)
      for (const [dr, dc] of [...DIRS].reverse()) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && !g[nr][nc].visited) {
          // Peek to avoid duplicates in stack
          if (!stack.some(([sr, sc]) => sr === nr && sc === nc)) {
            stack.push([nr, nc]);
            // Mark as "in stack" to avoid re-adding
            g[nr][nc] = { order: -1, level: 1, visited: true };
          }
        }
      }

      setGrid(g);
      setFrontier(stack);
      setVisitOrder(order);

      if (stack.length === 0) {
        setDone(true);
        setMessage(`DFS complete! Visited ${order - 1} cells. Stack empty.`);
      } else {
        setMessage(`DFS: visited (${r},${c}). Stack size: ${stack.length}. Next: (${stack[stack.length-1][0]},${stack[stack.length-1][1]})`);
      }
    }
  }

  function reset() {
    setGrid(makeGrid());
    setFrontier([]);
    setStarted(false);
    setDone(false);
    setVisitOrder(0);
    setCurrentLevel(0);
    setMessage('Click a cell to set the start point.');
  }

  function switchMode(m: Mode) {
    setMode(m);
    reset();
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Graph Traversal — BFS & DFS</h3>
        <p className="text-sm text-slate-400">Click a cell to start, step through traversal</p>
      </div>

      {/* Mode toggle */}
      <div className="flex gap-2">
        {(['bfs', 'dfs'] as Mode[]).map(m => (
          <button key={m} onClick={() => switchMode(m)}
            className={`px-4 py-2 rounded-lg text-sm font-medium border transition-colors ${mode === m ? 'bg-blue-700 border-blue-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-300 hover:bg-slate-600'}`}>
            {m.toUpperCase()}
          </button>
        ))}
        <span className="text-xs text-slate-500 self-center ml-2">
          {mode === 'bfs' ? 'Queue — expands level by level' : 'Stack — goes deep before wide'}
        </span>
      </div>

      {/* Grid */}
      <div className="inline-block">
        {grid.map((row, r) => (
          <div key={r} className="flex gap-1 mb-1">
            {row.map((cell, c) => {
              const inFrontier = frontier.some(([fr, fc]) => fr === r && fc === c);
              let colorClass = 'bg-slate-700';
              if (cell.visited) {
                if (mode === 'bfs') {
                  colorClass = LEVEL_COLORS[cell.level % LEVEL_COLORS.length];
                } else {
                  // DFS: blue for visited-and-processed, yellow for in-stack
                  colorClass = cell.order >= 0 ? 'bg-blue-600' : 'bg-yellow-600';
                }
              }
              return (
                <button key={c} onClick={() => handleCellClick(r, c)}
                  className={`w-12 h-12 rounded-lg border-2 text-xs font-bold transition-all
                    ${colorClass}
                    ${inFrontier ? 'border-white scale-105' : 'border-transparent'}
                    ${!started ? 'cursor-pointer hover:bg-slate-600' : 'cursor-default'}
                    ${cell.visited ? 'text-white' : 'text-slate-500'}`}>
                  {cell.visited && cell.order >= 0 ? cell.order : ''}
                </button>
              );
            })}
          </div>
        ))}
      </div>

      {/* Legend */}
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

      <div className="flex gap-3">
        <button onClick={nextStep} disabled={!started || done}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={reset} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-white text-sm font-medium rounded-lg">
          Reset
        </button>
      </div>
    </div>
  );
}
