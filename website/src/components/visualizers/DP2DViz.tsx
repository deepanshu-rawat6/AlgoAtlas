import { useState } from 'react';

const TAB_BTN = 'px-3 py-1.5 text-xs font-medium rounded border transition-colors';
const ACTIVE = 'bg-blue-700 text-white border-blue-500';
const INACTIVE = 'bg-slate-700 text-slate-300 border-slate-600';

// ── LCS ────────────────────────────────────────────────────────────────────────
function LCS() {
  const [s1, setS1] = useState('ABCBDAB');
  const [s2, setS2] = useState('BDCAB');
  const [dp, setDp] = useState<number[][]>([]);
  const [i, setI] = useState(1);
  const [j, setJ] = useState(1);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [msg, setMsg] = useState('LCS (Longest Common Subsequence). Press "Start".');

  function start() {
    const rows = s1.length + 1, cols = s2.length + 1;
    const table = Array.from({ length: rows }, () => Array(cols).fill(0));
    setDp(table); setI(1); setJ(1); setStarted(true); setDone(false);
    setMsg(`Initialized ${rows}×${cols} table with 0s. Filling cell by cell.`);
  }

  function next() {
    if (!started || done) return;
    const table = dp.map(r => [...r]);
    const ci = i, cj = j;
    if (s1[ci - 1] === s2[cj - 1]) {
      table[ci][cj] = table[ci - 1][cj - 1] + 1;
      setMsg(`s1[${ci-1}]='${s1[ci-1]}' == s2[${cj-1}]='${s2[cj-1]}' → dp[${ci}][${cj}] = dp[${ci-1}][${cj-1}]+1 = ${table[ci][cj]}`);
    } else {
      table[ci][cj] = Math.max(table[ci - 1][cj], table[ci][cj - 1]);
      setMsg(`s1[${ci-1}]='${s1[ci-1]}' ≠ s2[${cj-1}]='${s2[cj-1]}' → dp[${ci}][${cj}] = max(${table[ci-1][cj]}, ${table[ci][cj-1]}) = ${table[ci][cj]}`);
    }
    setDp(table);
    let ni = ci, nj = cj + 1;
    if (nj > s2.length) { ni++; nj = 1; }
    if (ni > s1.length) { setDone(true); setMsg(prev => `${prev} | LCS length = ${table[s1.length][s2.length]}`); return; }
    setI(ni); setJ(nj);
  }

  const maxVal = dp.length ? Math.max(...dp.flat()) : 0;

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">dp[i][j] = LCS length of s1[0..i] and s2[0..j]</p>
      <div className="flex flex-wrap gap-3">
        {([['String 1', s1, setS1], ['String 2', s2, setS2]] as const).map(([label, val, set]) => (
          <div key={label} className="flex-1 min-w-28">
            <label className="block text-xs text-slate-400 mb-1">{label}</label>
            <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={val} onChange={e => set(e.target.value)} />
          </div>
        ))}
        <div className="flex items-end">
          <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <table className="border-collapse text-xs font-mono">
            <thead>
              <tr>
                <th className="w-8 h-8 text-slate-600 border border-slate-700 bg-slate-900/60"></th>
                <th className="w-8 h-8 text-slate-500 border border-slate-700 bg-slate-900/60">ε</th>
                {s2.split('').map((c, idx) => (
                  <th key={idx} className="w-8 h-8 text-slate-400 border border-slate-700 bg-slate-900/60">{c}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {dp.map((row, ri) => (
                <tr key={ri}>
                  <td className="w-8 h-8 text-center text-slate-400 border border-slate-700 bg-slate-900/60">{ri === 0 ? 'ε' : s1[ri - 1]}</td>
                  {row.map((val, ci) => {
                    const isCurr = ri === i && ci === j;
                    const isMax = val === maxVal && maxVal > 0;
                    let bg = 'bg-slate-800';
                    if (isCurr) bg = 'bg-yellow-800 border-yellow-500';
                    else if (isMax && ri <= (started ? i : 999)) bg = 'bg-green-800';
                    else if (ri < i || (ri === i && ci < j)) bg = 'bg-blue-900/30';
                    return (
                      <td key={ci} className={`w-8 h-8 text-center border border-slate-700 text-slate-200 ${bg}`}>{val}</td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
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

// ── Edit Distance ──────────────────────────────────────────────────────────────
function EditDistance() {
  const [word1, setWord1] = useState('horse');
  const [word2, setWord2] = useState('ros');
  const [dp, setDp] = useState<number[][]>([]);
  const [i, setI] = useState(1);
  const [j, setJ] = useState(1);
  const [started, setStarted] = useState(false);
  const [done, setDone] = useState(false);
  const [msg, setMsg] = useState('Edit Distance DP. Press "Start".');

  function start() {
    const rows = word1.length + 1, cols = word2.length + 1;
    const table = Array.from({ length: rows }, (_, r) =>
      Array.from({ length: cols }, (_, c) => r === 0 ? c : c === 0 ? r : 0)
    );
    setDp(table); setI(1); setJ(1); setStarted(true); setDone(false);
    setMsg(`Base cases: dp[i][0]=i, dp[0][j]=j. Filling from dp[1][1].`);
  }

  function next() {
    if (!started || done) return;
    const table = dp.map(r => [...r]);
    const ci = i, cj = j;
    let opMsg = '';
    if (word1[ci - 1] === word2[cj - 1]) {
      table[ci][cj] = table[ci - 1][cj - 1];
      opMsg = `'${word1[ci-1]}' == '${word2[cj-1]}' → dp[${ci}][${cj}] = dp[${ci-1}][${cj-1}] = ${table[ci][cj]} (no op)`;
    } else {
      const del = table[ci - 1][cj];
      const ins = table[ci][cj - 1];
      const rep = table[ci - 1][cj - 1];
      table[ci][cj] = 1 + Math.min(del, ins, rep);
      const op = Math.min(del, ins, rep) === del ? 'delete' : Math.min(del, ins, rep) === ins ? 'insert' : 'replace';
      opMsg = `'${word1[ci-1]}' ≠ '${word2[cj-1]}' → 1+min(del=${del},ins=${ins},rep=${rep})=${table[ci][cj]} (${op})`;
    }
    setDp(table);
    setMsg(opMsg);
    let ni = ci, nj = cj + 1;
    if (nj > word2.length) { ni++; nj = 1; }
    if (ni > word1.length) {
      setDone(true);
      setMsg(opMsg + ` | Edit distance = ${table[word1.length][word2.length]}`);
      return;
    }
    setI(ni); setJ(nj);
  }

  return (
    <div className="space-y-6">
      <p className="text-sm text-slate-400">dp[i][j] = min ops to convert word1[0..i-1] to word2[0..j-1]</p>
      <div className="flex flex-wrap gap-3">
        {([['Word 1', word1, setWord1], ['Word 2', word2, setWord2]] as const).map(([label, val, set]) => (
          <div key={label} className="flex-1 min-w-28">
            <label className="block text-xs text-slate-400 mb-1">{label}</label>
            <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={val} onChange={e => set(e.target.value)} />
          </div>
        ))}
        <div className="flex items-end">
          <button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <table className="border-collapse text-xs font-mono">
            <thead>
              <tr>
                <th className="w-8 h-8 text-slate-600 border border-slate-700 bg-slate-900/60"></th>
                <th className="w-8 h-8 text-slate-500 border border-slate-700 bg-slate-900/60">ε</th>
                {word2.split('').map((c, idx) => (
                  <th key={idx} className="w-8 h-8 text-slate-400 border border-slate-700 bg-slate-900/60">{c}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {dp.map((row, ri) => (
                <tr key={ri}>
                  <td className="w-8 h-8 text-center text-slate-400 border border-slate-700 bg-slate-900/60">{ri === 0 ? 'ε' : word1[ri - 1]}</td>
                  {row.map((val, ci) => {
                    const isCurr = ri === i && ci === j && started && !done;
                    const isFilled = started && (ri < i || (ri === i && ci <= j));
                    let bg = 'bg-slate-800';
                    if (isCurr) bg = 'bg-yellow-800 border-yellow-500';
                    else if (isFilled) bg = 'bg-blue-900/40';
                    return (
                      <td key={ci} className={`w-8 h-8 text-center border border-slate-700 text-slate-200 ${bg}`}>{val}</td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {done && (
        <div className="bg-green-900/40 border border-green-700 rounded-lg px-4 py-3 text-green-300 text-sm font-mono">
          ✓ Edit distance = {dp[word1.length]?.[word2.length]}
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
export default function DP2DViz() {
  const [tab, setTab] = useState<'LCS' | 'Edit Distance'>('LCS');
  const tabs = ['LCS', 'Edit Distance'] as const;

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-3">2D Dynamic Programming</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`${TAB_BTN} ${tab === t ? ACTIVE : INACTIVE}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'LCS' ? <LCS /> : <EditDistance />}
    </div>
  );
}
