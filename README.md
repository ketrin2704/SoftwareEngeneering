# SoftwareEngeneering Final Project

The aim of this project is to help potential investor with decision making by automatically analysing a big amount of data, provided on US SECURITIES AND EXCHANGE COMISSION site (https://www.sec.gov/). 
The program collects data from the target website, creates a dataset, containing the information about economic reporting indicators of different public companies. 
In order to simplify investment decisions making the program analyses the received dataset and classifies the data, highlighting the number of assets of companies in the context of the industry, using HADOOP cluster.




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The file with requirements is provided in the main branch.
To configure the default requirements file:
1. Open the Settings/Preferences dialog box of the PyCharm, and then click the page Python Integrated Tools.
2. In the Package requirements file field, type the name of the requirements file. 

In order to run the program there is a need deploy a **HADOOP** cluster, using Google Cloud service.
*https://cloud.google.com/dataproc/*


### Run job localy

To run job localy, type in cli:
`cat result_total.csv | python mapper.py | sort | python reducer.py`
