const fs = require('fs');
const content = fs.readFileSync('molecular-weight-calculator.html', 'utf8');

// Extract script
const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>\s*<\/body>/);
if (!scriptMatch) {
  console.error("Could not find main script!");
  process.exit(1);
}

// Mock DOM elements and Chart
const dom = {};
global.window = {
  location: { search: '', href: 'https://calcworld.net' },
  addEventListener: () => {}
};
global.document = {
  documentElement: { classList: { contains: () => true, add: () => {}, remove: () => {} } },
  getElementById: (id) => {
    if (!dom[id]) {
      dom[id] = {
        value: '',
        textContent: '',
        innerHTML: '',
        className: '',
        classList: { add: () => {}, remove: () => {}, contains: () => false },
        querySelectorAll: () => []
      };
    }
    return dom[id];
  },
  querySelectorAll: () => []
};
global.Chart = function() {
  return { destroy: () => {} };
};

// Evaluate the script in our mock environment
eval(scriptMatch[1]);

console.log("Script evaluated successfully.");

const testFormulas = [
  'H2O',
  'C6H12O6',
  'C8H10N4O2',
  'C2H5OH',
  'C9H8O4',
  'H2SO4',
  'C16H18N2O4S',
  'C27H46O',
  'CuSO4*5H2O',
  'K4[Fe(CN)6]',
  '(NH4)2HPO4',
  'CH3COOH',
  'Ca(OH)2',
  'Fe2(SO4)3',
  '[Co(NH3)5Cl]Cl2',
  '2H2O'
];

for (const f of testFormulas) {
  try {
    calculateFormula(f);
    console.log(`[PASS] ${f} -> Molar Mass = ${currentParsed.totalMolarMass.toFixed(3)} g/mol, Empirical = ${currentParsed.empirical}, Atoms = ${currentParsed.totalAtoms}`);
  } catch (err) {
    console.error(`[FAIL] ${f} -> ${err.message}`);
  }
}
