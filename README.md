# RenpyGacha — RPG Character Gacha Framework

A modular, extensible Character Gacha and Inventory System engineered for **Ren'Py 8.2+**.

---

## Overview

**RenpyGacha** provides a complete RPG-style gacha pull and collection mechanic within Ren'Py. Characters are generated dynamically with distinct races, classes, randomized stats, rarity tiers, and skillsets. It can easily be integrated into any visual novel or RPG project as a minigame, recruitment system, or core mechanic.

---

## Key Features

- **Procedural Character Generation:**
  - **Races:** Human, Elf, Dwarf with thematic name pools.
  - **Classes:** Thief, Swordsman, Priest.
  - **Stat Allocation:** Strength, Agility, Intelligence, Defence, and calculated total Power.
  - **Skill Synergies:** Stealth, Sword Mastery, Healing, Archery, Magic, Defense.
- **Rarity Tier Architecture:**
  - Tiered roll odds with visual color coding (Common, Rare, Epic, Legendary).
- **Interactive UI & Visual Cards:**
  - Pull animation screen with individual character reveal cards.
  - Portrait visuals mapped per race and appearance variation.
  - Collection/inventory browsing screen.
- **Clean Object-Oriented Code:**
  - Pure Python classes extending `renpy.store.object` for persistent saving and serialization support.

---

## Directory Structure

```text
RenpyGacha/
├── game/
│   ├── gui/                 # Engine GUI assets
│   ├── images/              # Character portraits, background art, popup frames
│   ├── gui.rpy              # Base theme configuration
│   ├── options.rpy          # Game setup
│   ├── screens.rpy          # UI screens
│   └── script.rpy           # Character class logic, gacha pull mechanics, and roll scripts
├── .gitignore
└── README.md
```

---

## Installation & Usage

1. Clone or download this repository:
   ```bash
   git clone https://github.com/untuksw-pixel/RenpyGacha.git
   ```
2. Open the **Ren'Py Launcher** (version 8.2 or newer).
3. Select **RenpyGacha** from your projects and click **Launch Project**.

---

## Compatibility

- **Engine:** Ren'Py 8.2+ (Python 3)
- **Native Resolution:** 1920 × 1080 (Full HD, 16:9)
- **Platforms:** Windows, macOS, Linux
