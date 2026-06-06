import { useState } from 'react';

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

export default function MathViz() {
  const [size, setSize] = useState(4);
  const [frames, setFrames] = useState<ReturnType<typeof buildSpiralFrames>>([]);
  const [step, setStep] = useState(0);
  const [started, setStarted] = useState(false);

  function start() {
    const f = buildSpiralFrames(Math.min(size, 6));
    setFrames(f); setStep(0); setStarted(true);
  }

  const frame = frames[step];

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Math & Geometry — Spiral Matrix</h3>
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
                const isFilled = val !== null;
                return (
                  <div key={c} className={`w-11 h-11 flex items-center justify-center font-mono font-bold text-sm rounded border-2 ${isCurr ? 'bg-yellow-800 border-yellow-400 text-white' : isFilled ? 'bg-blue-900/50 border-blue-700 text-blue-200' : 'bg-slate-700 border-slate-600 text-slate-600'}`}>
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
