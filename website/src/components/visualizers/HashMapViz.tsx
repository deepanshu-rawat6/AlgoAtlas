import { useState, useRef, useEffect } from 'react';

const TS_DEFAULT = [2, 7, 11, 15];
const TS_TARGET = 9;
const PS_DEFAULT = [1, 1, 1, 2, 3];
const PS_K = 3;

// ── Two Sum tab ──────────────────────────────────────────────────────────────
interface TSSnap { step: number; map: Record<number, number>; found: [number, number] | null; msg: string; }

function TwoSumTab() {
  const [arrInput, setArrInput] = useState(TS_DEFAULT.join(', '));
  const [tgtInput, setTgtInput] = useState(String(TS_TARGET));
  const [step, setStep] = useState(-1);
  const [map, setMap] = useState<Record<number, number>>({});
  const [found, setFound] = useState<[number, number] | null>(null);
  const [msg, setMsg] = useState('Press "Next Step" to walk through Two Sum hash map lookup.');
  const [history, setHistory] = useState<TSSnap[]>([]);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const nextRef = useRef<() => void>(() => {});

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const target = parseInt(tgtInput) || TS_TARGET;

  function reset() {
    setPlaying(false);
    setHistory([]);
    setStep(-1); setMap({}); setFound(null);
    setMsg('Press "Next Step" to walk through Two Sum hash map lookup.');
  }

  function next() {
    if (found || step >= arr.length - 1) return;
    const ni = step + 1;
    const complement = target - arr[ni];
    setHistory(h => [...h, { step, map, found, msg }]);
    if (map[complement] !== undefined) {
      setFound([map[complement], ni]);
      setMsg(`✓ Found! arr[${map[complement]}]=${complement} + arr[${ni}]=${arr[ni]} = ${target}`);
    } else {
      setMap(prev => ({ ...prev, [arr[ni]]: ni }));
      setMsg(`i=${ni}: arr[${ni}]=${arr[ni]}, complement=${complement} not in map → store {${arr[ni]}: ${ni}}`);
    }
    setStep(ni);
  }

  useEffect(() => { nextRef.current = next; });

  const done = found !== null || (step >= arr.length - 1 && step >= 0);

  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed]);

  useEffect(() => { if (done) setPlaying(false); }, [done]);

  function stepBack() {
    setPlaying(false);
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setStep(s.step); setMap(s.map); setFound(s.found); setMsg(s.msg);
      return prev;
    });
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={arrInput} onChange={e => { setArrInput(e.target.value); reset(); }} />
        </div>
        <div className="w-24">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Target</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={tgtInput} onChange={e => { setTgtInput(e.target.value); reset(); }} />
        </div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, i) => {
          const isFound = found && (i === found[0] || i === found[1]);
          const isActive = i === step && !isFound;
          const cellStyle = isFound
            ? {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'}
            : isActive
              ? {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'}
              : {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
          return (
            <div key={i} className="flex flex-col items-center gap-1">
              <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg" style={cellStyle}>{v}</div>
              <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{i}]</div>
            </div>
          );
        })}
      </div>

      <div className="rounded-lg p-4" style={{background:'var(--surface-sunken)'}}>
        <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem',fontFamily:'var(--mono)'}}>HashMap: seen = {'{'}</div>
        <div className="flex flex-wrap gap-2 ml-4">
          {Object.entries(map).length === 0
            ? <span style={{color:'var(--text-faint)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>empty</span>
            : Object.entries(map).map(([k, v]) => (
                <span key={k} style={{fontSize:'0.875rem',fontFamily:'var(--mono)',background:'var(--surface-raised)',border:'1px solid var(--border)',padding:'0.25rem 0.5rem',borderRadius:'0.25rem',color:'var(--accent)'}}>{k}: {v}</span>
              ))}
        </div>
        <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginTop:'0.5rem',fontFamily:'var(--mono)'}}>{'}'}</div>
      </div>

      <div className={found ? '' : 'viz-info'}
        style={found ? {background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'} : undefined}>{msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={done}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={done}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Prefix Sum tab ───────────────────────────────────────────────────────────
interface PSStep {
  index: number;
  currSum: number;
  prefixMap: Record<number, number>;
  count: number;
  foundRanges: [number, number][];
  done: boolean;
  msg: string;
}

function buildPSSteps(arr: number[], k: number): PSStep[] {
  const steps: PSStep[] = [];
  let currSum = 0;
  let count = 0;
  const prefixMap: Record<number, number> = { 0: 1 };
  const foundRanges: [number, number][] = [];

  steps.push({ index: -1, currSum: 0, prefixMap: { 0: 1 }, count: 0, foundRanges: [], done: false,
    msg: 'Initial: prefix_map={0:1}, curr_sum=0. Press "Next Step".' });

  for (let i = 0; i < arr.length; i++) {
    currSum += arr[i];
    const need = currSum - k;
    const snapMap = { ...prefixMap };
    let newCount = count;
    const newRanges = [...foundRanges];

    if (snapMap[need] !== undefined) {
      newCount += snapMap[need];
      newRanges.push([i - (snapMap[need] > 0 ? 1 : 0), i]);
      steps.push({
        index: i, currSum, prefixMap: { ...snapMap, [currSum]: (snapMap[currSum] ?? 0) + 1 },
        count: newCount, foundRanges: newRanges, done: false,
        msg: `i=${i}: prefix=${currSum}, check ${currSum}-${k}=${need} in map → found! count+=map[${need}]=${snapMap[need]}. Total subarrays=${newCount}`,
      });
    } else {
      steps.push({
        index: i, currSum, prefixMap: { ...snapMap, [currSum]: (snapMap[currSum] ?? 0) + 1 },
        count: newCount, foundRanges: newRanges, done: false,
        msg: `i=${i}: prefix=${currSum}, check ${currSum}-${k}=${need} not in map. Store prefix ${currSum}.`,
      });
    }

    prefixMap[currSum] = (prefixMap[currSum] ?? 0) + 1;
    count = newCount;
    foundRanges.length = 0;
    newRanges.forEach(r => foundRanges.push(r));
  }

  steps[steps.length - 1] = { ...steps[steps.length - 1], done: true,
    msg: steps[steps.length - 1].msg + ` — Done! Total = ${count}.` };
  return steps;
}

function PrefixSumTab() {
  const [arrInput, setArrInput] = useState(PS_DEFAULT.join(', '));
  const [kInput, setKInput] = useState(String(PS_K));
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const k = parseInt(kInput) || PS_K;
  const steps = buildPSSteps(arr.length ? arr : PS_DEFAULT, k);

  const [stepIdx, setStepIdx] = useState(0);

  function reset() { setPlaying(false); setStepIdx(0); }

  const s = steps[stepIdx];
  const isDone = s.done;

  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => {
      setStepIdx(i => {
        if (i >= steps.length - 1) { setPlaying(false); return i; }
        return i + 1;
      });
    }, 1100 - speed * 200);
    return () => clearInterval(id);
  }, [playing, speed, steps.length]);

  useEffect(() => { if (isDone) setPlaying(false); }, [isDone]);

  function getCellStyle(i: number): React.CSSProperties {
    if (i === s.index) return {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
    for (const [lo, hi] of s.foundRanges) {
      if (i >= lo && i <= hi) return {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'};
    }
    return {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={arrInput} onChange={e => { setArrInput(e.target.value); setStepIdx(0); }} />
        </div>
        <div className="w-20">
          <label style={{display:'block',color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>K</label>
          <input className="w-full"
            style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none'}}
            value={kInput} onChange={e => { setKInput(e.target.value); setStepIdx(0); }} />
        </div>
      </div>

      <div className="flex gap-2 flex-wrap">
        {arr.map((v, i) => (
          <div key={i} className="flex flex-col items-center gap-1">
            <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg" style={getCellStyle(i)}>{v}</div>
            <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{i}]</div>
          </div>
        ))}
      </div>

      <div className="rounded-lg p-4" style={{background:'var(--surface-sunken)'}}>
        <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem',fontFamily:'var(--mono)'}}>prefix_map = {'{'}</div>
        <div className="flex flex-wrap gap-2 ml-4">
          {Object.entries(s.prefixMap).length === 0
            ? <span style={{color:'var(--text-faint)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>empty</span>
            : Object.entries(s.prefixMap).map(([pk, pv]) => (
                <span key={pk} style={{fontSize:'0.875rem',fontFamily:'var(--mono)',background:'var(--surface-raised)',border:'1px solid var(--border)',padding:'0.25rem 0.5rem',borderRadius:'0.25rem',color:'var(--accent)'}}>{pk}: {pv}</span>
              ))}
        </div>
        <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginTop:'0.5rem',fontFamily:'var(--mono)'}}>{'}'}</div>
        <div style={{color:'var(--text-dim)',fontSize:'0.75rem',marginTop:'0.5rem'}}>Subarrays found: <span style={{color:'var(--tier-3)',fontFamily:'var(--mono)',fontWeight:'bold'}}>{s.count}</span></div>
      </div>

      <div className={s.count > 0 ? '' : 'viz-info'}
        style={s.count > 0 ? {background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'} : undefined}>{s.msg}</div>

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={() => setStepIdx(i => Math.min(i + 1, steps.length - 1))} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
        <button onClick={() => { setPlaying(false); setStepIdx(i => Math.max(0, i - 1)); }} disabled={stepIdx === 0}
          className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
        <button onClick={() => setPlaying(p => !p)} disabled={isDone}
          className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={reset} className="viz-btn">Reset</button>
        <div className="flex items-center gap-2">
          <span style={{color:'var(--text-faint)',fontSize:'0.75rem'}}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{color:'var(--text-dim)',fontSize:'0.75rem'}}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────
export default function HashMapViz() {
  const [tab, setTab] = useState<'twosum' | 'prefixsum'>('twosum');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.25rem'}}>Hash Map</h3>
        <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>Trade space for time with complement / prefix lookups</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('twosum')} className={tab === 'twosum' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Two Sum</button>
        <button onClick={() => setTab('prefixsum')} className={tab === 'prefixsum' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Prefix Sum</button>
      </div>

      {tab === 'twosum' ? <TwoSumTab /> : <PrefixSumTab />}
    </div>
  );
}
