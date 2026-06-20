import { useState } from 'react';

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

function parentIdx(i: number) { return Math.floor((i - 1) / 2); }
function leftIdx(i: number) { return 2 * i + 1; }
function rightIdx(i: number) { return 2 * i + 2; }

const POS: Record<number, [number, number]> = {
  0: [50, 10], 1: [25, 32], 2: [75, 32],
  3: [12, 55], 4: [37, 55], 5: [62, 55], 6: [87, 55],
};
const EDGES = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]];

// ── Min-Heap ───────────────────────────────────────────────────────────────────
function MinHeap() {
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
    setHeap(h); setInputVal(''); setHighlight(steps.flat());
    setMsg(steps.length === 0
      ? `Inserted ${val} at index ${h.length - 1}. No sift-up needed.`
      : `Inserted ${val}, sifted up ${steps.length} time(s) to maintain heap property.`);
    setTimeout(() => setHighlight([]), 1200);
  }

  function extractMin() {
    if (heap.length === 0) return;
    const min = heap[0];
    const h = [...heap];
    h[0] = h[h.length - 1]; h.pop();
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
    setHeap(h); setHighlight(swaps.flat());
    setMsg(`Extracted min = ${min}. Moved last element to root, sifted down ${swaps.length} time(s).`);
    setTimeout(() => setHighlight([]), 1200);
  }

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">Insert (sift-up) and Extract-Min (sift-down)</p>
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
      <div className="bg-slate-900/60 rounded-lg p-2">
        <svg viewBox="0 0 400 160" className="w-full max-w-md mx-auto" style={{ height: 160 }}>
          {EDGES.filter(([a, b]) => a < heap.length && b < heap.length).map(([a, b]) => (
            <line key={`${a}-${b}`} x1={`${POS[a][0]}%`} y1={POS[a][1] * 1.5 + 10} x2={`${POS[b][0]}%`} y2={POS[b][1] * 1.5 + 10} stroke="#334155" strokeWidth="2" />
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

// ── Heap helpers (min/max) ─────────────────────────────────────────────────────
function heapPush(h: number[], val: number, cmp: (a: number, b: number) => boolean) {
  h.push(val);
  let i = h.length - 1;
  while (i > 0) {
    const p = parentIdx(i);
    if (cmp(h[i], h[p])) { [h[i], h[p]] = [h[p], h[i]]; i = p; } else break;
  }
}
function heapPop(h: number[], cmp: (a: number, b: number) => boolean): number {
  const top = h[0];
  h[0] = h[h.length - 1]; h.pop();
  let i = 0;
  while (true) {
    let best = i, l = leftIdx(i), r = rightIdx(i);
    if (l < h.length && cmp(h[l], h[best])) best = l;
    if (r < h.length && cmp(h[r], h[best])) best = r;
    if (best === i) break;
    [h[i], h[best]] = [h[best], h[i]]; i = best;
  }
  return top;
}
const minCmp = (a: number, b: number) => a < b;
const maxCmp = (a: number, b: number) => a > b;

const DEFAULT_STREAM = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6];

// ── Two Heaps Median ───────────────────────────────────────────────────────────
function TwoHeapsMedian() {
  // small = max-heap (stored negated for intuition display), large = min-heap
  const [small, setSmall] = useState<number[]>([]); // actual max-heap values
  const [large, setLarge] = useState<number[]>([]); // min-heap values
  const [streamIdx, setStreamIdx] = useState(0);
  const [msg, setMsg] = useState('Two Heaps Median. Press "Next Step" to add each number.');
  const [stream] = useState(DEFAULT_STREAM);

  function reset() {
    setSmall([]); setLarge([]); setStreamIdx(0);
    setMsg('Reset. Press "Next Step" to start.');
  }

  function addNum() {
    if (streamIdx >= stream.length) return;
    const num = stream[streamIdx];
    const s = [...small], l = [...large];

    // Step 1: push to small (max-heap)
    heapPush(s, num, maxCmp);
    // Step 2: balance — if small top > large top, move to large
    if (l.length > 0 && s[0] > l[0]) {
      heapPush(l, heapPop(s, maxCmp), minCmp);
    }
    // Step 3: size balance — small can be at most 1 larger
    if (s.length > l.length + 1) {
      heapPush(l, heapPop(s, maxCmp), minCmp);
    } else if (l.length > s.length) {
      heapPush(s, heapPop(l, minCmp), maxCmp);
    }

    const median = s.length === l.length
      ? (s[0] + l[0]) / 2
      : s[0];

    setSmall(s); setLarge(l); setStreamIdx(streamIdx + 1);
    setMsg(`Add ${num} → small=[${s.join(',')}], large=[${l.join(',')}], median=${median}`);
  }

  const median = small.length === 0 ? null
    : small.length === large.length ? (small[0] + large[0]) / 2
    : small[0];

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">small = max-heap (lower half), large = min-heap (upper half)</p>
      <div className="flex items-center gap-3 flex-wrap">
        <div className="text-sm text-slate-400 font-mono">
          Stream: [{stream.map((v, i) => (
            <span key={i} className={i < streamIdx ? 'text-slate-600' : i === streamIdx ? 'text-yellow-400 font-bold' : 'text-slate-300'}>{i > 0 ? ', ' : ''}{v}</span>
          ))}]
        </div>
      </div>

      <div className="flex gap-6 flex-wrap">
        {/* Small (max-heap) */}
        <div className="flex-1 min-w-40">
          <div className="text-xs text-slate-500 mb-2">small (max-heap) — lower half</div>
          <div className="flex gap-1 flex-wrap">
            {small.length === 0
              ? <span className="text-xs text-slate-600 font-mono">[]</span>
              : small.map((v, i) => (
                <span key={i} className={`px-2 py-1 rounded text-sm font-mono border ${i === 0 ? 'bg-purple-900/60 border-purple-500 text-purple-200' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>{v}</span>
              ))}
          </div>
        </div>
        {/* Large (min-heap) */}
        <div className="flex-1 min-w-40">
          <div className="text-xs text-slate-500 mb-2">large (min-heap) — upper half</div>
          <div className="flex gap-1 flex-wrap">
            {large.length === 0
              ? <span className="text-xs text-slate-600 font-mono">[]</span>
              : large.map((v, i) => (
                <span key={i} className={`px-2 py-1 rounded text-sm font-mono border ${i === 0 ? 'bg-blue-900/60 border-blue-500 text-blue-200' : 'bg-slate-700 border-slate-600 text-slate-300'}`}>{v}</span>
              ))}
          </div>
        </div>
      </div>

      {/* Median badge */}
      {median !== null && (
        <div className="flex justify-center">
          <div className="bg-green-900/40 border border-green-600 rounded-xl px-8 py-4 text-center">
            <div className="text-xs text-green-400 mb-1">Current Median</div>
            <div className="text-3xl font-bold text-green-300 font-mono">{median}</div>
            <div className="text-xs text-slate-500 mt-1">{small.length === large.length ? 'even — avg of two tops' : 'odd — top of small'}</div>
          </div>
        </div>
      )}

      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>
      <div className="flex gap-3">
        <button onClick={addNum} disabled={streamIdx >= stream.length}
          className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
          Next Step
        </button>
        <button onClick={reset} className="px-4 py-2 bg-slate-600 hover:bg-slate-500 text-white text-sm font-medium rounded-lg">Reset</button>
      </div>
    </div>
  );
}

// ── Root ───────────────────────────────────────────────────────────────────────
export default function HeapViz() {
  const [tab, setTab] = useState<'Min Heap' | 'Two Heaps — Median'>('Min Heap');
  const tabs = ['Min Heap', 'Two Heaps — Median'] as const;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">Heap Visualizer</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`${TAB_BTN} ${tab === t ? ACTIVE : INACTIVE}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'Min Heap' ? <MinHeap /> : <TwoHeapsMedian />}
    </div>
  );
}
