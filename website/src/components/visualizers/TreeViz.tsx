import { useState, useRef, useEffect } from 'react';

// Tree: [3, 9, 20, null, null, 15, 7]
const TREE = [3, 9, 20, null, null, 15, 7];
const W = 500, H = 200, R = 18;

const POS: Record<number, [number, number]> = {
  0: [250, 30],
  1: [120, 90],  2: [380, 90],
  3: [55,  160], 4: [185, 160], 5: [315, 160], 6: [445, 160],
};

const EDGES = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]].filter(
  ([a, b]) => TREE[a] !== null && TREE[b] !== null
);

// Pre-computed visit sequences (indices into TREE)
const SEQUENCES: Record<Tab, number[]> = {
  'level':     [0,1,2,5,6],   // 3,9,20,15,7  (BFS; skip null children)
  'preorder':  [0,1,2,5,6],   // 3,9,20,15,7
  'inorder':   [1,0,5,2,6],   // 9,3,15,20,7
  'postorder': [1,5,6,2,0],   // 9,15,7,20,3
};

type Tab = 'level' | 'preorder' | 'inorder' | 'postorder';
const TABS: { id: Tab; label: string }[] = [
  { id: 'level',     label: 'Level Order (BFS)' },
  { id: 'preorder',  label: 'Preorder (DFS)' },
  { id: 'inorder',   label: 'Inorder' },
  { id: 'postorder', label: 'Postorder' },
];

export default function TreeViz() {
  const [tab, setTab] = useState<Tab>('level');
  const [step, setStep] = useState(0);   // 0 = nothing visited yet; step N = first N nodes visited
  const [started, setStarted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  const seq = SEQUENCES[tab];
  const visitedIndices = seq.slice(0, step);
  const currentIdx = step < seq.length ? seq[step] : -1;
  const done = started && step >= seq.length;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }
  function switchTab(t: Tab) { stopPlay(); setTab(t); setStep(0); setStarted(false); }
  function reset() { stopPlay(); setStep(0); setStarted(false); }
  function start() { setStarted(true); setStep(0); }
  function nextStep() {
    if (!started || done) return;
    setStep(s => Math.min(seq.length, s + 1));
  }
  function prevStep() {
    if (playing) stopPlay();
    if (!started) return;
    setStep(s => Math.max(0, s - 1));
  }
  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setStep(s => { if (s >= seq.length) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const mountedRef = useRef(false);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    timerRef.current = setInterval(() => {
      setStep(s => { if (s >= seq.length) { stopPlay(); return s; } return s + 1; });
    }, 1100 - speed * 200);
  }, [speed]);

  function nodeColor(i: number) {
    if (currentIdx === i) return 'var(--accent-soft)';
    if (visitedIndices.includes(i)) return 'var(--accent)';
    return 'var(--surface-raised)';
  }
  function nodeStroke(i: number) {
    if (currentIdx === i) return 'var(--accent)';
    if (visitedIndices.includes(i)) return 'var(--accent)';
    return 'var(--border)';
  }

  const msg = !started
    ? `Press "Start" to begin ${TABS.find(t => t.id === tab)?.label}.`
    : done
      ? `Complete! Order: [${seq.map(i => TREE[i]).join(', ')}]`
      : step === 0
        ? `Ready. Press "Next Step" to visit first node.`
        : `Visiting node ${TREE[currentIdx === -1 ? seq[step-1] : currentIdx]} — step ${step}/${seq.length}`;

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Tree Traversal</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Step through traversal orders on a binary tree</p>
      </div>

      {/* Tab bar */}
      <div className="flex gap-2 flex-wrap">
        {TABS.map(t => (
          <button key={t.id} onClick={() => switchTab(t.id)}
            className={tab === t.id ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t.label}
          </button>
        ))}
      </div>

      {/* SVG Tree */}
      <div className="panel p-3">
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" style={{ maxHeight: 220 }}>
          {EDGES.map(([a, b]) => (
            <line key={`${a}-${b}`}
              x1={POS[a][0]} y1={POS[a][1] + R}
              x2={POS[b][0]} y2={POS[b][1] - R}
              stroke="var(--border)" strokeWidth="2" />
          ))}
          {TREE.map((val, i) => {
            if (val == null || !POS[i]) return null;
            return (
              <g key={i}>
                <circle cx={POS[i][0]} cy={POS[i][1]} r={R} fill={nodeColor(i)} stroke={nodeStroke(i)} strokeWidth="2" />
                <text x={POS[i][0]} y={POS[i][1]+5} textAnchor="middle" fill="var(--text)" fontSize="13" fontWeight="bold">{val}</text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* Visit sequence badges */}
      {visitedIndices.length > 0 && (
        <div className="flex gap-2 flex-wrap items-center">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Visited:</span>
          {visitedIndices.map((idx, pos) => (
            <span key={pos} style={{background:'color-mix(in srgb, var(--accent) 20%, transparent)',border:'1px solid var(--accent)',padding:'0.125rem 0.5rem',borderRadius:'0.25rem',fontSize:'0.875rem',fontFamily:'var(--mono)',color:'var(--accent)'}}>{TREE[idx]}</span>
          ))}
          {currentIdx !== -1 && (
            <span className="animate-pulse" style={{background:'var(--accent-soft)',border:'1px solid var(--accent)',padding:'0.125rem 0.5rem',borderRadius:'0.25rem',fontSize:'0.875rem',fontFamily:'var(--mono)',color:'var(--text)'}}>{TREE[currentIdx]}</span>
          )}
        </div>
      )}

      <div className="viz-info">{msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        {!started
          ? <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
          : <>
              <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
              <button onClick={prevStep} disabled={step === 0} className="viz-btn">← Back</button>
              <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
                {playing ? 'Pause' : '▶ Play'}
              </button>
              <button onClick={reset} className="viz-btn">Reset</button>
              <div className="flex items-center gap-2">
                <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
                <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
                <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
              </div>
            </>
        }
      </div>

      {/* Legend */}
      <div className="flex gap-4 text-xs" style={{color:'var(--text-dim)'}}>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--accent-soft)',border:'2px solid var(--accent)'}}></span>Current</span>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--accent)'}}></span>Visited</span>
        <span className="flex items-center gap-1"><span style={{display:'inline-block',width:'0.75rem',height:'0.75rem',borderRadius:'50%',background:'var(--surface-raised)',border:'2px solid var(--border)'}}></span>Unvisited</span>
      </div>
    </div>
  );
}
