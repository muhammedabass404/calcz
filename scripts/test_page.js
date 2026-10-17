const fs = require('fs');
const content = fs.readFileSync('molecular-weight-calculator.html', 'utf8');

// 1. Check JSON-LD
const jsonLdMatch = content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
if (jsonLdMatch) {
  try {
    const parsed = JSON.parse(jsonLdMatch[1]);
    console.log('JSON-LD: Valid JSON, graph entities:', parsed['@graph'].length);
  } catch (e) {
    console.error('JSON-LD Parse Error:', e.message);
  }
} else {
  console.error('JSON-LD not found!');
}

// 2. Educational Guide Word Count
const articleMatch = content.match(/<article[\s\S]*?<\/article>/);
if (articleMatch) {
  const stripped = articleMatch[0].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
  const words = stripped.trim().split(' ');
  console.log('Educational Guide word count:', words.length);
} else {
  console.error('Educational Guide not found!');
}

// 3. AdSense slots check
for (let i = 1; i <= 5; i++) {
  const hasSlot = content.includes('id="ad-slot-' + i + '"');
  console.log('AdSlot ' + i + ' present:', hasSlot);
}

// 4. Banned words check (AI cliches / forbidden terms)
const forbidden = [
  'delve', 'tapestry', 'testament', 'beacon', 'plethora', 'game-changer', 
  'in today\'s fast-paced world', 'look no further', 'unlock the secrets',
  'embark on a journey', 'without further ado'
];
const found = forbidden.filter(w => content.toLowerCase().includes(w));
console.log('Banned words found:', found);

// 5. Check all 118 elements in client script
const elMatch = content.match(/const elements = (\[[\s\S]*?\]);/);
if (elMatch) {
  const els = eval(elMatch[1]);
  console.log('Client script elements count:', els.length);
}
