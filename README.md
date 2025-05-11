# 🚀 Galactic Cargo Management System (GCMS)
This project implements a space-efficient and time-optimized cargo management system for interstellar shipments, developed as part of COL106 Assignment 2. It uses advanced bin packing algorithms (Largest Fit and Compact Fit) to efficiently assign cargo to bins based on size and special handling requirements (color-coded).
## 📦 Problem Overview
Each cargo item has:
- A size, unique ID, and a color (Red, Blue, Yellow, or Green).
Each bin has:
- A capacity and a unique ID.

Color-Based Handling Rules:
- 🔵 Blue (Compact Fit, Least ID)
- 🟡 Yellow (Compact Fit, Greatest ID)
- 🔴 Red (Largest Fit, Least ID)
- 🟢 Green (Largest Fit, Greatest ID)
The algorithm chooses the best-fitting bin for a given cargo, following these rules.
## 🛠 Features
- Add/remove cargo bins and objects.
- Automatically assigns cargo to bins using color-specific fit algorithms.
- Retrieves cargo and bin information.
- Ensures logarithmic time complexity using AVL Trees (custom implementation).
- Prevents object collisions and overflows by raising appropriate exceptions.

## 🧱 Project Structure
> gcms.py          # Main system interface
> 
> bin.py           # Bin data structure and logic
> 
> object.py        # Cargo object representation
> 
> avl.py           # Custom AVL Tree implementation
> 
> node.py          # AVL Tree node structure
> 
> exceptions.py    # Contains NoBinFoundException (do not modify)
> 
> main.py          # Sample test runner for debugging

## ⚠ Constraints
- ❌ No use of Python dictionaries or sets.
- 🧠 Must use AVL Trees for efficient insertion and search.
- ⏱ Time Complexity: O(log n + log m) for all core operations.
- 📦 Space Complexity: O(n + m).
