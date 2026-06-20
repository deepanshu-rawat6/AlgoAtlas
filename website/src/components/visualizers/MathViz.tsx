import { useState } from 'react';

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

// ── Spiral Matrix ─────────────────────────────────────────────────────────────
function buildSpiralFrames(n: number): { grid: (number|null)[][]; pos: [number,number]; order: number }[] {
  const grid: (number|null)[][] = Array.from({ length: n }, () => Array(n).fill(null));
  const frames = [];
  let top = 0, bottom = n - 1, left = 0, right = n - 1, num = 1;
  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) { grid[top][i] = num; frames.push({ grid: grid.map(r => [...r]), pos: [top, i] as [number,number], order: num }); num++; }
    top++;
    for (let i = top; i <= bottom; i++) { grid[i][right] = num; frames.push({ grid: grid.map(r => [...r]), pos: [i, right] as [number,number], order: num }); num++; }
    right--;
    if (top <= bottom) { for (let i = right; i >= left; i--) { grid[bottom][i] = num; frames.push({ grid: grid.map(r => [...r]), pos: [bottom, i] as [number,number], order: num }); num++; } bottom--; }
    if (left <= right) { for (let i = bottom; i >= top; i--) { grid[i][left] = num; frames.push({ grid: grid.map(r => [...r]), pos: [i, left] as [number,number], order: num }); num++; } left++; }
  }
  return frames;
}

function SpiralTab() {
  const [size, setSize] = useState(4);
  const [frames, setFrames] = useState<ReturnType<typeof buildSpiralFrames>>([]);
  const [step, setStep] = useState(0);
  const [started, setStarted] = useState(false);

  function start() { const f = buildSpiralFrames(Math.min(size, 6)); setFrames(f); setStep(0); setStarted(true); }
  const frame = frames[step];

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Spiral Matrix</h3>
        <p className="text-sm text-slate-400">Traverse an n×n matrix in spiral order using boundary shrinking</p>
      </div>
      <div className="flex gap-3 items-end">
        <div>
          <label className="block text-xs text-slate-400 mb-1">Size n (max 6)</label>
          <input type="number" min="2" max="6"
            className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={size} onChange={e => setSize(Math.min(6, Math.max(2, parseInt(e.target.value) || 4)))} />
        </div>
        <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
      </div>
      {frame && (
        <div className="inline-block bg-slate-900/60 rounded-lg p-4">
          {frame.grid.map((row, r) => (
            <div key={r} className="flex gap-1 mb-1">
              {row.map((val, c) => {
                const isCurr = frame.pos[0] === r && frame.pos[1] === c;
                return (
                  <div key={c} className={`w-11 h-11 flex items-center justify-center font-mono font-bold text-sm rounded border-2 ${isCurr ? 'bg-yellow-800 border-yellow-400 text-white' : val !== null ? 'bg-blue-900/50 border-blue-700 text-blue-200' : 'bg-slate-700 border-slate-600 text-slate-600'}`}>
                    {val ?? '·'}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}
      {frame && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono text-slate-300">
          Placing {frame.order} at ({frame.pos[0]}, {frame.pos[1]}) · Step {step + 1}/{frames.length}
        </div>
      )}
      {started && (
        <div className="flex gap-3">
          <button onClick={() => setStep(s => Math.max(0, s - 1))} disabled={step === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={step >= frames.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
        </div>
      )}
    </div>
  );
}

// ── Rotate Image ──────────────────────────────────────────────────────────────
interface RotateFrame {
  matrix: number[][];
  phase: 1 | 2 | 0; // 0 = initial/done
  highlightCells: [number,number][];
  highlightRow: number | null;
  msg: string;
}

function buildRotateFrames(n: number): RotateFrame[] {
  const matrix: number[][] = Array.from({ length: n }, (_, r) => Array.from({ length: n }, (_, c) => r * n + c + 1));
  const frames: RotateFrame[] = [];

  frames.push({ matrix: matrix.map(r => [...r]), phase: 0, highlightCells: [], highlightRow: null, msg: 'Original matrix. Phase 1: Transpose (swap across diagonal).' });

  // Phase 1: Transpose
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const a = matrix[i][j], b = matrix[j][i];
      [matrix[i][j], matrix[j][i]] = [b, a];
      frames.push({
        matrix: matrix.map(r => [...r]),
        phase: 1,
        highlightCells: [[i, j], [j, i]],
        highlightRow: null,
        msg: `Phase 1: Transpose — Swap matrix[${i}][${j}]=${a} ↔ matrix[${j}][${i}]=${b}`,
      });
    }
  }

  frames.push({ matrix: matrix.map(r => [...r]), phase: 0, highlightCells: [], highlightRow: null, msg: 'Transpose complete. Phase 2: Reverse each row.' });

  // Phase 2: Reverse rows
  for (let i = 0; i < n; i++) {
    matrix[i].reverse();
    frames.push({
      matrix: matrix.map(r => [...r]),
      phase: 2,
      highlightCells: [],
      highlightRow: i,
      msg: `Phase 2: Reverse Rows — Reversed row ${i}: [${matrix[i].join(', ')}]`,
    });
  }

  frames.push({ matrix: matrix.map(r => [...r]), phase: 0, highlightCells: [], highlightRow: null, msg: '✓ Rotation complete! (90° clockwise)' });
  return frames;
}

function RotateTab() {
  const [size, setSize] = useState(3);
  const [frames, setFrames] = useState<RotateFrame[]>([]);
  const [step, setStep] = useState(0);
  const [started, setStarted] = useState(false);

  function start() { setFrames(buildRotateFrames(size)); setStep(0); setStarted(true); }
  const frame = frames[step];

  // Original matrix for side-by-side (row major 1..n²)
  const original: number[][] = Array.from({ length: size }, (_, r) => Array.from({ length: size }, (_, c) => r * size + c + 1));

  function cellClass(r: number, c: number): string {
    if (!frame) return 'bg-slate-700 border-slate-600 text-slate-300';
    if (frame.highlightRow === r) return 'bg-orange-800 border-orange-400 text-white';
    if (frame.highlightCells.some(([hr, hc]) => hr === r && hc === c)) return 'bg-yellow-800 border-yellow-400 text-white';
    return 'bg-slate-700 border-slate-600 text-slate-200';
  }

  const phaseLabel = frame ? (frame.phase === 1 ? 'Phase 1: Transpose' : frame.phase === 2 ? 'Phase 2: Reverse Rows' : '') : '';

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Rotate Image (90° Clockwise)</h3>
        <p className="text-sm text-slate-400">In-place: transpose matrix, then reverse each row</p>
      </div>
      <div className="flex gap-3 items-end">
        <div>
          <label className="block text-xs text-slate-400 mb-1">Size n (2–4)</label>
          <input type="number" min="2" max="4"
            className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={size} onChange={e => setSize(Math.min(4, Math.max(2, parseInt(e.target.value) || 3)))} />
        </div>
        <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
      </div>

      {phaseLabel && <span className="inline-block text-xs font-semibold px-2 py-1 rounded bg-slate-700 text-blue-300">{phaseLabel}</span>}

      {frame && (
        <div className="flex gap-8 flex-wrap">
          {/* Original */}
          <div>
            <p className="text-xs text-slate-500 mb-2">Original</p>
            <div className="inline-block bg-slate-900/60 rounded-lg p-3">
              {original.map((row, r) => (
                <div key={r} className="flex gap-1 mb-1">
                  {row.map((val, c) => (
                    <div key={c} className="w-10 h-10 flex items-center justify-center font-mono font-bold text-sm rounded border-2 bg-slate-800 border-slate-600 text-slate-400">{val}</div>
                  ))}
                </div>
              ))}
            </div>
          </div>
          {/* In-progress / result */}
          <div>
            <p className="text-xs text-slate-500 mb-2">{frame.phase === 0 && step === frames.length - 1 ? 'Rotated' : 'In Progress'}</p>
            <div className="inline-block bg-slate-900/60 rounded-lg p-3">
              {frame.matrix.map((row, r) => (
                <div key={r} className="flex gap-1 mb-1">
                  {row.map((val, c) => (
                    <div key={c} className={`w-10 h-10 flex items-center justify-center font-mono font-bold text-sm rounded border-2 ${cellClass(r, c)}`}>{val}</div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {frame && (
        <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${frame.msg.startsWith('✓') ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>
          {frame.msg}
        </div>
      )}

      {started && (
        <div className="flex gap-3">
          <button onClick={() => setStep(s => Math.max(0, s - 1))} disabled={step === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={step >= frames.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
          <span className="text-xs text-slate-500 self-center">{step + 1}/{frames.length}</span>
        </div>
      )}
    </div>
  );
}

// ── Main ──────────────────────────────────────────────────────────────────────
export default function MathViz() {
  const [tab, setTab] = useState<'spiral' | 'rotate'>('spiral');
  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div className="flex gap-2">
        <button className={TAB_BTN(tab === 'spiral')} onClick={() => setTab('spiral')}>Spiral Matrix</button>
        <button className={TAB_BTN(tab === 'rotate')} onClick={() => setTab('rotate')}>Rotate Image</button>
      </div>
      {tab === 'spiral' ? <SpiralTab /> : <RotateTab />}
    </div>
  );
}
