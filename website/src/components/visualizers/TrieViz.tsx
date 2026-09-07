import { useState } from 'react';

interface TrieNode { children: Record<string, TrieNode>; isEnd: boolean; }
const makeNode = (): TrieNode => ({ children: {}, isEnd: false });

function insertWord(root: TrieNode, word: string): TrieNode {
  let node = root;
  for (const ch of word) {
    if (!node.children[ch]) node.children[ch] = makeNode();
    node = node.children[ch];
  }
  node.isEnd = true;
  return root;
}

function searchWord(root: TrieNode, word: string): boolean {
  let node = root;
  for (const ch of word) {
    if (!node.children[ch]) return false;
    node = node.children[ch];
  }
  return node.isEnd;
}

function TrieTree({ node, prefix, highlight }: { node: TrieNode; prefix: string; highlight: string }) {
  const chars = Object.keys(node.children).sort();
  if (chars.length === 0) return null;
  return (
    <ul style={{ marginLeft: '1rem', borderLeft: '1px solid var(--border)', paddingLeft: '0.75rem' }} className="space-y-1">
      {chars.map(ch => {
        const child = node.children[ch];
        const path = prefix + ch;
        const isHl = highlight.startsWith(path);
        return (
          <li key={ch}>
            <span style={{
              fontFamily: 'var(--mono)', fontSize: '0.875rem', padding: '0.125rem 0.375rem', borderRadius: '0.25rem',
              background: isHl ? 'color-mix(in srgb, var(--tier-2) 20%, transparent)' : 'transparent',
              color: child.isEnd ? 'var(--tier-3)' : isHl ? 'var(--text)' : 'var(--text-secondary)',
              border: child.isEnd ? '1px solid color-mix(in srgb, var(--tier-3) 40%, transparent)' : 'none',
            }}>
              {ch}{child.isEnd ? ' *' : ''}
            </span>
            <TrieTree node={child} prefix={path} highlight={highlight} />
          </li>
        );
      })}
    </ul>
  );
}

const inputStyle: React.CSSProperties = {
  background: 'var(--surface-raised)', border: '1px solid var(--border)',
  borderRadius: '0.375rem', padding: '0.375rem 0.75rem', width: '7rem',
  color: 'var(--text)', fontSize: '0.875rem', outline: 'none',
};

export default function TrieViz() {
  const [root, setRoot] = useState<TrieNode>(() => {
    let r = makeNode();
    for (const w of ['apple', 'app', 'apt', 'bat', 'ball']) r = insertWord(r, w);
    return r;
  });
  const [insertInput, setInsertInput] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [highlight, setHighlight] = useState('');
  const [msg, setMsg] = useState('Trie preloaded with: apple, app, apt, bat, ball');

  function insert() {
    const w = insertInput.trim().toLowerCase();
    if (!w) return;
    setRoot(r => insertWord({ ...r }, w));
    setHighlight(w);
    setMsg(`Inserted "${w}" → created/followed nodes: ${w.split('').join(' → ')}, marked end *`);
    setInsertInput('');
    setTimeout(() => setHighlight(''), 1500);
  }

  function search() {
    const w = searchInput.trim().toLowerCase();
    if (!w) return;
    const found = searchWord(root, w);
    setHighlight(w);
    setMsg(found ? `✓ "${w}" found in trie (end marker * present)` : `✗ "${w}" not found in trie`);
    setTimeout(() => setHighlight(''), 1500);
  }

  const msgOk = msg.startsWith('✓');
  const msgBad = msg.startsWith('✗');

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Trie — Insert & Search</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Prefix tree for O(m) string operations. * = end of word.</p>
      </div>

      <div className="flex flex-wrap gap-4">
        <div className="flex gap-2 items-end">
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Insert word</label>
            <input style={inputStyle} value={insertInput}
              onChange={e => setInsertInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && insert()} />
          </div>
          <button onClick={insert} className="viz-btn viz-btn--primary">Insert</button>
        </div>
        <div className="flex gap-2 items-end">
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Search word</label>
            <input style={inputStyle} value={searchInput}
              onChange={e => setSearchInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && search()} />
          </div>
          <button onClick={search} className="viz-btn viz-btn--primary">Search</button>
        </div>
      </div>

      <div style={{ background: 'var(--surface-sunken)', borderRadius: '0.5rem', padding: '1rem', maxHeight: '18rem', overflowY: 'auto' }}>
        <span style={{ fontFamily: 'var(--mono)', color: 'var(--text-dim)', fontSize: '0.875rem' }}>root</span>
        <TrieTree node={root} prefix="" highlight={highlight} />
      </div>

      <div className="viz-info" style={msgOk ? { color: 'var(--tier-3)' } : msgBad ? { color: 'var(--bad, #ef4444)' } : {}}>
        {msg}
      </div>
    </div>
  );
}
