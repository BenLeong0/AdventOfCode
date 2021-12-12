from typing import List, Set


test_input1: List[Set[str]] = [
    ("start", "A"),
    ("start", "b"),
    ("A", "c"),
    ("A", "b"),
    ("b", "d"),
    ("A", "end"),
    ("b", "end"),
]

test_input2: List[Set[str]] = [
    ("dc", "end"),
    ("HN", "start"),
    ("start", "kj"),
    ("dc", "start"),
    ("dc", "HN"),
    ("LN", "dc"),
    ("HN", "end"),
    ("kj", "sa"),
    ("kj", "HN"),
    ("kj", "dc"),
]

test_input3: List[Set[str]] = [
    ("fs", "end"),
    ("he", "DX"),
    ("fs", "he"),
    ("start", "DX"),
    ("pj", "DX"),
    ("end", "zg"),
    ("zg", "sl"),
    ("zg", "pj"),
    ("pj", "he"),
    ("RW", "he"),
    ("fs", "DX"),
    ("pj", "RW"),
    ("zg", "RW"),
    ("start", "pj"),
    ("he", "WI"),
    ("zg", "he"),
    ("pj", "fs"),
    ("start", "RW"),
]

full_input: List[Set[str]] = [
    ("start","YY"),
    ("av","rz"),
    ("rz","VH"),
    ("fh","av"),
    ("end","fh"),
    ("sk","gp"),
    ("ae","av"),
    ("YY","gp"),
    ("end","VH"),
    ("CF","qz"),
    ("qz","end"),
    ("qz","VG"),
    ("start","gp"),
    ("VG","sk"),
    ("rz","YY"),
    ("VH","sk"),
    ("rz","gp"),
    ("VH","av"),
    ("VH","fh"),
    ("sk","rz"),
    ("YY","sk"),
    ("av","gp"),
    ("rz","qz"),
    ("VG","start"),
    ("sk","fh"),
    ("VG","av"),
]
