
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from retention_cleanup import cleanup_records


class RetentionCleanupTests(unittest.TestCase):
    def test_simulation_does_not_change_file(self):
        old_date = (datetime.now(timezone.utc) - timedelta(days=120))
        old_date = old_date.isoformat()

        recent_date = datetime.now(timezone.utc).isoformat()

        records = [
            {"deal_id": "OLD", "enriched_at": old_date},
            {"deal_id": "NEW", "enriched_at": recent_date},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "records.json"
            original = json.dumps(records)
            path.write_text(original, encoding="utf-8")

            expired = cleanup_records(path, retention_days=90, apply=False)

            self.assertEqual(expired, 1)
            self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_apply_removes_old_records(self):
        old_date = (datetime.now(timezone.utc) - timedelta(days=120))
        old_date = old_date.isoformat()

        recent_date = datetime.now(timezone.utc).isoformat()

        records = [
            {"deal_id": "OLD", "enriched_at": old_date},
            {"deal_id": "NEW", "enriched_at": recent_date},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "records.json"
            path.write_text(json.dumps(records), encoding="utf-8")

            expired = cleanup_records(path, retention_days=90, apply=True)
            remaining = json.loads(path.read_text(encoding="utf-8"))

            self.assertEqual(expired, 1)
            self.assertEqual(len(remaining), 1)
            self.assertEqual(remaining[0]["deal_id"], "NEW")


if __name__ == "__main__":
    unittest.main()
