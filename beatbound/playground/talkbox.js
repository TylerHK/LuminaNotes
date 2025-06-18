import * as Tone from 'tone';

const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const presetSelect = document.getElementById('preset');

let mic;
let filterA;
let filterB;
let analyser;
let running = false;

const presets = {
    clean: { Q: 10 },
    nasal: { Q: 20 },
    bass: { Q: 5 }
};

async function start() {
    await Tone.start();
    mic = new Tone.UserMedia();
    filterA = new Tone.BiquadFilter({ type: 'bandpass', Q: presets[presetSelect.value].Q, frequency: 600 });
    filterB = new Tone.BiquadFilter({ type: 'bandpass', Q: presets[presetSelect.value].Q, frequency: 1200 });
    analyser = new Tone.Analyser('fft', 1024);

    mic.connect(filterA);
    filterA.connect(filterB);
    filterB.connect(analyser);
    filterB.toDestination();

    await mic.open();
    running = true;
    update();
}

function stop() {
    if (mic) {
        mic.close();
        mic.disconnect();
    }
    running = false;
}

function update() {
    if (!running) return;
    const data = analyser.getValue();
    let slope = 0;
    for (let i = 1; i < data.length; i++) {
        slope += data[i] - data[i - 1];
    }
    slope /= data.length;

    const base = slope > 0 ? 800 : slope < 0 ? -800 : 0;
    filterA.frequency.value = 600 + base;
    filterB.frequency.value = 1200 + base;
    requestAnimationFrame(update);
}

startBtn.addEventListener('click', start);
stopBtn.addEventListener('click', stop);
