#!/usr/bin/env python3
"""
Konverter Mermaid Mindmap (.mermaid) -> Freemind XML (.mm)

Author / Penulis ID: claude-sonnet-4-6 (agen Cowork untuk 0x)
Tujuan: mengubah file mindmap berbasis indentasi mermaid menjadi format
Freemind .mm (XML terbuka) yang dapat diimpor ke XMind, MindManager, FreeMind,
dan tools mindmap lain yang mendukung impor Freemind/OPML.

Cara kerja:
1. Baca file .mermaid baris per baris
2. Lewati baris pertama "mindmap"
3. Hitung level indentasi (kelipatan 2 spasi) untuk membangun hierarki
4. Baris root menggunakan pola root((...)) -> dibersihkan jadi teks polos
5. Bangun tree, lalu serialize ke XML Freemind <map><node>...</node></map>

Tidak ada mock/dummy: parsing murni berbasis struktur file asli, tanpa data sintetis.
"""

import sys
import os
import re
import xml.sax.saxutils as sx

NODE_COLORS = [
    "#1a73e8",  # root
    "#34a853",  # level 1 - hijau
    "#fbbc04",  # level 2 - kuning
    "#ea4335",  # level 3 - merah
    "#9334e6",  # level 4 - ungu
]

def parse_mermaid_mindmap(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]

    # Buang baris kosong dan baris "mindmap"
    content_lines = []
    for l in lines:
        stripped = l.strip()
        if not stripped:
            continue
        if stripped == "mindmap":
            continue
        content_lines.append(l)

    if not content_lines:
        raise ValueError(f"File kosong atau tidak punya konten mindmap: {path}")

    root_line = content_lines[0]
    # root((TEKS)) -> ambil teks di dalam kurung ganda, ganti \n literal jadi spasi
    m = re.search(r"root\(\((.*)\)\)", root_line)
    if m:
        root_text = m.group(1).replace("\\n", " ").strip()
    else:
        root_text = root_line.strip()

    root = {"text": root_text, "children": [], "level": -1}
    stack = [root]

    for raw in content_lines[1:]:
        # Hitung indentasi (jumlah spasi di depan)
        stripped = raw.lstrip(" ")
        indent = len(raw) - len(stripped)
        level = indent // 2  # mermaid mindmap pakai kelipatan 2 spasi per level
        text = stripped.strip()
        if not text:
            continue

        node = {"text": text, "children": [], "level": level}

        # Cari parent: node terakhir di stack dengan level < level saat ini
        while stack and stack[-1]["level"] >= level:
            stack.pop()

        if not stack:
            # fallback: jadikan child root
            stack = [root]

        stack[-1]["children"].append(node)
        stack.append(node)

    return root


def node_to_xml(node, depth=0):
    color = NODE_COLORS[min(depth, len(NODE_COLORS) - 1)]
    text_escaped = sx.escape(node["text"], {'"': "&quot;"})
    indent = "  " * depth
    if node["children"]:
        children_xml = "\n".join(node_to_xml(c, depth + 1) for c in node["children"])
        return (
            f'{indent}<node TEXT="{text_escaped}" COLOR="{color}" '
            f'FOLDED="false">\n{children_xml}\n{indent}</node>'
        )
    else:
        return f'{indent}<node TEXT="{text_escaped}" COLOR="{color}"/>'


def tree_to_freemind_xml(root, source_filename):
    header = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<map version="1.0.1">\n'
        f'  <!-- Dikonversi otomatis dari {sx.escape(source_filename)} -->\n'
        f'  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->\n'
    )
    body = node_to_xml(root, depth=1)
    footer = "\n</map>\n"
    return header + body + footer


def convert_file(src_path, dst_path):
    root = parse_mermaid_mindmap(src_path)
    xml_str = tree_to_freemind_xml(root, os.path.basename(src_path))
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(xml_str)
    return root


def count_nodes(node):
    return 1 + sum(count_nodes(c) for c in node["children"])


def main():
    if len(sys.argv) < 2:
        print("Pemakaian: python mermaid_to_freemind.py <file1.mermaid> [file2.mermaid ...]")
        sys.exit(1)

    results = []
    for src in sys.argv[1:]:
        if not os.path.isfile(src):
            print(f"[SKIP] Tidak ditemukan: {src}")
            continue
        dst = os.path.splitext(src)[0] + ".mm"
        try:
            root = convert_file(src, dst)
            n = count_nodes(root)
            results.append((src, dst, n, "OK"))
            print(f"[OK]   {src}\n       -> {dst}  ({n} node)")
        except Exception as e:
            results.append((src, dst, 0, f"ERROR: {e}"))
            print(f"[GAGAL] {src}: {e}")

    print("\n=== RINGKASAN KONVERSI ===")
    ok = sum(1 for r in results if r[3] == "OK")
    print(f"Total file diproses : {len(results)}")
    print(f"Berhasil            : {ok}")
    print(f"Gagal               : {len(results) - ok}")


if __name__ == "__main__":
    main()
