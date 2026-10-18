import { useState, useRef, useEffect } from 'react';

// ── Two Sum II tab ───────────────────────────────────────────────────────────
const TS2_DEFAULT = [1, 2, 4, 6, 8, 9, 14, 15];
const TS2_TARGET = 13;

type TS2Phase = 'idle' | 'found' | 'done';
interface TS2State {
  array: number[]; target: number;
  left: number; right: number; phase: TS2Phase;
  foundLeft: number; foundRight: number; message: string;
}

function ts2Init(array: number[], target: number): TS2State {
  const sorted = [...array].sort((a, b) => a - b);
  return { array: sorted, target, left: 0, right: sorted.length - 1, phase: 'idle', foundLeft: -1, foundRight: -1,
    message: `Array sorted. Find two numbers summing to ${target}. Press "Next Step".` };
}

function ts2Step(s: TS2State): TS2State {
  const { array, target, left, right } = s;
  if (left >= right) return { ...s, phase: 'done', message: `No pair found that sums to ${target}.` };
  const sum = array[left] + array[right];
  if (sum === target) return { ...s, phase: 'found', foundLeft: left, foundRight: right,
    message: `Found! arr[${left}]=${array[left]} + arr[${right}]=${array[right]} = ${sum} ✓` };
  if (sum < target) return { ...s, left: left + 1,
    message: `Sum ${sum} < ${target} → move left pointer right (need larger values)` };
  return { ...s, right: right - 1,
    message: `Sum ${sum} > ${target} → move right pointer left (need smaller values)` };
}

function TwoSumIITab() {
  const [arrayInput, setArrayInput] = useState(TS2_DEFAULT.join(', '));
  const [targetInput, setTargetInput] = useState(String(TS2_TARGET));
  const [state, setState] = useState<TS2State>(() => ts2Init(TS2_DEFAULT, TS2_TARGET));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<TS2State[]>([]);
  const mountedTS2Ref = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }
  function reset() {
    stopPlay();
    setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    const tgt = parseInt(targetInput) || TS2_TARGET;
    setState(ts2Init(arr.length ? arr : TS2_DEFAULT, tgt));
  }
  function nextStep() {
    setState(prev => {
      if (prev.phase === 'found' || prev.phase === 'done') return prev;
      setHistory(h => [...h, prev]);
      return ts2Step(prev);
    });
  }
  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
      return prev;
    });
  }
  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; } return ts2Step(prev); });
    }, 1100 - speed * 200);
  }
  useEffect(() => {
    if (!mountedTS2Ref.current) { mountedTS2Ref.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.phase === 'found' || prev.phase === 'done') { stopPlay(); return prev; } return ts2Step(prev); });
    }, 1100 - speed * 200);
  }, [speed]);
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, left, right, phase, foundLeft, foundRight, message } = state;
  const done = phase === 'found' || phase === 'done';

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Array (will be sorted)</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Target</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={targetInput} onChange={e => setTargetInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, i) => {
            const isLeft = i === left, isRight = i === right;
            const isFound = phase === 'found' && (i === foundLeft || i === foundRight);
            let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)' };
            if (isFound) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)' };
            else if (isLeft) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', borderColor: 'var(--tier-3)' };
            else if (isRight) cellStyle = { background: 'color-mix(in srgb, #ef4444 15%, transparent)', borderColor: '#ef4444' };
            return (
              <div key={i} className="flex flex-col items-center gap-1">
                <div style={cellStyle} className="w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg">
                  <span style={{ color: 'var(--text)' }}>{val}</span>
                </div>
                <div className="text-xs h-4" style={{ color: isLeft ? 'var(--tier-3)' : isRight ? '#f87171' : 'transparent' }}>
                  {isLeft ? 'L' : isRight ? 'R' : '.'}
                </div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{i}</div>
              </div>
            );
          })}
        </div>
      </div>

      {phase === 'found'
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)', minHeight: '3rem' }}>{message}</div>
        : phase === 'done'
        ? <div style={{ background: 'color-mix(in srgb, #ef4444 15%, transparent)', border: '1px solid #ef4444', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: '#ef4444', fontSize: '0.875rem', fontFamily: 'var(--mono)', minHeight: '3rem' }}>{message}</div>
        : <div className="viz-info">{message}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── 3Sum tab ─────────────────────────────────────────────────────────────────
const TS3_DEFAULT = [-1, 0, 1, 2, -1, -4];

interface TS3State {
  array: number[];        // sorted
  i: number;              // outer pointer
  left: number;
  right: number;
  triplets: [number, number, number][];
  done: boolean;
  message: string;
}

function ts3Init(raw: number[]): TS3State {
  const array = [...raw].sort((a, b) => a - b);
  return { array, i: 0, left: 1, right: array.length - 1, triplets: [], done: array.length < 3,
    message: `Sorted: [${array.join(', ')}]. Fix i=0 (val=${array[0]}), L=1, R=${array.length - 1}. Press "Next Step".` };
}

function ts3Step(s: TS3State): TS3State {
  const { array, triplets } = s;
  const n = array.length;
  let { i, left, right } = s;

  // Skip duplicate i
  if (i > 0 && array[i] === array[i - 1]) {
    i++;
    if (i >= n - 2) return { ...s, done: true, message: `Done! Found ${triplets.length} triplet(s).` };
    left = i + 1; right = n - 1;
    return { ...s, i, left, right, message: `Skip duplicate i=${i} (val=${array[i]}). L=${left}, R=${right}.` };
  }

  if (left >= right) {
    // advance i
    const ni = i + 1;
    if (ni >= n - 2) return { ...s, done: true, message: `Done! Found ${triplets.length} triplet(s).` };
    // skip duplicate ni
    let nii = ni;
    while (nii < n - 2 && array[nii] === array[nii - 1] && nii > 0) nii++;
    return { ...s, i: nii, left: nii + 1, right: n - 1,
      message: `L≥R, advance i → Fix i=${nii} (val=${array[nii]}), L=${nii + 1}, R=${n - 1}.` };
  }

  const sum = array[i] + array[left] + array[right];

  if (sum === 0) {
    const triplet: [number, number, number] = [array[i], array[left], array[right]];
    const newTriplets = [...triplets, triplet];
    // skip duplicates at left and right
    let nl = left + 1, nr = right - 1;
    while (nl < nr && array[nl] === array[nl - 1]) nl++;
    while (nl < nr && array[nr] === array[nr + 1]) nr--;
    return { ...s, triplets: newTriplets, left: nl, right: nr,
      message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${array[i]}+(${array[left]})+(${array[right]})=0 → triplet found! [${triplet.join(',')}]` };
  }

  if (sum < 0) {
    return { ...s, left: left + 1, message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${sum}<0 → move L right.` };
  }

  return { ...s, right: right - 1, message: `Fix i=${i} (val=${array[i]}), L=${left}, R=${right}: sum=${sum}>0 → move R left.` };
}

function ThreeSumTab() {
  const [arrayInput, setArrayInput] = useState(TS3_DEFAULT.join(', '));
  const [state, setState] = useState<TS3State>(() => ts3Init(TS3_DEFAULT));
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<TS3State[]>([]);
  const mountedTS3Ref = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    setHistory([]);
    const arr = arrayInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
    setState(ts3Init(arr.length >= 3 ? arr : TS3_DEFAULT));
  }

  function nextStep() {
    setState(prev => {
      if (prev.done) return prev;
      setHistory(h => [...h, prev]);
      return ts3Step(prev);
    });
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setState(s);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return ts3Step(prev); });
    }, 1100 - speed * 200);
  }

  useEffect(() => {
    if (!mountedTS3Ref.current) { mountedTS3Ref.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => {
      setState(prev => { if (prev.done) { stopPlay(); return prev; } return ts3Step(prev); });
    }, 1100 - speed * 200);
  }, [speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const { array, i, left, right, triplets, done, message } = state;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Array (will be sorted)</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={arrayInput} onChange={e => setArrayInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      <div className="overflow-x-auto pb-2">
        <div className="flex gap-1 min-w-max">
          {array.map((val, idx) => {
            const isI = idx === i;
            const isLeft = idx === left;
            const isRight = idx === right;
            let cellStyle = { background: 'var(--surface-raised)', borderColor: 'var(--border)' };
            if (isI) cellStyle = { background: 'color-mix(in srgb, #f97316 20%, transparent)', borderColor: '#f97316' };
            else if (isLeft) cellStyle = { background: 'color-mix(in srgb, var(--tier-3) 20%, transparent)', borderColor: 'var(--tier-3)' };
            else if (isRight) cellStyle = { background: 'color-mix(in srgb, #ef4444 15%, transparent)', borderColor: '#ef4444' };
            const label = isI ? 'i' : isLeft ? 'L' : isRight ? 'R' : '';
            const labelColor = isI ? '#fb923c' : isLeft ? 'var(--tier-3)' : '#f87171';
            return (
              <div key={idx} className="flex flex-col items-center gap-1">
                <div style={cellStyle} className="w-12 h-12 flex items-center justify-center font-mono font-bold text-lg border-2 rounded-lg">
                  <span style={{ color: 'var(--text)' }}>{val}</span>
                </div>
                <div className="text-xs h-4 font-medium" style={{ color: label ? labelColor : 'transparent' }}>{label || '.'}</div>
                <div style={{ color: 'var(--text-faint)', fontSize: '0.7rem' }}>{idx}</div>
              </div>
            );
          })}
        </div>
      </div>

      {triplets.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {triplets.map((t, idx) => (
            <span key={idx} style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.375rem', padding: '0.25rem 0.5rem', color: 'var(--tier-3)', fontFamily: 'var(--mono)', fontSize: '0.75rem' }}>
              [{t.join(', ')}]
            </span>
          ))}
        </div>
      )}

      {done
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)', minHeight: '3rem' }}>{message}</div>
        : <div className="viz-info">{message}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Container With Most Water tab ────────────────────────────────────────────
const CWW_DEFAULT = [1, 8, 6, 2, 5, 4, 8, 3, 7];

interface ContainerStep { left: number; right: number; currentArea: number; maxArea: number; msg: string; }

function buildContainerSteps(heights: number[]): ContainerStep[] {
  const steps: ContainerStep[] = [];
  const n = heights.length;
  let left = 0, right = n - 1, maxArea = 0;

  while (left < right) {
    const area = Math.min(heights[left], heights[right]) * (right - left);
    maxArea = Math.max(maxArea, area);
    const moveLeft = heights[left] <= heights[right];
    const nextLeft = moveLeft ? left + 1 : left;
    const nextRight = moveLeft ? right : right - 1;
    steps.push({
      left, right, currentArea: area, maxArea,
      msg: `L=${left}(h=${heights[left]}), R=${right}(h=${heights[right]}): area = min(${heights[left]},${heights[right]})×${right - left} = ${area}. maxArea=${maxArea}. Move ${moveLeft ? 'L right' : 'R left'}.`,
    });
    left = nextLeft;
    right = nextRight;
  }
  if (steps.length > 0) {
    const last = steps[steps.length - 1];
    steps.push({ ...last, left, right, currentArea: 0, msg: `Done! Max area = ${last.maxArea}` });
  }
  return steps;
}

function ContainerTab() {
  const [heightsInput, setHeightsInput] = useState(CWW_DEFAULT.join(', '));
  const [heights, setHeights] = useState(CWW_DEFAULT);
  const [steps, setSteps] = useState<ContainerStep[]>(() => buildContainerSteps(CWW_DEFAULT));
  const [stepIdx, setStepIdx] = useState(0);
  const [history, setHistory] = useState<number[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const mountedRef = useRef(false);
  const nextRef = useRef(() => {});

  const step = steps[stepIdx] ?? steps[0];
  const isDone = stepIdx >= steps.length - 1;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function reset() {
    stopPlay();
    const h = heightsInput.split(',').map(v => parseInt(v.trim())).filter(v => !isNaN(v) && v > 0);
    const arr = h.length >= 2 ? h : CWW_DEFAULT;
    setHeights(arr);
    const s = buildContainerSteps(arr);
    setSteps(s); setStepIdx(0); setHistory([]);
  }

  function nextStep() {
    if (isDone) { stopPlay(); return; }
    setHistory(h => [...h, stepIdx]);
    setStepIdx(s => Math.min(steps.length - 1, s + 1));
  }

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setStepIdx(s);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => { nextRef.current = nextStep; });
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);
  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay(); setPlaying(true);
    timerRef.current = setInterval(() => { nextRef.current(); }, 1100 - speed * 200);
  }, [speed]); // eslint-disable-line react-hooks/exhaustive-deps

  // SVG bar chart
  const SVG_W = 360, SVG_H = 130, PAD_B = 20;
  const n = heights.length;
  const maxH = Math.max(...heights);
  const barW = Math.min(28, Math.floor((SVG_W - 20) / n));
  const gap = Math.floor((SVG_W - 20 - barW * n) / (n + 1));
  const scaleY = (SVG_H - PAD_B - 10) / maxH;

  function barX(i: number) { return 10 + gap + i * (barW + gap); }
  function barY(h: number) { return SVG_H - PAD_B - h * scaleY; }

  const waterH = step ? Math.min(heights[step.left], heights[step.right]) * scaleY : 0;
  const waterLeft = step ? barX(step.left) : 0;
  const waterRight = step ? barX(step.right) + barW : 0;
  const waterTop = step ? SVG_H - PAD_B - waterH : 0;

  return (
    <div className="space-y-6">
      <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Move the shorter side inward — area = min(h[L],h[R]) × (R−L)</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label style={{ display: 'block', color: 'var(--text-faint)', fontSize: '0.75rem', marginBottom: '0.25rem' }}>Heights</label>
          <input style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem', padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none', width: '100%' }}
            value={heightsInput} onChange={e => setHeightsInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="viz-btn">Reset</button></div>
      </div>

      <div style={{ background: 'var(--surface-sunken)', borderRadius: '0.5rem', padding: '0.75rem', overflowX: 'auto' }}>
        <svg width={SVG_W} height={SVG_H}>
          {/* water fill */}
          {step && step.currentArea > 0 && (
            <rect x={waterLeft} y={waterTop} width={waterRight - waterLeft} height={waterH}
              fill="rgba(59,130,246,0.18)" stroke="rgba(59,130,246,0.4)" strokeWidth={1} />
          )}
          {/* bars */}
          {heights.map((h, i) => {
            const isL = step && i === step.left;
            const isR = step && i === step.right;
            const bx = barX(i), bh = h * scaleY, by = barY(h);
            return (
              <g key={i}>
                <rect x={bx} y={by} width={barW} height={bh} rx={2}
                  fill={isL ? '#3b82f6' : isR ? '#f97316' : 'var(--border)'}
                  opacity={0.85} />
                <text x={bx + barW / 2} y={by - 3} textAnchor="middle" fontSize={9} fill="var(--text-faint)">{h}</text>
                <text x={bx + barW / 2} y={SVG_H - 6} textAnchor="middle" fontSize={9}
                  fill={isL ? '#3b82f6' : isR ? '#f97316' : 'var(--text-faint)'}>
                  {isL ? 'L' : isR ? 'R' : i}
                </text>
              </g>
            );
          })}
        </svg>
        {step && (
          <div className="flex gap-4 mt-2 text-xs font-mono" style={{ color: 'var(--text-dim)' }}>
            <span>Current area: <span style={{ color: 'var(--accent)' }}>{step.currentArea}</span></span>
            <span>Max area: <span style={{ color: 'var(--tier-3)' }}>{step.maxArea}</span></span>
          </div>
        )}
      </div>

      {isDone
        ? <div style={{ background: 'color-mix(in srgb, var(--tier-3) 15%, transparent)', border: '1px solid var(--tier-3)', borderRadius: '0.5rem', padding: '0.75rem 1rem', color: 'var(--tier-3)', fontSize: '0.875rem', fontFamily: 'var(--mono)' }}>{step?.msg}</div>
        : <div className="viz-info">{step?.msg}</div>
      }

      <div className="flex flex-wrap items-center gap-3">
        <button onClick={nextStep} disabled={isDone} className="viz-btn viz-btn--primary disabled:opacity-40 disabled:cursor-not-allowed">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn disabled:opacity-40 disabled:cursor-not-allowed">← Back</button>
        <button onClick={togglePlay} disabled={isDone} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <div className="flex items-center gap-2">
          <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
          <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
          <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
        </div>
      </div>
    </div>
  );
}

// ── Root ─────────────────────────────────────────────────────────────────────
export default function TwoPointersViz() {
  const [tab, setTab] = useState<'twosum2' | 'threesum' | 'container'>('twosum2');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Two Pointers</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Two boundaries that move toward each other on sorted input</p>
      </div>

      <div className="flex gap-2">
        <button onClick={() => setTab('twosum2')} className={tab === 'twosum2' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Two Sum II</button>
        <button onClick={() => setTab('threesum')} className={tab === 'threesum' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>3Sum</button>
        <button onClick={() => setTab('container')} className={tab === 'container' ? 'viz-btn viz-btn--primary' : 'viz-btn'}>Container</button>
      </div>

      {tab === 'twosum2' ? <TwoSumIITab /> : tab === 'threesum' ? <ThreeSumTab /> : <ContainerTab />}
    </div>
  );
}
