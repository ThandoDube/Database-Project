

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
        count_indep = 0
        for row in rows:
            if 'IndepYear' in row and 'CountryName' in row:
                try:
                    Year = int(row['IndepYear'])
                    if 1960 <= Year <= 1980:
                        count_indep += 1
                except ValueError:
                    #Skip invalid entries like 'NULL' or non-numeric values
                    continue
        file.write("\n\nQuestion d: \n" + str(count_indep) )

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

        # f) Jessie: Top 5 African countries by life expectancy
        African = set()
        for row in rows:
                Cont = row['Continent']
                if Cont == "Africa":
                    life = float(row['LifeExpectancy'])
                    Country = row['CountryName']
                    African.add((Country,life))
        Afri5 = sorted(African,key=lambda z: z[1], reverse=True)[:5]
        file.write("\n\nQuestion f: \n " + str(Afri5))

        # g) Thando: Top 5 languages by country count
        lang_count = {}
        for row in rows:
            if 'Language' in row:
                try:
                    langs = [lang.strip() for lang in row['Language'].split(',')]
                    for lang in langs:
                        if lang: #Ensure the language string is not empty
                            lang_count[lang] = lang_count.get(lang, 0) + 1
                except AttributeError:
                    #Handle cases where 'Language' is unexpected (e.g., a non-string type)
                    continue
        #Sort languages by count in descending order and select top 5
        sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
        top5_langs = [lang for lang, count in sorted_langs[:5]]
        file.write("\n\nQuestion g: \n" + str(top5_langs))
            
        # Jessie: h) Country names that end with 'a' without repetition
        Base = set()
        for row in rows:
            country = row['CountryName'] # calls to dictionary rows to find the header CountryName
            if country.endswith("a"):  #searchs through the dictionary for countrys that end with a 
                Base.add(country)
        file.write("\n\nQuestion h: \n" + str(Base))

       
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    