import pytest
import pathlib
import sys
# Get parent folder path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))
import logrec

def test_log_and_tail(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    with open(f"{tmp_path}/t.log") as ll :
        p = ll
    p.write("")
    # add lines
    logrec.log(str(p), "first")
    logrec.log(str(p), "second")
    logrec.log(str(p), "third")
    res = logrec.tail(str(p), 2)
    assert isinstance(res, list)
    assert len(res) == 2
    assert "third" in res[-1]


def test_search_by_keyword(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    with open(f"{tmp_path}/s.log") as ll :
        p = ll
    p.write("")
    logrec.log(str(p), "alpha beta")
    logrec.log(str(p), "gamma alpha")
    found = logrec.search_by_keyword(str(p), "alpha", case_sensitive=False)
    assert isinstance(found, list)
    assert len(found) == 2
    assert all("alpha" in line.lower() for _, line in found)

def test_change_and_remove(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    with open(f"{tmp_path}/c.log") as ll :
        p = ll
    p.write("")
    logrec.log(str(p), "line1")
    logrec.log(str(p), "line2")
    # search line 0 exists
    line0 = logrec.search(str(p), 0)
    assert "line1" in line0
    # change line 0
    logrec.change(str(p), 0, "[2025-12-31 00:00:00] Normal log : replaced")
    assert "replaced" in logrec.search(str(p), 0)
    # remove line 1
    logrec.rem(str(p), 1)
    with pytest.raises(Exception):
        logrec.search(str(p), 1)


def test_gettime_getlevel_and_logrec_class(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    with open(f"{tmp_path}/g.log") as ll :
        p = ll
    p.write("")
    logrec.log(str(p), "alpha")
    logrec.warn(str(p), "beta")
    # gettime and getlevel
    times = logrec.gettime(str(p))
    levels = logrec.getlevel(str(p))
    assert isinstance(times, list) and len(times) == 2
    assert isinstance(levels, list) and len(levels) == 2
    # LogRecorder class
    lr = logrec.LogRecorder(str(p))
    assert "alpha" in lr.read()

# Requires: see ../requirements.txt for external packages used in tests/tools
