"""Coefficient de transmission de puissance entre une antenne et une puce RFID.

tau = 4 * Ra * Rc / |Za + Zc|^2   (0 <= tau <= 1)

Exemple :
    python coef_transmission.py --za 3.8+139j --zc 23.3-145j
"""
import argparse


def tau(za: complex, zc: complex) -> float:
    """Retourne le coefficient de transmission de puissance tau."""
    return 4 * za.real * zc.real / abs(za + zc) ** 2


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--za", type=complex, required=True, help="Impédance de l'antenne, ex. 3.8+139j")
    p.add_argument("--zc", type=complex, required=True, help="Impédance de la puce, ex. 23.3-145j")
    a = p.parse_args()
    t = tau(a.za, a.zc)
    print(f"Za = {a.za} ohm, Zc = {a.zc} ohm -> tau = {t:.3f}")


if __name__ == "__main__":
    main()
