import { useState } from 'react';

const DEFAULT: [number, number][] = [[1,3],[2,6],[8,10],[15,18]];

export default function IntervalsViz() {
  const [intervals, setIntervals] = useState<[number,number][]>(DEFAULT);
  const [step, setStep] = useState(0);
  const [merged, setMerged] = useState<[number,number][]>([]);
  const [msg, setMsg] = useState('Intervals sorted by start. Press "Next Step" to merge.');

  const sorted = [...intervals].sort((a, b) => a[0] - b[0]);
  const max = Math.max(...intervals.map(i => i[1])) + 1;

  function reset() {
    setStep(0); setMerged([]);
    setMsg('Intervals sorted by start. Press "Next Step" to merge.');
  }

  function next() {
    if (step >= sorted.length) return;
    const curr = sorted[step];
    const m = [...merged];

    if (m.length === 0 || m[m.length - 1][1] < curr[0]) {
      m.push([...curr]);
      setMsg(`[${curr}] does NOT overlap with last merged → push as new interval.`);
    } else {
      const last = m[m.length - 1];
      const newEnd = Math.max(last[1], curr[1]);
      setMsg(`[${curr}] overlaps with [${last}] → merge: end = max(${last[1]}, ${curr[1]}) = ${newEnd}`);
      m[m.length - 1] = [last[0], newEnd];
    }
    setMerged(m);
    setStep(step + 1);
    if (step + 1 >= sorted.length) setMsg(prev => prev + `. Done! ${m.length} merged interval(s).`);
  }

  const scale = 480 / (max + 1);

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Merge Intervals</h3>
        <p className="text-sm text-slate-400">Sort by start, merge overlapping intervals greedily</p>
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4 overflow-x-auto">
        <svg width="100%" viewBox={`0 0 500 ${(intervals.length + merged.length + 2) * 28 + 10}`} style={{ minWidth: 320 }}>
          {/* Axis */}
          <line x1="10" y1="5" x2={max * scale + 10} y2="5" stroke="#334155" strokeWidth="1" />
          {Array.from({ length: max + 1 }, (_, i) => (
            <g key={i}>
              <line x1={i * scale + 10} y1="3" x2={i * scale + 10} y2="7" stroke="#475569" strokeWidth="1" />
              <text x={i * scale + 10} y="18" textAnchor="middle" fill="#64748b" fontSize="9">{i}</text>
            </g>
          ))}

          {/* Original intervals */}
          {sorted.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + i * 28} width={(e - s) * scale} height="18"
                fill={i < step ? '#1e3a5f' : i === step ? '#1d4ed8' : '#1e293b'}
                stroke={i < step ? '#334155' : i === step ? '#60a5fa' : '#475569'} strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + i * 28 + 13} fill="#94a3b8" fontSize="10">[{s},{e}]</text>
            </g>
          ))}

          {/* Separator */}
          <line x1="10" y1={28 + sorted.length * 28 + 8} x2={max * scale + 10} y2={28 + sorted.length * 28 + 8} stroke="#334155" strokeWidth="1" strokeDasharray="4" />
          <text x="12" y={28 + sorted.length * 28 + 20} fill="#64748b" fontSize="9">merged:</text>

          {/* Merged intervals */}
          {merged.map(([s, e], i) => (
            <g key={i}>
              <rect x={s * scale + 10} y={28 + sorted.length * 28 + 24 + i * 28} width={(e - s) * scale} height="18"
                fill="#14532d" stroke="#22c55e" strokeWidth="1.5" rx="3" />
              <text x={s * scale + 15} y={28 + sorted.length * 28 + 24 + i * 28 + 13} fill="#86efac" fontSize="10">[{s},{e}]</text>
            </g>
          ))}
        </svg>
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>

      <div className="flex gap-3">
        <button onClick={next} disabled={step >= sorted.length} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
        <button onClick={reset} className="px-3 py-2 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded-lg">Reset</button>
      </div>
    </div>
  );
}
