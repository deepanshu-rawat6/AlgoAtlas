import { useState } from 'react';

function parentIdx(i: number) { return Math.floor((i - 1) / 2); }
function leftIdx(i: number) { return 2 * i + 1; }
function rightIdx(i: number) { return 2 * i + 2; }

// SVG positions for heap nodes (up to 7 nodes)
const POS: Record<number, [number, number]> = {
  0: [50, 10], 1: [25, 32], 2: [75, 32],
  3: [12, 55], 4: [37, 55], 5: [62, 55], 6: [87, 55],
};
const EDGES = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]];

export default function HeapViz() {
  const [heap, setHeap] = useState<number[]>([3, 8, 5, 12, 10]);
  const [inputVal, setInputVal] = useState('');
  const [highlight, setHighlight] = useState<number[]>([]);
  const [msg, setMsg] = useState('Min-Heap. Insert a value or Extract Min to see sift operations.');

  function insert() {
    const val = parseInt(inputVal);
    if (isNaN(val)) return;
    const h = [...heap, val];
    let i = h.length - 1;
    const steps: number[][] = [];
    while (i > 0 && h[parentIdx(i)] > h[i]) {
      steps.push([i, parentIdx(i)]);
      [h[i], h[parentIdx(i)]] = [h[parentIdx(i)], h[i]];
      i = parentIdx(i);
    }
    setHeap(h);
    setInputVal('');
    setHighlight(steps.flat());
    setMsg(steps.length === 0
      ? `Inserted ${val} at index ${h.length - 1}. No sift-up needed.`
      : `Inserted ${val}, sifted up ${steps.length} time(s) to maintain heap property.`);
    setTimeout(() => setHighlight([]), 1200);
  }

  function extractMin() {
    if (heap.length === 0) return;
    const min = heap[0];
    const h = [...heap];
    h[0] = h[h.length - 1];
    h.pop();
    let i = 0;
    const swaps: number[][] = [];
    while (true) {
      let smallest = i;
      const l = leftIdx(i), r = rightIdx(i);
      if (l < h.length && h[l] < h[smallest]) smallest = l;
      if (r < h.length && h[r] < h[smallest]) smallest = r;
      if (smallest === i) break;
      swaps.push([i, smallest]);
      [h[i], h[smallest]] = [h[smallest], h[i]];
      i = smallest;
    }
    setHeap(h);
    setHighlight(swaps.flat());
    setMsg(`Extracted min = ${min}. Moved last element to root, sifted down ${swaps.length} time(s).`);
    setTimeout(() => setHighlight([]), 1200);
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Min-Heap</h3>
        <p className="text-sm text-slate-400">Insert (sift-up) and Extract-Min (sift-down)</p>
      </div>

      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block text-xs text-slate-400 mb-1">Insert value</label>
          <input className="w-24 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={inputVal} onChange={e => setInputVal(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && insert()} placeholder="e.g. 4" />
        </div>
        <button onClick={insert} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm font-medium rounded-lg">Insert</button>
        <button onClick={extractMin} disabled={heap.length === 0} className="px-4 py-2 bg-orange-700 hover:bg-orange-600 disabled:opacity-40 text-white text-sm font-medium rounded-lg">Extract Min</button>
      </div>

      {/* SVG Heap */}
      <div className="bg-slate-900/60 rounded-lg p-2">
        <svg viewBox="0 0 400 160" className="w-full max-w-md mx-auto" style={{ height: 160 }}>
          {EDGES.filter(([a, b]) => a < heap.length && b < heap.length).map(([a, b]) => (
            <line key={`${a}-${b}`}
              x1={`${POS[a][0]}%`} y1={POS[a][1] * 1.5 + 10}
              x2={`${POS[b][0]}%`} y2={POS[b][1] * 1.5 + 10}
              stroke="#334155" strokeWidth="2" />
          ))}
          {heap.slice(0, 7).map((val, i) => {
            const isHl = highlight.includes(i);
            return (
              <g key={i}>
                <circle cx={`${POS[i][0]}%`} cy={POS[i][1] * 1.5 + 10} r="16"
                  fill={i === 0 ? '#1d4ed8' : isHl ? '#92400e' : '#1e293b'}
                  stroke={i === 0 ? '#60a5fa' : isHl ? '#fbbf24' : '#475569'} strokeWidth="2" />
                <text x={`${POS[i][0]}%`} y={POS[i][1] * 1.5 + 15} textAnchor="middle" fill="white" fontSize="12" fontWeight="bold">{val}</text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* Array representation */}
      <div className="flex gap-1 flex-wrap items-center">
        <span className="text-xs text-slate-500 font-mono">Array:</span>
        {heap.map((v, i) => (
          <span key={i} className={`px-2 py-1 rounded text-sm font-mono border ${i === 0 ? 'bg-blue-900/50 border-blue-700 text-blue-300' : highlight.includes(i) ? 'bg-yellow-900/50 border-yellow-700 text-yellow-300' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>{v}</span>
        ))}
      </div>

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>
    </div>
  );
}
