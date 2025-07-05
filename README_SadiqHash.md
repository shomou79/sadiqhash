# 🔒 SadiqHash

**A simple, open-source tool to verify file and folder integrity using SHA-256.**  
Because truth begins with data that can't be silently changed.

---

## 🚀 Features

- Sign and verify individual files
- Recursively scan folders and save file hashes
- Detect any file modification, addition, or deletion
- Stores hashes in a readable JSON index file

---

## 📦 How to Use

### ▶️ Run the tool:

```bash
python3 sadiqhash.py
```

### 📋 Options:

```
1. Sign a file          → Creates a `.sig` file next to the original
2. Verify a file        → Compares file hash to its `.sig`
3. Scan a folder        → Saves all file hashes in `sadiqhash_index.json`
4. Verify a folder      → Detects any changed, missing, or added files
```

---

## 🧪 Example

```bash
Choose (1, 2, 3 or 4): 3
Enter folder path to scan: documents
✅ Hashed: file1.txt → a7f3...
✅ Hashed: report.pdf → e2c1...
🗂️ All hashes saved in documents/sadiqhash_index.json
```

Then later:

```bash
Choose (1, 2, 3 or 4): 4
Enter folder path to verify: documents
✅ OK: file1.txt
⚠️ CHANGED: report.pdf
⚠️ MISSING: old_notes.txt
```

---

## 💡 Why?

In a world full of data manipulation, **trust should never be blind.**  
This tool helps you detect silent changes in your files — from the smallest bit to complete tampering.

Use it to protect:
- Documents
- Code repositories
- Archives
- Evidence or contracts
- Any file where integrity matters

---

## ☕️ Support This Project

If you find value in SadiqHash, consider supporting its development and helping cover the cost of electricity and time.

**PayPal**  
📧 sho.mou.78@gmail.com

**Bitcoin (BTC)**  
💰 1BFcLSACrmpcPkd2hhD3yo1BMfNo7VL2Pe

**Tether (USDT - TRC20)**  
💰 TCxtsKjrEWpmBvroFvBaKSVnrxeUgQhrjD

---

## 📜 License

MIT License – You are free to use, share, and modify this software.

---

> _"Don’t trust — verify.  
Truth begins with integrity."_  
— SadiqHash
