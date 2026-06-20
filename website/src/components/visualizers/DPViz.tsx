import { useState } from 'react';

const DEFAULT_COINS = [1, 3, 5];
const DEFAULT_AMOUNT = 7;
const DEFAULT_HOUSES = [2, 7, 9, 3, 1];

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

// ── Coin Change ────────────────────────────────────────────────────────────────
function CoinChange() {
  const [coinsInput, setCoinsInput] = useState(DEFAULT_COINS.join(', '));
  const [amtInput, setAmtInput] = useState(String(DEFAULT_AMOUNT));
  const [dp, setDp] = useState<(number | null)[]>([]);
  const [step, setStep] = useState(-1);
  const [msg, setMsg] = useState('Coin Change DP. Press "Start" to initialize the table.');
  const [started, setStarted] = useState(false);

  const coins = coinsInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const amount = parseInt(amtInput) || DEFAULT_AMOUNT;

  function start() {
    const table = Array(amount + 1).fill(null) as (number | null)[];
    table[0] = 0;
    setDp(table); setStep(1); setStarted(true);
    setMsg(`dp[0] = 0 (base case). Filling dp[1..${amount}] using coins [${coins.join(', ')}].`);
  }

  function next() {
    if (step > amount) return;
    const table = [...dp];
    const best = coins
      .filter(c => c <= step && table[step - c] !== null)
      .map(c => (table[step - c] as number) + 1);
    table[step] = best.length ? Math.min(...best) : Infinity;
    const usedCoins = coins.filter(c => c <= step && table[step - c] !== null && (table[step - c] as number) + 1 === table[step]);
    setDp(table); setStep(step + 1);
    if (table[step] === Infinity) {
      setMsg(`dp[${step}] = ∞ (not reachable with coins [${coins.join(', ')}])`);
    } else {
      setMsg(`dp[${step}] = ${table[step]} → used coin ${usedCoins[0]} from dp[${step - usedCoins[0]}] + 1`);
    }
  }

  const done = step > amount;

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">dp[i] = min coins to make amount i (unbounded knapsack)</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Coins</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={coinsInput} onChange={e => setCoinsInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label className="block text-xs text-slate-400 mb-1">Amount</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={amtInput} onChange={e => setAmtInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <div className="flex gap-1 min-w-max">
            {dp.map((val, i) => {
              const isCurr = i === step - 1;
              let bg = 'bg-slate-800 border-slate-700 text-slate-600';
              if (isCurr) bg = 'bg-yellow-800 border-yellow-400 text-white';
              else if (val !== null && val !== Infinity) bg = 'bg-blue-900 border-blue-600 text-blue-200';
              else if (val === Infinity) bg = 'bg-red-900/50 border-red-800 text-red-400';
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>
                    {val === null ? '?' : val === Infinity ? '∞' : val}
                  </div>
                  <div className="text-xs text-slate-600">{i}</div>
                </div>
              );
            })}
          </div>
        </div>
      )}
      {done && dp[amount] !== null && dp[amount] !== Infinity && (
        <div className="bg-green-900/40 border border-green-700 rounded-lg px-4 py-3 text-green-300 text-sm font-mono">
          ✓ Minimum coins for amount {amount} = {dp[amount]}
        </div>
      )}
      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>
      <button onClick={next} disabled={!started || done}
        className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
        Next Step
      </button>
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

  const nums = numsInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));

  function start() {
    const table: (number | null)[] = Array(nums.length).fill(null);
    if (nums.length === 0) return;
    table[0] = nums[0];
    if (nums.length > 1) table[1] = Math.max(nums[0], nums[1]);
    const initStep = nums.length === 1 ? 1 : 2;
    setDp(table); setStep(initStep); setStarted(true);
    setMsg(nums.length === 1
      ? `dp[0] = ${nums[0]} (only one house)`
      : `dp[0]=${nums[0]}, dp[1]=max(${nums[0]},${nums[1]})=${table[1]}`);
  }

  function next() {
    if (!started || step >= nums.length) return;
    const table = [...dp];
    const prev1 = table[step - 1] as number;
    const prev2 = table[step - 2] as number;
    const opt2 = prev2 + nums[step];
    table[step] = Math.max(prev1, opt2);
    setDp(table);
    setMsg(`dp[${step}] = max(dp[${step-1}]=${prev1}, dp[${step-2}]+nums[${step}]=${prev2}+${nums[step]}=${opt2}) = ${table[step]}`);
    setStep(step + 1);
  }

  const done = started && step >= nums.length;

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">dp[i] = max money robbing houses 0..i</p>
      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">House Values</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={numsInput} onChange={e => setNumsInput(e.target.value)} />
        </div>
        <div className="flex items-end">
          <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
        </div>
      </div>

      {/* Houses */}
      {nums.length > 0 && (
        <div>
          <div className="text-xs text-slate-500 mb-2">Houses</div>
          <div className="flex gap-2 flex-wrap">
            {nums.map((v, i) => {
              const isCurr = started && i === step - 1;
              const isPrev1 = started && i === step - 2;
              const isPrev2 = started && i === step - 3;
              let bg = 'bg-slate-700 border-slate-600 text-slate-300';
              if (isCurr) bg = 'bg-yellow-700 border-yellow-400 text-white';
              else if (isPrev1) bg = 'bg-blue-800 border-blue-500 text-blue-200';
              else if (isPrev2) bg = 'bg-purple-800 border-purple-500 text-purple-200';
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>{v}</div>
                  <div className="text-xs text-slate-600">h[{i}]</div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* DP table */}
      {dp.length > 0 && (
        <div>
          <div className="text-xs text-slate-500 mb-2">dp table</div>
          <div className="flex gap-2 flex-wrap">
            {dp.map((val, i) => {
              const isFilled = val !== null;
              const isCurr = started && i === step - 1;
              let bg = 'bg-slate-800 border-slate-700 text-slate-600';
              if (isCurr) bg = 'bg-yellow-800 border-yellow-400 text-white';
              else if (isFilled) bg = 'bg-blue-900 border-blue-600 text-blue-200';
              return (
                <div key={i} className="flex flex-col items-center gap-1">
                  <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg text-sm ${bg}`}>
                    {val === null ? '?' : val}
                  </div>
                  <div className="text-xs text-slate-600">dp[{i}]</div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {done && (
        <div className="bg-green-900/40 border border-green-700 rounded-lg px-4 py-3 text-green-300 text-sm font-mono">
          ✓ Max money = {dp[nums.length - 1]}
        </div>
      )}
      <div className="bg-slate-900/60 rounded-lg px-4 py-3 text-sm font-mono min-h-10 text-slate-300">{msg}</div>
      <button onClick={next} disabled={!started || done}
        className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">
        Next Step
      </button>
    </div>
  );
}

// ── Root ───────────────────────────────────────────────────────────────────────
export default function DPViz() {
  const [tab, setTab] = useState<'Coin Change' | 'House Robber'>('Coin Change');
  const tabs = ['Coin Change', 'House Robber'] as const;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">1D Dynamic Programming</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`${TAB_BTN} ${tab === t ? ACTIVE : INACTIVE}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'Coin Change' ? <CoinChange /> : <HouseRobber />}
    </div>
  );
}
