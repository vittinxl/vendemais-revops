
#!/usr/bin/env python3
"""Limpeza de registros vencidos em um JSON local de demonstração."""

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def cleanup_records(file_path, retention_days=90, apply=False):
    """Identifica registros antigos e os remove somente com apply=True."""
    path = Path(file_path)

    if retention_days < 1:
        raise ValueError("O prazo de retenção deve ser de pelo menos 1 dia.")

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    records = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(records, list):
        raise ValueError("O JSON deve conter uma lista de registros.")

    cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)
    kept = []
    expired = []

    for record in records:
        if not isinstance(record, dict) or "enriched_at" not in record:
            kept.append(record)
            continue

        try:
            timestamp = datetime.fromisoformat(
                record["enriched_at"].replace("Z", "+00:00")
            )
            if timestamp.tzinfo is None:
                timestamp = timestamp.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError, AttributeError):
            kept.append(record)
            continue

        if timestamp < cutoff:
            expired.append(record)
        else:
            kept.append(record)

    print(f"Registros analisados: {len(records)}")
    print(f"Registros vencidos: {len(expired)}")
    print(f"Prazo de retenção: {retention_days} dias")

    if apply:
        path.write_text(
            json.dumps(kept, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Exclusão concluída. Registros restantes: {len(kept)}")
    else:
        print("Simulação: nenhum dado foi alterado.")
        print("Para aplicar a exclusão, execute novamente com --apply.")

    return len(expired)


def main():
    parser = argparse.ArgumentParser(
        description="Limpeza de registros vencidos em JSON local."
    )
    parser.add_argument("arquivo", help="Caminho do arquivo JSON")
    parser.add_argument("--dias", type=int, default=90, help="Retenção em dias")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica a exclusão; sem esta opção, apenas simula",
    )
    args = parser.parse_args()

    cleanup_records(args.arquivo, args.dias, args.apply)


if __name__ == "__main__":
    main()
