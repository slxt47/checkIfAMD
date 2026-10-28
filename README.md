# checkIfAMD

Python-Skript, das prüft, ob eine **AMD-GPU** im System steckt, und für jede gefundene Karte
den VRAM-Verbrauch anzeigt.

```
GPU 0: AMD Radeon RX 7800 XT (0000:03:00.0)
  VRAM: 1.204 MiB von 16.368 MiB belegt (7%)
```

## Benutzen

```bash
pip install -r requirements.txt     # pyamdgpuinfo, nur Linux mit amdgpu-Treiber
python checkForAMD_GPU.py
echo $?                             # 0 = AMD-GPU da, 1 = keine, 2 = Modul fehlt
```

Der Exit-Code macht das Skript auch in Shell-Skripten nutzbar, z. B. um je nach Grafikkarte
eine andere `docker-compose.yml` zu starten:

```bash
python checkForAMD_GPU.py >/dev/null && docker compose -f linux_radeon/docker-compose.yml up -d
```

## Änderungen (Oktober 2026)

- Fehler behoben: `query_vram_usage()` liefert **Bytes**, ausgegeben wurde der Wert aber als „MB“.
- Zeigt jetzt alle AMD-GPUs mit Name, PCI-Slot und Gesamt-VRAM.
- Klare Exit-Codes und eine Meldung, falls `pyamdgpuinfo` fehlt.
