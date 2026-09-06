import { useState, useRef, useEffect } from 'react';

type DP2DSnap = { dp: number[][], i: number, j: number, done: boolean, msg: string };

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
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<DP2DSnap[]>([]);
  const nextStepRef = useRef<() => void>(() => {});
  const mountedRef = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function start() {
    stopPlay();
    const rows = s1.length + 1, cols = s2.length + 1;
    const table = Array.from({ length: rows }, () => Array(cols).fill(0));
    setDp(table); setI(1); setJ(1); setStarted(true); setDone(false); setHistory([]);
    setMsg(`Initialized ${rows}×${cols} table with 0s. Filling cell by cell.`);
  }

  function next() {
    if (!started || done) { stopPlay(); return; }
    setHistory(h => [...h, { dp: dp.map(r => [...r]), i, j, done, msg }]);
    const table = dp.map(r => [...r]);
    const ci = i, cj = j;
    let newDone = false;
    let newMsg = msg;
    if (s1[ci - 1] === s2[cj - 1]) {
      table[ci][cj] = table[ci - 1][cj - 1] + 1;
      newMsg = `s1[${ci-1}]='${s1[ci-1]}' == s2[${cj-1}]='${s2[cj-1]}' → dp[${ci}][${cj}] = dp[${ci-1}][${cj-1}]+1 = ${table[ci][cj]}`;
    } else {
      table[ci][cj] = Math.max(table[ci - 1][cj], table[ci][cj - 1]);
      newMsg = `s1[${ci-1}]='${s1[ci-1]}' ≠ s2[${cj-1}]='${s2[cj-1]}' → dp[${ci}][${cj}] = max(${table[ci-1][cj]}, ${table[ci][cj-1]}) = ${table[ci][cj]}`;
    }
    setDp(table);
    let ni = ci, nj = cj + 1;
    if (nj > s2.length) { ni++; nj = 1; }
    if (ni > s1.length) {
      newDone = true;
      newMsg = newMsg + ` | LCS length = ${table[s1.length][s2.length]}`;
      setDone(true); stopPlay();
    } else {
      setI(ni); setJ(nj);
    }
    setMsg(newMsg);
  }

  useEffect(() => { nextStepRef.current = next; });

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setDp(s.dp); setI(s.i); setJ(s.j); setDone(s.done); setMsg(s.msg);
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

  const maxVal = dp.length ? Math.max(...dp.flat()) : 0;

  const thStyle: React.CSSProperties = {width:'2rem',height:'2rem',color:'var(--text-faint)',border:'1px solid var(--border)',background:'var(--surface-sunken)',textAlign:'center',fontSize:'0.75rem',fontFamily:'var(--mono)'};
  const thLabelStyle: React.CSSProperties = {...thStyle,color:'var(--text-dim)'};

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>dp[i][j] = LCS length of s1[0..i] and s2[0..j]</p>
      <div className="flex flex-wrap gap-3">
        {([['String 1', s1, setS1], ['String 2', s2, setS2]] as const).map(([label, val, set]) => (
          <div key={label} className="flex-1 min-w-28">
            <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>{label}</label>
            <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
              value={val} onChange={e => set(e.target.value)} />
          </div>
        ))}
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <table className="border-collapse text-xs font-mono">
            <thead>
              <tr>
                <th style={thStyle}></th>
                <th style={thStyle}>ε</th>
                {s2.split('').map((c, idx) => (
                  <th key={idx} style={thLabelStyle}>{c}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {dp.map((row, ri) => (
                <tr key={ri}>
                  <td style={{...thLabelStyle,textAlign:'center'}}>{ri === 0 ? 'ε' : s1[ri - 1]}</td>
                  {row.map((val, ci) => {
                    const isCurr = ri === i && ci === j;
                    const isMax = val === maxVal && maxVal > 0;
                    let cellStyle: React.CSSProperties = {background:'var(--surface-raised)',border:'1px solid var(--border)',color:'var(--text)',textAlign:'center',width:'2rem',height:'2rem'};
                    if (isCurr) cellStyle = {...cellStyle,background:'var(--accent-soft)',borderColor:'var(--accent)'};
                    else if (isMax && ri <= (started ? i : 999)) cellStyle = {...cellStyle,background:'color-mix(in srgb, var(--tier-3) 20%, transparent)',borderColor:'var(--tier-3)'};
                    else if (ri < i || (ri === i && ci < j)) cellStyle = {...cellStyle,background:'var(--surface-sunken)',color:'var(--text-secondary)'};
                    return (
                      <td key={ci} style={cellStyle}>{val}</td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
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
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const [history, setHistory] = useState<DP2DSnap[]>([]);
  const nextStepRef = useRef<() => void>(() => {});
  const mountedRef = useRef(false);

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function start() {
    stopPlay();
    const rows = word1.length + 1, cols = word2.length + 1;
    const table = Array.from({ length: rows }, (_, r) =>
      Array.from({ length: cols }, (_, c) => r === 0 ? c : c === 0 ? r : 0)
    );
    setDp(table); setI(1); setJ(1); setStarted(true); setDone(false); setHistory([]);
    setMsg(`Base cases: dp[i][0]=i, dp[0][j]=j. Filling from dp[1][1].`);
  }

  function next() {
    if (!started || done) { stopPlay(); return; }
    setHistory(h => [...h, { dp: dp.map(r => [...r]), i, j, done, msg }]);
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
    let ni = ci, nj = cj + 1;
    if (nj > word2.length) { ni++; nj = 1; }
    if (ni > word1.length) {
      setDone(true);
      setMsg(opMsg + ` | Edit distance = ${table[word1.length][word2.length]}`);
      stopPlay();
      return;
    }
    setI(ni); setJ(nj);
    setMsg(opMsg);
  }

  useEffect(() => { nextStepRef.current = next; });

  function stepBack() {
    if (playing) stopPlay();
    setHistory(h => {
      if (h.length === 0) return h;
      const prev = [...h];
      const s = prev.pop()!;
      setDp(s.dp); setI(s.i); setJ(s.j); setDone(s.done); setMsg(s.msg);
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

  const thStyle: React.CSSProperties = {width:'2rem',height:'2rem',color:'var(--text-faint)',border:'1px solid var(--border)',background:'var(--surface-sunken)',textAlign:'center',fontSize:'0.75rem',fontFamily:'var(--mono)'};
  const thLabelStyle: React.CSSProperties = {...thStyle,color:'var(--text-dim)'};

  return (
    <div className="space-y-6">
      <p style={{color:'var(--text-dim)',fontSize:'0.875rem'}}>dp[i][j] = min ops to convert word1[0..i-1] to word2[0..j-1]</p>
      <div className="flex flex-wrap gap-3">
        {([['Word 1', word1, setWord1], ['Word 2', word2, setWord2]] as const).map(([label, val, set]) => (
          <div key={label} className="flex-1 min-w-28">
            <label className="block" style={{color:'var(--text-faint)',fontSize:'0.75rem',marginBottom:'0.25rem'}}>{label}</label>
            <input style={{background:'var(--surface-raised)',border:'1px solid var(--border)',borderRadius:'0.375rem',padding:'0.375rem 0.75rem',color:'var(--text)',fontSize:'0.875rem',outline:'none',width:'100%'}}
              value={val} onChange={e => set(e.target.value)} />
          </div>
        ))}
        <div className="flex items-end">
          <button onClick={start} className="viz-btn viz-btn--primary">Start</button>
        </div>
      </div>
      {dp.length > 0 && (
        <div className="overflow-x-auto pb-2">
          <table className="border-collapse text-xs font-mono">
            <thead>
              <tr>
                <th style={thStyle}></th>
                <th style={thStyle}>ε</th>
                {word2.split('').map((c, idx) => (
                  <th key={idx} style={thLabelStyle}>{c}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {dp.map((row, ri) => (
                <tr key={ri}>
                  <td style={{...thLabelStyle,textAlign:'center'}}>{ri === 0 ? 'ε' : word1[ri - 1]}</td>
                  {row.map((val, ci) => {
                    const isCurr = ri === i && ci === j && started && !done;
                    const isFilled = started && (ri < i || (ri === i && ci <= j));
                    let cellStyle: React.CSSProperties = {background:'var(--surface-raised)',border:'1px solid var(--border)',color:'var(--text)',textAlign:'center',width:'2rem',height:'2rem'};
                    if (isCurr) cellStyle = {...cellStyle,background:'var(--accent-soft)',borderColor:'var(--accent)'};
                    else if (isFilled) cellStyle = {...cellStyle,background:'var(--surface-sunken)',color:'var(--text-secondary)'};
                    return (
                      <td key={ci} style={cellStyle}>{val}</td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {done && (
        <div style={{background:'color-mix(in srgb, var(--tier-3) 15%, transparent)',border:'1px solid var(--tier-3)',borderRadius:'0.5rem',padding:'0.75rem 1rem',color:'var(--tier-3)',fontSize:'0.875rem',fontFamily:'var(--mono)'}}>
          ✓ Edit distance = {dp[word1.length]?.[word2.length]}
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

// ── Root ───────────────────────────────────────────────────────────────────────
export default function DP2DViz() {
  const [tab, setTab] = useState<'LCS' | 'Edit Distance'>('LCS');
  const tabs = ['LCS', 'Edit Distance'] as const;

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{color:'var(--text)',fontSize:'1.05rem',fontWeight:600,marginBottom:'0.75rem'}}>2D Dynamic Programming</h3>
        <div className="flex gap-2">
          {tabs.map(t => (
            <button key={t} onClick={() => setTab(t)} className={`viz-btn${tab === t ? ' viz-btn--primary' : ''}`}>{t}</button>
          ))}
        </div>
      </div>
      {tab === 'LCS' ? <LCS /> : <EditDistance />}
    </div>
  );
}
