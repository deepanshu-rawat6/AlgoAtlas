import { useState } from 'react';

const DEFAULT = [2, 7, 11, 15];
const DEFAULT_TARGET = 9;

export default function HashMapViz() {
  const [arrInput, setArrInput] = useState(DEFAULT.join(', '));
  const [tgtInput, setTgtInput] = useState(String(DEFAULT_TARGET));
  const [step, setStep] = useState(-1);
  const [map, setMap] = useState<Record<number, number>>({});
  const [found, setFound] = useState<[number,number] | null>(null);
  const [msg, setMsg] = useState('Press "Next Step" to walk through Two Sum hash map lookup.');

  const arr = arrInput.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
  const target = parseInt(tgtInput) || DEFAULT_TARGET;

  function reset() {
    setStep(-1); setMap({}); setFound(null);
    setMsg('Press "Next Step" to walk through Two Sum hash map lookup.');
  }

  function next() {
    if (found || step >= arr.length - 1) return;
    const i = step + 1;
    const complement = target - arr[i];
    if (map[complement] !== undefined) {
      setFound([map[complement], i]);
      setMsg(`✓ Found! arr[${map[complement]}]=${complement} + arr[${i}]=${arr[i]} = ${target}`);
    } else {
      setMap(prev => ({ ...prev, [arr[i]]: i }));
      setMsg(`i=${i}: arr[${i}]=${arr[i]}, complement=${complement} not in map → store {${arr[i]}: ${i}}`);
    }
    setStep(i);
  }

  const done = found !== null || (step >= arr.length - 1 && !found);

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Hash Map — Two Sum</h3>
        <p className="text-sm text-slate-400">Trade space for time: store complement lookups</p>
      </div>

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 min-w-40">
          <label className="block text-xs text-slate-400 mb-1">Array</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={arrInput} onChange={e => setArrInput(e.target.value)} />
        </div>
        <div className="w-24">
          <label className="block text-xs text-slate-400 mb-1">Target</label>
          <input className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={tgtInput} onChange={e => setTgtInput(e.target.value)} />
        </div>
        <div className="flex items-end"><button onClick={reset} className="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-slate-200 text-sm rounded">Reset</button></div>
      </div>

      {/* Array */}
      <div className="flex gap-2 flex-wrap">
        {arr.map((v, i) => {
          const isActive = i === step;
          const isFound = found && (i === found[0] || i === found[1]);
          let bg = 'bg-slate-700 border-slate-600 text-slate-300';
          if (isFound) bg = 'bg-green-800 border-green-400 text-white';
          else if (isActive) bg = 'bg-yellow-800 border-yellow-400 text-white';
          return (
            <div key={i} className="flex flex-col items-center gap-1">
              <div className={`w-12 h-12 flex items-center justify-center font-mono font-bold border-2 rounded-lg ${bg}`}>{v}</div>
              <div className="text-xs text-slate-500">[{i}]</div>
            </div>
          );
        })}
      </div>

      {/* Hash map state */}
      <div className="bg-slate-900/60 rounded-lg p-4">
        <div className="text-xs text-slate-500 mb-2 font-mono">HashMap: seen = {'{'}</div>
        <div className="flex flex-wrap gap-2 ml-4">
          {Object.entries(map).length === 0
            ? <span className="text-slate-600 text-sm font-mono">empty</span>
            : Object.entries(map).map(([k, v]) => (
                <span key={k} className="text-sm font-mono bg-blue-900/40 border border-blue-700 px-2 py-1 rounded text-blue-300">
                  {k}: {v}
                </span>
              ))
          }
        </div>
        <div className="text-xs text-slate-500 mt-2 font-mono">{'}'}</div>
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${found ? 'bg-green-900/40 text-green-300' : 'bg-slate-900/60 text-slate-300'}`}>{msg}</div>

      <div className="flex gap-3">
        <button onClick={next} disabled={done} className="px-4 py-2 bg-blue-700 hover:bg-blue-600 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg">Next Step</button>
      </div>
    </div>
  );
}
