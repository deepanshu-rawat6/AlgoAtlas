import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../..');
const CONTENT_DIR = path.resolve(__dirname, '../src/content/patterns');
const DATA_DIR = path.resolve(__dirname, '../src/data/patterns');

const PHASE_MAP = {
  1: ['arrays_and_hashing', 'two_pointers', 'sliding_window', 'trees', 'graphs', 'advanced_graphs'],
  2: ['heap', 'binary_search', 'linked_list', 'stack', 'tries', 'intervals'],
  3: ['1d_dp', '2d_dp', 'backtracking', 'greedy', 'strings', 'bit_manipulation', 'math_and_geometry', 'recursion', 'algorithms', 'utilities'],
};

const PHASE_BY_SLUG = {};
for (const [phase, slugs] of Object.entries(PHASE_MAP)) {
  for (const slug of slugs) PHASE_BY_SLUG[slug] = Number(phase);
}

function toTitle(slug) {
  return slug.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

// Clean and recreate dirs
for (const dir of [CONTENT_DIR, DATA_DIR]) {
  if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true });
  fs.mkdirSync(dir, { recursive: true });
}

const allSlugs = Object.values(PHASE_MAP).flat();
let total = 0;

for (const slug of allSlugs) {
  const srcDir = path.join(REPO_ROOT, slug);
  if (!fs.existsSync(srcDir)) {
    console.warn(`  skipping ${slug} (not found)`);
    continue;
  }

  // Copy README and NOTES to data dir (fixing mermaid syntax in the process)
  const dataDestDir = path.join(DATA_DIR, slug);
  fs.mkdirSync(dataDestDir, { recursive: true });

  for (const file of ['README.md', 'NOTES.md']) {
    const src = path.join(srcDir, file);
    if (!fs.existsSync(src)) continue;
    let content = fs.readFileSync(src, 'utf8');
    // Fix mermaid v11 syntax inside mermaid blocks
    content = content.replace(/```mermaid\n([\s\S]*?)```/g, (_, block) => {
      let fixed = block
        .replace(/<br>/g, '<br/>')   // bare <br> → <br/>
        .replace(/\\n/g, '<br/>');   // literal \n → <br/>
      // Quote unquoted diamond labels {text} with special chars
      fixed = fixed.replace(/\{([^"{}][^{}]*)\}/g, (m, inner) =>
        /[()[\]\/<>]/.test(inner) ? `{"${inner}"}` : m
      );
      // Quote unquoted square node labels [text] with special chars
      fixed = fixed.replace(/\[([^"\]<][^\]]*)\]/g, (m, inner) =>
        /[()[\]\/]/.test(inner) && !inner.startsWith('"') ? `["${inner}"]` : m
      );
      return '```mermaid\n' + fixed + '```';
    });
    fs.writeFileSync(path.join(dataDestDir, file), content);
  }

  // Copy solution files
  const codeDir = path.join(srcDir, 'code');
  let problemCount = 0;

  if (fs.existsSync(codeDir)) {
    const problems = fs.readdirSync(codeDir).filter(d =>
      fs.statSync(path.join(codeDir, d)).isDirectory()
    );
    problemCount = problems.length;

    const solutionsDir = path.join(dataDestDir, 'solutions');
    for (const problem of problems) {
      const solutionSrc = path.join(codeDir, problem, 'solution.py');
      if (fs.existsSync(solutionSrc)) {
        fs.mkdirSync(solutionsDir, { recursive: true });
        fs.copyFileSync(solutionSrc, path.join(solutionsDir, `${problem}.py`));
      }
    }
  }

  // Write flat meta JSON for Astro content collection
  const meta = {
    slug,
    title: toTitle(slug),
    phase: PHASE_BY_SLUG[slug] ?? 3,
    problemCount,
  };
  fs.writeFileSync(path.join(CONTENT_DIR, `${slug}.json`), JSON.stringify(meta, null, 2));

  console.log(`  ✓ ${slug} (${problemCount} problems, phase ${meta.phase})`);
  total++;
}

console.log(`\nSynced ${total} patterns to src/content/patterns/ and src/data/patterns/`);
