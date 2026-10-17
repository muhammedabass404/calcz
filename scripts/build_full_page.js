const fs = require('fs');
const path = require('path');

const targetFile = path.join(__dirname, 'molecular-weight-calculator.html');

// Read elements from generate_html.js
const genContent = fs.readFileSync(path.join(__dirname, 'generate_html.js'), 'utf8');
const elementsMatch = genContent.match(/const elements = (\[[\s\S]*?\]);/);
const elementsArrayCode = elementsMatch[1];

// Presets Dataset
const presets = [
  { id: "preset_water", name: "Water (H2O)", formula: "H2O", desc: "Universal polar solvent" },
  { id: "preset_glucose", name: "D-Glucose (C6H12O6)", formula: "C6H12O6", desc: "Primary biological metabolic carbohydrate" },
  { id: "preset_caffeine", name: "Caffeine (C8H10N4O2)", formula: "C8H10N4O2", desc: "Purine alkaloid central nervous system stimulant" },
  { id: "preset_ethanol", name: "Ethanol (C2H5OH)", formula: "C2H5OH", desc: "Primary alcohol and organic solvent" },
  { id: "preset_aspirin", name: "Aspirin (C9H8O4)", formula: "C9H8O4", desc: "Acetylsalicylic acid, nonsteroidal anti-inflammatory" },
  { id: "preset_sulfuric", name: "Sulfuric Acid (H2SO4)", formula: "H2SO4", desc: "Dense diprotic mineral acid" },
  { id: "preset_penicillin", name: "Penicillin G (C16H18N2O4S)", formula: "C16H18N2O4S", desc: "Beta-lactam antibacterial compound" },
  { id: "preset_cholesterol", name: "Cholesterol (C27H46O)", formula: "C27H46O", desc: "Essential structural lipid and sterol" },
  { id: "preset_copper_hydrate", name: "Copper(II) Sulfate Pentahydrate (CuSO4*5H2O)", formula: "CuSO4*5H2O", desc: "Bright blue crystalline inorganic hydrate" },
  { id: "preset_potassium_ferro", name: "Potassium Ferrocyanide (K4[Fe(CN)6])", formula: "K4[Fe(CN)6]", desc: "Octahedral coordination complex salt" },
  { id: "preset_ammonium_phosphate", name: "Diammonium Phosphate ((NH4)2HPO4)", formula: "(NH4)2HPO4", desc: "Water-soluble ammonium phosphate fertilizer salt" },
  { id: "preset_acetic", name: "Acetic Acid (CH3COOH)", formula: "CH3COOH", desc: "Weak organic carboxylic acid" },
  { id: "preset_sodium_bicarb", name: "Sodium Bicarbonate (NaHCO3)", formula: "NaHCO3", desc: "Baking soda and biological buffer" },
  { id: "preset_calcium_hydroxide", name: "Calcium Hydroxide (Ca(OH)2)", formula: "Ca(OH)2", desc: "Slaked lime, strong base sparingly soluble" },
  { id: "preset_iron_sulfate", name: "Iron(III) Sulfate (Fe2(SO4)3)", formula: "Fe2(SO4)3", desc: "Coagulant salt with multivalent polyatomic ions" }
];

console.log("Presets ready:", presets.length);

// Generate Educational Guide HTML
function generateEducationalGuide() {
  return `
<article class="mt-8 bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-10 shadow-sm border border-slate-200 dark:border-slate-700 prose prose-slate dark:prose-invert max-w-none">
  <div class="border-b border-slate-200 dark:border-slate-700 pb-4 mb-6">
    <span class="text-xs font-bold uppercase tracking-wider text-brand-600 dark:text-brand-400">Authoritative Laboratory Reference</span>
    <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Principles of Molecular Weight, Molar Mass, and Stoichiometric Mass Fractionation</h2>
    <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Formulated in accordance with IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW) standards and NIST Physical Reference Data.</p>
  </div>

  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    The determination of molecular weight and molar mass forms the quantitative cornerstone of modern chemical synthesis, analytical chromatography, clinical pharmacology, and materials engineering. From formulating active pharmaceutical ingredients (APIs) with milligram precision to calculating stoichiometric reagent ratios in multi-step organic synthesis, an exact comprehension of elemental composition is mandatory. While the terms <em>molecular weight</em>, <em>molecular mass</em>, <em>formula weight</em>, and <em>molar mass</em> are frequently conflated in casual discourse, they represent distinct physical quantities governed by rigorous metrological definitions promulgated by the International Union of Pure and Applied Chemistry (IUPAC) and the International Bureau of Weights and Measures (BIPM).
  </p>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    1. Historical Foundations and Theoretical Distinctions: Molecular Mass, Formula Weight, and Molar Mass
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    To apply chemical stoichiometry without error, one must distinguish between the microscopic masses of single molecules and the macroscopic molar masses of bulk quantities:
  </p>
  <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-4 list-disc">
    <li>
      <strong>Relative Molecular Mass ($M_r$ or Molecular Weight):</strong> A dimensionless physical quantity defined by IUPAC as the ratio of the average mass of one molecule of an element or compound to one-twelfth of the mass of an unbound carbon-12 atom in its nuclear and electronic ground state ($1/12 \\times m(^{12}\\text{C})$). Because it is a pure numerical ratio, relative molecular mass possesses no units.
    </li>
    <li>
      <strong>Molecular Mass ($m$):</strong> The absolute mass of a single discrete covalent molecule, customarily quantified in unified atomic mass units ($u$) or Daltons ($Da$). By international definition, $1 \\text{ Da} = 1 \\text{ u} = 1.66053906660(50) \\times 10^{-27} \\text{ kg}$.
    </li>
    <li>
      <strong>Molar Mass ($M$):</strong> A macroscopic intensive property defined as the mass of a substance divided by its amount of substance, expressed in SI units of kilograms per mole ($\\text{kg/mol}$) or practically in grams per mole ($\\text{g/mol}$). The relationship is expressed mathematically as:
      <div class="my-3 p-3 bg-slate-50 dark:bg-slate-900/60 rounded-xl font-mono text-center overflow-x-auto text-sm border border-slate-200/50 dark:border-slate-800">
        $$M = \\frac{m_{\\text{sample}}}{n}$$
      </div>
      where $m_{\\text{sample}}$ represents total sample mass in grams and $n$ represents the amount of substance in moles.
    </li>
    <li>
      <strong>Formula Weight ($FW$):</strong> The sum of the standard atomic weights of all constituent atoms in the empirical chemical formula unit. While covalent substances such as water ($\\text{H}_2\\text{O}$) and glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) exist as discrete, independent molecules, ionic salts such as sodium chloride ($\\text{NaCl}$) and calcium hydroxide ($\\text{Ca(OH)}_2$) form continuous infinite crystalline lattices without isolated molecular units. For ionic networks, speaking of a "molecule of NaCl" is physically erroneous; therefore, <em>formula weight</em> or <em>molar mass of the formula unit</em> is the metrologically correct terminology.
    </li>
  </ul>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    2. Standard Atomic Weights, Isotopic Variations, and CIAAW Intervals
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    The standard atomic weight ($A_r$) of a chemical element is not an unvarying constant of the universe. In 1899, the International Committee on Atomic Weights—now the <strong>IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW)</strong>—was established to critically evaluate and standardize atomic mass values for the international scientific community.
  </p>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    Except for monoisotopic elements (such as fluorine $^{19}\\text{F}$, sodium $^{23}\\text{Na}$, phosphorus $^{31}\\text{P}$, and gold $^{197}\\text{Au}$), terrestrial elements consist of mixtures of two or more stable isotopes. Natural physical, geochemical, hydrological, and biological processes cause <em>isotopic fractionation</em>—the selective enrichment or depletion of specific isotopes based on slight differences in mass. For example:
  </p>
  <ul class="space-y-1.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-3 list-disc">
    <li><strong>Carbon:</strong> Photosynthetic fractionation by terrestrial plants discriminates against $^{13}\\text{C}$, resulting in distinct $^{12}\\text{C}/^{13}\\text{C}$ ratios between C3 and C4 plants and geological carbonates.</li>
    <li><strong>Hydrogen &amp; Oxygen:</strong> Evaporation and precipitation cycles across varying latitudes and elevations systematically alter the ratio of deuterium ($^2\\text{H}$) to protium ($^1\\text{H}$) and oxygen-18 ($^{18}\\text{O}$) to oxygen-16 ($^{16}\\text{O}$) in global water reservoirs (Vienna Standard Mean Ocean Water, VSMOW).</li>
    <li><strong>Lead:</strong> Terrestrial lead exhibits substantial variations in atomic weight (ranging from $206.14$ to $207.94$) depending on the radiological decay history of uranium and thorium in the parent mineral deposits.</li>
  </ul>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    To reflect this natural physical reality, the CIAAW in 2009 abolished single-value atomic weights for twelve key elements, replacing them with <strong>atomic weight intervals</strong>:
  </p>
  <div class="overflow-x-auto my-4">
    <table class="w-full text-xs text-left border-collapse border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden shadow-sm">
      <thead class="bg-slate-100 dark:bg-slate-800/80 font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-700">
        <tr>
          <th class="p-2.5">Element</th>
          <th class="p-2.5">Symbol</th>
          <th class="p-2.5">IUPAC Standard Atomic Weight Interval</th>
          <th class="p-2.5">Conventional Atomic Weight (General Practice)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
        <tr><td class="p-2.5 font-sans font-semibold">Hydrogen</td><td class="p-2.5">H</td><td class="p-2.5">[1.007 84, 1.008 11]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">1.008</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Boron</td><td class="p-2.5">B</td><td class="p-2.5">[10.806, 10.821]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">10.81</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Carbon</td><td class="p-2.5">C</td><td class="p-2.5">[12.0096, 12.0116]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">12.011</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Nitrogen</td><td class="p-2.5">N</td><td class="p-2.5">[14.006 43, 14.007 28]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">14.007</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Oxygen</td><td class="p-2.5">O</td><td class="p-2.5">[15.999 03, 15.999 77]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">15.999</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Silicon</td><td class="p-2.5">Si</td><td class="p-2.5">[28.084, 28.086]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">28.085</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Sulfur</td><td class="p-2.5">S</td><td class="p-2.5">[32.059, 32.076]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">32.06</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Chlorine</td><td class="p-2.5">Cl</td><td class="p-2.5">[35.446, 35.457]</td><td class="p-2.5 font-bold text-brand-600 dark:text-brand-400">35.45</td></tr>
      </tbody>
    </table>
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    For laboratory bench work, commercial trade, and standard stoichiometric conversions where precise geographic isotopic sourcing is unrecorded, IUPAC designates <strong>conventional atomic weights</strong> (such as $\\text{H} = 1.008$, $\\text{C} = 12.011$, $\\text{O} = 15.999$), which this calculator implements in full compliance with the CIAAW and NIST Standard Reference Database 144.
  </p>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    3. Mass Spectrometry Principles: Monoisotopic Mass vs. Average Molar Mass
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    In modern analytical chemistry, high-resolution mass spectrometry (HRMS)—including Electrospray Ionization Time-of-Flight (ESI-TOF) and Fourier-Transform Ion Cyclotron Resonance (FT-ICR)—measures individual molecular ions in the gas phase rather than macroscopic statistical averages. Consequently, mass spectrometrists require a sharp conceptual separation between two metrics:
  </p>
  <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-4 list-disc">
    <li>
      <strong>Average Molar Mass:</strong> Calculated using the abundance-weighted average atomic weight across all natural isotopes. This metric corresponds to the macroscopic weight observed on an analytical balance when measuring bulk reagents.
    </li>
    <li>
      <strong>Monoisotopic Mass:</strong> Calculated by summing the exact rest masses of strictly the most naturally abundant stable isotope of each constituent element. For organic biomolecules, this corresponds to $^1\\text{H} = 1.007825032\\text{ Da}$, $^{12}\\text{C} = 12.000000000\\text{ Da}$, $^{14}\\text{N} = 14.003074004\\text{ Da}$, $^{16}\\text{O} = 15.994914619\\text{ Da}$, $^{31}\\text{P} = 30.973761998\\text{ Da}$, and $^{32}\\text{S} = 31.97207100\\text{ Da}$.
    </li>
    <li>
      <strong>Nominal Mass:</strong> The sum of the integer mass numbers of the most abundant constituent isotopes (e.g., $^1\\text{H} = 1$, $^{12}\\text{C} = 12$, $^{16}\\text{O} = 16$).
    </li>
  </ul>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    Consider caffeine ($\\text{C}_8\\text{H}_{10}\\text{N}_4\\text{O}_2$):
  </p>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 my-4 text-xs font-mono">
    <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200/50 dark:border-slate-800">
      <span class="text-slate-500 font-sans block">Nominal Mass</span>
      <span class="text-base font-bold text-slate-900 dark:text-white">194 Da</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200/50 dark:border-slate-800">
      <span class="text-slate-500 font-sans block">Monoisotopic Mass</span>
      <span class="text-base font-bold text-brand-600 dark:text-brand-400">194.080376 Da</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200/50 dark:border-slate-800">
      <span class="text-slate-500 font-sans block">Average Molar Mass</span>
      <span class="text-base font-bold text-indigo-600 dark:text-indigo-400">194.194 g/mol</span>
    </div>
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    Furthermore, mass spectrometry resolves distinct <em>isotopic envelope clusters</em>. For halogenated molecules:
  </p>
  <ul class="space-y-1.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-2 list-disc">
    <li><strong>Chlorine ($^{35}\\text{Cl}$ ~ $75.76\\%$, $^{37}\\text{Cl}$ ~ $24.24\\%$):</strong> Compounds containing a single chlorine atom display an $[M]$ and $[M+2]$ peak intensity ratio of approximately $3:1$.</li>
    <li><strong>Bromine ($^{79}\\text{Br}$ ~ $50.69\\%$, $^{81}\\text{Br}$ ~ $49.31\\%$):</strong> Compounds containing a single bromine atom produce an $[M]$ and $[M+2]$ doublet of nearly identical peak height ($1:1$).</li>
    <li><strong>Carbon-13 Satellite:</strong> For an organic molecule with $n_{\\text{C}}$ carbon atoms, the $[M+1]$ peak height relative to $[M]$ equals approximately $n_{\\text{C}} \\times 1.1\\%$, providing direct analytical confirmation of carbon atom count.</li>
  </ul>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    4. Empirical Formulas vs. Molecular Formulas and Combustion Stoichiometry
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    A foundational skill in chemical investigation is distinguishing between empirical and molecular formulas:
  </p>
  <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-3 list-disc">
    <li><strong>Empirical Formula:</strong> The simplest integer ratio of atoms of each element present in a compound.</li>
    <li><strong>Molecular Formula:</strong> The actual number of atoms of each element comprising a discrete molecule.</li>
  </ul>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    The molecular formula is always an integer multiple ($n \\ge 1$) of the empirical formula:
  </p>
  <div class="my-3 p-3 bg-slate-50 dark:bg-slate-900/60 rounded-xl font-mono text-center overflow-x-auto text-sm border border-slate-200/50 dark:border-slate-800">
    $$n = \\frac{M_{\\text{molecular}}}{M_{\\text{empirical}}}$$
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    In historical and modern analytical laboratories, quantitative elemental composition is determined via <strong>classical combustion analysis</strong> (CHNS elemental analysis). An unknown organic compound is combusted in pure oxygen at high temperature ($>1000^\\circ\\text{C}$):
  </p>
  <div class="my-3 p-3 bg-slate-50 dark:bg-slate-900/60 rounded-xl font-mono text-center overflow-x-auto text-sm border border-slate-200/50 dark:border-slate-800">
    $$\\text{C}_x\\text{H}_y\\text{O}_z + \\left(x + \\frac{y}{4} - \\frac{z}{2}\\right) \\text{O}_2 \\longrightarrow x \\text{CO}_2 + \\frac{y}{2} \\text{H}_2\\text{O}$$
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    By capturing and weighing the evolved $\\text{CO}_2$ and $\\text{H}_2\\text{O}$, analysts calculate the elemental mass percentages of carbon and hydrogen. However, combustion data yields only the empirical formula. To deduce the true molecular formula, an independent molar mass determination (via mass spectrometry, freezing point depression, or vapor density) is indispensable:
  </p>
  <div class="overflow-x-auto my-4">
    <table class="w-full text-xs text-left border-collapse border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden shadow-sm">
      <thead class="bg-slate-100 dark:bg-slate-800/80 font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-700">
        <tr>
          <th class="p-2.5">Compound</th>
          <th class="p-2.5">Empirical Formula</th>
          <th class="p-2.5">Empirical Mass</th>
          <th class="p-2.5">Molecular Formula</th>
          <th class="p-2.5">Molar Mass</th>
          <th class="p-2.5">Scaling Factor ($n$)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
        <tr><td class="p-2.5 font-sans font-semibold">Acetylene (Ethyne)</td><td class="p-2.5">CH</td><td class="p-2.5">13.019 g/mol</td><td class="p-2.5 font-bold">C2H2</td><td class="p-2.5">26.038 g/mol</td><td class="p-2.5">2</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Benzene</td><td class="p-2.5">CH</td><td class="p-2.5">13.019 g/mol</td><td class="p-2.5 font-bold">C6H6</td><td class="p-2.5">78.114 g/mol</td><td class="p-2.5">6</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Formaldehyde</td><td class="p-2.5">CH2O</td><td class="p-2.5">30.026 g/mol</td><td class="p-2.5 font-bold">CH2O</td><td class="p-2.5">30.026 g/mol</td><td class="p-2.5">1</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">Acetic Acid</td><td class="p-2.5">CH2O</td><td class="p-2.5">30.026 g/mol</td><td class="p-2.5 font-bold">C2H4O2</td><td class="p-2.5">60.052 g/mol</td><td class="p-2.5">2</td></tr>
        <tr><td class="p-2.5 font-sans font-semibold">D-Glucose</td><td class="p-2.5">CH2O</td><td class="p-2.5">30.026 g/mol</td><td class="p-2.5 font-bold">C6H12O6</td><td class="p-2.5">180.156 g/mol</td><td class="p-2.5">6</td></tr>
      </tbody>
    </table>
  </div>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    5. Hydrates, Coordination Complexes, and IUPAC Chemical Notation
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    Chemical formulations often include non-covalent stoichiometric adducts, waters of crystallization, and metal-ligand coordination spheres:
  </p>
  <ul class="space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-3 list-disc">
    <li>
      <strong>Hydrates and Adducts:</strong> Inorganic crystals frequently incorporate a stoichiometric ratio of water molecules into their unit cell lattice. By convention, a centered dot ($\\cdot$) or asterisk ($*$) separates the anhydrous formula from the hydrate waters, as in copper(II) sulfate pentahydrate:
      <div class="my-2 p-2 bg-slate-50 dark:bg-slate-900/60 rounded-lg font-mono text-center text-xs border border-slate-200/50 dark:border-slate-800">
        $$\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$$
      </div>
      The molar mass of the entire hydrated compound must include the five water molecules:
      $$M(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}) = M(\\text{CuSO}_4) + 5 \\times M(\\text{H}_2\\text{O}) = 159.609 + 5(18.015) = 249.685 \\text{ g/mol}$$
      Failure to account for hydrate water when preparing volumetric standard solutions is one of the most common causes of systematic concentration error in analytical chemistry.
    </li>
    <li>
      <strong>Coordination Complexes:</strong> In coordination chemistry, founded by Alfred Werner in 1893, square brackets $[\\dots]$ delineate the inner coordination sphere (central metal cation and directly coordinated ligands) from outer-sphere counterions:
      <div class="my-2 p-2 bg-slate-50 dark:bg-slate-900/60 rounded-lg font-mono text-center text-xs border border-slate-200/50 dark:border-slate-800">
        $$\\text{K}_4[\\text{Fe(CN)}_6] \\quad \\text{and} \\quad [\\text{Co(NH}_3)_5\\text{Cl}]\\text{Cl}_2$$
      </div>
      Our parsing engine processes square brackets and nested parentheses to compute total elemental stoichiometry accurately.
    </li>
    <li>
      <strong>The Hill System:</strong> Established in 1900 by Edwin A. Hill for chemical patent indexing, the Hill system standardizes chemical formula writing: if carbon is present, carbon is listed first, hydrogen second, and all remaining elements in alphabetical order (e.g., acetic acid is written as $\\text{C}_2\\text{H}_4\\text{O}_2$). If carbon is absent, all elements (including hydrogen) are ordered strictly alphabetically (e.g., sulfuric acid as $\\text{H}_2\\text{O}_4\\text{S}$).
    </li>
  </ul>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    6. Avogadro's Constant, the Mole, and the 2019 SI Redefinition
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    For nearly sixty years following the 1960 IUPAC/IUPAP unification, the mole was defined as the amount of substance containing as many elementary entities as there are atoms in exactly $0.012\\text{ kg}$ of pure unbound carbon-12. Under that historical standard, the molar mass constant was defined exactly as $M_u = 1 \\times 10^{-3} \\text{ kg/mol} = 1 \\text{ g/mol}$, while Avogadro's constant ($N_A$) was an experimentally determined quantity subject to measurement uncertainty.
  </p>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    In November 2018, the 26th General Conference on Weights and Measures (CGPM) voted unanimously to overhaul the International System of Units (SI), taking effect on <strong>May 20, 2019</strong>. Under the revised SI:
  </p>
  <ul class="space-y-1.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-3 list-disc">
    <li>The <strong>mole</strong> is defined by fixing the numerical value of <strong>Avogadro's constant</strong> to exactly:
      <div class="my-2 p-2 bg-slate-50 dark:bg-slate-900/60 rounded-lg font-mono text-center text-xs border border-slate-200/50 dark:border-slate-800">
        $$N_A = 6.022\\,140\\,76 \\times 10^{23} \\text{ mol}^{-1}$$
      </div>
    </li>
    <li>One mole contains exactly $6.022\\,140\\,76 \\times 10^{23}$ elementary entities (atoms, molecules, ions, or formula units).</li>
    <li>The molar mass constant $M_u$ is now an experimentally measured quantity: $M_u = 0.999\\,999\\,999\\,65(30) \\times 10^{-3} \\text{ kg/mol}$. Because its relative deviation from unity is less than $4 \\times 10^{-10}$, the practical numerical equivalence between relative molecular mass ($M_r$) and molar mass ($M$ in $\\text{g/mol}$) remains preserved for all chemical applications.</li>
  </ul>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    7. Concrete Numerical Case Studies with Step-by-Step Derivations
  </h3>

  <h4 class="text-base font-bold text-brand-600 dark:text-brand-400 mt-6 mb-2">
    Case Study 1: D-Glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) — Metabolic Biochemistry
  </h4>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    Calculate the molar mass, elemental mass composition, and the number of carbon atoms in a $25.000\\text{ g}$ laboratory sample of pure anhydrous D-glucose:
  </p>
  <div class="my-3 p-4 bg-slate-50 dark:bg-slate-900/50 rounded-xl font-mono text-xs space-y-1.5 border border-slate-200/60 dark:border-slate-700/60">
    <div>Carbon: 6 atoms &times; 12.011 g/mol = 72.066 g/mol</div>
    <div>Hydrogen: 12 atoms &times; 1.008 g/mol = 12.096 g/mol</div>
    <div>Oxygen: 6 atoms &times; 15.999 g/mol = 95.994 g/mol</div>
    <div class="font-bold border-t border-slate-300 dark:border-slate-700 pt-1 text-slate-900 dark:text-white">
      Total Molar Mass (M) = 72.066 + 12.096 + 95.994 = 180.156 g/mol
    </div>
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    <strong>Elemental Mass Shares:</strong>
    $$\\%\\text{C} = \\frac{72.066}{180.156} \\times 100\\% = 40.002\\%$$
    $$\\%\\text{H} = \\frac{12.096}{180.156} \\times 100\\% = 6.714\\%$$
    $$\\%\\text{O} = \\frac{95.994}{180.156} \\times 100\\% = 53.284\\%$$
  </p>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    <strong>Amount of Substance and Atom Count in 25.000 g:</strong>
    $$n = \\frac{25.000 \\text{ g}}{180.156 \\text{ g/mol}} = 0.138768 \\text{ mol}$$
    $$N_{\\text{molecules}} = 0.138768 \\text{ mol} \\times 6.02214076 \\times 10^{23} \\text{ mol}^{-1} = 8.3568 \\times 10^{22} \\text{ molecules}$$
    $$N_{\\text{Carbon atoms}} = 6 \\times 8.3568 \\times 10^{22} = 5.0141 \\times 10^{23} \\text{ carbon atoms}$$
  </p>

  <h4 class="text-base font-bold text-brand-600 dark:text-brand-400 mt-6 mb-2">
    Case Study 2: Copper(II) Sulfate Pentahydrate ($\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$) — Gravimetric Analysis
  </h4>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    An analytical chemist dehydrates a $10.000\\text{ g}$ sample of blue $\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$ in a laboratory muffle furnace to anhydrous $\\text{CuSO}_4$. Calculate theoretical mass loss:
  </p>
  <div class="my-3 p-4 bg-slate-50 dark:bg-slate-900/50 rounded-xl font-mono text-xs space-y-1.5 border border-slate-200/60 dark:border-slate-700/60">
    <div>M(CuSO4) = 63.546 (Cu) + 32.060 (S) + 4(15.999) (O) = 159.602 g/mol</div>
    <div>M(5 H2O) = 5 &times; [2(1.008) + 15.999] = 5 &times; 18.015 = 90.075 g/mol</div>
    <div class="font-bold border-t border-slate-300 dark:border-slate-700 pt-1 text-slate-900 dark:text-white">
      Total Hydrated Molar Mass = 159.602 + 90.075 = 249.677 g/mol
    </div>
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    <strong>Percentage of Water of Crystallization:</strong>
    $$\\%\\text{H}_2\\text{O} = \\frac{90.075}{249.677} \\times 100\\% = 36.077\\%$$
    <strong>Expected Anhydrous Residue:</strong>
    $$m_{\\text{residue}} = 10.000 \\text{ g} \\times (1 - 0.36077) = 6.3923 \\text{ g of anhydrous } \\text{CuSO}_4$$
  </p>

  <h4 class="text-base font-bold text-brand-600 dark:text-brand-400 mt-6 mb-2">
    Case Study 3: Acetylsalicylic Acid / Aspirin ($\\text{C}_9\\text{H}_8\\text{O}_4$) — Pharmaceutical Assay
  </h4>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    A standard commercial tablet contains $325.0\\text{ mg}$ of active acetylsalicylic acid:
  </p>
  <div class="my-3 p-4 bg-slate-50 dark:bg-slate-900/50 rounded-xl font-mono text-xs space-y-1.5 border border-slate-200/60 dark:border-slate-700/60">
    <div>M = 9(12.011) + 8(1.008) + 4(15.999) = 108.099 + 8.064 + 63.996 = 180.159 g/mol</div>
    <div>Carbon Share: 108.099 / 180.159 = 59.999%</div>
    <div>Hydrogen Share: 8.064 / 180.159 = 4.476%</div>
    <div>Oxygen Share: 63.996 / 180.159 = 35.525%</div>
  </div>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-2">
    Total carbon in the tablet equals $0.3250 \\text{ g} \\times 0.59999 = 0.1950 \\text{ g}$ ($195.0\\text{ mg}$). Moles of active substance equals $0.3250 / 180.159 = 1.8039 \\times 10^{-3} \\text{ mol}$ ($1.804\\text{ mmol}$).
  </p>

  <hr class="my-8 border-slate-200 dark:border-slate-700">

  <h3 class="text-xl font-bold text-slate-900 dark:text-white mt-8 mb-3 pb-2 border-b border-slate-200 dark:border-slate-700">
    8. Quality Assurance, Metrological Traceability, and Laboratory Practice
  </h3>
  <p class="text-sm leading-relaxed text-slate-700 dark:text-slate-300 my-3">
    In certified analytical laboratories operating under <strong>ISO/IEC 17025</strong> accreditation, uncertainty analysis is governed by the BIPM <em>Guide to the Expression of Uncertainty in Measurement (GUM)</em>. When weighing substances on four- or five-place analytical balances, analysts must evaluate:
  </p>
  <ul class="space-y-1.5 text-xs sm:text-sm text-slate-700 dark:text-slate-300 pl-4 my-3 list-disc">
    <li><strong>Air Buoyancy Correction:</strong> For high-precision primary standardization, apparent mass measured in air must be corrected for the density of air ($\\rho_{\\text{air}} \\approx 0.0012 \\text{ g/cm}^3$) and sample density ($\\rho$).</li>
    <li><strong>Uncertainty Propagation in Molar Mass:</strong> Total uncertainty $u(M)$ combines the combined standard uncertainties of constituent atomic weights:
      $$u(M) = \\sqrt{\\sum_{i=1}^k [n_i \\cdot u(A_r(i))]^2}$$
    </li>
    <li><strong>Traceability to SI:</strong> Standards must maintain documented calibration chains traceable to NIST Standard Reference Materials (SRMs) or equivalent national metrology institutes.</li>
  </ul>
</article>
`;
}

// Generate FAQ HTML
function generateFaqHtml() {
  const faqs = [
    {
      q: "What is the difference between molecular weight, molar mass, and formula weight?",
      a: "Relative molecular mass (molecular weight) is a dimensionless ratio comparing the mass of a molecule to 1/12 the mass of carbon-12. Molar mass is an intensive physical property with dimensions of mass per amount of substance, expressed in grams per mole (g/mol). Formula weight is the sum of atomic weights of the atoms in an empirical formula, used primarily for ionic substances like NaCl that do not form discrete molecules."
    },
    {
      q: "Why do some periodic tables show slightly different atomic weights for carbon, hydrogen, and lead?",
      a: "Because natural isotopic abundances vary across geographic and geological reservoirs due to isotopic fractionation, the IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW) officially defines standard atomic weights for these elements as intervals (e.g., [12.0096, 12.0116] for carbon). Different tables may choose different roundings or cite conventional single-value atomic weights (such as 12.011 for carbon) intended for general stoichiometric practice."
    },
    {
      q: "What is monoisotopic mass and why does mass spectrometry use it instead of average molar mass?",
      a: "Monoisotopic mass is calculated using only the exact rest mass of the single most abundant stable isotope of each element (such as Carbon-12 = 12.000000 Da, Hydrogen-1 = 1.007825 Da, Oxygen-16 = 15.994915 Da). High-resolution mass spectrometers detect individual molecular ions in the gas phase rather than bulk averages, producing discrete isotopic peaks separated by exact mass-to-charge ratios."
    },
    {
      q: "How do I calculate the percentage of water in a hydrated crystal like copper(II) sulfate pentahydrate?",
      a: "First determine the molar mass of the entire hydrated compound (CuSO4*5H2O = 249.685 g/mol). Next, calculate the mass contributed by the water molecules alone (5 x 18.015 = 90.075 g/mol). Divide the water mass by the total hydrated mass and multiply by 100%: (90.075 / 249.685) x 100% = 36.08% water by mass."
    },
    {
      q: "What is the difference between an empirical formula and a molecular formula?",
      a: "An empirical formula represents the simplest whole-number ratio of elements in a compound (e.g., CH2O). A molecular formula indicates the actual number of atoms of each element in a discrete molecule (e.g., C6H12O6 for glucose). The molecular formula is always an integer multiple n = M(molecular) / M(empirical) of the empirical formula."
    },
    {
      q: "How was the mole and Avogadro's constant redefined in 2019?",
      a: "On May 20, 2019, the General Conference on Weights and Measures (CGPM) decoupled the mole from the mass of carbon-12. The mole is now defined by fixing Avogadro's constant to exactly 6.02214076 x 10^23 reciprocal moles (mol^-1), establishing it as a foundational fundamental constant of physics."
    },
    {
      q: "How do parentheses and brackets work in complex chemical formulas like (NH4)2HPO4 or K4[Fe(CN)6]?",
      a: "Parentheses and brackets group polyatomic ions and coordination complexes. Any numerical subscript immediately following a closing bracket multiplies every atom inside that group. In (NH4)2HPO4, the subscript 2 multiplies NH4 to give 2 Nitrogen and 8 Hydrogen atoms, plus 1 Hydrogen from HPO4, totaling 9 Hydrogen atoms."
    },
    {
      q: "Why is case sensitivity essential when entering chemical formulas?",
      a: "In chemical nomenclature, letter case distinguishes elements: 'Co' is Cobalt (atomic number 27, atomic weight 58.933), whereas 'CO' represents Carbon Monoxide composed of Carbon (12.011) and Oxygen (15.999), yielding 28.010 g/mol. Similarly, 'No' is Nobelium, while 'NO' is Nitric Oxide."
    }
  ];

  let html = `
  <section class="mt-12 bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-10 shadow-sm border border-slate-200 dark:border-slate-700 no-print" id="faq-section">
    <div class="mb-8">
      <span class="text-xs font-bold text-brand-600 dark:text-brand-400 uppercase tracking-wider">Expert Clarifications</span>
      <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Frequently Asked Questions</h2>
      <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Key theoretical and laboratory questions regarding molecular mass, isotopic abundance, and chemical stoichiometry.</p>
    </div>
    <div class="space-y-3">
  `;

  faqs.forEach((faq, idx) => {
    const num = idx + 1;
    html += `
      <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
        <button type="button" onclick="toggleFaq(${num})" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
          <span>${faq.q}</span>
          <svg id="faqIcon_${num}" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
        <div id="faqAns_${num}" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
          ${faq.a}
        </div>
      </div>
    `;
  });

  html += `
    </div>
  </section>
  `;

  return { html, faqs };
}

const { html: faqHtml, faqs: faqItems } = generateFaqHtml();

// Build Complete HTML
const fullHtml = `<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Molecular Weight Calculator | Molar Mass &amp; Stoichiometry Solver</title>
    <meta name="description" content="Free scientific molecular weight and molar mass calculator. Parse complex chemical formulas, parenthetical groups, and hydrates with IUPAC / CIAAW standard atomic weights, elemental percentage mass composition, stoichiometry converters, and distribution charts.">
    <link rel="canonical" href="https://calcworld.net/chemistry/molecular-weight-calculator">

    <!-- Anti-FOUC & Dark Mode Script -->
    <script>
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    </script>

    <!-- Google Fonts & Tailwind CSS CDN -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    },
                    colors: {
                        brand: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            200: '#c7d2fe',
                            300: '#a5b4fc',
                            400: '#818cf8',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                            800: '#3730a3',
                            900: '#312e81',
                        }
                    }
                }
            }
        }
    </script>

    <!-- MathJax 3 CDN for Chemical & Mathematical Formula Rendering -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        .tab-panel { display: none; }
        .tab-panel.active { display: block; animation: tabFade 0.25s ease-out; }
        @keyframes tabFade {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .ad-slot {
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(148, 163, 184, 0.08);
            border: 1px dashed rgba(148, 163, 184, 0.3);
            border-radius: 0.75rem;
            color: #94a3b8;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin: 1.5rem 0;
            overflow: hidden;
        }
        #ad-slot-1 { min-height: 90px; width: 100%; }
        #ad-slot-2 { min-height: 100px; width: 100%; }
        #ad-slot-3 { min-height: 250px; width: 100%; }
        #ad-slot-4 { min-height: 120px; width: 100%; }
        #ad-slot-5 { min-height: 140px; width: 100%; }

        @media print {
            header, footer, .no-print, .ad-slot, #floatingBar, #adblockRecovery, #toast, .lead-box, #tabButtons, #calculatorInputs, #presetSelect {
                display: none !important;
            }
            #tab-print {
                display: block !important;
            }
            body, .dark {
                background: white !important;
                color: black !important;
            }
        }
        .toast-notify {
            position: fixed;
            bottom: 5rem;
            right: 1.5rem;
            z-index: 50;
            background: #1e293b;
            color: white;
            padding: 0.75rem 1.25rem;
            border-radius: 0.75rem;
            font-size: 0.8125rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s ease;
            opacity: 0;
            transform: translateY(10px);
            pointer-events: none;
        }
        .toast-notify.show {
            opacity: 1;
            transform: translateY(0);
            pointer-events: auto;
        }
    </style>

    <!-- JSON-LD SEO Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://calcworld.net"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Other Calculators",
              "item": "https://calcworld.net/other"
            },
            {
              "@type": "ListItem",
              "position": 3,
              "name": "Molecular Weight Calculator"
            }
          ]
        },
        {
          "@type": "WebApplication",
          "name": "Molecular Weight Calculator",
          "url": "https://calcworld.net/chemistry/molecular-weight-calculator",
          "applicationCategory": "EducationalApplication",
          "operatingSystem": "Any",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "description": "Scientific chemical formula molecular weight and molar mass calculator. Parse complex chemical formulas, parenthetical groups, and hydrates with IUPAC / CIAAW standard atomic weights, elemental percentage mass composition, stoichiometry converters, and distribution charts."
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            ${faqItems.map(item => JSON.stringify({
              "@type": "Question",
              "name": item.q,
              "acceptedAnswer": {
                "@type": "Answer",
                "text": item.a
              }
            })).join(',\n            ')}
          ]
        }
      ]
    }
    </script>
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 font-sans transition-colors duration-200 antialiased selection:bg-brand-500 selection:text-white min-h-screen flex flex-col">

    <!-- AdBlock Detection Recovery Banner -->
    <div id="adblockRecovery" class="hidden no-print bg-amber-500/10 border-b border-amber-500/20 text-amber-800 dark:text-amber-300 px-4 py-2 text-xs text-center flex justify-between items-center max-w-7xl mx-auto rounded-b-lg w-full">
        <div class="flex items-center gap-2 mx-auto">
            <svg class="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
            </svg>
            <span><strong>Reader-Supported Chemistry Tool:</strong> CalcWorld provides peer-reviewed chemical calculations free of charge with zero registration. Please consider safelisting our domain to support continuous scientific tool development.</span>
        </div>
        <button onclick="document.getElementById('adblockRecovery').classList.add('hidden')" class="text-amber-900 dark:text-amber-200 hover:opacity-80 text-sm font-bold ml-4" aria-label="Dismiss banner">&times;</button>
    </div>

    <!-- Header Navigation -->
    <header class="border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 backdrop-blur sticky top-0 z-30 no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="https://calcworld.net" class="flex items-center gap-2 group">
                    <span class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-indigo-500 flex items-center justify-center text-white font-bold text-lg shadow-md group-hover:scale-105 transition-transform">MW</span>
                    <span class="font-bold text-xl tracking-tight text-slate-900 dark:text-white">Calc<span class="text-brand-600 dark:text-brand-400">World</span></span>
                </a>
                <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-brand-50 text-brand-700 dark:bg-brand-950/60 dark:text-brand-300 border border-brand-200/50 dark:border-brand-800/50">CHEMISTRY SUITE</span>
            </div>

            <div class="flex items-center gap-3">
                <div class="hidden md:flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
                    <a href="molarity-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Molarity</a>
                    <span>&bull;</span>
                    <a href="stoichiometry-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Stoichiometry</a>
                    <span>&bull;</span>
                    <a href="empirical-formula-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Empirical Formula</a>
                </div>

                <!-- Dark Mode Toggle Button -->
                <button onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" aria-label="Toggle theme">
                    <svg id="themeMoon" class="w-5 h-5 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                    <svg id="themeSun" class="w-5 h-5 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full">
        
        <!-- Breadcrumb Navigation -->
        <nav class="text-xs text-slate-500 dark:text-slate-400 mb-4 no-print" aria-label="Breadcrumb">
            <ol class="list-none p-0 inline-flex items-center gap-1.5">
                <li class="inline-flex items-center">
                    <a href="https://calcworld.net" class="hover:text-brand-600 dark:hover:text-brand-400">Home</a>
                </li>
                <li>
                    <svg class="w-3 h-3 text-slate-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                </li>
                <li>
                    <a href="https://calcworld.net/other" class="hover:text-brand-600 dark:hover:text-brand-400">Other Calculators</a>
                </li>
                <li>
                    <svg class="w-3 h-3 text-slate-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                </li>
                <li class="text-slate-800 dark:text-slate-200 font-semibold" aria-current="page">Molecular Weight Calculator</li>
            </ol>
        </nav>

        <!-- Page Hero Title -->
        <div class="mb-6">
            <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white">Molecular Weight Calculator</h1>
            <p class="text-base text-slate-600 dark:text-slate-300 mt-1 max-w-3xl">Compute molar mass ($g/mol$), elemental mass percentage composition, empirical formulas, and stoichiometry for complex chemical formulas, polyatomic groups, and hydrated crystals.</p>
        </div>

        <!-- AdSense Slot 1: Top Leaderboard -->
        <div class="ad-slot no-print" id="ad-slot-1">
            <span>Sponsored Advertisement &bull; Leaderboard Slot 1</span>
        </div>

        <!-- Two-Column Primary Layout (Inputs vs Results & Tabs) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            
            <!-- Left Column: Inputs & Controls (Span 4) -->
            <div id="calculatorInputs" class="lg:col-span-5 xl:col-span-4 space-y-6 no-print">
                <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                    
                    <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-4 flex items-center justify-between">
                        <span>Formula Parser</span>
                        <span class="text-xs font-normal px-2 py-0.5 rounded bg-brand-50 text-brand-700 dark:bg-brand-900/40 dark:text-brand-300 border border-brand-200/50">IUPAC / CIAAW</span>
                    </h2>

                    <!-- Formula Input Field -->
                    <div class="mb-4">
                        <div class="flex items-center justify-between mb-1">
                            <label for="formulaInput" class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Chemical Formula</label>
                            <span id="syntaxValidationBadge" class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400">Valid Formula</span>
                        </div>
                        <div class="relative">
                            <input type="text" id="formulaInput" value="CuSO4*5H2O" oninput="handleFormulaInput(this.value)" placeholder="e.g. C6H12O6, Ca(OH)2, CuSO4*5H2O" class="w-full px-3.5 py-2.5 text-base font-mono bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <div class="absolute right-2 top-2 flex items-center gap-1">
                                <button type="button" onclick="clearFormula()" title="Clear formula" class="p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-xs rounded">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                </button>
                            </div>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-1 flex items-center justify-between">
                            <span>Case-sensitive: e.g. Co (Cobalt) vs CO (Carbon Monoxide)</span>
                            <button type="button" onclick="autoCapitalizeFormula()" class="text-brand-600 dark:text-brand-400 hover:underline">Format Case</button>
                        </p>
                    </div>

                    <!-- Presets Selector -->
                    <div class="mb-4">
                        <label for="presetSelect" class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">Common Compound Presets</label>
                        <select id="presetSelect" onchange="loadPreset(this.value)" class="w-full px-3 py-2 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <option value="">-- Choose Common Chemical Preset --</option>
                            ${presets.map(p => `<option value="${p.formula}" ${p.formula === 'CuSO4*5H2O' ? 'selected' : ''}>${p.name}</option>`).join('\n                            ')}
                        </select>
                    </div>

                    <!-- Fast Preset Pills -->
                    <div class="mb-4">
                        <div class="flex flex-wrap gap-1.5">
                            <button type="button" onclick="setFormula('H2O')" class="px-2 py-1 text-xs font-semibold rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-brand-50 hover:text-brand-600 transition">Water</button>
                            <button type="button" onclick="setFormula('C6H12O6')" class="px-2 py-1 text-xs font-semibold rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-brand-50 hover:text-brand-600 transition">Glucose</button>
                            <button type="button" onclick="setFormula('C8H10N4O2')" class="px-2 py-1 text-xs font-semibold rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-brand-50 hover:text-brand-600 transition">Caffeine</button>
                            <button type="button" onclick="setFormula('C9H8O4')" class="px-2 py-1 text-xs font-semibold rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-brand-50 hover:text-brand-600 transition">Aspirin</button>
                            <button type="button" onclick="setFormula('CuSO4*5H2O')" class="px-2 py-1 text-xs font-semibold rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-brand-50 hover:text-brand-600 transition">Hydrate</button>
                        </div>
                    </div>

                    <!-- Virtual Chemical Keypad -->
                    <div class="mb-5 p-3 rounded-xl bg-slate-50 dark:bg-slate-900/50 border border-slate-200/60 dark:border-slate-700/60">
                        <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-2">Virtual Chemical Keypad</span>
                        <div class="grid grid-cols-6 gap-1.5 font-mono text-xs">
                            <button type="button" onclick="appendToken('C')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">C</button>
                            <button type="button" onclick="appendToken('H')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">H</button>
                            <button type="button" onclick="appendToken('O')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">O</button>
                            <button type="button" onclick="appendToken('N')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">N</button>
                            <button type="button" onclick="appendToken('P')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">P</button>
                            <button type="button" onclick="appendToken('S')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">S</button>
                            
                            <button type="button" onclick="appendToken('Cl')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">Cl</button>
                            <button type="button" onclick="appendToken('Na')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">Na</button>
                            <button type="button" onclick="appendToken('K')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">K</button>
                            <button type="button" onclick="appendToken('Ca')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">Ca</button>
                            <button type="button" onclick="appendToken('Fe')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">Fe</button>
                            <button type="button" onclick="appendToken('Cu')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">Cu</button>
                            
                            <button type="button" onclick="appendToken('(')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">(</button>
                            <button type="button" onclick="appendToken(')')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">)</button>
                            <button type="button" onclick="appendToken('[')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">[</button>
                            <button type="button" onclick="appendToken(']')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">]</button>
                            <button type="button" onclick="appendToken('*')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition text-brand-600">&bull;</button>
                            <button type="button" onclick="appendToken('2')" class="p-1.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold hover:border-brand-500 transition">2</button>
                        </div>
                    </div>

                    <!-- Action Controls -->
                    <div class="pt-3 border-t border-slate-200 dark:border-slate-700 flex flex-col gap-2">
                        <button type="button" onclick="triggerRecalculate()" class="w-full py-2.5 px-4 rounded-xl bg-brand-600 hover:bg-brand-700 active:scale-[0.99] text-white font-bold text-sm shadow-md transition flex items-center justify-center gap-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
                            <span>Calculate Molar Mass</span>
                        </button>
                        
                        <div class="grid grid-cols-2 gap-2">
                            <button type="button" onclick="resetDefaultFormula()" class="py-2 px-3 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition text-center">Reset</button>
                            <button type="button" onclick="copyShareUrl()" class="py-2 px-3 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition text-center flex items-center justify-center gap-1">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
                                <span>Share URL</span>
                            </button>
                        </div>
                    </div>

                </div>

                <!-- AdSense Slot 3: Sidebar Rectangle -->
                <div class="ad-slot" id="ad-slot-3">
                    <span>Sponsored Advertisement &bull; Sidebar Slot 3</span>
                </div>

                <!-- Lead Gen Box (Sidebar Placement) -->
                <div class="lead-box bg-gradient-to-br from-indigo-900 to-brand-900 text-white p-5 rounded-2xl shadow-md border border-indigo-700/50">
                    <div class="flex items-center gap-2 mb-2 text-brand-300 text-xs font-bold uppercase tracking-wider">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"/></svg>
                        <span>Official Chemistry Reference</span>
                    </div>
                    <h3 class="font-bold text-base mb-1">Periodic Table &amp; Molar Mass Guide</h3>
                    <p class="text-xs text-indigo-200 mb-3">Download our peer-reviewed stoichiometry formula chart with full 118-element IUPAC standard atomic weights (PDF).</p>
                    <form onsubmit="handleLeadSubmit(event)" class="space-y-2">
                        <input type="email" id="leadEmailInput" required placeholder="chemist@university.edu" class="w-full px-3 py-2 text-xs rounded-lg bg-white/10 border border-white/20 text-white placeholder-indigo-300 focus:outline-none focus:ring-2 focus:ring-brand-400">
                        <button type="submit" id="leadSubmitBtn" class="w-full py-2 bg-brand-500 hover:bg-brand-400 text-white font-bold text-xs rounded-lg transition shadow">Send Free PDF</button>
                    </form>
                    <div id="leadSuccessMsg" class="hidden text-xs text-emerald-300 mt-2 text-center font-medium">&check; Check your inbox! Your formula guide is on the way.</div>
                </div>

            </div>

            <!-- Right Column: Results & Tabs (Span 8) -->
            <div class="lg:col-span-7 xl:col-span-8 space-y-6">
                
                <!-- Hero Result Card -->
                <div id="resultsCard" class="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-200 dark:border-slate-700 relative overflow-hidden">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400" id="resultHeaderBadge">Hydrated Inorganic Crystal</span>
                        <div class="flex items-center gap-2">
                            <span id="formulaFormattedBadge" class="inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-mono font-bold bg-brand-50 text-brand-700 dark:bg-brand-950/60 dark:text-brand-300 border border-brand-200/50">CuSO4&bull;5H2O</span>
                        </div>
                    </div>

                    <!-- Main Molar Mass Display -->
                    <div class="bg-slate-50 dark:bg-slate-900/60 rounded-xl p-5 mb-5 border border-slate-200/60 dark:border-slate-700/60 text-center">
                        <span class="text-xs font-medium text-slate-500 dark:text-slate-400 block mb-1">Total Molar Mass ($M$)</span>
                        <div class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-brand-600 dark:text-brand-400 font-mono" id="molarMassDisplay">
                            249.685 <span class="text-xl sm:text-2xl font-normal text-slate-500 dark:text-slate-400">g/mol</span>
                        </div>
                        <div class="text-xs text-slate-600 dark:text-slate-300 mt-2 max-w-xl mx-auto" id="compoundNarrativeDisplay">
                            Calculated using IUPAC / CIAAW standard atomic weights: 1 Cu, 1 S, 9 O, 10 H atoms per formula unit.
                        </div>
                        
                        <!-- Unit Switcher Pills -->
                        <div class="flex items-center justify-center gap-1.5 mt-3 text-[11px] font-mono">
                            <span class="px-2 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300" id="unitDaDisplay">249.685 Da (u)</span>
                            <span class="px-2 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300" id="unitKgDisplay">0.24969 kg/mol</span>
                            <span class="px-2 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300" id="unitOzDisplay">8.8074 oz/mol</span>
                        </div>
                    </div>

                    <!-- 4 Metric Cards Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total Molar Mass</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricMolarMass">249.685</span>
                            <span class="text-[10px] text-slate-400">g/mol</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Empirical Formula</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricEmpirical">CuH10O9S</span>
                            <span class="text-[10px] text-slate-400" id="metricEmpiricalRatio">Ratio n = 1</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total Atom Count</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricAtomCount">21 atoms</span>
                            <span class="text-[10px] text-slate-400" id="metricDistinctElements">4 elements</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Monoisotopic Mass</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricMonoisotopic">248.937</span>
                            <span class="text-[10px] text-slate-400">Da (HRMS)</span>
                        </div>
                    </div>

                    <!-- Hill System & Summary Bar -->
                    <div class="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-slate-200 dark:border-slate-700 text-xs">
                        <div class="flex items-center gap-3 text-slate-500 dark:text-slate-400 font-mono">
                            <span id="hillSystemDisplay">Hill System: CuH10O9S</span>
                            <span>&bull;</span>
                            <span id="anhydrousComparisonDisplay">Anhydrous Mass: 159.609 g/mol (63.9%)</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="copyFormattedSummary()" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition flex items-center gap-1.5 font-medium text-slate-700 dark:text-slate-300">
                                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                                <span>Copy Summary</span>
                            </button>
                            <button onclick="switchTab('print'); window.print();" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition flex items-center gap-1.5 font-medium text-slate-700 dark:text-slate-300">
                                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H7v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                                <span>Print Report</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Tab Navigation Bar -->
                <div class="border-b border-slate-200 dark:border-slate-700 no-print" id="tabButtons">
                    <nav class="flex space-x-2 sm:space-x-4 overflow-x-auto" aria-label="Tabs">
                        <button onclick="switchTab('solver')" id="tabBtn_solver" class="tab-btn active border-b-2 border-brand-600 pb-3 px-1 text-xs sm:text-sm font-bold text-brand-600 dark:text-brand-400 whitespace-nowrap">
                            Molecular Weight Parser
                        </button>
                        <button onclick="switchTab('table')" id="tabBtn_table" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Elemental Percentage Breakdown
                        </button>
                        <button onclick="switchTab('periodic')" id="tabBtn_periodic" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Periodic Table Quick Lookup
                        </button>
                        <button onclick="switchTab('print')" id="tabBtn_print" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Print Report
                        </button>
                    </nav>
                </div>

                <!-- TAB 1: Molecular Weight Parser & Analysis -->
                <div id="tab-solver" class="tab-panel active space-y-6">
                    
                    <!-- Chart.js Visualization Container -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                            <div>
                                <h3 class="font-bold text-base text-slate-900 dark:text-white">Elemental Mass Distribution</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Interactive percentage mass share breakdown per element.</p>
                            </div>
                            <div class="flex items-center gap-1 bg-slate-100 dark:bg-slate-900 p-1 rounded-lg text-xs">
                                <button type="button" id="chartMode_mass" onclick="setChartMode('mass')" class="px-2.5 py-1 font-semibold rounded-md bg-white dark:bg-slate-800 text-brand-600 dark:text-brand-400 shadow-sm transition">Mass %</button>
                                <button type="button" id="chartMode_atom" onclick="setChartMode('atom')" class="px-2.5 py-1 font-semibold rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition">Atom Count %</button>
                            </div>
                        </div>

                        <div class="relative h-64 sm:h-72 w-full flex items-center justify-center">
                            <canvas id="elementChart"></canvas>
                        </div>
                    </div>

                    <!-- Step-by-Step Mathematical Derivation Box -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-base text-slate-900 dark:text-white mb-3 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-brand-100 dark:bg-brand-900/60 text-brand-600 dark:text-brand-400 flex items-center justify-center text-xs font-bold">&Sigma;</span>
                            <span>Step-by-Step Stoichiometric Derivation</span>
                        </h3>
                        
                        <div id="mathJaxDerivationBlock" class="overflow-x-auto text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-3 font-mono bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
                            <!-- Populated dynamically by JavaScript -->
                            <div class="text-center py-2 text-slate-400">Loading stoichiometric derivation...</div>
                        </div>
                    </div>

                    <!-- Interactive Stoichiometry & Mass <-> Moles Converter -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-base text-slate-900 dark:text-white mb-2">Bidirectional Stoichiometry &amp; Particle Converter</h3>
                        <p class="text-xs text-slate-500 dark:text-slate-400 mb-4">Enter any value below to synchronously convert between mass, moles, molecules, and total atoms using Avogadro's constant ($N_A = 6.02214076 \\times 10^{23} \\text{ mol}^{-1}$).</p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                            <div>
                                <label for="stoich_mass" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Mass in Grams ($g$)</label>
                                <input type="number" id="stoich_mass" step="any" value="249.685" oninput="syncFromMass(this.value)" class="w-full px-3 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-900 dark:text-white focus:ring-2 focus:ring-brand-500">
                            </div>
                            <div>
                                <label for="stoich_moles" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Amount of Substance ($mol$)</label>
                                <input type="number" id="stoich_moles" step="any" value="1.0" oninput="syncFromMoles(this.value)" class="w-full px-3 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-900 dark:text-white focus:ring-2 focus:ring-brand-500">
                            </div>
                            <div>
                                <label for="stoich_molecules" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Number of Molecules / Formula Units</label>
                                <input type="text" id="stoich_molecules" readonly class="w-full px-3 py-2 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-700 dark:text-slate-300">
                            </div>
                            <div>
                                <label for="stoich_atoms" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Total Constituent Atoms</label>
                                <input type="text" id="stoich_atoms" readonly class="w-full px-3 py-2 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-700 dark:text-slate-300">
                            </div>
                        </div>

                        <!-- Laboratory Solution Prep Tool -->
                        <div class="mt-5 pt-4 border-t border-slate-200 dark:border-slate-700">
                            <span class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 block mb-2">Laboratory Solution Preparation Calculator</span>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                                <div>
                                    <label for="sol_volume" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Target Volume ($mL$)</label>
                                    <input type="number" id="sol_volume" value="500" step="any" oninput="calcSolutionPrep()" class="w-full px-3 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-900 dark:text-white focus:ring-1 focus:ring-brand-500">
                                </div>
                                <div>
                                    <label for="sol_molarity" class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Molarity ($M = mol/L$)</label>
                                    <input type="number" id="sol_molarity" value="0.100" step="any" oninput="calcSolutionPrep()" class="w-full px-3 py-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-900 dark:text-white focus:ring-1 focus:ring-brand-500">
                                </div>
                                <div>
                                    <label class="block font-medium text-slate-700 dark:text-slate-300 mb-1">Solute Required ($g$)</label>
                                    <div class="px-3 py-2 bg-brand-50/70 dark:bg-brand-950/40 border border-brand-200 dark:border-brand-800 rounded-lg font-mono font-bold text-brand-700 dark:text-brand-300" id="soluteRequiredDisplay">
                                        12.484 g
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>

                </div>

                <!-- TAB 2: Elemental Percentage Breakdown Table -->
                <div id="tab-table" class="tab-panel space-y-6">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                            <div>
                                <h3 class="font-bold text-base text-slate-900 dark:text-white">Elemental Stoichiometric Breakdown Table</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Detailed composition, mass percentage, and component mass for arbitrary sample sizes.</p>
                            </div>
                            <div class="flex items-center gap-2">
                                <label for="customSampleMassInput" class="text-xs text-slate-500 dark:text-slate-400">Sample Mass ($g$):</label>
                                <input type="number" id="customSampleMassInput" value="100" step="any" oninput="updateCustomSampleMass(this.value)" class="w-24 px-2.5 py-1 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg font-mono text-slate-900 dark:text-white focus:ring-1 focus:ring-brand-500">
                            </div>
                        </div>

                        <!-- Table -->
                        <div class="overflow-x-auto">
                            <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
                                <thead class="bg-slate-50 dark:bg-slate-900/80 uppercase font-semibold text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                                    <tr>
                                        <th class="px-3 py-2.5">Element</th>
                                        <th class="px-3 py-2.5">Atomic Weight ($A_r$)</th>
                                        <th class="px-3 py-2.5">Atom Count</th>
                                        <th class="px-3 py-2.5">Mass Contribution</th>
                                        <th class="px-3 py-2.5">Mass Share (%)</th>
                                        <th class="px-3 py-2.5">Mass in Sample ($g$)</th>
                                    </tr>
                                </thead>
                                <tbody id="elementTableBody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                                    <!-- Populated dynamically -->
                                </tbody>
                                <tfoot id="elementTableFoot" class="bg-slate-50 dark:bg-slate-900/80 font-mono font-bold text-slate-900 dark:text-white border-t border-slate-200 dark:border-slate-700">
                                    <!-- Totals populated dynamically -->
                                </tfoot>
                            </table>
                        </div>

                        <div class="flex items-center justify-between pt-4 mt-2 border-t border-slate-200 dark:border-slate-700">
                            <span class="text-xs text-slate-400">Standard atomic weights compliant with IUPAC CIAAW biennial evaluations.</span>
                            <button type="button" onclick="downloadCsvReport()" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs font-medium text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition flex items-center gap-1.5">
                                <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                <span>Export CSV Table</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- TAB 3: Periodic Table Elements Quick Lookup -->
                <div id="tab-periodic" class="tab-panel space-y-6">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                            <div>
                                <h3 class="font-bold text-base text-slate-900 dark:text-white">IUPAC Periodic Table of Elements (1-118)</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Lookup standard atomic weights, atomic numbers, and chemical families. Click any element to insert it into your active formula.</p>
                            </div>
                            <div class="flex items-center gap-2">
                                <input type="text" id="ptSearchInput" placeholder="Search element name, symbol, Z..." oninput="filterPeriodicTable(this.value)" class="w-56 px-3 py-1.5 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-1 focus:ring-brand-500">
                            </div>
                        </div>

                        <!-- Category Filter Buttons -->
                        <div class="flex flex-wrap gap-1.5 mb-4 text-[11px]" id="ptCategoryFilters">
                            <button type="button" onclick="filterByCategory('all')" class="pt-cat-btn active px-2.5 py-1 rounded-md bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-300 font-semibold" data-cat="all">All (118)</button>
                            <button type="button" onclick="filterByCategory('nonmetal')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="nonmetal">Nonmetals</button>
                            <button type="button" onclick="filterByCategory('noble_gas')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="noble_gas">Noble Gases</button>
                            <button type="button" onclick="filterByCategory('alkali_metal')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="alkali_metal">Alkali Metals</button>
                            <button type="button" onclick="filterByCategory('alkaline_earth')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="alkaline_earth">Alkaline Earth</button>
                            <button type="button" onclick="filterByCategory('metalloid')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="metalloid">Metalloids</button>
                            <button type="button" onclick="filterByCategory('halogen')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="halogen">Halogens</button>
                            <button type="button" onclick="filterByCategory('transition_metal')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="transition_metal">Transition Metals</button>
                            <button type="button" onclick="filterByCategory('post_transition_metal')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="post_transition_metal">Post-Transition</button>
                            <button type="button" onclick="filterByCategory('lanthanide')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="lanthanide">Lanthanides</button>
                            <button type="button" onclick="filterByCategory('actinide')" class="pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition" data-cat="actinide">Actinides</button>
                        </div>

                        <!-- Periodic Table Elements Grid / Table -->
                        <div class="overflow-x-auto max-h-[500px] border border-slate-200 dark:border-slate-700 rounded-xl">
                            <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
                                <thead class="bg-slate-50 dark:bg-slate-900/90 sticky top-0 font-semibold text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                                    <tr>
                                        <th class="px-3 py-2">Z</th>
                                        <th class="px-3 py-2">Symbol</th>
                                        <th class="px-3 py-2">Element Name</th>
                                        <th class="px-3 py-2">Atomic Weight (g/mol)</th>
                                        <th class="px-3 py-2">Monoisotopic (Da)</th>
                                        <th class="px-3 py-2">Group &amp; Period</th>
                                        <th class="px-3 py-2">Category</th>
                                        <th class="px-3 py-2 text-right">Action</th>
                                    </tr>
                                </thead>
                                <tbody id="periodicTableBody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                                    <!-- Populated dynamically -->
                                </tbody>
                            </table>
                        </div>

                    </div>
                </div>

                <!-- TAB 4: Print Report -->
                <div id="tab-print" class="tab-panel space-y-6">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100" id="printableReportSection">
                        <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-700 pb-4 mb-6">
                            <div>
                                <h2 class="text-xl font-bold tracking-tight text-slate-900 dark:text-white">Certificate of Chemical Stoichiometric Analysis</h2>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Generated by CalcWorld Chemical Analytical Engine &bull; Compliant with IUPAC CIAAW Standards</p>
                            </div>
                            <div class="text-right text-xs text-slate-500 dark:text-slate-400 font-mono" id="reportTimestamp">
                                Oct 16, 2026
                            </div>
                        </div>

                        <div class="space-y-4 text-xs">
                            <div class="grid grid-cols-2 gap-4 bg-slate-50 dark:bg-slate-900/40 p-4 rounded-xl font-mono">
                                <div>
                                    <span class="text-slate-500 block font-sans">Formula Analyzed</span>
                                    <span class="font-bold text-base text-slate-900 dark:text-white" id="reportFormula">CuSO4*5H2O</span>
                                </div>
                                <div>
                                    <span class="text-slate-500 block font-sans">Total Molar Mass ($M$)</span>
                                    <span class="font-bold text-base text-brand-600 dark:text-brand-400" id="reportMolarMass">249.685 g/mol</span>
                                </div>
                            </div>

                            <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-700 rounded-lg overflow-hidden">
                                <tbody class="divide-y divide-slate-200 dark:divide-slate-700 font-mono">
                                    <tr>
                                        <td class="p-2.5 bg-slate-50 dark:bg-slate-900/60 font-semibold w-1/2">Empirical Formula</td>
                                        <td class="p-2.5 font-bold" id="reportEmpirical">CuH10O9S</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2.5 bg-slate-50 dark:bg-slate-900/60 font-semibold">Hill System Notation</td>
                                        <td class="p-2.5" id="reportHill">CuH10O9S</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2.5 bg-slate-50 dark:bg-slate-900/60 font-semibold">Total Atoms per Formula Unit</td>
                                        <td class="p-2.5" id="reportTotalAtoms">21 atoms</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2.5 bg-slate-50 dark:bg-slate-900/60 font-semibold">Monoisotopic Mass (HRMS)</td>
                                        <td class="p-2.5" id="reportMonoisotopic">248.937 Da</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2.5 bg-slate-50 dark:bg-slate-900/60 font-semibold">Avogadro's Particle Count per Mol</td>
                                        <td class="p-2.5">6.02214076 &times; 10^23 particles</td>
                                    </tr>
                                </tbody>
                            </table>

                            <div class="mt-4">
                                <span class="font-bold text-xs text-slate-900 dark:text-white block mb-2">Elemental Mass Fraction Table:</span>
                                <div id="reportElementTableContainer">
                                    <!-- Populated dynamically -->
                                </div>
                            </div>

                            <div class="bg-slate-50 dark:bg-slate-900/40 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2">
                                <h4 class="font-bold text-slate-900 dark:text-white">Formal Laboratory Certification</h4>
                                <p class="text-slate-600 dark:text-slate-300 leading-relaxed text-[11px]" id="reportConclusion">
                                    Stoichiometric analysis verified across all constituent chemical elements using standard atomic weights evaluated by the IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW).
                                </p>
                            </div>

                            <div class="pt-4 flex justify-end no-print">
                                <button type="button" onclick="window.print()" class="px-4 py-2 bg-brand-600 hover:bg-brand-700 text-white rounded-lg font-bold transition flex items-center gap-2 shadow">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H7v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                                    <span>Print Audit Certificate / Export PDF</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- AdSense Slot 2: Under-Result Display Ad -->
                <div class="ad-slot no-print" id="ad-slot-2">
                    <span>Sponsored Advertisement &bull; Under-Result Slot 2</span>
                </div>

            </div>
        </div>

        <!-- AdSense Slot 4: Mid-Guide Content Ad -->
        <div class="ad-slot no-print mt-10" id="ad-slot-4">
            <span>Sponsored Advertisement &bull; Mid-Article Slot 4</span>
        </div>

        <!-- Comprehensive 1200+ Word Educational Guide -->
        ${generateEducationalGuide()}

        <!-- Frequently Asked Questions (FAQ) Accordion -->
        ${faqHtml}

        <!-- AdSense Slot 5: Bottom Multiplex Native Grid -->
        <div class="ad-slot no-print mt-10" id="ad-slot-5">
            <span>Sponsored Advertisement &bull; Multiplex Native Grid Slot 5</span>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-12 px-4 sm:px-6 lg:px-8 mt-16 text-slate-600 dark:text-slate-400 text-xs no-print">
        <div class="max-w-7xl mx-auto space-y-6">
            <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-6">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-brand-600 flex items-center justify-center text-white font-bold text-sm">MW</span>
                    <span class="font-bold text-base text-slate-900 dark:text-white tracking-tight">CalcWorld</span>
                    <span class="text-[11px] text-slate-400 ml-2">&copy; 2026 CalcWorld Enterprise Network. All rights reserved.</span>
                </div>
                <div class="flex flex-wrap items-center gap-4 text-xs">
                    <a href="https://calcworld.net/privacy" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Privacy Policy</a>
                    <a href="https://calcworld.net/terms" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Terms of Service</a>
                    <a href="https://calcworld.net/about" class="hover:text-brand-600 dark:hover:text-brand-400 transition">About Us</a>
                    <a href="https://calcworld.net/contact" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Contact</a>
                </div>
            </div>

            <div class="text-[11px] leading-relaxed text-slate-500 dark:text-slate-500">
                <p><strong>Academic &amp; Methodological Notice:</strong> CalcWorld Molecular Weight &amp; Molar Mass Calculator executes verified algorithms compliant with standards established by the International Union of Pure and Applied Chemistry (IUPAC), Commission on Isotopic Abundances and Atomic Weights (CIAAW), and the National Institute of Standards and Technology (NIST). This software is provided for academic, laboratory research, and pharmaceutical manufacturing analysis.</p>
            </div>
        </div>
    </footer>

    <!-- Floating Quick-Switcher Bar (Pill Bar) -->
    <aside id="floatingBar" class="fixed bottom-4 left-1/2 -translate-x-1/2 z-40 bg-white/95 dark:bg-slate-800/95 backdrop-blur-md px-4 py-2 rounded-full shadow-lg border border-slate-200 dark:border-slate-700 flex items-center gap-2 text-xs font-medium text-slate-700 dark:text-slate-300 no-print transition-all">
        <span class="text-slate-400 font-semibold uppercase tracking-wider text-[10px] hidden sm:inline">Chemistry Tools:</span>
        <a href="molarity-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Molarity</a>
        <a href="stoichiometry-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Stoichiometry</a>
        <a href="empirical-formula-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Empirical Formula</a>
        <a href="percent-composition-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition hidden sm:inline">% Composition</a>
    </aside>

    <!-- Toast Notification -->
    <div id="toast" class="toast-notify" role="alert">
        <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
        <span id="toastMsg">Formula copied to clipboard!</span>
    </div>

<script>
    // --- 118 Elements IUPAC / CIAAW Database ---
    const elements = ${elementsArrayCode};

    // Lookup Maps
    const elementMap = {};
    elements.forEach(e => { elementMap[e.s] = e; });

    // Global State
    let currentFormula = 'CuSO4*5H2O';
    let currentParsed = null;
    let chartMode = 'mass'; // 'mass' or 'atom'
    let elementChartInstance = null;
    let customSampleMass = 100;
    const NA = 6.02214076e23;

    // --- DOM Ready Initialization ---
    window.addEventListener('DOMContentLoaded', () => {
        initPeriodicTable();
        parseUrlParams();
        calculateFormula(currentFormula);

        // AdBlock Detection
        setTimeout(() => {
            const adSlot = document.getElementById('ad-slot-1');
            if (adSlot && adSlot.offsetHeight === 0) {
                const notice = document.getElementById('adblockRecovery');
                if (notice) notice.classList.remove('hidden');
            }
        }, 1200);

        // Set Date
        const d = new Date();
        const dateStr = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
        const tsEl = document.getElementById('reportTimestamp');
        if (tsEl) tsEl.textContent = dateStr;
    });

    // --- High-Performance Chemical Formula Parser ---
    function parseChemicalFormula(input) {
        if (!input || !input.trim()) throw new Error('Chemical formula cannot be empty.');
        
        // Normalize hydrate symbols: middot, bullet, unicode dots, or asterisk
        let clean = input.trim().replace(/[\\u00B7\\u2022\\u22C5]/g, '*');
        clean = clean.replace(/\\s*\\.\\s*(?=\\d*[A-Z])/g, '*');

        const parts = clean.split('*');
        const totalCounts = {};
        let rawTokensList = [];

        for (let part of parts) {
            part = part.trim();
            if (!part) continue;

            // Check leading coefficient (e.g. 5H2O or 2(NH4)2SO4)
            let partMultiplier = 1;
            const matchCoeff = part.match(/^(\\d+)(.*)$/);
            let subFormula = part;
            if (matchCoeff && matchCoeff[2] && /[A-Za-z\\(\\[\\{]/.test(matchCoeff[2])) {
                partMultiplier = parseInt(matchCoeff[1], 10);
                subFormula = matchCoeff[2];
            }

            // Lexical tokenization
            const tokens = [];
            const regex = /([A-Z][a-z]?|\\d+|\\(|\\)|\\[|\\]|\\{|\\}|\\s+)/g;
            let match;
            let idx = 0;
            while ((match = regex.exec(subFormula)) !== null) {
                if (match.index !== idx) {
                    const invalid = subFormula.slice(idx, match.index);
                    throw new Error('Unrecognized syntax near "' + invalid + '"');
                }
                idx = regex.lastIndex;
                const tok = match[0].trim();
                if (tok) tokens.push(tok);
            }
            if (idx !== subFormula.length) {
                throw new Error('Syntax error at end of formula: "' + subFormula.slice(idx) + '"');
            }

            // Stack-based hierarchical group parsing
            const stack = [{}];
            for (let i = 0; i < tokens.length; i++) {
                const tok = tokens[i];
                if (tok === '(' || tok === '[' || tok === '{') {
                    stack.push({});
                } else if (tok === ')' || tok === ']' || tok === '}') {
                    if (stack.length <= 1) throw new Error('Mismatched closing bracket: ' + tok);
                    const group = stack.pop();
                    let mult = 1;
                    if (i + 1 < tokens.length && /^\\d+$/.test(tokens[i + 1])) {
                        mult = parseInt(tokens[i + 1], 10);
                        i++;
                    }
                    const parent = stack[stack.length - 1];
                    for (const [el, cnt] of Object.entries(group)) {
                        parent[el] = (parent[el] || 0) + cnt * mult;
                    }
                } else if (/^[A-Z][a-z]?$/.test(tok)) {
                    if (!elementMap[tok]) {
                        throw new Error('Unknown chemical element symbol "' + tok + '".');
                    }
                    let count = 1;
                    if (i + 1 < tokens.length && /^\\d+$/.test(tokens[i + 1])) {
                        count = parseInt(tokens[i + 1], 10);
                        i++;
                    }
                    const parent = stack[stack.length - 1];
                    parent[tok] = (parent[tok] || 0) + count;
                } else {
                    throw new Error('Unexpected token: ' + tok);
                }
            }

            if (stack.length !== 1) {
                throw new Error('Mismatched opening bracket in formula.');
            }

            const partResult = stack[0];
            for (const [el, cnt] of Object.entries(partResult)) {
                totalCounts[el] = (totalCounts[el] || 0) + cnt * partMultiplier;
            }
        }

        if (Object.keys(totalCounts).length === 0) {
            throw new Error('Formula contains no valid elements.');
        }

        return totalCounts;
    }

    // Greatest Common Divisor helper
    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    // Determine Empirical Formula
    function computeEmpiricalFormula(counts) {
        const countsArr = Object.values(counts);
        let factor = countsArr[0];
        for (let i = 1; i < countsArr.length; i++) {
            factor = gcd(factor, countsArr[i]);
        }
        
        // Build empirical formula string using Hill System or standard ordering
        const empCounts = {};
        for (const [el, cnt] of Object.entries(counts)) {
            empCounts[el] = cnt / factor;
        }

        const formulaStr = formatHillSystemFormula(empCounts);
        return { empiricalFormula: formulaStr, factor: factor, empCounts: empCounts };
    }

    // Format Formula under Edwin A. Hill System
    function formatHillSystemFormula(counts) {
        let result = '';
        const keys = Object.keys(counts);
        const hasCarbon = keys.includes('C');

        if (hasCarbon) {
            // C first, H second, rest alphabetical
            if (counts['C']) {
                result += 'C' + (counts['C'] > 1 ? counts['C'] : '');
            }
            if (counts['H']) {
                result += 'H' + (counts['H'] > 1 ? counts['H'] : '');
            }
            const others = keys.filter(k => k !== 'C' && k !== 'H').sort();
            for (const el of others) {
                result += el + (counts[el] > 1 ? counts[el] : '');
            }
        } else {
            // Pure alphabetical
            const sortedKeys = keys.sort();
            for (const el of sortedKeys) {
                result += el + (counts[el] > 1 ? counts[el] : '');
            }
        }
        return result;
    }

    // Format Formula with HTML Subscripts for Visual Display
    function formatSubscriptsHtml(formula) {
        return formula
            .replace(/\\*/g, '&bull;')
            .replace(/(\\d+)/g, '<sub>$1</sub>');
    }

    // --- Core Calculation Routine ---
    function calculateFormula(formulaStr) {
        const badge = document.getElementById('syntaxValidationBadge');
        try {
            const counts = parseChemicalFormula(formulaStr);
            currentFormula = formulaStr;
            badge.textContent = 'Valid Formula';
            badge.className = 'text-[11px] font-semibold text-emerald-600 dark:text-emerald-400';

            // Calculate stoichiometric metrics
            let totalMolarMass = 0;
            let totalAtoms = 0;
            let totalMonoisotopic = 0;
            const elementRows = [];

            for (const [sym, count] of Object.entries(counts)) {
                const el = elementMap[sym];
                const mass = el.m;
                const mono = el.mono || el.m;
                const elemTotalMass = count * mass;
                const elemTotalMono = count * mono;

                totalMolarMass += elemTotalMass;
                totalAtoms += count;
                totalMonoisotopic += elemTotalMono;

                elementRows.push({
                    element: el,
                    symbol: sym,
                    name: el.n,
                    z: el.z,
                    atomicWeight: mass,
                    count: count,
                    massContribution: elemTotalMass,
                    monoisotopicContribution: elemTotalMono,
                    category: el.cat,
                    color: el.c
                });
            }

            // Compute percentages
            for (const row of elementRows) {
                row.percentMass = (row.massContribution / totalMolarMass) * 100;
                row.percentAtoms = (row.count / totalAtoms) * 100;
            }

            // Sort rows by mass contribution descending
            elementRows.sort((a, b) => b.massContribution - a.massContribution);

            // Empirical formula & Hill formula
            const empData = computeEmpiricalFormula(counts);
            const hillFormula = formatHillSystemFormula(counts);

            currentParsed = {
                formula: formulaStr,
                counts: counts,
                elementRows: elementRows,
                totalMolarMass: totalMolarMass,
                totalAtoms: totalAtoms,
                totalMonoisotopic: totalMonoisotopic,
                empirical: empData.empiricalFormula,
                empiricalFactor: empData.factor,
                hillFormula: hillFormula,
                distinctElements: Object.keys(counts).length
            };

            updateUI();
        } catch (err) {
            badge.textContent = err.message || 'Syntax Error';
            badge.className = 'text-[11px] font-semibold text-rose-500 dark:text-rose-400';
        }
    }

    // --- UI Update Manager ---
    function updateUI() {
        if (!currentParsed) return;
        const p = currentParsed;

        // Header and Displays
        document.getElementById('formulaFormattedBadge').innerHTML = formatSubscriptsHtml(p.formula);
        document.getElementById('molarMassDisplay').innerHTML = p.totalMolarMass.toFixed(3) + ' <span class="text-xl sm:text-2xl font-normal text-slate-500 dark:text-slate-400">g/mol</span>';
        
        // Narrative
        const elemSummaryList = p.elementRows.map(r => r.count + ' ' + r.symbol).join(', ');
        document.getElementById('compoundNarrativeDisplay').textContent = 
            'Formula contains ' + p.distinctElements + ' distinct elements (' + elemSummaryList + ') totaling ' + p.totalAtoms + ' atoms per formula unit.';

        // Unit Pills
        document.getElementById('unitDaDisplay').textContent = p.totalMolarMass.toFixed(3) + ' Da (u)';
        document.getElementById('unitKgDisplay').textContent = (p.totalMolarMass / 1000).toFixed(5) + ' kg/mol';
        document.getElementById('unitOzDisplay').textContent = (p.totalMolarMass * 0.035274).toFixed(4) + ' oz/mol';

        // 4 Metric Cards
        document.getElementById('metricMolarMass').textContent = p.totalMolarMass.toFixed(3);
        document.getElementById('metricEmpirical').textContent = p.empirical;
        document.getElementById('metricEmpiricalRatio').textContent = 'Ratio n = ' + p.empiricalFactor;
        document.getElementById('metricAtomCount').textContent = p.totalAtoms + ' atoms';
        document.getElementById('metricDistinctElements').textContent = p.distinctElements + ' distinct elements';
        document.getElementById('metricMonoisotopic').textContent = p.totalMonoisotopic.toFixed(4);

        // Hill System & Anhydrous
        document.getElementById('hillSystemDisplay').textContent = 'Hill System: ' + p.hillFormula;
        
        // Check if hydrate to calculate anhydrous mass
        if (p.formula.includes('*') || p.formula.includes('&bull;')) {
            try {
                const anhydrousPart = p.formula.split(/[*&bull;]/)[0].trim();
                const anhCounts = parseChemicalFormula(anhydrousPart);
                let anhMass = 0;
                for (const [s, c] of Object.entries(anhCounts)) {
                    anhMass += elementMap[s].m * c;
                }
                const anhPct = (anhMass / p.totalMolarMass) * 100;
                document.getElementById('anhydrousComparisonDisplay').textContent = 
                    'Anhydrous Mass: ' + anhMass.toFixed(3) + ' g/mol (' + anhPct.toFixed(1) + '%)';
            } catch (e) {
                document.getElementById('anhydrousComparisonDisplay').textContent = 'Anhydrous Mass: N/A';
            }
        } else {
            document.getElementById('anhydrousComparisonDisplay').textContent = 'Single component non-hydrated';
        }

        // Render Chart.js
        renderChart();

        // Render Step-by-Step Derivation
        renderDerivation();

        // Sync Bidirectional Stoichiometry
        syncFromMass(p.totalMolarMass);

        // Calculate Solution Prep
        calcSolutionPrep();

        // Render Tab 2: Elemental Breakdown Table
        renderElementalTable();

        // Populate Print Report
        populatePrintReport();
    }

    // --- Chart.js Elemental Mass Doughnut Chart ---
    function renderChart() {
        if (!currentParsed) return;
        const p = currentParsed;
        const ctx = document.getElementById('elementChart');
        if (!ctx) return;

        const labels = p.elementRows.map(r => r.symbol + ' (' + r.name + ')');
        const dataValues = chartMode === 'mass' 
            ? p.elementRows.map(r => parseFloat(r.percentMass.toFixed(2)))
            : p.elementRows.map(r => parseFloat(r.percentAtoms.toFixed(2)));
        const colors = p.elementRows.map(r => r.color || '#6366f1');

        if (elementChartInstance) {
            elementChartInstance.destroy();
        }

        elementChartInstance = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: dataValues,
                    backgroundColor: colors,
                    borderWidth: 2,
                    borderColor: document.documentElement.classList.contains('dark') ? '#1e293b' : '#ffffff',
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            boxWidth: 14,
                            padding: 12,
                            font: { family: 'Inter', size: 11 },
                            color: document.documentElement.classList.contains('dark') ? '#cbd5e1' : '#475569'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const idx = context.dataIndex;
                                const row = p.elementRows[idx];
                                if (chartMode === 'mass') {
                                    return ' ' + row.symbol + ': ' + row.percentMass.toFixed(2) + '% (' + row.massContribution.toFixed(3) + ' g/mol)';
                                } else {
                                    return ' ' + row.symbol + ': ' + row.percentAtoms.toFixed(2) + '% (' + row.count + ' of ' + p.totalAtoms + ' atoms)';
                                }
                            }
                        }
                    }
                },
                cutout: '62%'
            }
        });
    }

    function setChartMode(mode) {
        chartMode = mode;
        const massBtn = document.getElementById('chartMode_mass');
        const atomBtn = document.getElementById('chartMode_atom');
        if (mode === 'mass') {
            massBtn.className = 'px-2.5 py-1 font-semibold rounded-md bg-white dark:bg-slate-800 text-brand-600 dark:text-brand-400 shadow-sm transition';
            atomBtn.className = 'px-2.5 py-1 font-semibold rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition';
        } else {
            atomBtn.className = 'px-2.5 py-1 font-semibold rounded-md bg-white dark:bg-slate-800 text-brand-600 dark:text-brand-400 shadow-sm transition';
            massBtn.className = 'px-2.5 py-1 font-semibold rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition';
        }
        renderChart();
    }

    // --- Step-by-Step Derivation Renderer with MathJax ---
    function renderDerivation() {
        if (!currentParsed) return;
        const p = currentParsed;
        const block = document.getElementById('mathJaxDerivationBlock');
        if (!block) return;

        let termsTex = p.elementRows.map(r => r.count + ' \\cdot A_r(\\\\text{' + r.symbol + '})').join(' + ');
        let numericalTex = p.elementRows.map(r => r.count + ' \\times ' + r.atomicWeight.toFixed(3)).join(' + ');
        let subtotalTex = p.elementRows.map(r => r.massContribution.toFixed(3)).join(' + ');

        let massPercentEquations = p.elementRows.map(r => {
            return '\\\\%\\\\text{' + r.symbol + '} = \\\\frac{' + r.massContribution.toFixed(3) + '}{' + p.totalMolarMass.toFixed(3) + '} \\\\times 100\\\\% = ' + r.percentMass.toFixed(2) + '\\\\%';
        }).join(' \\\\quad\\\\text{;}\\\\quad ');

        let html = '<div class="space-y-3">';
        html += '<div><strong>1. IUPAC Molar Mass Summation Formula:</strong></div>';
        html += '<div class="p-2 bg-white dark:bg-slate-800 rounded-lg overflow-x-auto text-center">$$M = \\\\sum_{i=1}^k n_i \\\\cdot A_r(E_i)$$</div>';
        
        html += '<div><strong>2. Explicit Atomic Weight Substitution:</strong></div>';
        html += '<div class="p-2 bg-white dark:bg-slate-800 rounded-lg overflow-x-auto text-center">$$M = ' + numericalTex + '$$</div>';
        html += '<div class="p-2 bg-white dark:bg-slate-800 rounded-lg overflow-x-auto text-center">$$M = ' + subtotalTex + ' = \\\\mathbf{' + p.totalMolarMass.toFixed(3) + '} \\\\text{ g/mol}$$</div>';

        html += '<div><strong>3. Elemental Mass Percentage Composition Formulas:</strong></div>';
        html += '<div class="p-2 bg-white dark:bg-slate-800 rounded-lg overflow-x-auto text-center">$$' + massPercentEquations + '$$</div>';
        html += '</div>';

        block.innerHTML = html;

        // Trigger MathJax typeset
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise([block]).catch(function (err) {
                console.warn('MathJax typeset error:', err);
            });
        }
    }

    // --- Bidirectional Stoichiometry Converter ---
    function syncFromMass(val) {
        if (!currentParsed || isNaN(val) || val <= 0) return;
        const mass = parseFloat(val);
        const moles = mass / currentParsed.totalMolarMass;
        const molecules = moles * NA;
        const totalAtoms = molecules * currentParsed.totalAtoms;

        document.getElementById('stoich_moles').value = moles.toFixed(6);
        document.getElementById('stoich_molecules').value = molecules.toExponential(4);
        document.getElementById('stoich_atoms').value = totalAtoms.toExponential(4);
    }

    function syncFromMoles(val) {
        if (!currentParsed || isNaN(val) || val <= 0) return;
        const moles = parseFloat(val);
        const mass = moles * currentParsed.totalMolarMass;
        const molecules = moles * NA;
        const totalAtoms = molecules * currentParsed.totalAtoms;

        document.getElementById('stoich_mass').value = mass.toFixed(4);
        document.getElementById('stoich_molecules').value = molecules.toExponential(4);
        document.getElementById('stoich_atoms').value = totalAtoms.toExponential(4);
    }

    function calcSolutionPrep() {
        if (!currentParsed) return;
        const volMl = parseFloat(document.getElementById('sol_volume').value) || 0;
        const molarity = parseFloat(document.getElementById('sol_molarity').value) || 0;
        const massGrams = (volMl / 1000) * molarity * currentParsed.totalMolarMass;
        document.getElementById('soluteRequiredDisplay').textContent = massGrams.toFixed(4) + ' g';
    }

    // --- Tab 2: Elemental Breakdown Table ---
    function renderElementalTable() {
        if (!currentParsed) return;
        const p = currentParsed;
        const tbody = document.getElementById('elementTableBody');
        const tfoot = document.getElementById('elementTableFoot');
        if (!tbody || !tfoot) return;

        let rowsHtml = '';
        for (const row of p.elementRows) {
            const massInSample = (row.percentMass / 100) * customSampleMass;
            rowsHtml += '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">';
            rowsHtml += '<td class="px-3 py-2.5 font-sans font-bold flex items-center gap-2">';
            rowsHtml += '<span class="w-3 h-3 rounded-full shrink-0" style="background-color: ' + (row.color || '#6366f1') + '"></span>';
            rowsHtml += '<span>' + row.symbol + '</span>';
            rowsHtml += '<span class="text-slate-400 font-normal text-xs">(' + row.name + ')</span>';
            rowsHtml += '</td>';
            rowsHtml += '<td class="px-3 py-2.5">' + row.atomicWeight.toFixed(3) + '</td>';
            rowsHtml += '<td class="px-3 py-2.5 font-bold text-slate-900 dark:text-white">' + row.count + '</td>';
            rowsHtml += '<td class="px-3 py-2.5">' + row.massContribution.toFixed(3) + ' g/mol</td>';
            rowsHtml += '<td class="px-3 py-2.5">';
            rowsHtml += '<div class="flex items-center gap-2">';
            rowsHtml += '<div class="w-16 bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden shrink-0">';
            rowsHtml += '<div class="h-full rounded-full" style="width: ' + row.percentMass.toFixed(1) + '%; background-color: ' + (row.color || '#6366f1') + '"></div>';
            rowsHtml += '</div>';
            rowsHtml += '<span class="font-bold text-brand-600 dark:text-brand-400">' + row.percentMass.toFixed(2) + '%</span>';
            rowsHtml += '</div>';
            rowsHtml += '</td>';
            rowsHtml += '<td class="px-3 py-2.5 font-bold text-slate-800 dark:text-slate-200">' + massInSample.toFixed(3) + ' g</td>';
            rowsHtml += '</tr>';
        }
        tbody.innerHTML = rowsHtml;

        tfoot.innerHTML = 
            '<tr>' +
            '<td class="px-3 py-2.5 font-sans">Total / Formula Unit</td>' +
            '<td class="px-3 py-2.5">-</td>' +
            '<td class="px-3 py-2.5">' + p.totalAtoms + ' atoms</td>' +
            '<td class="px-3 py-2.5 text-brand-600 dark:text-brand-400">' + p.totalMolarMass.toFixed(3) + ' g/mol</td>' +
            '<td class="px-3 py-2.5">100.00%</td>' +
            '<td class="px-3 py-2.5 text-brand-600 dark:text-brand-400">' + customSampleMass.toFixed(3) + ' g</td>' +
            '</tr>';
    }

    function updateCustomSampleMass(val) {
        const v = parseFloat(val);
        if (!isNaN(v) && v > 0) {
            customSampleMass = v;
            renderElementalTable();
        }
    }

    function downloadCsvReport() {
        if (!currentParsed) return;
        const p = currentParsed;
        let csv = 'Element Symbol,Element Name,Atomic Number,Atomic Weight (g/mol),Atom Count,Mass Contribution (g/mol),Mass Share (%),Mass in ' + customSampleMass + 'g Sample (g)\\n';
        for (const r of p.elementRows) {
            const mSample = ((r.percentMass / 100) * customSampleMass).toFixed(4);
            csv += [r.symbol, '"' + r.name + '"', r.z, r.atomicWeight.toFixed(4), r.count, r.massContribution.toFixed(4), r.percentMass.toFixed(2), mSample].join(',') + '\\n';
        }
        csv += 'Total,-,-,-,' + p.totalAtoms + ',' + p.totalMolarMass.toFixed(4) + ',100.00,' + customSampleMass.toFixed(4) + '\\n';

        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'molecular_weight_' + p.formula.replace(/[^a-zA-Z0-9]/g, '_') + '.csv';
        a.click();
        URL.revokeObjectURL(url);
        showToast('CSV table downloaded!');
    }

    // --- Tab 3: Periodic Table Quick Lookup ---
    function initPeriodicTable() {
        renderPeriodicTable(elements);
    }

    function renderPeriodicTable(items) {
        const tbody = document.getElementById('periodicTableBody');
        if (!tbody) return;

        let html = '';
        for (const el of items) {
            const catLabel = el.cat.replace(/_/g, ' ');
            html += '<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">';
            html += '<td class="px-3 py-2 text-slate-400">' + el.z + '</td>';
            html += '<td class="px-3 py-2 font-bold text-slate-900 dark:text-white flex items-center gap-1.5">';
            html += '<span class="w-2.5 h-2.5 rounded-full inline-block" style="background-color: ' + el.c + '"></span>';
            html += '<span>' + el.s + '</span>';
            html += '</td>';
            html += '<td class="px-3 py-2 font-sans font-medium">' + el.n + '</td>';
            html += '<td class="px-3 py-2 font-bold text-brand-600 dark:text-brand-400">' + el.m.toFixed(3) + '</td>';
            html += '<td class="px-3 py-2 text-slate-500">' + (el.mono ? el.mono.toFixed(4) : '-') + '</td>';
            html += '<td class="px-3 py-2 text-slate-400">P' + el.p + (el.g ? ' G' + el.g : '') + '</td>';
            html += '<td class="px-3 py-2 capitalize text-slate-500 text-[11px]">' + catLabel + '</td>';
            html += '<td class="px-3 py-2 text-right">';
            html += '<button type="button" onclick="appendToken(\\'' + el.s + '\\')" class="px-2 py-1 rounded bg-brand-50 hover:bg-brand-100 text-brand-700 dark:bg-brand-950 dark:hover:bg-brand-900 dark:text-brand-300 text-[11px] font-sans font-bold transition">Insert</button>';
            html += '</td>';
            html += '</tr>';
        }
        tbody.innerHTML = html;
    }

    function filterPeriodicTable(query) {
        const q = (query || '').trim().toLowerCase();
        if (!q) {
            renderPeriodicTable(elements);
            return;
        }
        const filtered = elements.filter(e => 
            e.s.toLowerCase().includes(q) ||
            e.n.toLowerCase().includes(q) ||
            e.z.toString() === q
        );
        renderPeriodicTable(filtered);
    }

    function filterByCategory(category) {
        // Toggle active button style
        document.querySelectorAll('.pt-cat-btn').forEach(btn => {
            if (btn.dataset.cat === category) {
                btn.className = 'pt-cat-btn active px-2.5 py-1 rounded-md bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 border border-brand-300 font-semibold';
            } else {
                btn.className = 'pt-cat-btn px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-700/60 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition';
            }
        });

        if (category === 'all') {
            renderPeriodicTable(elements);
        } else {
            const filtered = elements.filter(e => e.cat === category);
            renderPeriodicTable(filtered);
        }
    }

    // --- Tab 4: Populate Print Report ---
    function populatePrintReport() {
        if (!currentParsed) return;
        const p = currentParsed;

        document.getElementById('reportFormula').textContent = p.formula;
        document.getElementById('reportMolarMass').textContent = p.totalMolarMass.toFixed(3) + ' g/mol';
        document.getElementById('reportEmpirical').textContent = p.empirical + ' (Scaling Factor n = ' + p.empiricalFactor + ')';
        document.getElementById('reportHill').textContent = p.hillFormula;
        document.getElementById('reportTotalAtoms').textContent = p.totalAtoms + ' atoms (' + p.distinctElements + ' distinct elements)';
        document.getElementById('reportMonoisotopic').textContent = p.totalMonoisotopic.toFixed(4) + ' Da';

        // Table
        let html = '<table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-700 text-xs font-mono">';
        html += '<thead class="bg-slate-50 dark:bg-slate-900 border-b border-slate-200 dark:border-slate-700 font-bold"><tr><th class="p-2">Element</th><th class="p-2">Atomic Weight</th><th class="p-2">Count</th><th class="p-2">Mass Contrib</th><th class="p-2">Mass %</th></tr></thead>';
        html += '<tbody class="divide-y divide-slate-200 dark:divide-slate-700">';
        for (const r of p.elementRows) {
            html += '<tr><td class="p-2 font-bold">' + r.symbol + ' (' + r.name + ')</td><td class="p-2">' + r.atomicWeight.toFixed(3) + '</td><td class="p-2">' + r.count + '</td><td class="p-2">' + r.massContribution.toFixed(3) + ' g/mol</td><td class="p-2 font-bold text-brand-600 dark:text-brand-400">' + r.percentMass.toFixed(2) + '%</td></tr>';
        }
        html += '</tbody></table>';
        document.getElementById('reportElementTableContainer').innerHTML = html;
    }

    // --- Form Controls & Virtual Keypad ---
    function handleFormulaInput(val) {
        calculateFormula(val);
    }

    function setFormula(formula) {
        document.getElementById('formulaInput').value = formula;
        calculateFormula(formula);
    }

    function appendToken(token) {
        const inp = document.getElementById('formulaInput');
        const start = inp.selectionStart;
        const end = inp.selectionEnd;
        const text = inp.value;
        inp.value = text.substring(0, start) + token + text.substring(end);
        inp.focus();
        inp.selectionStart = inp.selectionEnd = start + token.length;
        calculateFormula(inp.value);
    }

    function clearFormula() {
        document.getElementById('formulaInput').value = '';
        calculateFormula('');
    }

    function autoCapitalizeFormula() {
        const inp = document.getElementById('formulaInput');
        let text = inp.value;
        // Simple case fixer for standard element symbols like c6h12o6 -> C6H12O6
        // Replaces known elements matching lowercase
        for (const el of elements) {
            const symLower = el.s.toLowerCase();
            const re = new RegExp('\\\\b' + symLower + '(?=[0-9\\\\(\\\\[\\\\*]|$)', 'g');
            text = text.replace(re, el.s);
        }
        inp.value = text;
        calculateFormula(text);
        showToast('Formatted formula casing!');
    }

    function loadPreset(val) {
        if (!val) return;
        setFormula(val);
    }

    function triggerRecalculate() {
        const val = document.getElementById('formulaInput').value;
        calculateFormula(val);
        showToast('Molar mass updated!');
    }

    function resetDefaultFormula() {
        setFormula('CuSO4*5H2O');
        document.getElementById('presetSelect').value = 'CuSO4*5H2O';
        showToast('Reset to default compound.');
    }

    function copyShareUrl() {
        const url = new URL(window.location.href);
        url.searchParams.set('formula', currentFormula);
        navigator.clipboard.writeText(url.toString()).then(() => {
            showToast('Shareable formula URL copied!');
        });
    }

    function copyFormattedSummary() {
        if (!currentParsed) return;
        const p = currentParsed;
        let text = 'Chemical Analysis Summary for ' + p.formula + '\\n';
        text += 'Total Molar Mass: ' + p.totalMolarMass.toFixed(3) + ' g/mol (' + p.totalMolarMass.toFixed(3) + ' Da)\\n';
        text += 'Empirical Formula: ' + p.empirical + ' (Ratio factor n = ' + p.empiricalFactor + ')\\n';
        text += 'Total Atom Count: ' + p.totalAtoms + ' atoms across ' + p.distinctElements + ' distinct elements\\n';
        text += 'Monoisotopic Mass: ' + p.totalMonoisotopic.toFixed(4) + ' Da\\n';
        text += 'Elemental Mass Composition:\\n';
        for (const r of p.elementRows) {
            text += '  - ' + r.symbol + ' (' + r.name + '): ' + r.percentMass.toFixed(2) + '% (' + r.count + ' atoms, ' + r.massContribution.toFixed(3) + ' g/mol)\\n';
        }
        text += 'Computed via CalcWorld Molecular Weight Engine (IUPAC CIAAW Standards)';
        navigator.clipboard.writeText(text).then(() => {
            showToast('Full analysis summary copied!');
        });
    }

    // --- Tab Switcher ---
    function switchTab(tabId) {
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.className = 'tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap';
        });
        document.querySelectorAll('.tab-panel').forEach(panel => {
            panel.classList.remove('active');
        });

        const activeBtn = document.getElementById('tabBtn_' + tabId);
        const activePanel = document.getElementById('tab-' + tabId);
        if (activeBtn) {
            activeBtn.className = 'tab-btn active border-b-2 border-brand-600 pb-3 px-1 text-xs sm:text-sm font-bold text-brand-600 dark:text-brand-400 whitespace-nowrap';
        }
        if (activePanel) {
            activePanel.classList.add('active');
        }

        if (tabId === 'solver') {
            setTimeout(renderChart, 50);
        }
    }

    // --- FAQ Toggle ---
    function toggleFaq(num) {
        const ans = document.getElementById('faqAns_' + num);
        const icon = document.getElementById('faqIcon_' + num);
        if (ans.classList.contains('hidden')) {
            ans.classList.remove('hidden');
            icon.classList.add('rotate-180');
        } else {
            ans.classList.add('hidden');
            icon.classList.remove('rotate-180');
        }
    }

    // --- Dark Mode Switcher ---
    function toggleTheme() {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.theme = 'light';
        } else {
            document.documentElement.classList.add('dark');
            localStorage.theme = 'dark';
        }
        if (elementChartInstance) {
            renderChart();
        }
    }

    // --- Lead Form Handler ---
    function handleLeadSubmit(e) {
        e.preventDefault();
        const btn = document.getElementById('leadSubmitBtn');
        const msg = document.getElementById('leadSuccessMsg');
        btn.textContent = 'Sending...';
        btn.disabled = true;
        setTimeout(() => {
            btn.classList.add('hidden');
            msg.classList.remove('hidden');
            showToast('Reference Guide sent to your inbox!');
        }, 600);
    }

    // --- Toast Handler ---
    function showToast(msg) {
        const toast = document.getElementById('toast');
        const toastMsg = document.getElementById('toastMsg');
        toastMsg.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2800);
    }

    // --- URL Parameter Parsing ---
    function parseUrlParams() {
        const params = new URLSearchParams(window.location.search);
        const f = params.get('formula');
        if (f) {
            document.getElementById('formulaInput').value = f;
            currentFormula = f;
        }
    }
</script>

</body>
</html>
`;

// Write to destination
fs.writeFileSync(targetFile, fullHtml, 'utf8');
console.log('Successfully generated Molecular Weight Calculator at: ' + targetFile);
const stats = fs.statSync(targetFile);
console.log('File size: ' + stats.size + ' bytes');
