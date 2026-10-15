import { useState, useRef, useEffect } from 'react';

interface TrieNode { children: Record<string, TrieNode>; isEnd: boolean; }
const makeNode = (): TrieNode => ({ children: {}, isEnd: false });

function deepCopy(node: TrieNode): TrieNode {
  return { isEnd: node.isEnd, children: Object.fromEntries(Object.entries(node.children).map(([k, v]) => [k, deepCopy(v)])) };
}

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

type AnimStep = { root: TrieNode; highlightPath: string; msg: string; };

function buildInsertSteps(root: TrieNode, word: string): AnimStep[] {
  const steps: AnimStep[] = [];
  const work = deepCopy(root);
  steps.push({ root: deepCopy(work), highlightPath: '', msg: `Inserting "${word}". Starting at root.` });
  let node = work;
  for (let i = 0; i < word.length; i++) {
    const ch = word[i];
    const isNew = !node.children[ch];
    if (isNew) node.children[ch] = makeNode();
    node = node.children[ch];
    if (i === word.length - 1) node.isEnd = true;
    const prefix = word.slice(0, i + 1);
    steps.push({ root: deepCopy(work), highlightPath: prefix,
      msg: isNew ? `Created new node '${ch}' → prefix "${prefix}"` : `Followed existing '${ch}' → prefix "${prefix}"` });
  }
  steps.push({ root: deepCopy(work), highlightPath: word, msg: `Marked end * at "${word}". Insert complete!` });
  return steps;
}

function buildSearchSteps(root: TrieNode, word: string): AnimStep[] {
  const steps: AnimStep[] = [{ root, highlightPath: '', msg: `Searching "${word}". Starting at root.` }];
  let node = root;
  for (let i = 0; i < word.length; i++) {
    const ch = word[i];
    if (!node.children[ch]) {
      steps.push({ root, highlightPath: word.slice(0, i), msg: `Character '${ch}' not found → "${word}" not in trie.` });
      return steps;
    }
    node = node.children[ch];
    const prefix = word.slice(0, i + 1);
    steps.push({ root, highlightPath: prefix, msg: `Found '${ch}' → at "${prefix}"${node.isEnd ? ' (end of word)' : ''}` });
  }
  steps.push({ root, highlightPath: word, msg: node.isEnd ? `✓ "${word}" found in trie` : `✗ "${word}" is only a prefix, not a full word` });
  return steps;
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

const INITIAL_WORDS = ['apple', 'app', 'apt', 'bat', 'ball'];

function makeInitialRoot() {
  let r = makeNode();
  for (const w of INITIAL_WORDS) r = insertWord(r, w);
  return r;
}

export default function TrieViz() {
  const [baseRoot, setBaseRoot] = useState<TrieNode>(makeInitialRoot);
  const [insertInput, setInsertInput] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [steps, setSteps] = useState<AnimStep[]>([]);
  const [stepIdx, setStepIdx] = useState(-1);
  const [isInsert, setIsInsert] = useState(false);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(3);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const nextStepRef = useRef<() => void>(() => {});

  const idle = stepIdx < 0 || steps.length === 0;
  const current = idle ? { root: baseRoot, highlightPath: '', msg: `Trie preloaded with: ${INITIAL_WORDS.join(', ')}` } : steps[stepIdx];

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }

  function startSteps(newSteps: AnimStep[], insert: boolean) {
    stopPlay();
    setSteps(newSteps);
    setStepIdx(0);
    setIsInsert(insert);
  }

  function startInsert() {
    const w = insertInput.trim().toLowerCase();
    if (!w) return;
    startSteps(buildInsertSteps(baseRoot, w), true);
    setInsertInput('');
  }

  function startSearch() {
    const w = searchInput.trim().toLowerCase();
    if (!w) return;
    startSteps(buildSearchSteps(baseRoot, w), false);
  }

  function nextStep() {
    if (idle) return;
    if (stepIdx < steps.length - 1) {
      setStepIdx(i => i + 1);
    } else {
      stopPlay();
      if (isInsert) setBaseRoot(deepCopy(steps[steps.length - 1].root));
      setSteps([]); setStepIdx(-1);
    }
  }

  function stepBack() {
    stopPlay();
    if (stepIdx <= 0) { setSteps([]); setStepIdx(-1); } else { setStepIdx(i => i - 1); }
  }

  function reset() {
    stopPlay(); setSteps([]); setStepIdx(-1); setBaseRoot(makeInitialRoot()); setInsertInput(''); setSearchInput('');
  }

  useEffect(() => { nextStepRef.current = nextStep; });

  useEffect(() => {
    if (!playing) {
      if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
      return;
    }
    timerRef.current = setInterval(() => { nextStepRef.current(); }, 1100 - speed * 200);
    return () => { if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; } };
  }, [playing, speed]);

  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  const msgOk = current.msg.startsWith('✓') || current.msg.includes('Insert complete');
  const msgBad = current.msg.startsWith('✗') || current.msg.includes('not found') || current.msg.includes('not in trie');

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
              onKeyDown={e => e.key === 'Enter' && startInsert()} />
          </div>
          <button onClick={startInsert} className="viz-btn viz-btn--primary">Insert</button>
        </div>
        <div className="flex gap-2 items-end">
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Search word</label>
            <input style={inputStyle} value={searchInput}
              onChange={e => setSearchInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && startSearch()} />
          </div>
          <button onClick={startSearch} className="viz-btn viz-btn--primary">Search</button>
        </div>
      </div>

      <div style={{ background: 'var(--surface-sunken)', borderRadius: '0.5rem', padding: '1rem', maxHeight: '18rem', overflowY: 'auto' }}>
        <span style={{ fontFamily: 'var(--mono)', color: 'var(--text-dim)', fontSize: '0.875rem' }}>root</span>
        <TrieTree node={current.root} prefix="" highlight={current.highlightPath} />
      </div>

      <div className="viz-info" style={msgOk ? { color: 'var(--tier-3)' } : msgBad ? { color: '#ef4444' } : {}}>
        {current.msg}
        {!idle && <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem', marginLeft: '0.5rem' }}>({stepIdx + 1}/{steps.length})</span>}
      </div>

      {!idle && (
        <div className="flex flex-wrap items-center gap-3">
          <button onClick={nextStep} className="viz-btn viz-btn--primary">
            {stepIdx === steps.length - 1 ? (isInsert ? 'Commit Insert' : 'Done') : 'Next Step'}
          </button>
          <button onClick={stepBack} className="viz-btn">← Back</button>
          <button onClick={() => setPlaying(p => !p)} disabled={stepIdx === steps.length - 1} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>
            {playing ? 'Pause' : '▶ Play'}
          </button>
          <button onClick={reset} className="viz-btn">Reset</button>
          <div className="flex items-center gap-2">
            <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
            <input type="range" min={1} max={5} value={speed} onChange={e => setSpeed(Number(e.target.value))} className="speed-slider w-24" />
            <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
          </div>
        </div>
      )}
    </div>
  );
}
