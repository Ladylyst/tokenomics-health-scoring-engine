# Methodology Summary

**Goal**: Build a Tokenomics Health Scoring Engine that evaluates whether a token’s design is structurally sustainable (not a price predictor).

**Scope**: 20 Ethereum tokens (for consistent on-chain data availability and comparable metrics). Multi-chain can be added later by swapping chain data sources.

## Data Sources

- CoinGecko: market price, market cap, volume, supply fields (current + 365-day history)

- Etherscan: ERC-20 transfer activity sample (distribution and concentration signals)

## Pipeline

1. Token master list created (metadata: name, symbol, coingecko_id, contract address, category, tier)

2. Market data pull:

- Snapshot (current)

- 365-day daily market history

3. Distribution features pull (Etherscan):

- Sample of token transfers

- Unique sender/receiver counts

- Concentration metrics (top sender/receiver share)

4. Pillar scoring:

- Market Health Score

- Distribution Health Score

- Supply Sustainability Score

5. Final health score engine:

- Weighted combination into tokenomics_health_score

- Converted into grades (A, B, C, D)

6. Output saved to data/processed/tokenomics_health_engine_output.csv

7. Streamlit dashboard for interactive viewing

## Interpretation
This system measures structural tokenomics health based on market behavior + activity distribution + supply logic. It does not forecast price.

## Limitations

- Etherscan rate limits and sampling constraints

- Ethereum-only scope in v1 (chosen intentionally for consistency)

- Some supply fields depend on data completeness from CoinGecko