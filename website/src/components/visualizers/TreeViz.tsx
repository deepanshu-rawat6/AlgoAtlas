import { useState, useRef, useEffect, useMemo } from 'react';

// ── Types ────────────────────────────────────────────────────────────────────
interface TNode { val: number; left: TNode | null; right: TNode | null; idx: number; }
type TraversalTab = 'level' | 'preorder' | 'inorder' | 'postorder';
type MainTab = 'traversal' | 'bst' | 'paths' | 'lca';
type BSTMode = 'search' | 'insert' | 'validate';

interface BSTStep { highlighted: number[]; current: number; newNode?: number; valid?: boolean; msg: string; }
interface PathStep { currentPath: number[]; allPaths: number[][]; currentNode: number; msg: string; }

const DEFAULT_INPUT = '[3,9,20,null,null,15,7]';
const BST_INPUT = '[8,4,12,2,6,10,15]';
const R = 18;

// ── Tree helpers ─────────────────────────────────────────────────────────────
function parseTree(input: string): (number | null)[] {
  return input.replace(/[\[\]]/g, '').split(',').map(s => {
    const t = s.trim();
    return (t === 'null' || t === '') ? null : parseInt(t, 10);
  });
}

function buildTree(arr: (number | null)[]): TNode | null {
  if (!arr.length || arr[0] == null) return null;
  const root: TNode = { val: arr[0], left: null, right: null, idx: 0 };
  const q: TNode[] = [root];
  let i = 1;
  while (q.length && i < arr.length) {
    const node = q.shift()!;
    if (i < arr.length && arr[i] != null) { node.left = { val: arr[i]!, left: null, right: null, idx: i }; q.push(node.left); }
    i++;
    if (i < arr.length && arr[i] != null) { node.right = { val: arr[i]!, left: null, right: null, idx: i }; q.push(node.right); }
    i++;
  }
  return root;
}

function computePositions(root: TNode | null, svgW: number, svgH: number): Map<number, [number, number]> {
  const depths = new Map<number, number>();
  const inorderX = new Map<number, number>();
  let counter = 0;
  function assignDepth(node: TNode | null, d: number) {
    if (!node) return;
    depths.set(node.idx, d);
    assignDepth(node.left, d + 1);
    assignDepth(node.right, d + 1);
  }
  function inorder(node: TNode | null) {
    if (!node) return;
    inorder(node.left);
    inorderX.set(node.idx, counter++);
    inorder(node.right);
  }
  assignDepth(root, 0);
  inorder(root);
  const n = counter || 1;
  const maxDepth = depths.size ? Math.max(...depths.values()) : 0;
  const margin = 30;
  const xScale = n > 1 ? (svgW - 2 * margin) / (n - 1) : 0;
  const yStep = maxDepth > 0 ? (svgH - 2 * margin) / maxDepth : svgH / 2;
  const pos = new Map<number, [number, number]>();
  for (const [idx, xi] of inorderX) {
    const x = n === 1 ? svgW / 2 : margin + xi * xScale;
    const y = margin + depths.get(idx)! * yStep;
    pos.set(idx, [x, y]);
  }
  return pos;
}

function getEdges(root: TNode | null): [number, number][] {
  const edges: [number, number][] = [];
  function dfs(n: TNode | null) {
    if (!n) return;
    if (n.left) { edges.push([n.idx, n.left.idx]); dfs(n.left); }
    if (n.right) { edges.push([n.idx, n.right.idx]); dfs(n.right); }
  }
  dfs(root);
  return edges;
}

function getTraversalSequence(root: TNode | null, type: TraversalTab): number[] {
  const seq: number[] = [];
  function level(r: TNode | null) {
    if (!r) return;
    const q = [r];
    while (q.length) { const n = q.shift()!; seq.push(n.idx); if (n.left) q.push(n.left); if (n.right) q.push(n.right); }
  }
  function pre(n: TNode | null) { if (!n) return; seq.push(n.idx); pre(n.left); pre(n.right); }
  function ino(n: TNode | null) { if (!n) return; ino(n.left); seq.push(n.idx); ino(n.right); }
  function post(n: TNode | null) { if (!n) return; post(n.left); post(n.right); seq.push(n.idx); }
  if (type === 'level') level(root);
  else if (type === 'preorder') pre(root);
  else if (type === 'inorder') ino(root);
  else post(root);
  return seq;
}

// ── BST step builders ────────────────────────────────────────────────────────
function buildSearchSteps(root: TNode | null, target: number): BSTStep[] {
  const steps: BSTStep[] = [];
  const path: number[] = [];
  let node = root;
  while (node) {
    path.push(node.idx);
    if (target === node.val) {
      steps.push({ highlighted: [...path], current: node.idx, path, msg: `✓ Found ${target}!`, valid: true });
      return steps;
    }
    const dir = target < node.val ? 'left' : 'right';
    steps.push({ highlighted: [...path], current: node.idx, msg: `${target} vs ${node.val} → go ${dir}` });
    node = target < node.val ? node.left : node.right;
  }
  steps.push({ highlighted: [...path], current: -1, msg: `✗ ${target} not found.`, valid: false });
  return steps;
}

function buildInsertSteps(root: TNode | null, val: number): BSTStep[] {
  const steps: BSTStep[] = [];
  if (!root) { steps.push({ highlighted: [], current: -1, msg: `Insert ${val} as root.` }); return steps; }
  const path: number[] = [];
  let node = root;
  while (node) {
    path.push(node.idx);
    const dir = val < node.val ? 'left' : 'right';
    steps.push({ highlighted: [...path], current: node.idx, msg: `${val} vs ${node.val} → go ${dir}` });
    const child = val < node.val ? node.left : node.right;
    if (!child) {
      // ponytail: new node gets a synthetic idx for highlighting; doesn't actually mutate tree
      const newIdx = 1000 + path.length;
      steps.push({ highlighted: [...path, newIdx], current: newIdx, newNode: newIdx, msg: `Insert ${val} as ${dir} child of ${node.val}.` });
      return steps;
    }
    node = child;
  }
  return steps;
}

function buildValidateSteps(root: TNode | null): BSTStep[] {
  const steps: BSTStep[] = [];
  function dfs(node: TNode | null, min: number, max: number) {
    if (!node) return;
    const valid = node.val > min && node.val < max;
    const minStr = min === -Infinity ? '-∞' : String(min);
    const maxStr = max === Infinity ? '+∞' : String(max);
    steps.push({ highlighted: [node.idx], current: node.idx, valid, msg: `Node ${node.val}: range (${minStr}, ${maxStr}) → ${valid ? '✓ valid' : '✗ INVALID!'}` });
    if (!valid) return;
    dfs(node.left, min, node.val);
    dfs(node.right, node.val, max);
  }
  dfs(root, -Infinity, Infinity);
  return steps;
}

// ── LCA step builder ─────────────────────────────────────────────────────────
interface LCAStep { highlighted: number[]; current: number; lcaIdx: number; msg: string; }

function findPath(root: TNode | null, targetVal: number): number[] {
  function dfs(node: TNode | null, path: number[]): boolean {
    if (!node) return false;
    path.push(node.idx);
    if (node.val === targetVal) return true;
    if (dfs(node.left, path) || dfs(node.right, path)) return true;
    path.pop();
    return false;
  }
  const path: number[] = [];
  dfs(root, path);
  return path;
}

function buildLCASteps(root: TNode | null, pVal: number, qVal: number, nodeVals: Map<number, number>): LCAStep[] {
  if (!root) return [];
  const pPath = findPath(root, pVal);
  const qPath = findPath(root, qVal);
  if (!pPath.length || !qPath.length) return [{
    highlighted: [], current: -1, lcaIdx: -1,
    msg: `Node ${!pPath.length ? pVal : qVal} not found in tree.`,
  }];
  // deepest common prefix
  let lcaIdx = -1;
  for (let i = 0; i < Math.min(pPath.length, qPath.length); i++) {
    if (pPath[i] === qPath[i]) lcaIdx = pPath[i]; else break;
  }
  const lcaVal = nodeVals.get(lcaIdx) ?? '?';
  return [
    { highlighted: pPath, current: pPath[pPath.length - 1], lcaIdx: -1,
      msg: `Path to p=${pVal}: [${pPath.map(i => nodeVals.get(i)).join(' → ')}]` },
    { highlighted: qPath, current: qPath[qPath.length - 1], lcaIdx: -1,
      msg: `Path to q=${qVal}: [${qPath.map(i => nodeVals.get(i)).join(' → ')}]` },
    { highlighted: [...new Set([...pPath, ...qPath])], current: -1, lcaIdx: -1,
      msg: `Both paths traced. Finding deepest common node...` },
    { highlighted: [...new Set([...pPath, ...qPath])], current: lcaIdx, lcaIdx,
      msg: `LCA(${pVal}, ${qVal}) = ${lcaVal} ✓ — deepest node that is ancestor of both.` },
  ];
}

// ── Path step builder ────────────────────────────────────────────────────────
function buildPathSteps(root: TNode | null): PathStep[] {
  const steps: PathStep[] = [];
  const allPaths: number[][] = [];
  function dfs(node: TNode | null, path: number[]) {
    if (!node) return;
    path.push(node.val);
    steps.push({ currentPath: [...path], allPaths: allPaths.map(p => [...p]), currentNode: node.idx, msg: `Visit ${node.val} → path: [${path.join(' → ')}]` });
    if (!node.left && !node.right) {
      allPaths.push([...path]);
      steps.push({ currentPath: [...path], allPaths: allPaths.map(p => [...p]), currentNode: node.idx, msg: `Leaf! Path complete: [${path.join(' → ')}]` });
    } else {
      if (node.left) dfs(node.left, path);
      if (node.right) dfs(node.right, path);
    }
    path.pop();
  }
  dfs(root, []);
  if (steps.length) steps.push({ ...steps[steps.length - 1], msg: `Done. ${allPaths.length} path(s) found.` });
  return steps;
}

// ── Shared SVG component ──────────────────────────────────────────────────────
function TreeSVG({ positions, edges, highlighted, current, newNode, nodeVals, validMap }: {
  positions: Map<number, [number, number]>;
  edges: [number, number][];
  highlighted: number[];
  current: number;
  newNode?: number;
  nodeVals: Map<number, number>;
  validMap?: Map<number, boolean>;
}) {
  const svgH = 200;
  return (
    <div className="panel p-3">
      <svg viewBox={`0 0 500 ${svgH}`} className="w-full" style={{ maxHeight: svgH + 20 }}>
        {edges.map(([a, b]) => {
          const pa = positions.get(a), pb = positions.get(b);
          if (!pa || !pb) return null;
          return <line key={`${a}-${b}`} x1={pa[0]} y1={pa[1] + R} x2={pb[0]} y2={pb[1] - R} stroke="var(--border)" strokeWidth="2" />;
        })}
        {[...positions.entries()].map(([idx, [cx, cy]]) => {
          const isCurrent = current === idx;
          const isHl = highlighted.includes(idx);
          const isNew = newNode === idx;
          const vld = validMap?.get(idx);
          let fill = 'var(--surface-raised)', stroke = 'var(--border)';
          if (isNew) { fill = 'var(--tier-3)'; stroke = 'var(--tier-3)'; }
          else if (isCurrent) { fill = 'var(--accent-soft)'; stroke = 'var(--accent)'; }
          else if (vld === false) { fill = 'color-mix(in srgb, #ef4444 30%, transparent)'; stroke = '#ef4444'; }
          else if (vld === true) { fill = 'color-mix(in srgb, var(--tier-3) 25%, transparent)'; stroke = 'var(--tier-3)'; }
          else if (isHl) { fill = 'var(--accent)'; stroke = 'var(--accent)'; }
          const val = nodeVals.get(idx);
          return (
            <g key={idx}>
              <circle cx={cx} cy={cy} r={R} fill={fill} stroke={stroke} strokeWidth="2" />
              <text x={cx} y={cy + 5} textAnchor="middle" fill="var(--text)" fontSize="12" fontWeight="bold">{val}</text>
            </g>
          );
        })}
        {newNode !== undefined && (() => {
          // draw synthetic new node at a plausible position (below current)
          const cp = positions.get(current);
          if (!cp) return null;
          const nx = cp[0] + 30, ny = cp[1] + 50;
          const val = newNode; // will be labelled from outside
          return (
            <g>
              <line x1={cp[0]} y1={cp[1] + R} x2={nx} y2={ny - R} stroke="var(--tier-3)" strokeWidth="2" strokeDasharray="4" />
              <circle cx={nx} cy={ny} r={R} fill="color-mix(in srgb, var(--tier-3) 30%, transparent)" stroke="var(--tier-3)" strokeWidth="2" strokeDasharray="4" />
              <text x={nx} y={ny + 5} textAnchor="middle" fill="var(--tier-3)" fontSize="12" fontWeight="bold">new</text>
            </g>
          );
        })()}
      </svg>
    </div>
  );
}

// ── Shared step controls ──────────────────────────────────────────────────────
function StepControls({ onNext, onBack, onPlay, onReset, playing, done, histLen, speed, onSpeed }:
  { onNext: () => void; onBack: () => void; onPlay: () => void; onReset: () => void; playing: boolean; done: boolean; histLen: number; speed: number; onSpeed: (n: number) => void; }) {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <button onClick={onNext} disabled={done} className="viz-btn viz-btn--primary">Next Step</button>
      <button onClick={onBack} disabled={histLen === 0} className="viz-btn">← Back</button>
      <button onClick={onPlay} disabled={done} className={playing ? 'viz-btn' : 'viz-btn viz-btn--primary'}>{playing ? 'Pause' : '▶ Play'}</button>
      <button onClick={onReset} className="viz-btn">Reset</button>
      <div className="flex items-center gap-2">
        <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Speed</span>
        <input type="range" min={1} max={5} value={speed} onChange={e => onSpeed(Number(e.target.value))} className="speed-slider w-24" />
        <span style={{ color: 'var(--text-dim)', fontSize: '0.75rem' }}>{speed}x</span>
      </div>
    </div>
  );
}

// ── useStepPlayer hook ────────────────────────────────────────────────────────
function useStepPlayer(totalSteps: number, speed: number) {
  const [stepIdx, setStepIdx] = useState(-1);
  const [playing, setPlaying] = useState(false);
  const [history, setHistory] = useState<number[]>([]);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const nextRef = useRef<() => void>(() => {});

  function stopPlay() {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
    setPlaying(false);
  }
  function reset() { stopPlay(); setStepIdx(-1); setHistory([]); }
  function next() {
    if (stepIdx >= totalSteps - 1) { setPlaying(false); return; }
    setHistory(h => [...h, stepIdx]);
    setStepIdx(s => s + 1);
  }
  function back() { stopPlay(); if (history.length === 0) return; setStepIdx(history[history.length - 1]); setHistory(h => h.slice(0, -1)); }
  function togglePlay() {
    if (playing) { stopPlay(); return; }
    setPlaying(true);
    timerRef.current = setInterval(() => nextRef.current(), 1100 - speed * 200);
  }

  useEffect(() => { nextRef.current = next; });
  useEffect(() => {
    if (!playing) return;
    if (timerRef.current) clearInterval(timerRef.current);
    timerRef.current = setInterval(() => nextRef.current(), 1100 - speed * 200);
  }, [speed, playing]);
  useEffect(() => () => { if (timerRef.current) clearInterval(timerRef.current); }, []);

  return { stepIdx, playing, history, reset, next, back, togglePlay, stopPlay };
}

// ── Input styles ──────────────────────────────────────────────────────────────
const inputSm: React.CSSProperties = {
  background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: '0.375rem',
  padding: '0.375rem 0.75rem', color: 'var(--text)', fontSize: '0.875rem', outline: 'none',
};

// ── Main component ────────────────────────────────────────────────────────────
export default function TreeViz() {
  const [treeInput, setTreeInput] = useState(DEFAULT_INPUT);
  const [treeArr, setTreeArr] = useState<(number | null)[]>(() => parseTree(DEFAULT_INPUT));
  const [mainTab, setMainTab] = useState<MainTab>('traversal');
  const [traversalTab, setTraversalTab] = useState<TraversalTab>('level');
  const [bstMode, setBstMode] = useState<BSTMode>('search');
  const [bstInput, setBstInput] = useState('6');
  const [bstSteps, setBstSteps] = useState<BSTStep[]>([]);
  const [lcaInputP, setLcaInputP] = useState('15');
  const [lcaInputQ, setLcaInputQ] = useState('7');
  const [lcaSteps, setLcaSteps] = useState<LCAStep[]>([]);
  const [speed, setSpeed] = useState(3);

  const treeRoot = useMemo(() => buildTree(treeArr), [treeArr]);
  const positions = useMemo(() => computePositions(treeRoot, 500, 180), [treeRoot]);
  const edges = useMemo(() => getEdges(treeRoot), [treeRoot]);
  const nodeVals = useMemo(() => {
    const m = new Map<number, number>();
    function walk(n: TNode | null) { if (!n) return; m.set(n.idx, n.val); walk(n.left); walk(n.right); }
    walk(treeRoot);
    return m;
  }, [treeRoot]);

  // Traversal
  const travSeq = useMemo(() => getTraversalSequence(treeRoot, traversalTab), [treeRoot, traversalTab]);
  const trav = useStepPlayer(travSeq.length, speed);

  // BST
  const bst = useStepPlayer(bstSteps.length, speed);

  // Paths
  const pathSteps = useMemo(() => buildPathSteps(treeRoot), [treeRoot]);
  const paths = useStepPlayer(pathSteps.length, speed);

  // LCA
  const lca = useStepPlayer(lcaSteps.length, speed);

  function applyTree() {
    const arr = parseTree(treeInput);
    setTreeArr(arr);
    trav.reset(); bst.reset(); setBstSteps([]); paths.reset(); lca.reset(); setLcaSteps([]);
  }

  function switchMainTab(t: MainTab) {
    setMainTab(t);
    trav.reset(); bst.reset(); setBstSteps([]); paths.reset(); lca.reset(); setLcaSteps([]);
    if (t === 'bst') { setTreeInput(BST_INPUT); setTreeArr(parseTree(BST_INPUT)); }
    if (t === 'lca') { setTreeInput(DEFAULT_INPUT); setTreeArr(parseTree(DEFAULT_INPUT)); }
  }

  function runLCA() {
    const p = parseInt(lcaInputP, 10), q = parseInt(lcaInputQ, 10);
    if (isNaN(p) || isNaN(q)) return;
    lca.reset();
    setLcaSteps(buildLCASteps(treeRoot, p, q, nodeVals));
  }

  function runBST() {
    const val = parseInt(bstInput, 10);
    if (isNaN(val)) return;
    bst.reset();
    if (bstMode === 'search') setBstSteps(buildSearchSteps(treeRoot, val));
    else if (bstMode === 'insert') setBstSteps(buildInsertSteps(treeRoot, val));
    else setBstSteps(buildValidateSteps(treeRoot));
  }

  // Current step data
  const travStep = trav.stepIdx >= 0 ? trav.stepIdx : -1;
  const travVisited = travSeq.slice(0, travStep + 1);
  const travCurrent = travStep < travSeq.length ? travSeq[travStep] : -1;

  const bstStep = bst.stepIdx >= 0 && bst.stepIdx < bstSteps.length ? bstSteps[bst.stepIdx] : null;
  const pathStep = paths.stepIdx >= 0 && paths.stepIdx < pathSteps.length ? pathSteps[paths.stepIdx] : null;

  // Validate map for coloring
  const validateMap = useMemo(() => {
    if (bstMode !== 'validate') return undefined;
    const m = new Map<number, boolean>();
    for (const s of bstSteps) { if (s.valid !== undefined) m.set(s.current, s.valid); }
    return m;
  }, [bstSteps, bstMode]);

  return (
    <div className="panel p-6 space-y-6">
      <div>
        <h3 style={{ color: 'var(--text)', fontSize: '1.05rem', fontWeight: 600, marginBottom: '0.25rem' }}>Tree Visualizer</h3>
        <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Traversals · BST operations · Path problems</p>
      </div>

      {/* Custom tree input */}
      <div className="flex gap-2 items-end flex-wrap">
        <div>
          <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Tree (array notation)</label>
          <input style={{ ...inputSm, width: '18rem' }} value={treeInput}
            onChange={e => setTreeInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && applyTree()}
            placeholder="[3,9,20,null,null,15,7]" />
        </div>
        <button onClick={applyTree} className="viz-btn viz-btn--primary">Apply</button>
        <button onClick={() => { setTreeInput(DEFAULT_INPUT); setTreeArr(parseTree(DEFAULT_INPUT)); trav.reset(); bst.reset(); setBstSteps([]); paths.reset(); }} className="viz-btn">Reset Tree</button>
      </div>

      {/* Main tabs */}
      <div className="flex gap-2 flex-wrap">
        {(['traversal', 'bst', 'paths', 'lca'] as MainTab[]).map(t => (
          <button key={t} onClick={() => switchMainTab(t)} className={mainTab === t ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
            {t === 'traversal' ? 'Traversal' : t === 'bst' ? 'BST Operations' : t === 'paths' ? 'Path Problems' : 'LCA'}
          </button>
        ))}
      </div>

      {/* ── TRAVERSAL ── */}
      {mainTab === 'traversal' && (
        <div className="space-y-4">
          <div className="flex gap-2 flex-wrap">
            {(['level', 'preorder', 'inorder', 'postorder'] as TraversalTab[]).map(t => (
              <button key={t} onClick={() => { setTraversalTab(t); trav.reset(); }}
                className={traversalTab === t ? 'viz-btn viz-btn--primary' : 'viz-btn'} style={{ fontSize: '0.8rem' }}>
                {t === 'level' ? 'Level Order (BFS)' : t === 'preorder' ? 'Preorder' : t === 'inorder' ? 'Inorder' : 'Postorder'}
              </button>
            ))}
          </div>
          <TreeSVG positions={positions} edges={edges} highlighted={travVisited} current={travCurrent} nodeVals={nodeVals} />
          {travStep >= 0 && (
            <div className="flex gap-2 flex-wrap items-center">
              <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Visited:</span>
              {travVisited.map((idx, i) => (
                <span key={i} style={{ background: 'color-mix(in srgb, var(--accent) 20%, transparent)', border: '1px solid var(--accent)', padding: '0.125rem 0.5rem', borderRadius: '0.25rem', fontSize: '0.875rem', fontFamily: 'var(--mono)', color: 'var(--accent)' }}>{nodeVals.get(idx)}</span>
              ))}
            </div>
          )}
          <div className="viz-info">
            {trav.stepIdx < 0 ? `Press Next Step to begin ${traversalTab} traversal.`
              : trav.stepIdx >= travSeq.length ? `Done! Order: [${travSeq.map(i => nodeVals.get(i)).join(', ')}]`
              : `Visiting node ${nodeVals.get(travCurrent)} — step ${trav.stepIdx + 1}/${travSeq.length}`}
          </div>
          <StepControls onNext={trav.next} onBack={trav.back} onPlay={trav.togglePlay} onReset={trav.reset}
            playing={trav.playing} done={trav.stepIdx >= travSeq.length} histLen={trav.history.length} speed={speed} onSpeed={setSpeed} />
        </div>
      )}

      {/* ── BST OPERATIONS ── */}
      {mainTab === 'bst' && (
        <div className="space-y-4">
          <div className="flex gap-2 flex-wrap">
            {(['search', 'insert', 'validate'] as BSTMode[]).map(m => (
              <button key={m} onClick={() => { setBstMode(m); bst.reset(); setBstSteps([]); }}
                className={bstMode === m ? 'viz-btn viz-btn--primary' : 'viz-btn'}>
                {m.charAt(0).toUpperCase() + m.slice(1)}
              </button>
            ))}
          </div>
          {bstMode !== 'validate' && (
            <div className="flex gap-2 items-end">
              <div>
                <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>
                  {bstMode === 'search' ? 'Search for value' : 'Insert value'}
                </label>
                <input style={{ ...inputSm, width: '6rem' }} value={bstInput}
                  onChange={e => setBstInput(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && runBST()} placeholder="e.g. 6" />
              </div>
              <button onClick={runBST} className="viz-btn viz-btn--primary">
                {bstMode === 'search' ? 'Search' : 'Insert'}
              </button>
            </div>
          )}
          {bstMode === 'validate' && (
            <button onClick={runBST} className="viz-btn viz-btn--primary">Run Validation</button>
          )}
          <TreeSVG positions={positions} edges={edges}
            highlighted={bstStep?.highlighted ?? []}
            current={bstStep?.current ?? -1}
            newNode={bstStep?.newNode}
            nodeVals={nodeVals}
            validMap={bstMode === 'validate' && bstStep ? (() => {
              const m = new Map<number, boolean>();
              for (let i = 0; i <= bst.stepIdx && i < bstSteps.length; i++) {
                const s = bstSteps[i];
                if (s.valid !== undefined) m.set(s.current, s.valid);
              }
              return m;
            })() : undefined}
          />
          <div className="viz-info" style={bstStep?.valid === false ? { color: '#ef4444' } : bstStep?.valid === true ? { color: 'var(--tier-3)' } : {}}>
            {bstSteps.length === 0 ? `Configure and press ${bstMode === 'validate' ? 'Run Validation' : bstMode.charAt(0).toUpperCase() + bstMode.slice(1)} to start.`
              : bstStep ? bstStep.msg
              : 'Press Next Step.'}
          </div>
          {bstSteps.length > 0 && (
            <StepControls onNext={bst.next} onBack={bst.back} onPlay={bst.togglePlay} onReset={bst.reset}
              playing={bst.playing} done={bst.stepIdx >= bstSteps.length - 1} histLen={bst.history.length} speed={speed} onSpeed={setSpeed} />
          )}
          {bstMode !== 'validate' && (
            <p style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>
              Tip: Use BST tree <code>[8,4,12,2,6,10,15]</code> for best results. The tree input above controls the tree.
            </p>
          )}
        </div>
      )}

      {/* ── PATH PROBLEMS ── */}
      {mainTab === 'paths' && (
        <div className="space-y-4">
          <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Root-to-leaf DFS — watch each path build and complete.</p>
          <TreeSVG positions={positions} edges={edges}
            highlighted={pathStep ? pathSteps.slice(0, paths.stepIdx + 1).map(s => s.currentNode) : []}
            current={pathStep?.currentNode ?? -1}
            nodeVals={nodeVals}
          />
          {/* Found paths */}
          {pathStep && pathStep.allPaths.length > 0 && (
            <div className="space-y-1">
              <div style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Completed paths:</div>
              {pathStep.allPaths.map((p, i) => (
                <div key={i} style={{ fontFamily: 'var(--mono)', fontSize: '0.875rem', color: 'var(--tier-3)' }}>
                  [{p.join(' → ')}]
                </div>
              ))}
            </div>
          )}
          {/* Current path progress */}
          {pathStep && (
            <div className="flex gap-1 flex-wrap items-center">
              <span style={{ color: 'var(--text-faint)', fontSize: '0.75rem' }}>Current path:</span>
              {pathStep.currentPath.map((v, i) => (
                <span key={i} style={{ background: 'color-mix(in srgb, var(--accent) 20%, transparent)', border: '1px solid var(--accent)', padding: '0.125rem 0.5rem', borderRadius: '0.25rem', fontSize: '0.875rem', fontFamily: 'var(--mono)', color: 'var(--accent)' }}>{v}</span>
              ))}
            </div>
          )}
          <div className="viz-info">
            {paths.stepIdx < 0 ? 'Press Next Step to start DFS path enumeration.'
              : pathStep ? pathStep.msg
              : 'Done.'}
          </div>
          <StepControls onNext={paths.next} onBack={paths.back} onPlay={paths.togglePlay} onReset={paths.reset}
            playing={paths.playing} done={paths.stepIdx >= pathSteps.length - 1} histLen={paths.history.length} speed={speed} onSpeed={setSpeed} />
        </div>
      )}

      {/* ── LCA ── */}
      {mainTab === 'lca' && (
        <div className="space-y-4">
          <p style={{ color: 'var(--text-dim)', fontSize: '0.875rem' }}>Lowest Common Ancestor — deepest node that is an ancestor of both p and q.</p>
          <div className="flex flex-wrap gap-3 items-end">
            <div>
              <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Node p (value)</label>
              <input style={{ ...inputSm, width: '5rem' }} value={lcaInputP} onChange={e => setLcaInputP(e.target.value)} onKeyDown={e => e.key === 'Enter' && runLCA()} />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-faint)', marginBottom: '0.25rem' }}>Node q (value)</label>
              <input style={{ ...inputSm, width: '5rem' }} value={lcaInputQ} onChange={e => setLcaInputQ(e.target.value)} onKeyDown={e => e.key === 'Enter' && runLCA()} />
            </div>
            <button onClick={runLCA} className="viz-btn viz-btn--primary">Find LCA</button>
          </div>
          {(() => {
            const lcaStep = lca.stepIdx >= 0 && lca.stepIdx < lcaSteps.length ? lcaSteps[lca.stepIdx] : null;
            const isFound = lcaStep?.lcaIdx !== undefined && lcaStep.lcaIdx >= 0;
            return (
              <>
                <TreeSVG positions={positions} edges={edges}
                  highlighted={lcaStep?.highlighted ?? []}
                  current={lcaStep?.current ?? -1}
                  nodeVals={nodeVals}
                />
                <div className="viz-info" style={isFound ? { color: 'var(--tier-3)' } : {}}>
                  {lcaSteps.length === 0 ? 'Enter two node values and press Find LCA.'
                    : lcaStep ? lcaStep.msg
                    : 'Press Next Step.'}
                </div>
                {lcaSteps.length > 0 && (
                  <StepControls onNext={lca.next} onBack={lca.back} onPlay={lca.togglePlay} onReset={lca.reset}
                    playing={lca.playing} done={lca.stepIdx >= lcaSteps.length - 1} histLen={lca.history.length} speed={speed} onSpeed={setSpeed} />
                )}
              </>
            );
          })()}
        </div>
      )}

      {/* Legend */}
      <div className="flex gap-4 text-xs flex-wrap" style={{ color: 'var(--text-dim)' }}>
        <span className="flex items-center gap-1"><span style={{ display: 'inline-block', width: '0.75rem', height: '0.75rem', borderRadius: '50%', background: 'var(--accent-soft)', border: '2px solid var(--accent)' }}></span>Current</span>
        <span className="flex items-center gap-1"><span style={{ display: 'inline-block', width: '0.75rem', height: '0.75rem', borderRadius: '50%', background: 'var(--accent)' }}></span>Visited/Path</span>
        {mainTab === 'bst' && bstMode === 'validate' && <>
          <span className="flex items-center gap-1"><span style={{ display: 'inline-block', width: '0.75rem', height: '0.75rem', borderRadius: '50%', background: 'color-mix(in srgb, var(--tier-3) 25%, transparent)', border: '2px solid var(--tier-3)' }}></span>Valid</span>
          <span className="flex items-center gap-1"><span style={{ display: 'inline-block', width: '0.75rem', height: '0.75rem', borderRadius: '50%', background: 'color-mix(in srgb, #ef4444 30%, transparent)', border: '2px solid #ef4444' }}></span>Invalid</span>
        </>}
      </div>
    </div>
  );
}
