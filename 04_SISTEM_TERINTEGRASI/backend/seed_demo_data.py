import sqlite3
from datetime import datetime, timedelta

def seed_demo_data():
    conn = sqlite3.connect('kmu_procurement.db')
    cursor = conn.cursor()

    print("Mengosongkan data lama untuk Demo...")
    tables = ['activity_log', 'kso_evaluations', 'kso_tariffs', 'kso_metrics',
              'purchase_orders', 'requisitions', 'tenders', 'vendors']
    for table in tables:
        try:
            cursor.execute(f"DELETE FROM {table}")
        except Exception:
            pass  # tabel belum ada, skip

    print("Menyuntikkan Master Data Vendor...")
    vendors = [
        ('VND-001', 'PT. Medika Sejahtera',     'Medika Sejahtera',  '987654321', 'approved', 'Jl. Sudirman 1, Balikpapan',       'admin@medika.com',      'KSO Alat Lab'),
        ('VND-002', 'PT. Reagen Nusantara',      'Reagen Nusantara',  '123456789', 'approved', 'Jl. Thamrin 2, Jakarta',           'sales@reagen.com',      'Suplier Reagen'),
        ('VND-003', 'CV. Maju Konstruksi',       'Maju Konstruksi',   '112233445', 'submitted','Jl. Gatot Subroto, Samarinda',    'info@maju.com',         'Jasa Konstruksi'),
        ('VND-004', 'PT. EH SYAM',               'EH SYAM',           '445566778', 'approved', 'Jl. Sangatta No. 12, Kutim',       'ehsyam@kso.com',        'KSO Alat Lab'),
        ('VND-005', 'PT. BEM',                   'BEM',               '556677889', 'approved', 'Jl. Bontang Raya No. 5, Bontang', 'bem@kso.com',           'KSO Alat Lab'),
        ('VND-006', 'PT. Farma Andalan',         'Farma Andalan',     '667788990', 'approved', 'Jl. DI Panjaitan No. 88, Balikpapan','farma@andalan.com',  'Suplier Obat'),
        ('VND-007', 'PT. Tekno Medis Utama',     'Tekno Medis',       '778899001', 'submitted','Jl. Mulawarman 44, Samarinda',    'tekno@medis.com',       'Alkes Investasi'),
    ]
    for v in vendors:
        cursor.execute('''
            INSERT INTO vendors (vendor_id, company_name, company_name_short, npwp, vendor_status,
                                 address_street, email, vendor_category, registration_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (*v, datetime.now()))

    print("Menyuntikkan Data Requisition (Skenario Approval Berjenjang)...")
    today = datetime.now()
    reqs = [
        # (req_number, req_type, title, desc, amount, status, sbu, created_at)
        ('REQ-2026-001', 'PP',   'Pembelian Reagen Kimia Klinik',   'Reagen Kimia Klinik Batch Q2',    9500000,   'pending_manager',    'SBU-LAB',      today - timedelta(days=12)),
        ('REQ-2026-002', 'PP',   'Pengadaan UPS Ruang Server',      'UPS 10 KVA Ruang Server IT',      35000000,  'pending_gm',         'SBU-IT',       today - timedelta(days=8)),
        ('REQ-2026-003', 'SPPJ', 'Jasa Pemeliharaan AC Central',    'Pemeliharaan AC 6 unit selama 1 tahun', 150000000,'pending_dir_ops','SBU-TEKNISI',  today - timedelta(days=5)),
        ('REQ-2026-004', 'PP',   'Reagen KSO Hematologi (Rutin)',   'Reagen Hematologi Sysmex',       22000000,  'approved_final',     'SBU-LAB',      today - timedelta(days=15)),
        ('REQ-2026-005', 'SPPJ', 'Jasa Outsourcing Security',       'Security 6 orang x 12 bulan',   480000000,  'pending_dir_utama',  'SBU-UMUM',     today - timedelta(days=3)),
        ('REQ-2026-006', 'PP',   'ATK dan Alat Tulis Kantor',       'ATK Bulanan Q2 2026',             4500000,   'approved_final',     'SBU-SEKRETARIAT', today - timedelta(days=2)),
        ('REQ-2026-007', 'PP',   'Pengadaan Tabung Reaksi (BMHP)',  'Tabung 5ml 10.000 pcs',           8000000,   'pending_kasie',      'SBU-LAB',      today - timedelta(days=1)),
    ]
    for r in reqs:
        cursor.execute('''
            INSERT INTO requisitions (req_number, req_type, title, description, total_amount, status, sbu_name, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', r)

    print("Menyuntikkan Data Purchase Order (PO)...")
    pos = [
        ('PO-2026-001', 4, 'VND-001', 22000000, 'issued'),
        ('PO-2026-002', 1, 'VND-001', 50000000, 'issued'),
        ('PO-2026-003', 2, 'VND-002', 15000000, 'issued'),
        ('PO-2026-004', 6, 'VND-006', 4500000,  'issued'),
    ]
    for p in pos:
        cursor.execute('''
            INSERT INTO purchase_orders (po_number, req_id, vendor_id, total_amount, status)
            VALUES (?, ?, ?, ?, ?)
        ''', p)

    print("Menyuntikkan Data Evaluasi KSO 7-Dimensi (Fase 8)...")

    # Helper: hitung weighted final score dari 7 dimensi
    def calc_final(d, q, r, p, c, f, rel):
        return round(d*0.20 + q*0.20 + r*0.15 + p*0.15 + c*0.15 + f*0.10 + rel*0.05, 2)

    evaluations = [
        # VND-001 PO-2026-001: Fair, selesai baik
        {
            'vendor_id': 'VND-001', 'po_number': 'PO-2026-001', 'period_month': '2026-05',
            'vendor_score_delivery': 90, 'vendor_score_quality': 95, 'vendor_score_response': 90,
            'vendor_remarks': 'Barang dikirim sesuai jadwal H+1, packing aman.',
            'qc_evaluator_name': 'Siska (QC Lab)',
            'qc_score_delivery': 85, 'qc_score_quality': 90, 'qc_score_response': 85,
            'qc_remarks': 'Diterima baik, no defect.',
            'score_pricing': 80, 'score_compliance': 90, 'score_financial_health': 85, 'score_relationship': 88,
            'dim4_notes': 'Harga kompetitif, invoice akurat 100%, bayar tepat waktu.',
            'deviation_flag': 0, 'status': 'completed',
            'evaluation_date': today - timedelta(days=2),
        },
        # VND-001 PO-2026-002: DISPUTE - vendor claim tinggi, QC rendah
        {
            'vendor_id': 'VND-001', 'po_number': 'PO-2026-002', 'period_month': '2026-05',
            'vendor_score_delivery': 100, 'vendor_score_quality': 100, 'vendor_score_response': 100,
            'vendor_remarks': 'Instalasi PCR selesai sempurna, mesin berfungsi normal.',
            'qc_evaluator_name': 'Siska (QC Lab)',
            'qc_score_delivery': 50, 'qc_score_quality': 60, 'qc_score_response': 40,
            'qc_remarks': 'Mesin error di hari ke-3, teknisi baru hadir 2 hari kemudian.',
            'score_pricing': 75, 'score_compliance': 70, 'score_financial_health': 80, 'score_relationship': 60,
            'dim4_notes': 'Respons komplain lambat, perlu eskalasi ke Manager.',
            'deviation_flag': 1, 'status': 'disputed',
            'evaluation_date': today - timedelta(days=1),
        },
        # VND-002 PO-2026-003: Penalti mangkir (vendor tidak lapor)
        {
            'vendor_id': 'VND-002', 'po_number': 'PO-2026-003', 'period_month': '2026-05',
            'vendor_score_delivery': None, 'vendor_score_quality': None, 'vendor_score_response': None,
            'vendor_remarks': None,
            'qc_evaluator_name': 'Anton (Logistik)',
            'qc_score_delivery': 70, 'qc_score_quality': 80, 'qc_score_response': 70,
            'qc_remarks': 'Reagen datang tapi vendor tidak update BAPB sama sekali.',
            'score_pricing': 85, 'score_compliance': 55, 'score_financial_health': 75, 'score_relationship': 65,
            'dim4_notes': 'Compliance rendah: tidak mengirim dokumen BAPB dan COA sesuai SPO.',
            'deviation_flag': 1, 'status': 'completed_penalty',
            'evaluation_date': today,
        },
        # VND-004 EH SYAM: Evaluasi reguler bulan ini
        {
            'vendor_id': 'VND-004', 'po_number': 'PO-2026-001', 'period_month': '2026-06',
            'vendor_score_delivery': 92, 'vendor_score_quality': 88, 'vendor_score_response': 85,
            'vendor_remarks': 'Volume poli melebihi target, ready stok selalu terpenuhi.',
            'qc_evaluator_name': 'Budi (Manajer Pengadaan)',
            'qc_score_delivery': 90, 'qc_score_quality': 86, 'qc_score_response': 83,
            'qc_remarks': 'Reagen stabil, kalibrasi alat terjadwal dengan baik.',
            'score_pricing': 78, 'score_compliance': 88, 'score_financial_health': 82, 'score_relationship': 85,
            'dim4_notes': 'Harga sedikit di atas pasar tapi konsisten, invoice akurat.',
            'deviation_flag': 0, 'status': 'completed',
            'evaluation_date': today - timedelta(days=3),
        },
        # VND-005 BEM: Evaluasi reguler bulan ini
        {
            'vendor_id': 'VND-005', 'po_number': 'PO-2026-002', 'period_month': '2026-06',
            'vendor_score_delivery': 88, 'vendor_score_quality': 84, 'vendor_score_response': 80,
            'vendor_remarks': 'Pengiriman tepat waktu, ada 1 item yang perlu reorder.',
            'qc_evaluator_name': 'Budi (Manajer Pengadaan)',
            'qc_score_delivery': 85, 'qc_score_quality': 82, 'qc_score_response': 78,
            'qc_remarks': 'Performa stabil, ada keterlambatan minor reagen MCU.',
            'score_pricing': 88, 'score_compliance': 85, 'score_financial_health': 80, 'score_relationship': 80,
            'dim4_notes': 'Harga kompetitif, diskon 1.5% early payment, invoice baik.',
            'deviation_flag': 0, 'status': 'completed',
            'evaluation_date': today - timedelta(days=3),
        },
    ]

    for e in evaluations:
        # Compute final score
        d = e['qc_score_delivery'] or 0
        q = e['qc_score_quality'] or 0
        r = e['qc_score_response'] or 0
        p = e['score_pricing'] or 0
        c = e['score_compliance'] or 0
        f = e['score_financial_health'] or 0
        rel = e['score_relationship'] or 0
        if e['status'] == 'completed_penalty':
            final = 0.0
        else:
            final = calc_final(d, q, r, p, c, f, rel)

        cursor.execute('''
            INSERT INTO kso_evaluations (
                vendor_id, po_number, period_month,
                vendor_score_delivery, vendor_score_quality, vendor_score_response, vendor_remarks,
                qc_evaluator_name, qc_score_delivery, qc_score_quality, qc_score_response, qc_remarks,
                score_pricing, score_compliance, score_financial_health, score_relationship, dim4_notes,
                final_score, deviation_flag, status, evaluation_date
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            e['vendor_id'], e['po_number'], e['period_month'],
            e['vendor_score_delivery'], e['vendor_score_quality'], e['vendor_score_response'], e['vendor_remarks'],
            e['qc_evaluator_name'], e['qc_score_delivery'], e['qc_score_quality'], e['qc_score_response'], e['qc_remarks'],
            e['score_pricing'], e['score_compliance'], e['score_financial_health'], e['score_relationship'], e['dim4_notes'],
            final, e['deviation_flag'], e['status'], e['evaluation_date'],
        ))

    print("Menyuntikkan Data Finansial KSO (Fase 5 - LabCore)...")
    metrics = [
        ('VND-004', 62540000, 3695, 2212, 1483),
        ('VND-005', 67659000, 3712, 2195, 1517),
    ]
    for m in metrics:
        cursor.execute('''
            INSERT INTO kso_metrics (vendor_id, total_revenue, total_volume, poli_volume, mcu_volume)
            VALUES (?, ?, ?, ?, ?)
        ''', m)

    tariffs = [
        ('VND-004', 'Gamma GT',               28000),
        ('VND-004', 'Ureum (Darah/Urine)',    23000),
        ('VND-004', 'Darah Rutin (Automatic)',37500),
        ('VND-004', 'Rhesus Factor',           7000),
        ('VND-004', 'TSH (Thyroid)',           95000),
        ('VND-004', 'HbA1c',                  98000),
        ('VND-005', 'Gamma GT',               26000),
        ('VND-005', 'Ureum (Darah/Urine)',    21000),
        ('VND-005', 'Darah Rutin (Automatic)',36000),
        ('VND-005', 'Rhesus Factor',           8000),
        ('VND-005', 'TSH (Thyroid)',           92000),
        ('VND-005', 'HbA1c',                  95000),
    ]
    for t in tariffs:
        cursor.execute('INSERT INTO kso_tariffs (vendor_id, test_name, price) VALUES (?,?,?)', t)

    print("Menyuntikkan Data Tender (Fase 4 - Manajemen Tender)...")
    tenders = [
        ('TND-2026-001', 'Pengadaan Reagen Hematologi Sysmex XN-550',   'alkes',    'Reagen untuk mesin Sysmex XN-550 di lab utama',                      450000000, '2026-06-25', '2026-07-15', 'published', 'Kasie Pengadaan Barang'),
        ('TND-2026-002', 'Pengadaan UPS 10KVA Ruang Server',             'investasi','UPS Rack Mount APC Smart 10KVA 3-Phase, warranty 3 tahun',           280000000, '2026-06-30', '2026-07-30', 'published', 'Kasie Pengadaan Barang'),
        ('TND-2026-003', 'Jasa Pemeliharaan Genset Diesel 500 KVA',      'jasa',     'Service berkala 6 bulan selama 2 tahun oleh teknisi bersertifikat',   120000000, '2026-06-20', '2026-08-01', 'closed',    'Kasie Pengadaan Jasa'),
        ('TND-2026-004', 'Pengadaan Alat USG 2D Color Doppler',          'alkes',    'USG portable 2D/3D Color Doppler untuk poli kebidanan',               890000000, '2026-07-10', '2026-09-01', 'draft',     'Kasie Pengadaan Barang'),
        ('TND-2026-005', 'Jasa Outsourcing Tenaga Security 24 Jam',      'jasa',     '6 personil security shift 3x8 jam, 365 hari',                         480000000, '2026-06-15', '2026-07-01', 'awarded',   'Kasie Pengadaan Jasa'),
    ]
    for t in tenders:
        cursor.execute('''
            INSERT INTO tenders (tender_number, title, category, description, budget_max,
                                 bid_closing_date, expected_delivery_date, status, created_by)
            VALUES (?,?,?,?,?,?,?,?,?)
        ''', t)

    print("Menyuntikkan Data Jadwal Pembayaran Keuangan (payment_schedules)...")
    schedules = [
        # (po_number, project_title, vendor_name, negotiated_amount, dp_percentage, dp_status, dp_planned_date, dp_realized_date, remaining_status, remaining_planned_date, remaining_realized_date)
        ('PO-2026-001', 'Reagen KSO Hematologi (Rutin)', 'PT. Medika Sejahtera', 22000000, 30.0, 'Lunas', '2026-06-10', '2026-06-09', 'Belum Dibayar', '2026-07-10', None),
        ('PO-2026-002', 'Pembelian Reagen Kimia Klinik', 'PT. Medika Sejahtera', 50000000, 20.0, 'Belum Dibayar', None, None, 'Belum Dibayar', None, None),
        ('PO-2026-003', 'Pengadaan UPS Ruang Server', 'PT. Reagen Nusantara', 15000000, 0.0, 'Tidak Ada', None, None, 'Belum Dibayar', '2026-06-25', None),
        ('PO-2026-004', 'ATK dan Alat Tulis Kantor', 'PT. Farma Andalan', 4500000, 0.0, 'Tidak Ada', None, None, 'Lunas', '2026-06-05', '2026-06-04'),
    ]
    for s in schedules:
        cursor.execute('''
            INSERT INTO payment_schedules (
                po_number, project_title, vendor_name, negotiated_amount, dp_percentage,
                dp_status, dp_planned_date, dp_realized_date, remaining_status, remaining_planned_date, remaining_realized_date
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
        ''', s)

    print("Menyuntikkan Data Rencana Belanja Realisasi Investasi (investment_spending_plans)...")
    spending_plans = [
        # (month_target, project_title, category, sbu_name, negotiated_price, installation_fee, testing_fee, tax_amount, shipping_cost, total_amount, dp_pct, dp_amount)
        ('Agt 2026', 'Pengadaan Reagen Kimia Klinik Semester 2', 'Barang Medis', 'RS PKT Bontang', 1250000000, 0, 10000000, 138600000, 5000000, 1403600000, 20.0, 250000000),
        ('Nov 2026', 'Penyediaan Jasa Keamanan (Security) 2027', 'Jasa', 'Seluruh SBU', 3100000000, 0, 0, 341000000, 0, 3441000000, 0.0, 0),
    ]
    for sp in spending_plans:
        cursor.execute('''
            INSERT INTO investment_spending_plans (
                month_target, project_title, category, sbu_name, negotiated_price,
                installation_fee, testing_fee, tax_amount, shipping_cost, total_amount, dp_pct, dp_amount
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        ''', sp)

    conn.commit()
    conn.close()
    print("\n=== SELESAI! Database siap untuk demo Senin. ===")
    print("Ringkasan:")
    print(f"  - {len(vendors)} Vendor")
    print(f"  - {len(reqs)} Requisition (berbagai level approval)")
    print(f"  - {len(pos)} Purchase Order")
    print(f"  - {len(evaluations)} Evaluasi KSO (7 Dimensi)")
    print(f"  - {len(tenders)} Tender aktif")


if __name__ == "__main__":
    seed_demo_data()
