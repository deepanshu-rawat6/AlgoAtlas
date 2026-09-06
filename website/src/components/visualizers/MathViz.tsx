import { useState, useRef, useEffect } from 'react';

const TAB_BTN = (active: boolean) => active ? 'viz-btn viz-btn--primary' : 'viz-btn';

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
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  useEffect(() => {
    if (!playing || frames.length === 0) return;
    const id = setInterval(() => {
      setStep(s => {
        if (s >= frames.length - 1) { setPlaying(false); return s; }
        return s + 1;
      });
    }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed, frames.length]);

  function start() {
    setPlaying(false);
    const f = buildSpiralFrames(Math.min(size, 6));
    setFrames(f); setStep(0); setStarted(true);
  }

  const frame = frames[step];
  const isDone = started && step >= frames.length - 1;

  return (
    <div className="space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Spiral Matrix</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Traverse an n×n matrix in spiral order using boundary shrinking</p>
      </div>
      <div className="flex gap-3 items-end">
        <div>
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Size n (max 6)</label>
          <input type="number" min="2" max="6"
            className="w-20"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={size} onChange={e => setSize(Math.min(6, Math.max(2, parseInt(e.target.value) || 4)))} />
        </div>
        <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
      </div>
      {frame && (
        <div className="inline-block rounded-lg p-4" style={{background:'var(--surface-sunken)'}}>
          {frame.grid.map((row, r) => (
            <div key={r} className="flex gap-1 mb-1">
              {row.map((val, c) => {
                const isCurr = frame.pos[0] === r && frame.pos[1] === c;
                const cellStyle = isCurr
                  ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
                  : val !== null
                    ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
                    : {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
                return (
                  <div key={c} className="w-11 h-11 flex items-center justify-center font-mono font-bold text-sm rounded border-2" style={cellStyle}>
                    {val ?? '·'}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}
      {frame && (
        <div className="viz-info">
          Placing {frame.order} at ({frame.pos[0]}, {frame.pos[1]}) · Step {step + 1}/{frames.length}
        </div>
      )}
      {started && (
        <div className="flex flex-wrap items-center gap-3">
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={isDone}
            className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
          <button onClick={() => { setPlaying(false); setStep(s => Math.max(0, s - 1)); }} disabled={step === 0}
            className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
          <button onClick={() => setPlaying(p => !p)} disabled={isDone}
            className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
            {playing ? 'Pause' : '▶ Play'}
          </button>
          <button onClick={start} className="viz-btn">Reset</button>
          <div className="flex items-center gap-2">
            <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
            <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
            <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
          </div>
        </div>
      )}
    </div>
  );
}

// ── Rotate Image ──────────────────────────────────────────────────────────────
interface RotateFrame {
  matrix: number[][];
  phase: 1 | 2 | 0;
  highlightCells: [number,number][];
  highlightRow: number | null;
  msg: string;
}

function buildRotateFrames(n: number): RotateFrame[] {
  const matrix: number[][] = Array.from({ length: n }, (_, r) => Array.from({ length: n }, (_, c) => r * n + c + 1));
  const frames: RotateFrame[] = [];

  frames.push({ matrix: matrix.map(r => [...r]), phase: 0, highlightCells: [], highlightRow: null, msg: 'Original matrix. Phase 1: Transpose (swap across diagonal).' });

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
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  useEffect(() => {
    if (!playing || frames.length === 0) return;
    const id = setInterval(() => {
      setStep(s => {
        if (s >= frames.length - 1) { setPlaying(false); return s; }
        return s + 1;
      });
    }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed, frames.length]);

  function start() {
    setPlaying(false);
    setFrames(buildRotateFrames(size));
    setStep(0); setStarted(true);
  }

  const frame = frames[step];
  const isDone = started && step >= frames.length - 1;

  const original: number[][] = Array.from({ length: size }, (_, r) => Array.from({ length: size }, (_, c) => r * size + c + 1));

  function cellStyle(r: number, c: number): React.CSSProperties {
    if (!frame) return {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
    if (frame.highlightRow === r) return {background:'color-mix(in srgb, var(--accent) 30%, transparent)',borderColor:'var(--accent)',color:'var(--text)'};
    if (frame.highlightCells.some(([hr, hc]) => hr === r && hc === c)) return {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
    return {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
  }

  const phaseLabel = frame ? (frame.phase === 1 ? 'Phase 1: Transpose' : frame.phase === 2 ? 'Phase 2: Reverse Rows' : '') : '';

  return (
    <div className="space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Rotate Image (90° Clockwise)</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>In-place: transpose matrix, then reverse each row</p>
      </div>
      <div className="flex gap-3 items-end">
        <div>
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Size n (2–4)</label>
          <input type="number" min="2" max="4"
            className="w-20"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={size} onChange={e => setSize(Math.min(4, Math.max(2, parseInt(e.target.value) || 3)))} />
        </div>
        <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
      </div>

      {phaseLabel && <span style={{display:'inline-block',fontSize:'0.75rem',fontWeight:600,padding:'0.25rem 0.5rem',borderRadius:'0.25rem',background:'var(--surface-raised)',color:'var(--accent)'}}>{phaseLabel}</span>}

      {frame && (
        <div className="flex gap-8 flex-wrap">
          <div>
            <p style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>Original</p>
            <div className="inline-block rounded-lg p-3" style={{background:'var(--surface-sunken)'}}>
              {original.map((row, r) => (
                <div key={r} className="flex gap-1 mb-1">
                  {row.map((val, c) => (
                    <div key={c} className="w-10 h-10 flex items-center justify-center font-mono font-bold text-sm rounded border-2"
                      style={{background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-faint)'}}>{val}</div>
                  ))}
                </div>
              ))}
            </div>
          </div>
          <div>
            <p style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>{frame.phase === 0 && step === frames.length - 1 ? 'Rotated' : 'In Progress'}</p>
            <div className="inline-block rounded-lg p-3" style={{background:'var(--surface-sunken)'}}>
              {frame.matrix.map((row, r) => (
                <div key={r} className="flex gap-1 mb-1">
                  {row.map((val, c) => (
                    <div key={c} className="w-10 h-10 flex items-center justify-center font-mono font-bold text-sm rounded border-2" style={cellStyle(r, c)}>{val}</div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {frame && (
        <div className={frame.msg.startsWith('✓') ? '' : 'viz-info'}
          style={frame.msg.startsWith('✓') ? {background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'} : undefined}>
          {frame.msg}
        </div>
      )}

      {started && (
        <div className="flex flex-wrap items-center gap-3">
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={isDone}
            className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
          <button onClick={() => { setPlaying(false); setStep(s => Math.max(0, s - 1)); }} disabled={step === 0}
            className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
          <button onClick={() => setPlaying(p => !p)} disabled={isDone}
            className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
            {playing ? 'Pause' : '▶ Play'}
          </button>
          <button onClick={start} className="viz-btn">Reset</button>
          <div className="flex items-center gap-2">
            <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
            <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
            <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
          </div>
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>{step + 1}/{frames.length}</span>
        </div>
      )}
    </div>
  );
}

// ── Main ──────────────────────────────────────────────────────────────────────
export default function MathViz() {
  const [tab, setTab] = useState<'spiral' | 'rotate'>('spiral');
  return (
    <div className="panel p-6 space-y-6">
      <div className="flex gap-2">
        <button className={TAB_BTN(tab === 'spiral')} onClick={() => setTab('spiral')}>Spiral Matrix</button>
        <button className={TAB_BTN(tab === 'rotate')} onClick={() => setTab('rotate')}>Rotate Image</button>
      </div>
      {tab === 'spiral' ? <SpiralTab /> : <RotateTab />}
    </div>
  );
}
