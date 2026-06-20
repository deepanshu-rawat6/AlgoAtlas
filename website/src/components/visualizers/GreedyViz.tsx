import { useState } from 'react';

const TAB_BTN = (active: boolean) =>
  `px-3 py-1.5 text-xs font-medium rounded border transition-colors ${active ? 'bg-blue-700 text-white border-blue-500' : 'bg-slate-700 text-slate-300 border-slate-600'}`;

// ── Jump Game ────────────────────────────────────────────────────────────────

const DEFAULT_JUMP = [2, 3, 1, 1, 4];

function JumpGame() {
  const [arrInput, setArrInput] = useState(DEFAULT_JUMP.join(', '));
  const [i, setI] = useState(-1);
  const [maxReach, setMaxReach] = useState(0);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [canJump, setCanJump] = useState<boolean | null>(null);
  const [msg, setMsg] = useState('Jump Game: can you reach the last index? Press "Start".');

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));

  function start() {
    setI(0); setMaxReach(arr[0] ?? 0); setStarted(true); setDone(false); setCanJump(null);
    setMsg(`Start at i=0, maxReach = arr[0] = ${arr[0]}. Press "Next Step".`);
  }

  function next() {
    if (!started || done) return;
    const ni = i + 1;
    if (ni >= arr.length) {
      setDone(true); setCanJump(maxReach >= arr.length - 1);
      setMsg(`✓ Reached end! maxReach=${maxReach} ≥ lastIndex=${arr.length - 1}`);
      return;
    }
    if (ni > maxReach) {
      setDone(true); setCanJump(false);
      setMsg(`✗ i=${ni} > maxReach=${maxReach} — can't reach here! Return false.`);
      setI(ni); return;
    }
    const newReach = Math.max(maxReach, ni + arr[ni]);
    setI(ni); setMaxReach(newReach);
    setMsg(`i=${ni}, arr[${ni}]=${arr[ni]} → maxReach = max(${maxReach}, ${ni}+${arr[ni]}) = ${newReach}`);
    if (newReach >= arr.length - 1) {
      setDone(true); setCanJump(true);
      setMsg(`i=${ni}, arr[${ni}]=${arr[ni]} → maxReach=${newReach} ≥ lastIndex=${arr.length - 1} — Can reach! ✓`);
    }
  }

  function reset() { setI(-1); setMaxReach(0); setStarted(false); setDone(false); setCanJump(null); setMsg('Jump Game: can you reach the last index? Press "Start".'); }

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">Track farthest reachable index greedily</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (max jump from each index)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => { setArrInput(e.target.value); reset(); }} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded">Start</button>
          <button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button>
        </div>
      </div>
      <div className="flex gap-2 flex-wrap">
        {arr.map((v, idx) => {
          const isCurr = idx === i;
          const isReachable = idx <= maxReach && started;
          const isBlocked = done && !canJump && idx > maxReach;
          let bg = 'bg-slate-700 border-slate-600 text-slate-400';
          if (isCurr) bg = 'bg-yellow-800 border-yellow-400 text-white';
          else if (idx === arr.length - 1 && canJump) bg = 'bg-green-800 border-green-400 text-white';
          else if (isBlocked) bg = 'bg-red-900/60 border-red-800 text-red-400';
          else if (isReachable) bg = 'bg-blue-900/50 border-blue-700 text-blue-200';
          return (
            <div key={idx} className="flex flex-col items-center gap-1">
              <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg ${bg}`}>{v}</div>
              <div className="text-xs text-slate-600">[{idx}]</div>
            </div>
          );
        })}
      </div>
      {started && (
        <div className="flex items-center gap-3 text-sm">
          <span className="text-slate-400 font-mono">maxReach:</span>
          <span className="bg-blue-900/50 border border-blue-700 px-3 py-1 rounded text-blue-300 font-mono font-bold">{maxReach}</span>
        </div>
      )}
      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${canJump === true ? 'bg-green-900/40 text-green-300' : canJump === false ? 'bg-red-900/40 text-red-300' : 'bg-slate-900/60 text-slate-300'}`}>{msg}</div>
      <button onClick={next} disabled={!started || done} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
    </div>
  );
}

// ── Merge Intervals ──────────────────────────────────────────────────────────

type Interval = [number, number];

interface MergeStep {
  current: Interval;
  merged: Interval[];
  remaining: Interval[];
  msg: string;
}

function parseIntervals(s: string): Interval[] {
  return s.trim().split(/\s+/).map(p => {
    const [a, b] = p.split(',').map(Number);
    return [a, b] as Interval;
  }).filter(([a, b]) => !isNaN(a) && !isNaN(b));
}

function buildMergeSteps(raw: Interval[]): MergeStep[] {
  const sorted = [...raw].sort((a, b) => a[0] - b[0]);
  const steps: MergeStep[] = [];
  const merged: Interval[] = [];

  for (let i = 0; i < sorted.length; i++) {
    const cur = sorted[i];
    const remaining = sorted.slice(i + 1);
    if (merged.length === 0) {
      merged.push([...cur] as Interval);
      steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `Init merged with [${cur}]` });
    } else {
      const last = merged[merged.length - 1];
      if (cur[0] <= last[1]) {
        const prev = [...last] as Interval;
        last[1] = Math.max(last[1], cur[1]);
        steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `[${cur}] overlaps with [${prev}] (${cur[0]}≤${prev[1]}) → merge to [${last}]` });
      } else {
        merged.push([...cur] as Interval);
        steps.push({ current: cur, merged: merged.map(x => [...x] as Interval), remaining, msg: `[${cur}] no overlap with [${merged[merged.length - 2]}] → add as new` });
      }
    }
  }
  return steps;
}

function MergeIntervalsViz() {
  const [input, setInput] = useState('1,3 2,6 8,10 15,18');
  const [steps, setSteps] = useState<MergeStep[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);

  function start() {
    const ivs = parseIntervals(input);
    if (ivs.length === 0) return;
    const s = buildMergeSteps(ivs);
    setSteps(s);
    setStepIdx(0);
  }

  function reset() { setSteps([]); setStepIdx(-1); }

  const step = steps[stepIdx] ?? null;
  const allIntervals = parseIntervals(input).sort((a, b) => a[0] - b[0]);
  const maxVal = allIntervals.reduce((m, [, e]) => Math.max(m, e), 0) || 1;

  const SVG_W = 340, SVG_H = 20, PAD = 10;
  function bar(iv: Interval, color: string, y: number, key: string) {
    const x1 = PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD);
    const x2 = PAD + (iv[1] / maxVal) * (SVG_W - 2 * PAD);
    return <rect key={key} x={x1} y={y} width={Math.max(x2 - x1, 4)} height={14} rx={3} fill={color} opacity={0.85} />;
  }

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">Sort intervals by start, then merge overlapping pairs</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Intervals (format: "1,3 2,6 8,10")</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={input} onChange={e => { setInput(e.target.value); reset(); }} />
        </div>
        <div className="flex items-end gap-2">
          <button onClick={start} className="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded">Start</button>
          <button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button>
        </div>
      </div>

      {/* Timeline SVG */}
      <div className="bg-slate-900/60 rounded-lg p-4 space-y-3">
        <div className="text-xs text-slate-500 mb-1">Timeline (0 → {maxVal})</div>
        {/* Axis */}
        <svg width={SVG_W} height={16}>
          <line x1={PAD} y1={8} x2={SVG_W - PAD} y2={8} stroke="#475569" strokeWidth={1} />
          {[0, 0.25, 0.5, 0.75, 1].map(t => {
            const x = PAD + t * (SVG_W - 2 * PAD);
            return <g key={t}><line x1={x} y1={4} x2={x} y2={12} stroke="#475569" strokeWidth={1} /><text x={x} y={16} textAnchor="middle" fontSize={8} fill="#94a3b8">{Math.round(t * maxVal)}</text></g>;
          })}
        </svg>

        {/* Input intervals */}
        <div>
          <div className="text-xs text-slate-500 mb-1">Input (sorted):</div>
          <svg width={SVG_W} height={allIntervals.length * 20 + 4}>
            {allIntervals.map((iv, i) => {
              const isCurr = step && iv[0] === step.current[0] && iv[1] === step.current[1];
              const isInRemaining = step?.remaining.some(r => r[0] === iv[0] && r[1] === iv[1]);
              const color = isCurr ? '#ca8a04' : isInRemaining ? '#475569' : '#1e40af';
              return <g key={i}>{bar(iv, color, i * 20, `in-${i}`)}<text x={PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD)} y={i * 20 + 11} fontSize={9} fill="#e2e8f0">{`[${iv}]`}</text></g>;
            })}
          </svg>
        </div>

        {/* Merged result */}
        {step && step.merged.length > 0 && (
          <div>
            <div className="text-xs text-slate-500 mb-1">Merged so far:</div>
            <svg width={SVG_W} height={step.merged.length * 20 + 4}>
              {step.merged.map((iv, i) => (
                <g key={i}>{bar(iv, '#15803d', i * 20, `mg-${i}`)}<text x={PAD + (iv[0] / maxVal) * (SVG_W - 2 * PAD)} y={i * 20 + 11} fontSize={9} fill="#e2e8f0">{`[${iv}]`}</text></g>
              ))}
            </svg>
          </div>
        )}
      </div>

      {step && <div className="rounded-lg px-4 py-3 text-sm font-mono bg-slate-900/60 text-slate-300">{step.msg}</div>}

      <div className="flex gap-3 items-center">
        <button onClick={() => setStepIdx(s => Math.max(0, s - 1))} disabled={stepIdx <= 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm font-medium rounded-lg">← Prev</button>
        <button onClick={() => setStepIdx(s => Math.min(steps.length - 1, s + 1))} disabled={stepIdx < 0 || stepIdx >= steps.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">Next Step →</button>
        {steps.length > 0 && <span className="text-xs text-slate-500">{stepIdx + 1} / {steps.length}</span>}
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────

export default function GreedyViz() {
  const [tab, setTab] = useState<'jump' | 'merge'>('jump');
  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">Greedy</h3>
        <div className="flex gap-2">
          <button className={TAB_BTN(tab === 'jump')} onClick={() => setTab('jump')}>Jump Game</button>
          <button className={TAB_BTN(tab === 'merge')} onClick={() => setTab('merge')}>Merge Intervals</button>
        </div>
      </div>
      {tab === 'jump' ? <JumpGame /> : <MergeIntervalsViz />}
    </div>
  );
}
