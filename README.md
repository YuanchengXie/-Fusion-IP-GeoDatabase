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

## ipsame accuracy

ipsame accuracy is the experimental result of our verification of the accuracy of IPsame data using the CAIDA ITDK dataset. During the evaluation, we filter out the location information of MaxMind provided in ITDK. We conclude that locating consistent IP addresses across multiple GeoIPDBs is highly reliable.

## Latency Data Cleaning Dataset

This data set is the experimental data recorded by us in the "Cut Head and Tail" and "low frequency rejection" operations, discussing the parameters a and b of these two methods. Through this experiment, we determined the parameters a=20, b=1000.

## Data Consistency Dataset

The data consistency rate dataset is obtained by extracting IP addresses located in 42 experimental cities from multiple IP geolocation databases. We compared four commercial databases, and conducted pairwise comparisons, three database comparisons, and four database comparisons for 42 experimental cities. The final comparison results are recorded in this data set, and we extracted part of the data for analysis in the paper.

## Routing reachability

This file is the test result of the reachability of the route for the IP address and the network segment. The routable ratio of IP addresses is the ratio of the routable IPs obtained by pinging all IP addresses of a city-db to the total number of IPs contained in the city-db. Similarly, the routable ratio of a network segment is the ratio of the number of routable network segments to the total number of network segments contained in the city-db when ping detection is performed on the network segments contained in a city-db. If a network segment has an ip routable, then the network segment is routable.

## Accuracy Comparision

Accuracy Comparision is the experimental data obtained by comparing the city positioning information with the verification data set, including the accuracy results of multiple commercial IP geolocation databases and fusion databases in the experimental cities.

## Prefix-file

Prefix-file refers to the original IP address located in 42 experimental cities extracted from the original IP geolocation database. We counted the number of IP addresses in different cities assigned by each database and recorded them in 'Data Consistency Dataset.xlsx'. The two files Prefix-ipsame3 and Prefix-ipsame4 respectively record the prefix of ipsame3 and the prefix of ipsame4.

## Fusion

All the files in the 'Fusion' folder are the data generated after the judgment of the "city delay-based segment location determination algorithm", which is the reference fusion database in the paper.
