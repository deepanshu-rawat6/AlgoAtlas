import { useState, useRef, useEffect } from 'react';

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

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
      <p className="text-sm text-slate-400">Choose / Explore / Unchoose recursion tree</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (max 4 elements)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button></div>
      </div>
      {started && (
        <div className="overflow-y-auto max-h-80 space-y-1">
          {visible.map(node => {
            const isCurr = node.id === current?.id;
            return (
              <div key={node.id} className={`flex items-center gap-2 py-1 px-2 rounded ${isCurr ? 'bg-yellow-900/50 border border-yellow-700' : 'bg-slate-800/40'}`}
                style={{ marginLeft: node.path.length * 20 }}>
                <span className="font-mono text-sm text-slate-300">[{node.path.join(', ')}]</span>
                {node.path.length === nums.length && <span className="text-xs text-green-400 ml-1">← leaf subset ✓</span>}
                {isCurr && <span className="text-xs text-yellow-400 ml-auto">← current</span>}
              </div>
            );
          })}
        </div>
      )}
      {leaves.length > 0 && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3">
          <div className="text-xs text-slate-500 mb-2">Subsets found so far:</div>
          <div className="flex flex-wrap gap-2">
            {leaves.map(n => <span key={n.id} className="bg-green-900/40 border border-green-800 px-2 py-1 rounded text-sm font-mono text-green-300">[{n.path.join(', ') || '∅'}]</span>)}
          </div>
        </div>
      )}
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone || !started}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={!started || curr <= 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone || !started}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        {started && <span className="text-xs text-slate-500 self-center">{curr + 1} / {steps.length} nodes</span>}
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
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
      <p className="text-sm text-slate-400">Swap-based backtracking to generate all orderings</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (max 3 elements)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => setInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button></div>
      </div>

      {started && step && (
        <div className="space-y-3">
          {/* Current array state with swapped positions highlighted */}
          <div>
            <div className="text-xs text-slate-500 mb-2" style={{ marginLeft: step.depth * 20 }}>
              depth={step.depth} — {step.action === 'result' ? '✓ result!' : step.action === 'choose' ? `swap [${step.swapFrom}]↔[${step.swapTo}]` : `undo swap [${step.swapFrom}]↔[${step.swapTo}]`}
            </div>
            <div className="flex gap-2" style={{ marginLeft: step.depth * 20 }}>
              {step.arr.map((v, idx) => {
                const isFixed = idx < step.depth;
                const isSwapped = idx === step.swapFrom || idx === step.swapTo;
                const isResult = step.action === 'result';
                let bg = 'bg-slate-700 border-slate-600 text-slate-300';
                if (isResult) bg = 'bg-green-800 border-green-400 text-white';
                else if (isSwapped && step.swapFrom !== step.swapTo) bg = 'bg-yellow-800 border-yellow-400 text-white';
                else if (isFixed) bg = 'bg-blue-900/50 border-blue-700 text-blue-200';
                return (
                  <div key={idx} className="flex flex-col items-center gap-1">
                    <div className={`w-10 h-10 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>{v}</div>
                    <div className="text-xs text-slate-600">[{idx}]</div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Path being built */}
          <div className="bg-slate-900/60 rounded-lg px-4 py-2 text-sm font-mono text-slate-300">
            Building: [{step.path.join(', ')}]{step.action === 'result' ? ' ✓' : '...'}
          </div>
        </div>
      )}

      {found.length > 0 && (
        <div className="bg-slate-900/60 rounded-lg px-4 py-3">
          <div className="text-xs text-slate-500 mb-2">Permutations found ({found.length}):</div>
          <div className="flex flex-wrap gap-2">
            {found.map((s, i) => <span key={i} className="bg-green-900/40 border border-green-800 px-2 py-1 rounded text-sm font-mono text-green-300">[{s.path.join(', ')}]</span>)}
          </div>
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone || !started}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={stepBack} disabled={!started || curr <= 0}
          className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-sm font-medium rounded-lg">
          ← Back
        </button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone || !started}
          className="px-4 py-2 bg-purple-700 hover:bg-purple-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        {started && <span className="text-xs text-slate-500 self-center">{curr + 1} / {steps.length} steps</span>}
        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-500">Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))}
            className="w-24" />
          <span className="text-xs text-slate-400">{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────

export default function BacktrackingViz() {
  const [tab, setTab] = useState<'subsets' | 'perms'>('subsets');
  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">Backtracking</h3>
        <div className="flex gap-2">
          <button className={TAB_BTN(tab === 'subsets')} onClick={() => setTab('subsets')}>Subsets</button>
          <button className={TAB_BTN(tab === 'perms')} onClick={() => setTab('perms')}>Permutations</button>
        </div>
      </div>
      {tab === 'subsets' ? <SubsetsViz /> : <PermutationsViz />}
    </div>
  );
}
