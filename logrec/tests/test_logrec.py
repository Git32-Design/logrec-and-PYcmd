import pytest
import pathlib
import sys
# Get parent folder path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))
import logrec

def test_log_and_tail(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    path = tmp_path / "t.log"
    with open(path, 'w', encoding="utf-8") as ll :
        ll.write("")
        logrec.log(str(ll), "first")
        logrec.log(str(ll), "second")
        logrec.log(str(ll), "third")
        res = logrec.tail(str(ll), 2)
        assert isinstance(res, list)
        assert len(res) == 2
        assert "third" in res[-1]


def test_search_by_keyword(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    path = tmp_path / "s.log"
    with open(path, 'w', encoding="utf-8") as ll :
        ll.write("")
        logrec.log(str(ll), "alpha beta")
        logrec.log(str(ll), "gamma alpha")
        found = logrec.search_by_keyword(str(ll), "alpha", case_sensitive=False)
        assert isinstance(found, list)
        assert len(found) == 2
        assert all("alpha" in line.lower() for _, line in found)
    

def test_change_and_remove(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    path = tmp_path / "c.log"
    with open(path, 'w', encoding="utf-8") as ll :
        ll.write("")
        logrec.log(str(ll), "line1")
        logrec.log(str(ll), "line2")
        # search line 0 exists
        line0 = logrec.search(str(ll), 0)
        assert "line1" in line0
        # change line 0
        logrec.change(str(ll), 0, "[2025-12-31 00:00:00] Normal log : replaced")
        assert "replaced" in logrec.search(str(ll), 0)
        # remove line 1
        logrec.rem(str(ll), 1)
        with pytest.raises(Exception):
            logrec.search(str(ll), 1)


def test_gettime_getlevel_and_logrec_class(tmp_path = f"{pathlib.Path(__file__).parent.absolute()}"):
    path = tmp_path / "g.log"
    with open(f"{tmp_path}/g.log", 'w', encoding="utf-8") as ll :
        ll.write("")
        logrec.log(str(ll), "alpha")
        logrec.warn(str(ll), "beta")
        # gettime and getlevel
        times = logrec.gettime(str(ll))
        levels = logrec.getlevel(str(ll))
        assert isinstance(times, list) and len(times) == 2
        assert isinstance(levels, list) and len(levels) == 2
        # LogRecorder class
        lr = logrec.LogRecorder(str(ll))
        assert "alpha" in lr.read()

# Requires: see ../requirements.txt for external packages used in tests/tools
