# Tokenomics Health Scoring Engine
A Multi-Pillar Decision System for Evaluating Crypto Token Sustainability

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-red)](https://tokenomics-health-scoring-engine.streamlit.app/)

## Live Interactive Dashboard

Explore the Tokenomics Health Scoring Engine through an interactive Streamlit application.

 **Launch the live app:**  
[Tokenomics Health Engine – Streamlit Dashboard](https://tokenomics-health-scoring-engine.streamlit.app/)

### What you can do in the app
- Select any token and view its final Tokenomics Health Score and grade
- Inspect pillar-level scores for:
  - Market Health
  - On-chain Distribution Health
  - Supply Sustainability
- Understand how structural token design differs across tokens
- Explore scores based on public, verifiable data (not price predictions)

## Project Overview
This project builds an automated Tokenomics Health Scoring Engine designed to help founders, investors, and analysts evaluate whether a crypto token’s design is structurally sustainable.

Instead of relying on narratives, hype, or subjective opinions, the system uses public, verifiable data to score tokens across three independent pillars:
- Market Health
- On-Chain Distribution Health
- Supply Sustainability

Each pillar is scored separately and then aggregated into a final Tokenomics Health Score and qualitative grade.

## Problem Statement
Many crypto tokens fail not because of technology, but due to:
- Poor liquidity structure
- Overly concentrated usage
- Hidden dilution or inflation risk

Existing evaluations often focus on price action or sentiment while ignoring deeper structural risks.  
This project addresses that gap by building a data-driven decision engine that evaluates tokenomics fundamentals objectively.

## Data Sources
All data used in this project comes from public APIs:

**CoinGecko API**
- Market price
- Market capitalization
- Trading volume
- Circulating and max supply
- Fully diluted valuation (FDV)

**Etherscan API (v2)**
- Verified contract status
- ERC-20 transfer activity
- On-chain participation proxies

No proprietary or paid data sources are used.

## Methodology
This project follows a structured, multi-step analytics pipeline to evaluate tokenomics sustainability using market data and on-chain signals.

 **Read the full methodology here:**  
[METHODOLOGY.md](Methodology.md)

The engine is built around three independent analytical pillars.

## Pillar 1: Market Health
**Objective:**  
Measure whether a token is liquid, actively traded, and viable in the market today.

**Key metrics:**
- Market capitalization
- 24-hour trading volume
- Volume-to-market-cap ratio
- Volatility and drawdown behavior (historical)

**Scoring approach:**
- Metrics are normalized within peer groups
- Tokens are scored relative to similar assets, not in isolation

**Interpretation:**
- High score → strong liquidity and market participation
- Low score → thin liquidity or unstable trading behavior

## Pillar 2: Distribution Health (On-Chain Activity)
**Objective:**  
Evaluate how broadly token activity is distributed across participants.

**Important note:**  
This pillar measures activity distribution, not wallet balances.

**Method:**
- The most recent 5,000 ERC-20 transfers are pulled for each token
- On-chain interaction patterns are analyzed

**Key metrics:**
- Number of unique senders
- Number of unique receivers
- Total unique addresses involved
- Concentration of activity among top 10 senders
- Concentration of activity among top 10 receivers
- Contract verification status

**Why this matters:**
- Broad participation suggests healthier network usage
- Highly concentrated activity suggests centralization risk

## Pillar 3: Supply Sustainability
**Objective:**  
Assess long-term dilution and supply-side risk using fully automated rules.

**Key metrics:**
- Circulating supply vs max supply ratio
- FDV-to-market-cap ratio (valuation overhang)
- Contract verification transparency
- Max supply certainty

**Design philosophy:**
- No narrative assumptions
- No manual overrides
- No subjective judgments

This ensures the system remains reproducible and scalable.

## Final Tokenomics Health Score
Each pillar is aggregated into a final score using the following weights:

| Pillar                     | Weight |
|---------------------------|--------|
| Market Health             | 40%    |
| Distribution Health       | 30%    |
| Supply Sustainability     | 30%    |

**Final outputs:**
- Tokenomics Health Score (0–100)
- Health grade:
  - A (Healthy)
  - B (Solid)
  - C (Watch)
  - D (Risky)
  - F (High Risk)

## Outputs
The project generates several structured datasets:
- `market_health_scores.csv`
- `distribution_health_scores.csv`
- `supply_sustainability_scores.csv`
- `tokenomics_health_engine_output.csv` (final combined output)

> **MVP Rationale:**  
> This project was intentionally scoped as a minimum viable decision engine to validate a transparent, reproducible tokenomics scoring framework before scaling coverage or complexity.

## Limitations
- The current analysis is conducted on a **curated set of 20 representative tokens**, selected to validate the scoring framework across diverse token models.
- Distribution analysis is **activity-based**, rather than balance-based, due to public API constraints.
- Token unlock schedules and emission mechanics are **not manually annotated** in the current version.
- Results reflect **structural tokenomics health**, not short-term price performance or investment recommendations.

These limitations are intentional design choices that preserve automation, objectivity, and interpretability at the MVP stage.

## Future Improvements
- Expand coverage to a larger and continuously updated token universe.
- Implement true holder balance concentration analysis.
- Integrate token unlock schedules and emission dynamics into supply sustainability scoring.
- Enable multi-chain support beyond Ethereum.
- Extend the dashboard with historical trends, peer benchmarking, and comparisons.
- Expose the scoring engine via an API-based service for programmatic access.

## Conclusion
This project demonstrates how tokenomics can be evaluated systematically using transparent, reproducible data pipelines.  
It is designed to function both as an analytics project and as a foundation for a real-world decision engine.


