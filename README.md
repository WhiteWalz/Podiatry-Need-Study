# Podiatry-Need-Study
A simple program which determines potential underserved areas for podiatry by comparing rates of associated ailments (ie. diabetes, arthritis, etc) and the number of existing podiatrists per capita.

## Method
### Data Sourcing & Extracting
Data is pulled from the Department of Health and Human Services (NPI registrations to represent podiatrists) and the Centers for Disease Control and Prevention (ailment data). Initial design will be based on uploading CSV files from the sources to a SQL database, however it is designed with the idea of eventually being API based. Once data is cleaned and loaded, we can begin running our analysis.

### Analysis
Z-scores will be generated for all ailment values of interest, relating them to their prevelance nationally.
