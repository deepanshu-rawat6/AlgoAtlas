import { useState, useRef, useEffect } from 'react';

const DEFAULT_COINS = [1, 3, 5];
const DEFAULT_AMOUNT = 7;
const DEFAULT_HOUSES = [2, 7, 9, 3, 1];

// ── Coin Change ────────────────────────────────────────────────────────────────
function CoinChange() {
  const [coinsInput, setCoinsInput] = useState(DEFAULT_COINS.join(', '));
  const [amtInput, setAmtInput] = useState(String(DEFAULT_AMOUNT));
  const [dp, setDp] = useState<(number | null)[]>([]);
  const [step, setStep] = useState(-1);
  const [msg, setMsg] = useState('Coin Change DP. Press "Start" to initialize the table.');
  const [started, setStarted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<Array<{ dp: (number | null)[], step: number, msg: string }>>([]);
  const nextStepRef = useRef<() => void>(() => {});
  const mountedRef = useRef(false);

  const coins = coinsInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const amount = parseInt(amtInput) || DEFAULT_AMOUNT;
  const done = step > amount;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function start() {
    stopPlay();
    const table = Array(amount + 1).fill(null) as (number | null)[];
    table[0] = 0;
    setDp(table); setStep(1); setStarted(true); setHistory([]);
    setMsg(`dp[0] = 0 (base case). Filling dp[1..${amount}] using coins [${coins.join(', ')}].`);
  }

  function next() {
    if (!started || done) { stopPlay(); return; }
    setHistory(h => [...h, { dp: [...dp], step, msg }]);
    const table = [...dp];
    const best = coins
      .filter(c => c <= step && table[step - c] !== null)
      .map(c => (table[step - c] as number) + 1);
    table[step] = best.length ? Math.min(...best) : Infinity;
    const usedCoins = coins.filter(c => c <= step && table[step - c] !== null && (table[step - c] as number) + 1 === table[step]);
    const newStep = step + 1;
    setDp(table); setStep(newStep);
    if (table[step] === Infinity) {
      setMsg(`dp[${step}] = ∞ (not reachable with coins [${coins.join(', ')}])`);
    } else {
      setMsg(`dp[${step}] = ${table[step]} → used coin ${usedCoins[0]} from dp[${step - usedCoins[0]}] + 1`);
    }
    if (newStep > amount) stopPlay();
  }

  useEffect(() => { nextStepRef.current = next; });

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setDp(s.dp); setStep(s.step); setMsg(s.msg);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }, [speed]);

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>dp[i] = min coins to make amount i (unbounded knapsack)</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Coins</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={coinsInput} onChange={e => setCoinsInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Amount</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={amtInput} onChange={e => setAmtInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <div className="flex gap-1 min-w-max">
            {dp.map((val, i) => {
              const isCurr = i === step - 1;
              let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
              if (isCurr) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
              else if (val !== null && val !== Infinity) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
              else if (val === Infinity) cellStyle = {background:'color-mix(in srgb, #ef4444 15%, transparent)',borderColor:'#ef4444',color:'var(--text)'};
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>
                    {val === null ? '?' : val === Infinity ? '∞' : val}
                  </div>
                  <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>{i}</div>
                </div>
              );
            })}
          </div>
        </div>
      )}
      {done && dp[amount] !== null && dp[amount] !== Infinity && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          ✓ Minimum coins for amount {amount} = {dp[amount]}
        </div>
      )}
      <div className="viz-info">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={!started || done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={!started || done} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
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

// ── House Robber ───────────────────────────────────────────────────────────────
function HouseRobber() {
  const [numsInput, setNumsInput] = useState(DEFAULT_HOUSES.join(', '));
  const [dp, setDp] = useState<(number | null)[]>([]);
  const [step, setStep] = useState(-1);
  const [started, setStarted] = useState(false);
  const [msg, setMsg] = useState('House Robber DP. Press "Start" to begin.');
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<Array<{ dp: (number | null)[], step: number, msg: string }>>([]);
  const nextStepRef = useRef<() => void>(() => {});
  const mountedRef = useRef(false);

  const nums = numsInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const done = started && step >= nums.length;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function start() {
    stopPlay();
    const table: (number | null)[] = Array(nums.length).fill(null);
    if (nums.length === 0) return;
    table[0] = nums[0];
    if (nums.length > 1) table[1] = Math.max(nums[0], nums[1]);
    const initStep = nums.length === 1 ? 1 : 2;
    setDp(table); setStep(initStep); setStarted(true); setHistory([]);
    setMsg(nums.length === 1
      ? `dp[0] = ${nums[0]} (only one house)`
      : `dp[0]=${nums[0]}, dp[1]=max(${nums[0]},${nums[1]})=${table[1]}`);
  }

  function next() {
    if (!started || step >= nums.length) { stopPlay(); return; }
    setHistory(h => [...h, { dp: [...dp], step, msg }]);
    const table = [...dp];
    const prev1 = table[step - 1] as number;
    const prev2 = table[step - 2] as number;
    const opt2 = prev2 + nums[step];
    table[step] = Math.max(prev1, opt2);
    const newStep = step + 1;
    setDp(table);
    setMsg(`dp[${step}] = max(dp[${step-1}]=${prev1}, dp[${step-2}]+nums[${step}]=${prev2}+${nums[step]}=${opt2}) = ${table[step]}`);
    setStep(newStep);
    if (newStep >= nums.length) stopPlay();
  }

  useEffect(() => { nextStepRef.current = next; });

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setDp(s.dp); setStep(s.step); setMsg(s.msg);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay();
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }, [speed]);

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>dp[i] = max money robbing houses 0..i</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>House Values</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={numsInput} onChange={e => setNumsInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>

      {/* Houses */}
      {nums.length > 0 && (
        <div>
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>Houses</div>
          <div className="flex gap-2 flex-wrap">
            {nums.map((v, i) => {
              const isCurr = started && i === step - 1;
              const isPrev1 = started && i === step - 2;
              const isPrev2 = started && i === step - 3;
              let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
              if (isCurr) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
              else if (isPrev1 || isPrev2) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>{v}</div>
                  <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>h[{i}]</div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* DP table */}
      {dp.length > 0 && (
        <div>
          <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>dp table</div>
          <div className="flex gap-2 flex-wrap">
            {dp.map((val, i) => {
              const isFilled = val !== null;
              const isCurr = started && i === step - 1;
              let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
              if (isCurr) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
              else if (isFilled) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>
                    {val === null ? '?' : val}
                  </div>
                  <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>dp[{i}]</div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {done && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          ✓ Max money = {dp[nums.length - 1]}
        </div>
      )}
      <div className="viz-info">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={!started || done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={!started || done} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
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

// ── LIS ────────────────────────────────────────────────────────────────────────
const DEFAULT_LIS = [10, 9, 2, 5, 3, 7, 101, 18];

interface LISSnap { dp: (number | null)[]; i: number; j: number; done: boolean; msg: string; }

function buildLISSteps(nums: number[]): LISSnap[] {
  const n = nums.length;
  const dp: (number | null)[] = Array(n).fill(null);
  dp[0] = 1;
  const steps: LISSnap[] = [];
  steps.push({ dp: [...dp], i: 0, j: -1, done: false,
    msg: `Initialize: dp[0]=1 (LIS ending at nums[0]=${nums[0]} has length 1)` });
  for (let i = 1; i < n; i++) {
    dp[i] = 1;
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        const prev = dp[i]!;
        dp[i] = Math.max(dp[i]!, dp[j]! + 1);
        steps.push({ dp: [...dp], i, j, done: false,
          msg: `i=${i}(${nums[i]}), j=${j}(${nums[j]}): ${nums[j]}<${nums[i]} → dp[${i}]=max(${prev},${dp[j]}+1)=${dp[i]}` });
      } else {
        steps.push({ dp: [...dp], i, j, done: false,
          msg: `i=${i}(${nums[i]}), j=${j}(${nums[j]}): ${nums[j]}≥${nums[i]}, skip` });
      }
    }
  }
  const ans = Math.max(...(dp as number[]));
  steps.push({ dp: [...dp], i: n, j: -1, done: true, msg: `Done! LIS length = ${ans}` });
  return steps;
}

function LIS() {
  const [numsInput, setNumsInput] = useState(DEFAULT_LIS.join(', '));
  const [steps, setSteps] = useState<LISSnap[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);
  const [started, setStarted] = useState(false);
  const [msg, setMsg] = useState('LIS DP. dp[i] = length of LIS ending at i. Press "Start".');
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<number[]>([]);
  const nextStepRef = useRef<() => void>(() => {});
  const mountedRef = useRef(false);

  const nums = numsInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const snap = steps[stepIdx];
  const done = snap?.done ?? false;

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function start() {
    stopPlay();
    if (nums.length === 0) return;
    const s = buildLISSteps(nums);
    setSteps(s); setStepIdx(0); setStarted(true); setHistory([]);
    setMsg(s[0].msg);
  }

  function next() {
    if (!started || done || stepIdx >= steps.length - 1) { stopPlay(); return; }
    setHistory(h => [...h, stepIdx]);
    const ni = stepIdx + 1;
    setStepIdx(ni);
    setMsg(steps[ni].msg);
    if (steps[ni].done) stopPlay();
  }

  useEffect(() => { nextStepRef.current = next; });

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const si = prev.pop()!;
      setStepIdx(si); setMsg(steps[si].msg);
      return prev;
    });
  }

  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  useEffect(() => {
    if (!mountedRef.current) { mountedRef.current = true; return; }
    if (!playing) return;
    stopPlay(); setPlaying(true);
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
  }, [speed]); // eslint-disable-line react-hooks/exhaustive-deps

  const dp = snap?.dp ?? [];
  const maxDP = done ? Math.max(...(dp as number[])) : -1;

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>dp[i] = length of LIS ending at index i. O(n²) — check all j&lt;i where nums[j]&lt;nums[i].</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>Array</label>
          <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
            value={numsInput} onChange={e => setNumsInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>

      {started && nums.length > 0 && (
        <>
          <div>
            <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>nums</div>
            <div className="flex gap-2 flex-wrap">
              {nums.map((v, idx) => {
                const isI = snap && idx === snap.i;
                const isJ = snap && idx === snap.j;
                let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
                if (isI) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
                else if (isJ) cellStyle = {background:'color-mix(in srgb, #eab308 20%, transparent)',borderColor:'#eab308',color:'var(--text)'};
                else if (dp[idx] !== null) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
                return (
                  <div key={idx} className="flex flex-col items-center gap-1">
                    <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>{v}</div>
                    <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>[{idx}]</div>
                  </div>
                );
              })}
            </div>
          </div>

          <div>
            <div style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.5rem'}}>dp</div>
            <div className="flex gap-2 flex-wrap">
              {nums.map((_, idx) => {
                const val = dp[idx];
                const isI = snap && idx === snap.i;
                const isJ = snap && idx === snap.j;
                const isMax = done && val === maxDP;
                let cellStyle: React.CSSProperties = {background:'var(--surface-sunken)',borderColor:'var(--border-soft)',color:'var(--text-faint)'};
                if (isMax) cellStyle = {background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)',color:'var(--text)'};
                else if (isI) cellStyle = {background:'var(--accent-soft)',borderColor:'var(--accent)',color:'var(--text)'};
                else if (isJ) cellStyle = {background:'color-mix(in srgb, #eab308 20%, transparent)',borderColor:'#eab308',color:'var(--text)'};
                else if (val !== null) cellStyle = {background:'var(--surface-raised)',borderColor:'var(--border)',color:'var(--text-secondary)'};
                return (
                  <div key={idx} className="flex flex-col items-center gap-1">
                    <div className="w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm" style={cellStyle}>
                      {val === null ? '–' : val}
                    </div>
                    <div style={{color:'var(--text-faint)',fontSize:'0.7rem'}}>dp[{idx}]</div>
                  </div>
                );
              })}
            </div>
          </div>
        </>
      )}

      {done && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          ✓ LIS length = {maxDP}
        </div>
      )}
      <div className="viz-info">{msg}</div>
      <div className="flex flex-wrap items-center gap-3">
        <button onClick={next} disabled={!started || done} className="viz-btn viz-btn--primary">Next Step</button>
        <button onClick={stepBack} disabled={history.length === 0} className="viz-btn">← Back</button>
        <button onClick={togglePlay} disabled={!started || done} className="viz-btn viz-btn--primary">
          {playing ? 'Pause' : '▶ Play'}
        </button>
        <button onClick={start} className="viz-btn">Reset</button>
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
export default function DPViz() {
  const [tab, setTab] = useState<'Coin Change' | 'House Robber' | 'LIS'>('Coin Change');
  const tabs = ['Coin Change', 'House Robber', 'LIS'] as const;

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>1D Dynamic Programming</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`viz-btn${tab === t ? ' viz-btn--primary' : ''}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'Coin Change' ? <CoinChange /> : tab === 'House Robber' ? <HouseRobber /> : <LIS />}
    </div>
  );
}
