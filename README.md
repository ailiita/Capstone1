# Capstone1

The repository contains the following files :
- [flood.csv](https://github.com/ailiita/Capstone1/blob/main/flood.csv) : raw data, with missing values. Used for data preparation.
- [flood_cleaned.csv](https://github.com/ailiita/Capstone1/blob/main/flood_cleaned.csv) : cleaned data after data preparation, feature engineering. Used to train final model.
- [notebook.ipynb](https://github.com/ailiita/Capstone1/blob/main/notebook.ipynb) : Whole process : EDA, feature importance analysis Model selection process and parameter tuning
- [train.py](https://github.com/ailiita/Capstone1/blob/main/train.py) : Script that trains final model and saves it
- [predict.py](https://github.com/ailiita/Capstone1/blob/main/predict.py) : Script that loads model and serves it via flask
- [prediction_test.py](https://github.com/ailiita/Capstone1/blob/main/prediction_test.py) and [prediction_test.ipynb](https://github.com/ailiita/Midterm_project/blob/main/prediction_test.ipynb) : Script and notebook. Using input data, tests the model and gives the result of AQI prediction.
- model_lr.bin
- [Pipfile](https://github.com/ailiita/Capstone1/blob/main/Pipfile)
- [Pipfile.lock](https://github.com/ailiita/Capstone1/blob/main/Pipfile.lock)
- [Dockerfile](https://github.com/ailiita/Capstone1/blob/main/Dockerfile)

## Data Description
The dataset used for this analysis comprises numerous features, each representing a distinct parameter that influences flood occurrence and severity. These parameters include environmental factors such as monsoon intensity, river management, and topography drainage, as well as human-related factors like encroachments and societal vulnerability. Each row in the dataset corresponds to a specific region, with the columns providing scores for each parameter in that region. These scores quantify the level or impact of each parameter in the respective region, offering a comprehensive view of the contributing factors to flood risk. No further info about the regions, or countries were given.

- MonsoonIntensity: Higher volumes of rain during monsoons increase the probability of floods.
- TopographyDrainage: The drainage capacity based on the region's topography. Efficient drainage can help drain rainwater and reduce the risk of floods.
- RiverManagement: The quality and effectiveness of river management practices. Proper river management, including dredging and bank maintenance, can improve water flow and reduce floods.
- Deforestation: The extent of deforestation in the area.* Deforestation reduces the soil's ability to absorb water, increasing surface runoff and the risk of floods.
- Urbanization: The level of urbanization in the region. Urban areas have impermeable surfaces (asphalt, concrete), which reduce water infiltration, raising the risk of floods.
- ClimateChange: The impact of climate change on the region. Climate change can lead to more extreme precipitation patterns, including torrential rains that can cause floods.
- DamsQuality: The quality and maintenance status of dams. Well-maintained dams can control floods, and dams with structural problems can break and cause catastrophic floods.
- Siltation: The extent of siltation in rivers and reservoirs. The accumulation of sediments in rivers (siltation) reduces drainage capacity and increases the risk of floods.
- Agricultural Practices: The types and sustainability of agricultural practices. The intensification of agriculture can lead to deforestation, excessive use of fertilizers and pesticides, and inappropriate irrigation practices, reducing soil biodiversity and increasing the risk of floods.
- Encroachments:The degree of encroachment on flood plains and natural waterways. Construction in flood-prone areas impedes the natural flow of water and increases the risk of floods.
- IneffectiveDisasterPreparedness: ** The lack of emergency plans, warning systems, and simulations increases the negative impact of floods.
- DrainageSystems: Well-maintained and adequately sized drainage systems help drain rainwater and reduce the risk of floods.
- CoastalVulnerability: Low-lying coastal areas are prone to flooding from storm surges and sea level rise.
- Landslides: Steep slopes and unstable soils are more prone to landslides.
- Watersheds: Regions with more watersheds may have a higher or lower risk of flooding, depending on various factors.
- DeterioratingInfrastructure: Clogged culverts, damaged drainage channels, and other deficient infrastructure can increase the risk of floods.
- PopulationScore: Densely populated areas can suffer more severe losses.
- WetlandLoss: Wetlands act as natural sponges, absorbing excess water and helping to prevent floods.
- InadequatePlanning: Urban planning that does not consider the risk of flooding increases the vulnerability of communities.
- PoliticalFactors: Factors such as corruption and a lack of political will to invest in drainage infrastructure can make it difficult to manage flood risk.
- **FloodProbability**: The overall probability of flooding in the region. This is the **target variable** for predictive analysis. This is the target Variable.

## Context and Objective
Flooding has become an increasingly significant risk in many regions, exacerbated by the impacts of climate change. It causes significant damage, both in terms of human lives and infrastructure, and their effects can persist for months before affected regions can recover, as seen in Spain last fall. Rising sea levels, drought, more intense and unpredictable monsoons, and changes in weather patterns have heightened the frequency and severity of floods. As a result, predicting flood risk is crucial for mitigating damage, preparing communities, and adapting to the changing climate. This project aims to leverage environmental and societal data to forecast flood probabilities and help guide effective risk management strategies.  
After predicting the probability ***p***, predictions are classified into three risk classes :
- Low risk (p<0.2)
- Moderate (0.2<p<0.5)
- High (0.5<p<1)

## Model Selection and Parameter Tuning
I used three models to address this problem :
- Linear Regression
- Random Forest (tuned `n_estimators`, `max_depth` and `min_samples_leaf`)
- XGBoost (optimal parameters found using GridSearch)

The model was trained using 60% of the dataset and 20% was used for validation. Linear Regression and XGBoost have shown almost identical performances.

## Installing Dependencies
To create and activate the local environment, change directory to root folder of this project and run : 
```
pip install pipenv
pipenv install
pipenv shell
```

## Training the Final Model 
Model used for final training is Linear Regression. Model is saved to ***model_lr.bin*** file.   
The ***train.py*** file trains this model (80% for training, 20% for testing), it also performs cross-validation using 5 folds. Results :   

```
Cross-validation results :     
 0.007   
Training final model    
 Validation RMSE : 0.0074
```


## Running the Web Service and Predicting
A Flask web service is provided with an exposed endpoint (/predict). Requests containing the relevant features of a respondent (JSON format) can be sent to generate corresponding flood predictions.  
In project directory, run with following command :
```
pipenv run waitress-serve --listen=0.0.0.0:8686 predict:app
``` 
Using an example, a request can be made by running in project directory,: 
```
python prediction_test.py
```
The ***prediction_test.py*** provides the results of a test using some data as input. ***prediction_test.ipynb*** is the notebook that displays the result. 

## Containerization
***Dockerfile***; ***Pipfile***, ***Pifile.lock*** are provided.
To build and start the service's Docker container, follow these instructions :
- Download Docker Desktop
- In project directory, run :
```
docker build -t flood-prediction .
docker run -it --rm -p 8686:8686 flood-prediction
```
