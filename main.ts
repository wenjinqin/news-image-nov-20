// Contest program for make.fun's news-image-20261120 — "Sum up
// 20 November's world news in one image". The artwork lives in entry.png
// next to this file (drawn by draw20.py); this program delivers it to
// /output/entry.png, or to $MAKEFUN_OUTPUT_DIR when that is set.
// Node 22 standard library only — the grader runs it offline, twice,
// and both runs must write the same bytes, so this program only copies
// the checked file and never re-renders anything.

import { copyFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const here = new URL('./entry.png', import.meta.url);
const bytes = readFileSync(here);

// The gate accepts one whole PNG or JPEG of at most 1 MiB and 1024x1024.
// Check the header here so a bad asset fails with a readable reason.
if (bytes.length > 1_048_576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB gate limit`);
}
const isPng = bytes.subarray(0, 8).equals(
  Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
);
const isJpeg = bytes[0] === 0xff && bytes[1] === 0xd8 && bytes[bytes.length - 2] === 0xff && bytes[bytes.length - 1] === 0xd9;
if (!isPng && !isJpeg) {
  throw new Error('entry.png is not a complete PNG or JPEG');
}
if (isPng) {
  const w = bytes.readUInt32BE(16);
  const h = bytes.readUInt32BE(20);
  if (w > 1024 || h > 1024) {
    throw new Error(`entry.png is ${w}x${h}, over the 1024x1024 gate limit`);
  }
  // A whole PNG ends with the IEND chunk; a truncated file must not pass.
  if (!bytes.subarray(bytes.length - 12).equals(
    Buffer.from([0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]),
  )) {
    throw new Error('entry.png is missing its IEND chunk');
  }
}

const dest = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
copyFileSync(here, dest);

// Read the copy back: the judge sees exactly these bytes, so prove the
// file that landed is the file that was checked above.
const landed = readFileSync(dest);
if (!landed.equals(bytes)) {
  throw new Error('the copied entry.png differs from the checked source');
}
console.log(`delivered entry.png (${bytes.length} bytes) to ${dest}`);
