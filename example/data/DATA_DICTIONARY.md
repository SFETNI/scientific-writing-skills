# Data Dictionary

The artifact generator writes `example/data/concrete_compressive_strength.csv` with the following columns.

| Column | Role | Unit | Description |
|---|---|---:|---|
| `cement` | Feature | kg/m^3 | Cement content per cubic metre of mixture. |
| `blast_furnace_slag` | Feature | kg/m^3 | Blast furnace slag content per cubic metre of mixture. |
| `fly_ash` | Feature | kg/m^3 | Fly ash content per cubic metre of mixture. |
| `water` | Feature | kg/m^3 | Water content per cubic metre of mixture. |
| `superplasticizer` | Feature | kg/m^3 | Superplasticizer admixture content per cubic metre of mixture. |
| `coarse_aggregate` | Feature | kg/m^3 | Coarse aggregate content per cubic metre of mixture. |
| `fine_aggregate` | Feature | kg/m^3 | Fine aggregate content per cubic metre of mixture. |
| `age` | Feature | days | Curing age at strength measurement. |
| `compressive_strength` | Target | MPa | Concrete compressive strength. |
| `source_label` | Provenance | none | `UCI_CC_BY_4_0` for official UCI data, or `DETERMINISTIC_FALLBACK_NOT_UCI` for the local fallback. |

The model and figures use only the eight feature columns and the target column. `source_label` is carried only to prevent fallback data from being mistaken for the UCI dataset.
