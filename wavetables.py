import subprocess
import wave
from pathlib import Path

out = Path("AKWF--Akai-MPC-Wavetables")
out.mkdir(exist_ok=True)
for d in sorted(Path("AKWF--Akai-MPC").iterdir()):
    wavs = list(d.glob("*.wav"))
    nwav = len(wavs)
    dout = out / d.name
    dout.mkdir(exist_ok=True)

    subprocess.run(["sox", f"{str(d)}/*wav", f"{out}/{d.name}/{d.name}.wav"])

    wout_name = f"{dout}/{d.name}.wav"
    with wave.open(wout_name, "rb") as wout:
        p = wout.getparams()
        print(wout_name, p)
    #        print(p.nframes / 600)

    (dout / "format.json").write_text(
        """{{
    "formatInfo": {{
        "numSamplesPerSingleCycle": 600,
        "numSingleCycles": {nwav}
    }}
}}
""".format(nwav=nwav)
    )
