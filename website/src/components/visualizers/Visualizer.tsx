import SlidingWindowViz from './SlidingWindowViz';
import TwoPointersViz from './TwoPointersViz';
import BFSViz from './BFSViz';
import BinarySearchViz from './BinarySearchViz';
import HashMapViz from './HashMapViz';
import StackViz from './StackViz';
import LinkedListViz from './LinkedListViz';
import TreeViz from './TreeViz';
import HeapViz from './HeapViz';
import IntervalsViz from './IntervalsViz';
import DPViz from './DPViz';
import DP2DViz from './DP2DViz';
import BacktrackingViz from './BacktrackingViz';
import GreedyViz from './GreedyViz';
import TrieViz from './TrieViz';
import BitViz from './BitViz';
import RecursionViz from './RecursionViz';
import SortingViz from './SortingViz';
import StringViz from './StringViz';
import MathViz from './MathViz';

interface Props { slug: string; }

export default function Visualizer({ slug }: Props) {
  switch (slug) {
    case 'sliding_window':    return <SlidingWindowViz />;
    case 'two_pointers':      return <TwoPointersViz />;
    case 'graphs':
    case 'advanced_graphs':   return <BFSViz />;
    case 'binary_search':     return <BinarySearchViz />;
    case 'arrays_and_hashing':return <HashMapViz />;
    case 'stack':             return <StackViz />;
    case 'linked_list':       return <LinkedListViz />;
    case 'trees':             return <TreeViz />;
    case 'heap':              return <HeapViz />;
    case 'intervals':         return <IntervalsViz />;
    case '1d_dp':             return <DPViz />;
    case '2d_dp':             return <DP2DViz />;
    case 'backtracking':      return <BacktrackingViz />;
    case 'greedy':            return <GreedyViz />;
    case 'tries':             return <TrieViz />;
    case 'bit_manipulation':  return <BitViz />;
    case 'recursion':         return <RecursionViz />;
    case 'algorithms':        return <SortingViz />;
    case 'strings':           return <StringViz />;
    case 'math_and_geometry': return <MathViz />;
    default:
      return <p className="text-slate-500 py-4">No visualizer for this pattern yet.</p>;
  }
}
