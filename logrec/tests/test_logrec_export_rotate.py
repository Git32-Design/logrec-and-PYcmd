import pytest
import pathlib
import sys
import os
# Get parent folder path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))
import logrec


def test_json_log_and_export(tmp_path):
    p = tmp_path / "j.log"
    # write JSON logs
    logrec.json_log(str(p), "message one", level='Info')
    logrec.json_log(str(p), "message two", level='Error')
    # export to jsonl (should be identical content)
    out = tmp_path / "out.jsonl"
    n = logrec.export_logs(str(p), str(out), fmt='json')
    assert n == 2
    content = out.read_text(encoding='utf-8').strip().splitlines()
    assert len(content) == 2


def test_rotate_with_compression(tmp_path):
    p = tmp_path / "r.log"
    # create a file larger than small threshold
    with open(p, 'w', encoding='utf-8') as f:
        f.write('A' * 1024)
    # rotate with small max_bytes
    res = logrec.rotate_logs(str(p), max_bytes=10, backup_count=3)
    assert res is True
    # expect r.log.1.gz exists
    gz = str(p) + ".1.gz"
    assert os.path.exists(gz)
    # compressed file has non-zero size
    assert os.path.getsize(gz) > 0

# Requires: see ../requirements.txt for external packages used in tests/tools
