"""Sorting algorithms written from scratch. Each sorts a list of (key, payload) tuples in place by key,
counting comparisons and swaps (a 'swap' is a swap, shift or element move/write)."""
import threading
import time


class Cancelled(Exception):
    pass


class Stats:
    __slots__ = ("comparisons", "swaps")

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0


def _check(stop):
    if stop.is_set():
        raise Cancelled()


def bubble_sort(a, st, stop):
    n, c, s = len(a), 0, 0
    try:
        for i in range(n - 1):
            _check(stop)
            swapped = False
            for j in range(n - 1 - i):
                c += 1
                if a[j][0] > a[j + 1][0]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    s += 1
                    swapped = True
            if not swapped:
                break
    finally:
        st.comparisons += c
        st.swaps += s




def insertion_sort(a, st, stop):
    c = s = 0
    try:
        for i in range(1, len(a)):
            if i % 256 == 0:
                _check(stop)
            x, j = a[i], i - 1
            while j >= 0:
                c += 1
                if a[j][0] > x[0]:
                    a[j + 1] = a[j]
                    s += 1
                    j -= 1
                else:
                    break
            a[j + 1] = x
    finally:
        st.comparisons += c
        st.swaps += s


def _merge(a, lo, mid, hi, st):
    """Merge a[lo:mid] and a[mid:hi] (stable)."""
    left, right = a[lo:mid], a[mid:hi]
    i = j = 0
    k, c, s = lo, 0, 0
    while i < len(left) and j < len(right):
        c += 1
        if right[j][0] < left[i][0]:
            a[k] = right[j]
            j += 1
        else:
            a[k] = left[i]
            i += 1
        k += 1
        s += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
        s += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
        s += 1
    st.comparisons += c
    st.swaps += s


def merge_sort(a, st, stop):
    def rec(lo, hi):
        if hi - lo < 2:
            return
        _check(stop)
        mid = (lo + hi) // 2
        rec(lo, mid)
        rec(mid, hi)
        _merge(a, lo, mid, hi, st)
    rec(0, len(a))


def quick_sort(a, st, stop):
    """Iterative 3-way quicksort (safe on sorted input and on columns full of duplicates)."""
    c = s = 0
    stack = [(0, len(a) - 1)]
    try:
        while stack:
            _check(stop)
            lo, hi = stack.pop()
            if lo >= hi:
                continue
            pivot = a[(lo + hi) // 2][0]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                k = a[i][0]
                c += 1
                if k < pivot:
                    a[lt], a[i] = a[i], a[lt]
                    lt += 1
                    i += 1
                    s += 1
                else:
                    c += 1
                    if k > pivot:
                        a[i], a[gt] = a[gt], a[i]
                        gt -= 1
                        s += 1
                    else:
                        i += 1
            stack.append((lo, lt - 1))
            stack.append((gt + 1, hi))
    finally:
        st.comparisons += c
        st.swaps += s












# name -> (function, average, worst, stable)
ALGORITHMS = {
    "Bubble Sort": (bubble_sort, "O(n²)", "O(n²)", True),
    "Insertion Sort": (insertion_sort, "O(n²)", "O(n²)", True),
    "Merge Sort": (merge_sort, "O(n log n)", "O(n log n)", True),
    "Quick Sort": (quick_sort, "O(n log n)", "O(n²)", False),
}
QUADRATIC = {"Bubble Sort", "Insertion Sort"}


def describe(name):
    _, avg, worst, stable = ALGORITHMS[name]
    return f"Average {avg}, worst {worst}, {'stable' if stable else 'not stable'}"


def run_sort(name, items, stop=None):
    """Sort a copy of items. Returns (sorted_items, Stats, milliseconds)."""
    stop = stop or threading.Event()
    data, st = list(items), Stats()
    t0 = time.perf_counter()
    ALGORITHMS[name][0](data, st, stop)
    return data, st, (time.perf_counter() - t0) * 1000


# ---------------------------------------------------------------- keys
INF = float("inf")


def make_key(rec, col, kind, desc=False):
    """Comparable key for one column. Missing values always sort last. Descending is done by inverting
    the key, so every algorithm (stable or not) works in one pass and multi-level keys can be tuples."""
    v = rec.get(col)
    if kind == "num":
        if v is None:
            return INF
        return -v if desc else v
    s = (v or "").lower()
    if not s:
        return (10 ** 9,) if desc else "\U0010ffff"
    return tuple(-ord(ch) for ch in s) + (1,) if desc else s


def build_items(records, indices, specs, kinds):
    """specs: [(column, desc), ...] -> [(key, index)]; one spec gives plain keys, several give tuple keys."""
    if len(specs) == 1:
        col, desc = specs[0]
        return [(make_key(records[i], col, kinds[col], desc), i) for i in indices]
    return [(tuple(make_key(records[i], c, kinds[c], d) for c, d in specs), i) for i in indices]
