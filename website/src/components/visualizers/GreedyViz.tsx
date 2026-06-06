import { useState } from 'react';

const DEFAULT = [2, 3, 1, 1, 4];

export default function GreedyViz() {
  const [arrInput, setArrInput] = useState(DEFAULT.join(', '));
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
      setMsg(`✓ Reached end! maxReach=${maxReach} ≥ lastIndex=${arr.length-1}`);
      return;
    }
    if (ni > maxReach) {
      setDone(true); setCanJump(false);
      setMsg(`✗ i=${ni} > maxReach=${maxReach} — can't reach here! Return false.`);
      setI(ni);
      return;
    }
    const newReach = Math.max(maxReach, ni + arr[ni]);
    setI(ni); setMaxReach(newReach);
    setMsg(`i=${ni}, arr[${ni}]=${arr[ni]} → maxReach = max(${maxReach}, ${ni}+${arr[ni]}) = ${newReach}`);
    if (newReach >= arr.length - 1) {
      setDone(true); setCanJump(true);
      setMsg(prev => prev + ' — Can reach last index! ✓');
    }
  }

  function reset() { setI(-1); setMaxReach(0); setStarted(false); setDone(false); setCanJump(null); setMsg('Jump Game: can you reach the last index? Press "Start".'); }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Greedy — Jump Game</h3>
        <p className="text-sm text-slate-400">Track farthest reachable index greedily</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array (max jump from each index)</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => setArrInput(e.target.value)} />
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
