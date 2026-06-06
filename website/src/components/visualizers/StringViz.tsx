import { useState } from 'react';

function buildLPS(pattern: string): number[] {
  const lps = Array(pattern.length).fill(0);
  let len = 0, i = 1;
  while (i < pattern.length) {
    if (pattern[i] === pattern[len]) { lps[i++] = ++len; }
    else if (len) { len = lps[len - 1]; }
    else { lps[i++] = 0; }
  }
  return lps;
}

interface Frame { ti: number; pi: number; match: boolean; found: number | null; msg: string; }

function buildFrames(text: string, pattern: string): Frame[] {
  const frames: Frame[] = [];
  const lps = buildLPS(pattern);
  let ti = 0, pi = 0;
  while (ti < text.length) {
    if (text[ti] === pattern[pi]) {
      frames.push({ ti, pi, match: true, found: null, msg: `Match: text[${ti}]='${text[ti]}' == pattern[${pi}]` });
      ti++; pi++;
      if (pi === pattern.length) {
        frames.push({ ti: ti - 1, pi: pi - 1, match: true, found: ti - pi, msg: `✓ Pattern found at index ${ti - pi}!` });
        pi = lps[pi - 1];
      }
    } else {
      frames.push({ ti, pi, match: false, found: null, msg: `Mismatch: text[${ti}]='${text[ti]}' ≠ pattern[${pi}]${pi > 0 ? ` → use LPS, pi=${lps[pi-1]}` : ', advance ti'}` });
      if (pi) pi = lps[pi - 1]; else ti++;
    }
  }
  frames.push({ ti, pi, match: false, found: null, msg: pi === 0 ? 'Search complete.' : 'Pattern not found.' });
  return frames;
}

export default function StringViz() {
  const [text, setText] = useState('AABAABAAA');
  const [pattern, setPattern] = useState('AABA');
  const [frames, setFrames] = useState<Frame[]>([]);
  const [step, setStep] = useState(0);
  const [started, setStarted] = useState(false);

  function start() {
    setFrames(buildFrames(text, pattern));
    setStep(0); setStarted(true);
  }

  const frame = frames[step];
  const lps = buildLPS(pattern);

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">KMP Pattern Matching</h3>
        <p className="text-sm text-slate-400">O(n+m) using LPS (failure function) to avoid backtracking</p>
      </div>

      <div className="flex flex-wrap gap-3">
        {[['Text', text, setText], ['Pattern', pattern, setPattern]].map(([label, val, set]) => (
          <div key={label as string} className="flex-1 min-w-28">
            <label className="block text-xs text-slate-400 mb-1">{label as string}</label>
            <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 font-mono"
              value={val as string} onChange={e => (set as (v: string) => void)(e.target.value.toUpperCase())} />
          </div>
        ))}
        <div className="flex items-end"><button onClick={start} className="px-4 py-2 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded-lg">Start</button></div>
      </div>

      {/* LPS array */}
      <div className="flex gap-2 items-center flex-wrap">
        <span className="text-xs text-slate-500 font-mono">LPS:</span>
        {pattern.split('').map((c, i) => (
          <div key={i} className="flex flex-col items-center">
            <span className="text-xs font-mono text-slate-400 w-7 text-center">{c}</span>
            <span className="text-xs font-mono bg-slate-700 border border-slate-600 w-7 h-7 flex items-center justify-center rounded text-blue-300">{lps[i]}</span>
          </div>
        ))}
      </div>

      {/* Text with pointer */}
      {started && frame && (
        <div className="space-y-2">
          <div className="flex gap-1 flex-wrap">
            {text.split('').map((c, i) => {
              const isTi = i === frame.ti;
              const isFound = frame.found !== null && i >= frame.found && i < frame.found + pattern.length;
              let bg = 'bg-slate-700 border-slate-600 text-slate-300';
              if (isFound) bg = 'bg-green-800 border-green-400 text-white';
              else if (isTi) bg = `${frame.match ? 'bg-blue-800 border-blue-400' : 'bg-red-800 border-red-400'} text-white`;
              return (
                <div key={i} className="flex flex-col items-center">
                  <div className={`w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm ${bg}`}>{c}</div>
                  <span className="text-xs text-slate-600">{i}</span>
                </div>
              );
            })}
          </div>
          <div className="flex gap-1 flex-wrap items-center">
            <span className="text-xs text-slate-500">Pattern:</span>
            {pattern.split('').map((c, i) => {
              const isPi = i === frame.pi;
              return (
                <div key={i} className={`w-8 h-8 flex items-center justify-center font-mono font-bold border-2 rounded text-sm ${isPi ? 'bg-purple-800 border-purple-400 text-white' : 'bg-slate-700 border-slate-600 text-slate-400'}`}>{c}</div>
              );
            })}
          </div>
        </div>
      )}

      {frame && <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${frame.found !== null ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{frame.msg}</div>}

      {started && (
        <div className="flex gap-3">
          <button onClick={() => setStep(s => Math.max(0, s - 1))} disabled={step === 0} className="px-4 py-2 bg-slate-700 hover:bg-slate-600 disabled:opacity-40 text-slate-200 text-sm rounded-lg">← Prev</button>
          <button onClick={() => setStep(s => Math.min(frames.length - 1, s + 1))} disabled={step >= frames.length - 1} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 text-white text-sm rounded-lg">Next →</button>
          <span className="text-xs text-slate-500 self-center">{step + 1}/{frames.length}</span>
        </div>
      )}
    </div>
  );
}
