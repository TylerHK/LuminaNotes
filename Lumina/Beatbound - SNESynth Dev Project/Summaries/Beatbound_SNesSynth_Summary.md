# Beatbound – SNESynth Dev Project

## Brief Summary
Build a tool that converts live voice input into playful, SNES‑style audio by extracting SPC samples from SNES ROMs and applying custom audio processing.

## Current Status & Recent Progress
- **Day 1 Progress**
  - ROM extraction pipeline ~50% complete.
  - Voice recorder functional (`sounddevice`).
  - Granular slicing / bitcrushing engine prototyping started.
- Preset “Weirdness Levels” concept outlined.

## Immediate Next Steps
1. Rebuild project zip with working code + core `.wav` files.
2. Finish ROM extraction wrapper.
3. Package voice recorder and processing modules into a prototype.
4. Gather feedback on “musical vs. weird” balance.

## Key Assets & Files
- `beatbound.py`, `record.py`, `processor.py`, `talkbox_test.py`
- `README.md`, `start_here.txt`
- Presets JSON files (`aloboi_memory.json`, `snappy_90bpm.json`)

## Major Roadblocks or Bottlenecks
- No finalized `.wav` samples.
- No `requirements.txt` yet.
- Core audio‑processing logic still placeholder.

## Top Recommended Actions
1. Add real `.wav` samples and requirements file.
2. Complete SPC extraction logic.
3. Build and test the first prototype; solicit user feedback.
4. Automate packaging into a distributable zip.

## Emotional, Strategic, or Ethical Context
Developer enthusiasm is high; emphasis on playful creativity while ensuring technical soundness. Transparent communication and user feedback loops are valued.