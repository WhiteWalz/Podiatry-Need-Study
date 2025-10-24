# Podiatry-Need-Study
A simple program which determines potential underserved areas for podiatry by comparing rates of associated ailments (ie. diabetes, arthritis, etc) and the number of existing podiatrists per capita.

## Method
### Data Sourcing & Extracting
Data is pulled from the Department of Health and Human Services (NPI registrations to represent podiatrists) and the Centers for Disease Control and Prevention (ailment data). Initial design will be based on uploading CSV files from the sources to a SQL database, however it is designed with the idea of eventually being API based. Once data is cleaned and loaded, we can begin running our analysis.

### Analysis
First, baseline Z-scores are generated for each ailment and each zip code based on national prevelance. These are fed into an equation to find a value representing the demand of podiatrists in a given area based on weights provided by the user (represented by β) like so:

$$D_z = β_d Diabetes + β_a Arthritis + ...$$

With our demand value, we then calculate a number representing the need of a given area by putting it in a ratio with the number of podiatrists per 10k residents in a ZIP code.

$$N_z = D_z / (Pods_z + β_0)$$

We add some constant to our count of podiatrists per 10k residents to keep lower end outliers from skewing our results (ie a zip with no podiatrists). This value N<sub>z</sub> is our final representation of demand for a given ZIP and can then be used to rank areas of need, or represented as a heat map using software like Tableau. The data is served via API for the client to decide how to visualize the data.
