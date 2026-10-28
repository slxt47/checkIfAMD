"""Prüft, ob eine AMD-GPU vorhanden ist, und zeigt den VRAM-Verbrauch.

Exit-Code 0 = mindestens eine AMD-GPU gefunden, 1 = keine gefunden, 2 = Modul fehlt.
Nur Linux (nutzt den amdgpu-Treiber über pyamdgpuinfo).
"""
import sys

try:
    import pyamdgpuinfo
except ImportError:
    print("Modul fehlt: pip install pyamdgpuinfo  (nur Linux mit amdgpu-Treiber)")
    sys.exit(2)


def mib(nbytes: int) -> str:
    return f"{nbytes / 1024 ** 2:,.0f} MiB".replace(",", ".")


def main() -> int:
    anzahl = pyamdgpuinfo.detect_gpus()
    if anzahl == 0:
        print("Keine AMD-GPU gefunden.")
        return 1

    for i in range(anzahl):
        gpu = pyamdgpuinfo.get_gpu(i)
        name = gpu.name or "AMD-GPU"
        belegt = gpu.query_vram_usage()               # liefert Bytes
        gesamt = gpu.memory_info["vram_size"]
        print(f"GPU {i}: {name} ({gpu.pci_slot})")
        print(f"  VRAM: {mib(belegt)} von {mib(gesamt)} belegt ({belegt / gesamt:.0%})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
