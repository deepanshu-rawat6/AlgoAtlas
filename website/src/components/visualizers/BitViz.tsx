import { useState } from 'react';

const OPS = ['AND', 'OR', 'XOR', 'NOT', 'LEFT SHIFT', 'RIGHT SHIFT'] as const;
type Op = typeof OPS[number];

function toBits(n: number, len = 8) {
  return Array.from({ length: len }, (_, i) => (n >> (len - 1 - i)) & 1);
}

const inputStyle: React.CSSProperties = {
  background: 'var(--surface-raised)', border: '1px solid var(--border)',
  borderRadius: '0.375rem', padding: '0.375rem 0.75rem',
  color: 'var(--text)', fontSize: '0.875rem', outline: 'none',
};

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

  function BitRow({ bits, label, labelColor, isResult }: { bits: number[]; label: string; labelColor: string; isResult?: boolean }) {
    return (
      <div className="flex items-center gap-2">
        <span style={{ fontFamily: 'var(--mono)', fontSize: '0.75rem', width: '5rem', textAlign: 'right', color: labelColor }}>{label}</span>
        <div className="flex gap-1">
          {bits.map((bit, i) => (
            <div key={i} style={{
              width: '2rem', height: '2rem', display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: 'var(--mono)', fontWeight: 700, borderRadius: '0.375rem', border: '2px solid',
              background: isResult
                ? (bit ? 'color-mix(in srgb, var(--tier-2) 25%, transparent)' : 'var(--surface-sunken)')
                : (bit ? 'var(--accent-soft)' : 'var(--surface-sunken)'),
              borderColor: isResult
                ? (bit ? 'var(--tier-2)' : 'var(--border-soft)')
                : (bit ? 'var(--accent)' : 'var(--border-soft)'),
              color: bit ? 'var(--text)' : 'var(--text-faint)',
            }}>{bit}</div>
          ))}
        </div>
        <span style={{ fontFamily: 'var(--mono)', fontSize: '0.75rem', color: 'var(--text-dim)' }}>
          = {label === '~A' ? (~a) & 0xFF : label.includes('A') && !label.includes('B') ? (op.includes('SHIFT') ? result : a) : label === 'B' ? b : result}
        </span>
      </div>
    );
  }

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Bit Manipulation</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Visualize bitwise operations on 8-bit values</p>
      </div>

      <div className="flex flex-wrap gap-4 items-end">
        {[['A', a, setA], ['B', b, setB]].map(([label, val, set]) => (
          <div key={label as string}>
            <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>
              Value {label as string} (0-255)
            </label>
            <input type="number" min="0" max="255" style={{ ...inputStyle, width: '5rem' }}
              value={val as number}
              onChange={e => (set as (v: number) => void)(Math.min(255, Math.max(0, parseInt(e.target.value) || 0)))} />
          </div>
        ))}
        <div>
          <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Operation</label>
          <select style={{ ...inputStyle }} value={op} onChange={e => setOp(e.target.value as Op)}>
            {OPS.map(o => <option key={o} value={o}>{o}</option>)}
          </select>
        </div>
        {(op === 'LEFT SHIFT' || op === 'RIGHT SHIFT') && (
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Shift by</label>
            <input type="number" min="0" max="7" style={{ ...inputStyle, width: '4rem' }}
              value={shift}
              onChange={e => setShift(Math.min(7, Math.max(0, parseInt(e.target.value) || 0)))} />
          </div>
        )}
      </div>

      <div style={{ background: 'var(--surface-sunken)', borderRadius: '0.5rem', padding: '1rem', overflowX: 'auto' }} className="space-y-3">
        <div className="flex items-center gap-2 mb-2">
          <span style={{ fontFamily: 'var(--mono)', fontSize: '0.75rem', width: '5rem', textAlign: 'right', color: 'var(--text-faint)' }}>bit pos</span>
          <div className="flex gap-1">
            {Array.from({ length: 8 }, (_, i) => (
              <div key={i} style={{ width: '2rem', textAlign: 'center', fontSize: '0.75rem', fontFamily: 'var(--mono)', color: 'var(--text-faint)' }}>{7 - i}</div>
            ))}
          </div>
        </div>
        <BitRow bits={bitsA} label="A" labelColor="var(--accent)" />
        {op !== 'NOT' && op !== 'LEFT SHIFT' && op !== 'RIGHT SHIFT' && (
          <BitRow bits={bitsB} label="B" labelColor="var(--tier-2)" />
        )}
        <div style={{ borderTop: '1px solid var(--border)', paddingTop: '0.5rem' }}>
          <BitRow isResult
            bits={bitsR}
            label={op === 'NOT' ? '~A' : op === 'LEFT SHIFT' ? `A << ${shift}` : op === 'RIGHT SHIFT' ? `A >> ${shift}` : `A ${op === 'AND' ? '&' : op === 'OR' ? '|' : '^'} B`}
            labelColor="var(--tier-3)"
          />
        </div>
      </div>
    </div>
  );
}
