import { useState, useRef, useEffect } from 'react';

// ── Subsets ──────────────────────────────────────────────────────────────────

interface SubsetNode { path: number[]; idx: number; id: string; parentId: string | null; }

function generateSubsetSteps(nums: number[]): SubsetNode[] {
  const steps: SubsetNode[] = [];
  function bt(path: number[], idx: number, parentId: string | null) {
    const id = path.join(',') + '@' + idx;
    steps.push({ path: [...path], idx, id, parentId });
    for (let i = idx; i < nums.length; i++) {
      path.push(nums[i]);
      bt(path, i + 1, id);
      path.pop();
    }
  }
  bt([], 0, null);
  return steps;
}

function SubsetsViz() {
  const [input, setInput] = useState('1, 2, 3');
  const [steps, setSteps] = useState<SubsetNode[]>([]);
  const [curr, setCurr] = useState(-1);
  const [started, setStarted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  const nums = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n)).slice(0, 4);

  function start() {
    setPlaying(false);
    const s = generateSubsetSteps(nums);
    setSteps(s); setCurr(0); setStarted(true);
  }
  function nextStep() { if (curr < steps.length - 1) setCurr(c => c + 1); }
  function stepBack() { setPlaying(false); if (curr > 0) setCurr(c => c - 1); }

  const isDone = started && curr >= steps.length - 1;

  useEffect(() => {
    if (!playing) {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
      return;
    }
    timerRef.current = setInterval(() => {
      setCurr(c => {
        if (c >= steps.length - 1) { setPlaying(false); return c; }
        return c + 1;
      });
    }, 1100 - speed * 200);
    return () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
  }, [playing, speed, steps.length]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const visible = steps.slice(0, curr + 1);
  const current = steps[curr];
  const leaves = visible.filter(n => !visible.some(m => m.parentId === n.id));

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Choose / Explore / Unchoose recursion tree</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array (max 4 elements)</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>
      {started && (
        <div className="overflow-y-auto max-h-80 space-y-1">
          {visible.map(node => {
            const isCurr = node.id === current?.id;
            return (
              <div key={node.id}
                className="flex items-center gap-2 py-1 px-2 rounded"
                style={{
                  marginLeft: node.path.length * 20,
                  background: isCurr ? 'var(--accent-soft)' : 'var(--surface-sunken)',
                  border: isCurr ? '1px solid var(--accent)' : '1px solid transparent',
                }}>
                <span className="font-mono text-sm" style={{color:'var(--text)'}}>[{node.path.join(', ')}]</span>
                {node.path.length === nums.length && <span className="text-xs ml-1" style={{color:'var(--tier-3)'}}>← leaf subset ✓</span>}
                {isCurr && <span className="text-xs ml-auto" style={{color:'var(--accent)'}}>← current</span>}
              </div>
            );
          })}
        </div>
      )}
      {leaves.length > 0 && (
        <div style={{background:'var(--surface-sunken)',borderRadius:'0.5rem',padding:'0.75rem 1rem'}}>
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>Subsets found so far:</div>
          <div className="flex flex-wrap gap-2">
            {leaves.map(n => (
              <span key={n.id} className="px-2 py-1 rounded text-sm font-mono"
                style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',color:'var(--tier-3)'}}>
                [{n.path.join(', ') || '∅'}]
              </span>
            ))}
          </div>
        </div>
      )}
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone || !started} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={!started || curr <= 0} className="viz-btn">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone || !started} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        {started && <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}} className="self-center">{curr + 1} / {steps.length} nodes</span>}
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Permutations ─────────────────────────────────────────────────────────────

interface PermStep {
  arr: number[];
  swapFrom: number;
  swapTo: number;
  depth: number;
  action: 'choose' | 'unchoose' | 'result';
  path: number[];
}

function generatePermSteps(nums: number[]): PermStep[] {
  const steps: PermStep[] = [];
  const arr = [...nums];
  function bt(depth: number) {
    if (depth === arr.length) {
      steps.push({ arr: [...arr], swapFrom: -1, swapTo: -1, depth, action: 'result', path: [...arr] });
      return;
    }
    for (let i = depth; i < arr.length; i++) {
      // swap depth <-> i
      [arr[depth], arr[i]] = [arr[i], arr[depth]];
      steps.push({ arr: [...arr], swapFrom: depth, swapTo: i, depth, action: 'choose', path: arr.slice(0, depth + 1) });
      bt(depth + 1);
      // unswap
      [arr[depth], arr[i]] = [arr[i], arr[depth]];
      steps.push({ arr: [...arr], swapFrom: depth, swapTo: i, depth, action: 'unchoose', path: arr.slice(0, depth) });
    }
  }
  bt(0);
  return steps;
}

function PermutationsViz() {
  const [input, setInput] = useState('1, 2, 3');
  const [steps, setSteps] = useState<PermStep[]>([]);
  const [curr, setCurr] = useState(-1);
  const [started, setStarted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  const nums = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n)).slice(0, 3);

  function start() {
    setPlaying(false);
    const s = generatePermSteps(nums);
    setSteps(s); setCurr(0); setStarted(true);
  }
  function nextStep() { if (curr < steps.length - 1) setCurr(c => c + 1); }
  function stepBack() { setPlaying(false); if (curr > 0) setCurr(c => c - 1); }

  const isDone = started && curr >= steps.length - 1;

  useEffect(() => {
    if (!playing) {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
      return;
    }
    timerRef.current = setInterval(() => {
      setCurr(c => {
        if (c >= steps.length - 1) { setPlaying(false); return c; }
        return c + 1;
      });
    }, 1100 - speed * 200);
    return () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
  }, [playing, speed, steps.length]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const step = steps[curr] ?? null;
  const found = steps.slice(0, curr + 1).filter(s => s.action === 'result');

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Swap-based backtracking to generate all orderings</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array (max 3 elements)</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>

      {started && step && (
        <div className="space-y-3">
          {/* Current array state with swapped positions highlighted */}
          <div>
            <div style={{ marginLeft: step.depth * 20, color:'var(--text-faint)', fontSize:'0.75rem', marginBottom:'0.5rem' }}>
              depth={step.depth} — {step.action === 'result' ? '✓ result!' : step.action === 'choose' ? `swap [${step.swapFrom}]↔[${step.swapTo}]` : `undo swap [${step.swapFrom}]↔[${step.swapTo}]`}
            </div>
            <div className="flex gap-2" style={{ marginLeft: step.depth * 20 }}>
              {step.arr.map((v, idx) => {
                const isFixed = idx < step.depth;
                const isSwapped = idx === step.swapFrom || idx === step.swapTo;
                const isResult = step.action === 'result';
                let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
                if (isResult) cellStyle = {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'};
                else if (isSwapped && step.swapFrom !== step.swapTo) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
                else if (isFixed) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
                return (
                  <div key={idx} className="flex flex-col items-center gap-1">
                    <div className="w-10 h-10 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>{v}</div>
                    <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{idx}]</div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Path being built */}
          <div className="viz-info">
            Building: [{step.path.join(', ')}]{step.action === 'result' ? ' ✓' : '...'}
          </div>
        </div>
      )}

      {found.length > 0 && (
        <div style={{background:'var(--surface-sunken)',borderRadius:'0.5rem',padding:'0.75rem 1rem'}}>
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>Permutations found ({found.length}):</div>
          <div className="flex flex-wrap gap-2">
            {found.map((s, i) => (
              <span key={i} className="px-2 py-1 rounded text-sm font-mono"
                style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',color:'var(--tier-3)'}}>
                [{s.path.join(', ')}]
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone || !started} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={!started || curr <= 0} className="viz-btn">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone || !started} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        {started && <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}} className="self-center">{curr + 1} / {steps.length} steps</span>}
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────

export default function BacktrackingViz() {
  const [tab, setTab] = useState<'subsets' | 'perms'>('subsets');
  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>Backtracking</h3>
        <div className="flex gap-2">
          <button className={`viz-btn${tab === 'subsets' ? ' viz-btn--primary' : ''}`} onClick={() => setTab('subsets')}>Subsets</button>
          <button className={`viz-btn${tab === 'perms' ? ' viz-btn--primary' : ''}`} onClick={() => setTab('perms')}>Permutations</button>
        </div>
      </div>
      {tab === 'subsets' ? <SubsetsViz /> : <PermutationsViz />}
    </div>
  );
}
