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

// Render trie as nested list
function TrieTree({ node, prefix, highlight }: { node: TrieNode; prefix: string; highlight: string }) {
  const chars = Object.keys(node.children).sort();
  if (chars.length === 0) return null;
  return (
    <ul className="ml-4 border-l border-slate-700 pl-3 space-y-1">
      {chars.map(ch => {
        const child = node.children[ch];
        const path = prefix + ch;
        const isHl = highlight.startsWith(path);
        return (
          <li key={ch}>
            <span className={`font-mono text-sm px-1.5 py-0.5 rounded ${isHl ? 'bg-yellow-800 text-yellow-200' : 'text-slate-300'} ${child.isEnd ? 'border border-green-700 text-green-300' : ''}`}>
              {ch}{child.isEnd ? ' *' : ''}
            </span>
            <TrieTree node={child} prefix={path} highlight={highlight} />
          </li>
        );
      })}
    </ul>
  );
}

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

  return (
    <div className="bg-slate-800/60 rounded-xl p-6 space-y-6">
      <div>
        <h3 className="text-lg font-semibold text-slate-100 mb-1">Trie — Insert & Search</h3>
        <p className="text-sm text-slate-400">Prefix tree for O(m) string operations. * = end of word.</p>
      </div>

      <div className="flex flex-wrap gap-4">
        <div className="flex gap-2 items-end">
          <div>
            <label className="block text-xs text-slate-400 mb-1">Insert word</label>
            <input className="w-28 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={insertInput} onChange={e => setInsertInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && insert()} />
          </div>
          <button onClick={insert} className="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-sm rounded">Insert</button>
        </div>
        <div className="flex gap-2 items-end">
          <div>
            <label className="block text-xs text-slate-400 mb-1">Search word</label>
            <input className="w-28 bg-slate-700 border border-slate-600 rounded px-3 py-1.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              value={searchInput} onChange={e => setSearchInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && search()} />
          </div>
          <button onClick={search} className="px-3 py-1.5 bg-blue-700 hover:bg-blue-600 text-white text-sm rounded">Search</button>
        </div>
      </div>

      <div className="bg-slate-900/60 rounded-lg p-4 max-h-72 overflow-y-auto">
        <span className="font-mono text-slate-400 text-sm">root</span>
        <TrieTree node={root} prefix="" highlight={highlight} />
      </div>

      <div className={`rounded-lg px-4 py-3 text-sm font-mono min-h-10 ${msg.startsWith('✓') ? 'bg-green-900/40 text-green-300' : msg.startsWith('✗') ? 'bg-red-900/40 text-red-300' : 'bg-slate-900/60 text-slate-300'}`}>{msg}</div>
    </div>
  );
}
