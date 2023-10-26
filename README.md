# -Fusion-IP-GeoDatabase
This project is a supplementary file for the paper ‘**Evaluation method of IP geolocation database based on city delay characteristics**’, mainly including the files including the database, main code, and experimental data.

## Code

This folder contains the relevant codes for the key research content of the project:

> **Predd.py** is the preprocessing code for the original GeoIPDB; It is mainly aimed at the realization of the integrity detection of the network segment and the complete filling of the network segment.

> **FirstJPN. ipynb** is a standardized code for upgrading cities; Use the Zitong + bing interface to query the city;

> **Merge. py** is the code for filtering and comparing IPsame;Get the minimum value of the IP at the end of each line, and compare the consistency of geographic information.

> **cdccbdr.go** read ping result from rapath and get cdc of each city.

## Time Delay Distribution of NET-Seg

We obtained the original delay data of the network segment from the NETsame data provided in GeoIPDB, and we sorted the data from the perspective of whether the network segment is routable. The file contains the delay distribution data of the routable network segment and the non-routable network segment respectively.

## Time Delay Distribution of City IP Address Groups

Due to the large amount of Time Delay Distribution of City IP Address Groups data, we did not place it in this project. We put the original time delay data in the "timedelay" folder of "https://www.aliyundrive.com/s/eXhPoj2UBaG".

'timedelay 'collects time delay information from three collection points' Weihai, London and Newark', each collection point has collected delay data of all 42 experimental cities.Each collection point folder contains the original delay data obtained from the four experimental IP location databasesThe delay data of ipsame is the data of the IP address with the same location.IPSame3 represents the IP that is located consistently in the three databases,IPSame4 represents the IP that is located consistently in the four databases.

## CBDR-ipsame

This series of files is based on the city delay characteristic information (**including CBDR and CDC**) of 42 experimental cities obtained from the IPsame dataset. We uploaded the experimental data calculated based on the three detection nodes in London, Newark, and Weihai respectively, and carried out statistics on the urban delay characteristics based on the IPsame data of the three databases (ipsame3) and the four databases (ipsame4). During the experiment, the codes we used were all Chinese to mark the city names, so the city names were not modified in the data set.

## top100city1

The top100city1 file is related information about 100 international large cities, including the country, latitude and longitude, distance from the detection point and related delay information.

## accuracy File 

ipsame accuracy is the experimental result of our verification of the accuracy of IPsame data using the CAIDA ITDK dataset. During the evaluation, we filter out the location information of MaxMind provided in ITDK. We conclude that locating consistent IP addresses across multiple GeoIPDBs is highly reliable. 
The accuracy verification results data set is the accuracy results of four databases and three models verified using ITDK.

## Evaluation results based on reference database

Evaluation results based on the reference database are the evaluation results obtained by the four IP geolocation libraries after using the reference database CDCDB, including database accuracy, database recall, and database reliability scores.

## low-frequency rejection

This data set is the experimental data recorded by us in the "low-frequency rejection" operations, discussing the parameters a. Through this experiment, we determined the parameters a=1000.

## Prefix-file

Prefix-file refers to the original IP address located in 42 experimental cities extracted from the original IP geolocation database. We counted the number of IP addresses in different cities assigned by each database and recorded them in 'Data Consistency Dataset.xlsx'. The two files Prefix-ipsame3 and Prefix-ipsame4 respectively record the prefix of ipsame3 and the prefix of ipsame4.

## Fusion

All the files in the 'Fusion' folder are the data generated after the judgment of the "city delay-based segment location determination algorithm", which is the reference fusion database in the paper.
