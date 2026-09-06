import { useState, useRef, useEffect } from 'react';

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
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Insert (sift-up) and Extract-Min (sift-down)</p>
      <div className="flex gap-3 items-end flex-wrap">
        <div>
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Insert value</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'6rem'}}
            value={inputVal} onChange={e => setInputVal(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && insert()} placeholder="e.g. 4" />
        </div>
        <button onClick={insert} className="viz-btn viz-btn--primary">Insert</button>
        <button onClick={extractMin} disabled={heap.length === 0} className="viz-btn">Extract Min</button>
      </div>
      <div style={{background:'var(--surface-sunken)',borderRadius:'0.5rem',padding:'0.5rem'}}>
        <svg viewBox="0 0 400 160" className="w-full max-w-md mx-auto" style={{ height: 160 }}>
          {EDGES.filter(([a, b]) => a < heap.length && b < heap.length).map(([a, b]) => (
            <line key={`${a}-${b}`} x1={`${POS[a][0]}%`} y1={POS[a][1] * 1.5 + 10} x2={`${POS[b][0]}%`} y2={POS[b][1] * 1.5 + 10} stroke="var(--border)" strokeWidth="2" />
          ))}
          {heap.slice(0, 7).map((val, i) => {
            const isHl = highlight.includes(i);
            return (
              <g key={i}>
                <circle cx={`${POS[i][0]}%`} cy={POS[i][1] * 1.5 + 10} r="16"
                  fill={i === 0 ? 'var(--accent)' : isHl ? 'var(--accent-soft)' : 'var(--surface-raised)'}
                  stroke={i === 0 ? 'var(--accent)' : isHl ? 'var(--accent)' : 'var(--border)'} strokeWidth="2" />
                <text x={`${POS[i][0]}%`} y={POS[i][1] * 1.5 + 15} textAnchor="middle" fill="var(--text)" fontSize="12" fontWeight="bold">{val}</text>
              </g>
            );
          })}
        </svg>
      </div>
      <div className="flex gap-1 flex-wrap items-center">
        <span style={{color:'var(--text-faint)',fontSize:'0.75rem',fontFamily:'var(--mono)'}}>Array:</span>
        {heap.map((v, i) => (
          <span key={i} className="px-2 py-1 rounded text-sm font-mono border"
            style={i === 0
              ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
              : highlight.includes(i)
                ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
                : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
            }>{v}</span>
        ))}
      </div>
      <div className="viz-info">{msg}</div>
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

type TwoHeapSnapshot = { small: number[], large: number[], streamIdx: number, msg: string };

// ── Two Heaps Median ───────────────────────────────────────────────────────────
function TwoHeapsMedian() {
  // small = max-heap (stored negated for intuition display), large = min-heap
  const [small, setSmall] = useState<number[]>([]); // actual max-heap values
  const [large, setLarge] = useState<number[]>([]); // min-heap values
  const [streamIdx, setStreamIdx] = useState(0);
  const [msg, setMsg] = useState('Two Heaps Median. Press "Next Step" to add each number.');
  const [stream] = useState(DEFAULT_STREAM);
  const [history, setHistory] = useState<TwoHeapSnapshot[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const nextStepRef = useRef<() => void>(() => {});

  function reset() {
    setPlaying(false);
    setSmall([]); setLarge([]); setStreamIdx(0); setHistory([]);
    setMsg('Reset. Press "Next Step" to start.');
  }

  function addNum(s: number[], l: number[], idx: number) {
    const num = stream[idx];
    const sh = [...s], lh = [...l];
    heapPush(sh, num, maxCmp);
    if (lh.length > 0 && sh[0] > lh[0]) {
      heapPush(lh, heapPop(sh, maxCmp), minCmp);
    }
    if (sh.length > lh.length + 1) {
      heapPush(lh, heapPop(sh, maxCmp), minCmp);
    } else if (lh.length > sh.length) {
      heapPush(sh, heapPop(lh, minCmp), maxCmp);
    }
    const median = sh.length === lh.length ? (sh[0] + lh[0]) / 2 : sh[0];
    const newMsg = `Add ${num} → small=[${sh.join(',')}], large=[${lh.join(',')}], median=${median}`;
    setSmall(sh); setLarge(lh); setStreamIdx(idx + 1); setMsg(newMsg);
  }

  function nextStep() {
    if (streamIdx >= stream.length) { setPlaying(false); return; }
    setHistory(h => [...h, { small: [...small], large: [...large], streamIdx, msg }]);
    addNum(small, large, streamIdx);
  }

  function stepBack() {
    setPlaying(false);
    if (history.length === 0) return;
    const prev = history[history.length - 1];
    setSmall(prev.small);
    setLarge(prev.large);
    setStreamIdx(prev.streamIdx);
    setMsg(prev.msg);
    setHistory(h => h.slice(0, -1));
  }

  useEffect(() => { nextStepRef.current = nextStep; });

  useEffect(() => {
    if (!playing) {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
      return;
    }
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
    return () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
  }, [playing, speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const isDone = streamIdx >= stream.length;
  const median = small.length === 0 ? null
    : small.length === large.length ? (small[0] + large[0]) / 2
    : small[0];

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>small = max-heap (lower half), large = min-heap (upper half)</p>
      <div className="flex items-center gap-3 flex-wrap">
        <div className="font-mono" style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>
          Stream: [{stream.map((v, i) => (
            <span key={i} style={{color: i < streamIdx ? 'var(--text-faint)' : i === streamIdx ? 'var(--accent)' : 'var(--text)', fontWeight: i === streamIdx ? 700 : undefined}}>{i > 0 ? ', ' : ''}{v}</span>
          ))}]
        </div>
      </div>

      <div className="flex gap-6 flex-wrap">
        {/* Small (max-heap) */}
        <div className="flex-1 min-w-40">
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>small (max-heap) — lower half</div>
          <div className="flex gap-1 flex-wrap">
            {small.length === 0
              ? <span style={{color:'var(--text-faint)',fontFamily:'var(--mono)',fontSize:'0.75rem'}}>[]</span>
              : small.map((v, i) => (
                <span key={i} className="px-2 py-1 rounded text-sm font-mono border"
                  style={i === 0
                    ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
                    : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
                  }>{v}</span>
              ))}
          </div>
        </div>
        {/* Large (min-heap) */}
        <div className="flex-1 min-w-40">
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>large (min-heap) — upper half</div>
          <div className="flex gap-1 flex-wrap">
            {large.length === 0
              ? <span style={{color:'var(--text-faint)',fontFamily:'var(--mono)',fontSize:'0.75rem'}}>[]</span>
              : large.map((v, i) => (
                <span key={i} className="px-2 py-1 rounded text-sm font-mono border"
                  style={i === 0
                    ? {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text)'}
                    : {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'}
                  }>{v}</span>
              ))}
          </div>
        </div>
      </div>

      {/* Median badge */}
      {median !== null && (
        <div className="flex justify-center">
          <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.75rem',padding:'1rem 2rem',textAlign:'center'}}>
            <div style={{color:'var(--tier-3)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Current Median</div>
            <div style={{color:'var(--tier-3)',fontSize:'1.875rem',fontWeight:700,fontFamily:'var(--mono)'}}>{median}</div>
            <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginTop:'0.25rem'}}>{small.length === large.length ? 'even — avg of two tops' : 'odd — top of small'}</div>
          </div>
        </div>
      )}

      <div className="viz-info">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
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

// ── Root ───────────────────────────────────────────────────────────────────────
export default function HeapViz() {
  const [tab, setTab] = useState<'Min Heap' | 'Two Heaps — Median'>('Min Heap');
  const tabs = ['Min Heap', 'Two Heaps — Median'] as const;

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>Heap Visualizer</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`viz-btn${tab === t ? ' viz-btn--primary' : ''}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'Min Heap' ? <MinHeap /> : <TwoHeapsMedian />}
    </div>
  );
}
