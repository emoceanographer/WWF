# Principal Component Analysis(PCA) on DHS Food Balance Sheet Data with Socioeconomic Data.

For this project, we are interested to see if countries share a use PCA to reduce the dimensionality of our dataset, and to see if there is any natural clustering among our dataset.  On top of PCA, we run Kmeans to see if Kmeans clustering align with any of the nature clustering. In this study, our hypothesis of the nature clustering are continent level, region level, and income group level. We retreieved region and income level information from UN's country classification dataset. https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf

## Analysis 1

In our second analysis, we are interested to see if countries cluster together based solely on protein food balance sheet data. This incluses Milk, Bovine meat, Sheep and goat meat, Pigmeat, Poultry, Eggs, Fish, Maize, Rice, Wheat, Rye, Barley, Pulses, Starchy roots on continent region and income group level. 


## Analysis 2

In our second analysis, we are interested to see if countries cluster together solely based on protein food balance sheet data. We group protein foods into groups and introduce three new variables which are Average GDP, Urban and rural ratio(urban population/rural population), and permenent crops ratio(permenent crops area/total country area). This result into 'Bovine_Sheep_Pigmeat_Poultry','Cereals','Milk_Egg','Fish_x',' Av 2011+2012+2013 extracted from WDI (constant 2010 US$)','Urban_Rural_ratio','Permenent_Crops_Ratio'. 

## Analysis 3



## Datasets Inventory
- **binary_classifier**:
  - This folder contains pkl file for trained classfier and fitted count vector
- **master_final_merged_df_protein_gdp.csv**:
  - This is the master data file containing food balance sheet data and socioecnomoic data. 
- **pca_protein.csv**:
  - Result file. This file includes Principal componenet 1 and 2 computed using only protein foods data, and the clusters K means assigned the datapoint to. 
- **pca_socio.csv**:
  - Result file. This file includes Principal componenet 1 and 2 computed using grouped protein foods data along with socioeconomic data, and the clusters K means assigned the datapoint to.

