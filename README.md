# Podiatry-Need-Study
A simple program which determines potential underserved areas for podiatry by comparing rates of associated ailments (ie. diabetes, arthritis, etc) and the number of existing podiatrists per capita.

## Method
### Data Sourcing & Extracting
Data is pulled from the Department of Health and Human Services (NPI registrations to represent podiatrists) and the Centers for Disease Control and Prevention (ailment data). Initial design will be based on uploading CSV files from the sources to a SQL database, however it is designed with the idea of eventually being API based. Once data is cleaned and loaded, we can begin running our analysis.

### Analysis
First, baseline Z-scores are generated for each ailment and each county based on national prevelance. These are fed into an equation to find a value representing the demand of podiatrists in a given area based on weights provided by the user (represented by β) like so:

$$D_z = β_d Diabetes + β_a Arthritis + ...$$

With our demand value, we then calculate a number representing the need of a given area by putting it in a ratio with the number of podiatrists per 10k residents in a county.

$$N_z = D_z / (Pods_z + β_0)$$

We add some constant to our count of podiatrists per 10k residents to keep lower end outliers from skewing our results (ie a county with no podiatrists). This value N<sub>z</sub> is our final representation of demand for a given county and can then be used to rank areas of need, or represented as a heat map using software like Tableau. The data is served via API for the client to decide how to visualize the data.

## Considerations
This analysis, as presently designed (10/27/2025) makes some assumptions which, for more accuracy, would need to be rectified. Below are some of these oversights and assumptions that I acknowledge in its design. There may be more which I have not recognized, and I welcome anyone and everyone to create an issue or send me a message to bring these unacknowledged caveats to light. As I maintain the project, some will be addressed and will then be marked through here.

### Known Discrepancies
- **Data is analyzed on a county basis with no consideration for neighboring counties.** As such, a practice which currently exists near the border of one county will not be considered when determining podiatric need in a neighboring county despite some residents having a shorter distance to the practice than those living in its county. Another set of data containing what counties neighbor each other could be compiled in the future and factored into the algorithm to demonstrate counties having needs met by neighbors.
- **Health data is only sourced from the CDC's publicly available data.** This means if there is an inaccuracy in the single dataset of interest, or not all areas are represented, values in these areas can be skewed. A possible solution would be integrating other datasets, or providing another metric to represent the confidence level in our analysis of each county.
