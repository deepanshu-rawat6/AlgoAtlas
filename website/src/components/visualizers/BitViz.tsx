import { useState } from 'react';

const OPS = ['AND', 'OR', 'XOR', 'NOT', 'LEFT SHIFT', 'RIGHT SHIFT'] as const;
type Op = typeof OPS[number];

function toBits(n: number, len = 8) {
  return Array.from({ length: len }, (_, i) => (n >> (len - 1 - i)) & 1);
}

export default function BitViz() {
  const [a, setA] = useState(42);
  const [b, setB] = useState(27);
  const [op, setOp] = useState<Op>('AND');
  const [shift, setShift] = useState(2);

  let result = 0;
  if (op === 'AND') result = a & b;
  else if (op === 'OR') result = a | b;
  else if (op === 'XOR') result = a ^ b;
  else if (op === 'NOT') result = (~a) & 0xFF;
  else if (op === 'LEFT SHIFT') result = (a << shift) & 0xFF;
  else if (op === 'RIGHT SHIFT') result = a >> shift;

  const bitsA = toBits(a);
  const bitsB = toBits(b);
  const bitsR = toBits(result < 0 ? result & 0xFF : result);

  function BitRow({ bits, label, color }: { bits: number[]; label: string; color: string }) {
    return (
      <div className="flex items-center gap-2">
        <span className={`text-xs font-mono w-20 text-right ${color}`}>{label}</span>
        <div className="flex gap-1">
          {bits.map((b, i) => (
            <div key={i} className={`w-8 h-8 flex items-center justify-center font-mono font-bold rounded border ${b ? `bg-blue-800 border-blue-500 text-white` : 'bg-slate-700 border-slate-600 text-slate-500'}`}>{b}</div>
          ))}
        </div>
        <span className="text-xs font-mono text-slate-500">= {label === '~A' ? (~a) & 0xFF : label.includes('A') && !label.includes('B') ? (op.includes('SHIFT') ? result : a) : label === 'B' ? b : result}</span>
      </div>
    );
  }

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Bit Manipulation</h3>
        <p className="text-sm text-slate-400">Visualize bitwise operations on 8-bit values</p>
      </div>

      <div className="flex flex-wrap gap-4 items-end">
        {[['A', a, setA], ['B', b, setB]].map(([label, val, set]) => (
          <div key={label as string}>
            <label className="block text-xs text-slate-400 mb-1">Value {label as string} (0-255)</label>
            <input type="number" min="0" max="255"
              className="w-20 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={val as number} onChange={e => (set as (v: number) => void)(Math.min(255, Math.max(0, parseInt(e.target.value) || 0)))} />
          </div>
        ))}
        <div>
          <label className="block text-xs text-slate-400 mb-1">Operation</label>
          <select className="bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
            value={op} onChange={e => setOp(e.target.value as Op)}>
            {OPS.map(o => <option key={o} value={o}>{o}</option>)}
          </select>
        </div>
        {(op === 'LEFT SHIFT' || op === 'RIGHT SHIFT') && (
          <div>
            <label className="block text-xs text-slate-400 mb-1">Shift by</label>
            <input type="number" min="0" max="7"
              className="w-16 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={shift} onChange={e => setShift(Math.min(7, Math.max(0, parseInt(e.target.value) || 0)))} />
          </div>
        )}
      </div>

      {/* Bit visualization */}
      <div className="space-y-3 bg-slate-900/60 rounded-lg p-4 overflow-x-auto">
        <div className="flex items-center gap-2 mb-2">
          <span className="text-xs font-mono w-20 text-right text-slate-600">bit pos</span>
          <div className="flex gap-1">
            {Array.from({ length: 8 }, (_, i) => (
              <div key={i} className="w-8 text-center text-xs text-slate-600 font-mono">{7 - i}</div>
            ))}
          </div>
        </div>
        <BitRow bits={bitsA} label="A" color="text-blue-400" />
        {op !== 'NOT' && op !== 'LEFT SHIFT' && op !== 'RIGHT SHIFT' && (
          <BitRow bits={bitsB} label="B" color="text-purple-400" />
        )}
        <div className="border-t border-slate-700 pt-2">
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xs font-mono w-20 text-right text-yellow-400">
              {op === 'NOT' ? '~A' : op === 'LEFT SHIFT' ? `A << ${shift}` : op === 'RIGHT SHIFT' ? `A >> ${shift}` : `A ${op === 'AND' ? '&' : op === 'OR' ? '|' : '^'} B`}
            </span>
            <div className="flex gap-1">
              {bitsR.map((bit, i) => (
                <div key={i} className={`w-8 h-8 flex items-center justify-center font-mono font-bold rounded border ${bit ? 'bg-yellow-800 border-yellow-500 text-white' : 'bg-slate-700 border-slate-600 text-slate-500'}`}>{bit}</div>
              ))}
            </div>
            <span className="text-xs font-mono text-yellow-400">= {result < 0 ? result & 0xFF : result}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
