# 🛡️ CryptoMacro Sentinel

**Decentralized Macro Risk Oracle for Crypto Markets — Built on GenLayer**

[![GenLayer](https://img.shields.io/badge/Built%20on-GenLayer-orange)](https://www.genlayer.com/)
[![Python](https://img.shields.io/badge/Language-Python-blue)](https://docs.genlayer.com/)
[![Testnet](https://img.shields.io/badge/Network-Testnet%20Bradbury-green)](https://studio.genlayer.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## Overview

CryptoMacro Sentinel is an **Intelligent Contract** that acts as a decentralized macro-economic risk oracle for crypto traders. It leverages GenLayer's native web access and AI consensus to fetch real-world macro data and produce **on-chain, AI-verified risk scores** with directional BTC bias.

Traditional crypto trading tools rely on centralized APIs, single-source data feeds, and off-chain analysis. CryptoMacro Sentinel brings macro intelligence **fully on-chain** — trustless, decentralized, and composable.

### Why GenLayer?

This project is **impossible on any other blockchain**. It simultaneously requires:

- 🌐 **Native web access** — fetching live market data without oracle dependencies
- 🧠 **Natural language processing** — interpreting financial news and macro signals
- 🤝 **Non-deterministic consensus** — multiple AI models agreeing on subjective analysis

Only GenLayer's Intelligent Contracts enable all three.

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                   CryptoMacro Sentinel                   │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  📡 DATA LAYER (gl.get_webpage)                           │
│  ├── Crypto Fear & Greed Index                            │
│  ├── Market News Headlines                                │
│  ├── Oil / Energy Prices                                  │
│  └── Custom Event Search                                  │
│                                                           │
│  🧠 AI ANALYSIS LAYER (gl.exec_prompt)                    │
│  ├── Macro transmission chain reasoning                   │
│  │   (Event → Inflation → Fed → Liquidity → Crypto)      │
│  ├── Risk scoring (0-100 scale)                           │
│  ├── BTC directional bias classification                  │
│  └── Key factor extraction                                │
│                                                           │
│  ⚖️ CONSENSUS LAYER (Optimistic Democracy)                │
│  ├── Multi-validator verification (diverse LLMs)          │
│  ├── Comparative equivalence principle                    │
│  └── Appeal mechanism for disputed scores                 │
│                                                           │
│  💾 STATE LAYER (On-chain)                                │
│  ├── Current risk score + analysis                        │
│  ├── Historical scores (last 50 updates)                  │
│  ├── Trend computation                                    │
│  └── Alert subscriber registry                            │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Macro Transmission Chain Framework

The AI doesn't just report data — it reasons about **causal mechanisms**:

```
Oil Price Spike → Inflation Pressure → Fed Policy Constraint → Liquidity Squeeze → Crypto Drawdown
         or
Geopolitical De-escalation → Oil Drops → Inflation Eases → Fed Dovish → Liquidity Opens → Crypto Rally
```

This framework ensures every risk assessment traces a clear path from macro event to crypto impact.

---

## Contract Functions

### Write Functions

| Function | Description |
|----------|-------------|
| `scan_macro_environment()` | Full macro scan from 3+ live data sources. Produces risk score, BTC bias, key factors, and narrative analysis. |
| `scan_specific_event(query)` | Targeted scan for a specific event. Example: `"Fed rate decision"` or `"Strait of Hormuz oil crisis"` |
| `subscribe_alerts()` | Subscribe your address to risk change alerts |
| `unsubscribe_alerts()` | Unsubscribe from alerts |

### View Functions

| Function | Returns |
|----------|---------|
| `get_current_risk()` | `{risk_score, btc_bias, analysis, timestamp, total_updates}` |
| `get_risk_history()` | Array of historical risk entries (last 50) |
| `get_risk_trend()` | `{trend: IMPROVING/STABLE/DETERIORATING, current, average_recent}` |
| `get_subscriber_count()` | Number of active alert subscribers |

### Output Format

```json
{
  "risk_score": 35,
  "btc_bias": "BEAR",
  "analysis": "Elevated oil prices from Hormuz disruption maintaining inflation pressure. Fed constrained from cutting rates. Liquidity conditions tightening. Risk-off environment for crypto persists.",
  "timestamp": "12",
  "total_updates": 12
}
```

### Risk Score Scale

| Score | Zone | Meaning |
|-------|------|---------|
| 0-20 | 🔴 Extreme Risk-Off | Major macro headwinds. High probability of crypto drawdown. |
| 20-40 | 🟠 Risk-Off | Negative macro conditions. Defensive positioning recommended. |
| 40-60 | 🟡 Neutral | Mixed signals. No strong directional macro bias. |
| 60-80 | 🟢 Risk-On | Favorable macro conditions. Constructive for crypto. |
| 80-100 | 🟢 Extreme Risk-On | Strong macro tailwinds. High probability of crypto rally. |

### BTC Bias Classification

| Bias | Signal |
|------|--------|
| `STRONG_BEAR` | Multiple macro headwinds converging. Avoid longs. |
| `BEAR` | Negative macro lean. Reduce exposure. |
| `NEUTRAL` | No clear macro direction. Range-bound expected. |
| `BULL` | Positive macro lean. Accumulation zone. |
| `STRONG_BULL` | Multiple macro tailwinds. High conviction long. |

---

## Quick Start

### Prerequisites

- GenLayer Studio account or GenLayer CLI installed
- Testnet GEN tokens from [faucet](https://testnet-faucet.genlayer.foundation)

### Deploy via GenLayer Studio (Easiest)

1. Go to [GenLayer Studio](https://studio.genlayer.com/contracts)
2. Copy the contents of `contracts/crypto_macro_sentinel.py`
3. Paste into the Studio editor
4. Click **Deploy**
5. Interact with the contract through the Studio UI

### Deploy via CLI

```bash
# Install GenLayer CLI
npm install -g genlayer

# Select testnet network
genlayer network

# Deploy contract
genlayer deploy --contract contracts/crypto_macro_sentinel.py
```

### Interact with the Contract

```bash
# Trigger a macro scan
genlayer call scan_macro_environment

# Check current risk
genlayer call get_current_risk

# Scan a specific event
genlayer call scan_specific_event --args "Federal Reserve rate decision April 2026"

# Check risk trend
genlayer call get_risk_trend
```

---

## Project Structure

```
CryptoMacro-Sentinel/
├── contracts/
│   └── crypto_macro_sentinel.py    # Main Intelligent Contract
├── docs/
│   └── PROJECT_SUBMISSION.md       # Builder program submission
├── README.md
└── LICENSE
```

---

## Use Cases

### 🏦 DeFi Protocol Risk Management
DeFi protocols can read CryptoMacro Sentinel's risk score to automatically adjust parameters:
- **High risk** (score < 30) → Increase collateral requirements, reduce leverage limits
- **Low risk** (score > 70) → Relax parameters for capital efficiency

### 📊 Trader Decision Support
Query the contract before taking positions:
- Check macro alignment with your trading thesis
- Use `scan_specific_event()` for breaking news analysis
- Track risk trend to identify regime changes early

### 🔗 Cross-Chain Macro Oracle (via LayerZero)
Other blockchains can consume CryptoMacro Sentinel data through GenLayer's LayerZero integration — becoming the **first cross-chain macro risk oracle**.

### 🤖 AI Agent Infrastructure
Autonomous trading agents need trustless macro data feeds. This contract provides exactly that — no centralized API dependency, no single point of failure.

---

## Roadmap

| Phase | Status | Description |
|-------|--------|-------------|
| **MVP Contract** | ✅ Complete | Core contract with macro scan, event scan, risk scoring, history tracking |
| **Frontend Dashboard** | 🔨 In Progress | React/Next.js dashboard with real-time risk display and charts |
| **Extended Data Sources** | 📋 Planned | Treasury yields, DXY, on-chain metrics (exchange flows, whale movements) |
| **Cross-Chain Bridge** | 📋 Planned | LayerZero integration for multi-chain data consumption |
| **Community & Docs** | 📋 Planned | Tutorials, integration guides, open ecosystem contributions |

---

## Technical Details

### Data Sources

| Source | Data | Usage |
|--------|------|-------|
| alternative.me | Crypto Fear & Greed Index | Market sentiment baseline |
| coindesk.com | Market news headlines | Event detection, narrative analysis |
| investing.com | Crude oil prices | Energy/inflation proxy |
| google.com (event scan) | Custom search | Targeted event impact analysis |

### Consensus Mechanism

The contract uses `gl.eq_principle_prompt_comparative` — validators independently analyze the same macro data using different LLMs, then compare results. Consensus requires agreement on:
- Risk score direction (within 15 points tolerance)
- BTC bias classification
- Key macro factor identification

This ensures no single AI model can skew the risk assessment.

### State Management

- **Risk history**: Circular buffer of last 50 entries for efficient storage
- **Trend computation**: Rolling average comparison for regime detection
- **Subscriber registry**: On-chain list for alert notifications

---

## Built With

- **[GenLayer](https://www.genlayer.com/)** — AI-native blockchain with Intelligent Contracts
- **[GenVM SDK](https://docs.genlayer.com/)** — Python SDK for Intelligent Contract development
- **[Optimistic Democracy](https://docs.genlayer.com/)** — Multi-validator AI consensus mechanism

---

## Contributing

Contributions are welcome! Areas where help is needed:

1. **Additional data sources** — Treasury yields, DXY index, BTC ETF flows
2. **Frontend development** — React dashboard using genlayer-js
3. **Testing** — Edge cases, adversarial inputs, consensus edge conditions
4. **Documentation** — Tutorials, integration guides

Please open an issue to discuss before submitting PRs.

---

## Acknowledgments

- GenLayer team for building the first blockchain where this is possible
- The crypto trading community for validating the macro transmission chain framework
- GenLayer Builder Program for supporting early ecosystem development

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>Built with 🧠 on GenLayer — The Intelligence Layer of the Internet</b>
</p>
