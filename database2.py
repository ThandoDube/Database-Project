

file2 = "File2.txt" #creating a variable for the output file

try:
    with open('file.txt','r',encoding='utf-8-sig') as file:
        header = file.readline().strip().split(",") #to take the header from the top of the file
        rows = [dict(zip(header, line.strip().split(","))) for line in file]# this is to take the header and than make rows for each data to make it easily accesbile in a dictionary set
    #print(rows)
        
    with open (file2,'w' , encoding='utf-8-sig') as file: #to create the file where the answers are 
       
        # a) Countries ending with 'a'
        file.write("Question a: \n ")
        for row in rows:
            country = row['CountryName'] # calls to dictionary rows to find the header CountryName
            if country.endswith("a"):  #searchs through the dictionary for countrys that end with a 
                file.write(f"{country},")

         # b) Top 5 cities by population      
        citypop = set() #empty list to hold the population nuumbers
        for row in rows:
            if 'CityPopulation' in row and 'CityName' in row : #Calls the header directly in dictionary
                cityN = row['CityName']
                pop = int(row['CityPopulation'])#Converts the string in the dictionary into integers
                citypop.add((cityN,pop))
        # sorts the list citypop and then reverse the order to ensure the largest numbers are on top and then pulls the top 5
        city5 = sorted(citypop,key=lambda x: x[1] , reverse=True)[:5]
        file.write("\n\nQuestion b: \n " + str(city5))
        
        # c) Top 5 countries by landmass
        landMass = set() #empty list to hold the population nuumbers
        for row in rows:
            if 'LandMass' in row and 'CountryName' in row : #Calls the header directly in dictionary, changed CityName to CountryName so we can search for countries instead of cities
                country = row['CountryName']
                Land = row['LandMass']#Converts the string in the dictionary into integers. Thando: I removed the converttointeger command because it produced an error; this may be likely to the landmass column in the csv file using region names and not codes.
                landMass.add((country,Land))
        land5 = sorted(landMass,key=lambda x: x[1], reverse=True)[:5]
        file.write("\n\nQuestion c: \n" + str(land5) ) 
         
        # d) Countries with independence year between 1960-1980

        #Thando: This code counts the number of countries that have independence year between 1960 and 1980, then shows the total of thos countries in File2
        #count_indep = 0
        #for row in rows:
            #if 'IndepYear' in row and 'CountryName' in row:
                #try:
                    #Year = int(row['IndepYear'])
                    #if 1960 <= Year <= 1980:
                        #count_indep += 1
                #except ValueError:
                    #Skip invalid entries like 'NULL' or non-numeric values
                    #continue
        #file.write("\n\nQuestion d: \n" + str(count_indep) )

        #Thando: This code instead prints out the names of the countries with independence years between 1960-1980 into File2 instead of just counting them.
        indep_countries = []  
        for row in rows:
            if 'IndepYear' in row and 'CountryName' in row:
                try:
                    Year = int(row['IndepYear'])
                    if 1960 <= Year <= 1980:
                        #Add country name to the list
                        indep_countries.append(row['CountryName'])
                except ValueError:
                    #Skip invalid entries like 'NULL' or non-numeric values
                    continue
        file.write("\n\nQuestion d: \n" + str(indep_countries))

        # e) Countries with independence year between 1830-1850
        countries_indep = []
        for row in rows:
            if 'IndepYear' in row and 'CountryName' in row:
                try:
                    Years = int(row['IndepYear'])
                    if 1830 <= Years <= 1850:
                        #Add county name to the list
                        countries_indep.append(row['CountryName'])
                except ValueError:
                    #Skip invalid entries like 'NULL' or non-numeric values
                    continue
        file.write("\n\nQuestion e: \n" + str(countries_indep))

        # f) Top 5 African countries by life expectancy
        LifeExpect_max = {} #Use dictionary to hold maximum life expectancy for each country since there are duplicated countries in the dataset.
        for row in rows:
            #Check if the row has the keys we need and if it's in Africa
            if 'LifeExpectancy' in row and 'CountryName' in row and 'Continent' in row:
                if row['Continent'] == 'Africa':
                    country = row['CountryName']
                    try:
                        #Convert life expectancy to float to avoid losing decimal precision
                        life_expect = float(row['LifeExpectancy'])
                       #If the country is not in the dictionary, add it. If it is, update to the max life expectancy
                        if country not in LifeExpect_max or life_expect > LifeExpect_max[country]:
                            LifeExpect_max[country] = life_expect
                    except (ValueError, TypeError):
                        #Skip if conversion fails
                        continue
                #Convert to list and sort life_expectancy in descending order and take the top 5
                LifeExpect_list = [(country, life_expect) for country, life_expect in LifeExpect_max.items()]
                top5_africa = sorted(LifeExpect_list, key=lambda x: x[1], reverse=True)[:5]
                file.write("\n\nQuestion f: \n" + str(top5_africa))



       

       
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    