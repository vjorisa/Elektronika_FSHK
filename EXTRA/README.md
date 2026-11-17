# Analiza e Zerit perme Transformimit Fourier (FFT)

Ky projekt permban nje skript ne Python per kryerjen e Transformimit te Shpejte Fourier (FFT) mbi skedare audio, me qellim krahasimin dhe vizualizimin e frekuencave spektrale te zerit per disa persona te ndryshem.

## Permbajtja e Projektit (brenda dosjes EXTRA)
- `main.py` – Kodi kryesor qe ngarkon audio-skedaret, llogarit FFT-ne dhe vizualizon spektrin e frekuencave.
- `requirements.txt` – Lista e librarive te nevojshme per ekzekutimin e projektit.
- `krahasimi_fourier.png` – Grafiku i gjeneruar qe tregon krahasimin e magnitudes ne funksion te frekuences (Hz).
- `personi1.wav`, `personi2.wav`, `personi3.wav` – Skedaret e zerit te perdorur per analize.

## Perdorimi i Librarive
Projekti mbeshtetet ne librarite kryesore te shkences se te dhenave dhe perpunimit te sinjaleve ne Python:
- **NumPy**: Per llogaritjet numerike dhe strukturimin e vargjeve te FFT-se.
- **Librosa**: Per ngarkimin dhe leximin e sigurt te skedareve audio.
- **Matplotlib**: Per vizualizimin e spektrit te frekuencave ne grafike te lexueshem.

## Ekzekutimi
1. Sigurohu qe i ke te instaluara librarite e duhura:
   ```bash
   pip install -r requirements.txt
