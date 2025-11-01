# Podiatry-Need-Study
A simple program which determines potential underserved areas for podiatry by comparing rates of associated ailments (ie. diabetes, arthritis, etc) and the number of existing podiatrists per capita.

## Method
### Data Sourcing & Extracting
Data is pulled from the Department of Health and Human Services (NPI registrations to represent podiatrists) and the Centers for Disease Control and Prevention (ailment data). Initial design will be based on uploading CSV files from the sources to a SQL database, however it is designed with the idea of eventually being API based. Once data is cleaned and loaded, we can begin running our analysis.

### Analysis
First, baseline Z-scores are generated for each ailment and each county based on national prevelance. These will be used to represent the rate of each ailment in any given county. The number of podiatrists with respect to population can be modeled with the following equation for any single county, assuming a linear association:

$$P<sub>per 10k pop</sub> = β_d Diabetes + β_a Arthritis + ...$$

We will take 10000 counties at random to find the best coefficients using multiple linear regression. This will yield our expected coefficients which, when placed into our equation, should allow us to estimate the demand for podiatrists for any county based on their population. NOTE: Only counties with populations over 10k adults will be considered to prevent smaller areas from skewing the data.

Given our baselines, we will take the predicted population data from the US Census to generate our estimated need for podiatrists across all counties that meet our population requirement. We will then compute the difference between the number of podiatrists we predict are needed and the number of podiatrists currently in the county to find how many more or less are needed in each area.

## Considerations
This analysis, as presently designed (10/27/2025) makes some assumptions which, for more accuracy, would need to be rectified. Below are some of these oversights and assumptions that I acknowledge in its design. There may be more which I have not recognized, and I welcome anyone and everyone to create an issue or send me a message to bring these unacknowledged caveats to light. As I maintain the project, some will be addressed and will then be marked through here.

### Known Discrepancies
- **Data is analyzed on a county basis with no consideration for neighboring counties.** As such, a practice which currently exists near the border of one county will not be considered when determining podiatric need in a neighboring county despite some residents having a shorter distance to the practice than those living in its county. Another set of data containing what counties neighbor each other could be compiled in the future and factored into the algorithm to demonstrate counties having needs met by neighbors.
- **Health data is only sourced from the CDC's publicly available data.** This means if there is an inaccuracy in the single dataset of interest, or not all areas are represented, values in these areas can be skewed. A possible solution would be integrating other datasets, or providing another metric to represent the confidence level in our analysis of each county.
