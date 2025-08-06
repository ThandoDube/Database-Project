#Team Name : DataBaes
#Assignment: Practical 1

file2 = "File2.txt" #creating a variable for the output file

try:
    with open('file.txt','r',encoding='utf-8-sig') as file:
        header = file.readline().strip().split(",") #to take the header from the top of the file
        rows = [dict(zip(header, line.strip().split(","))) for line in file]# this is to take the header and than make rows for each data to make it easily accesbile in a dictionary set
    #print(rows)
        
    with open (file2,'w' , encoding='utf-8-sig') as file: #to create the file where the answers are 
       
        # ==========================================================
        #A) How many country names end with the letter 'a'? 
        # ==========================================================
        #Karabo: fixed code to correctly display the number of country names instead of the actual country names
        file.write("Question a: \n ")
        def question_A(rows):
            countryset = set() #empty set to hold the country names
            for row in rows:
                country = row['CountryName'] # calls to dictionary rows to find the header CountryName
                if country.endswith('a'):  # searches through the dictionary for countries that end with a
                    countryset.add(country) #adds the country to the set if it ends with a
            file.write(f"Total countries ending with 'a': {len(countryset)}") #writes the total number of countries ending with a to the file
            return len(countryset) #returns the total number of countries ending with a
        question_A(rows) #function call
        

        # ====================================================================
        # B)List the five cities that have the HIGHEST CITY POPULATION.
        # ====================================================================      
        def question_b(rows):
            citypop = set() #empty set to hold the population numbers
            for row in rows:
                if 'CityPopulation' in row and 'CityName' in row: #Calls the header directly in dictionary
                    cityN = row['CityName']
                    pop = int(row['CityPopulation'])#Converts the string in the dictionary into integers
                    citypop.add((cityN,pop))
            # sorts the list citypop and then reverses the order to ensure the largest numbers are on top and then pulls the top 5
            city5 = sorted(citypop,key=lambda x: x[1] , reverse=True)[:5]
            file.write("\n\nQuestion b: \n " + str(city5))
            return city5
        question_b(rows) #function call
        
        
        # ==========================================================
        #C) List the five countries that have the LARGEST LANDMASS.
        # ==========================================================
        #Jessie: I added the try and except method to actually get the countries and the landmass nunber , so readded the int value
        def question_c(rows):
            landMass = set() #empty list to hold the population numbers
            for row in rows:
                if 'LandMass' in row and 'CountryName' in row : #Calls the header directly in dictionary, changed CityName to CountryName so we can search for countries instead of cities
                    try:
                        country = row['CountryName']
                        Land = int(row['LandMass'])#Converts the string in the dictionary into integers. Thando: I removed the converttointeger command because it produced an error; this may be likely to the landmass column in the csv file using region names and not codes.
                        landMass.add((country,Land))
                    except ValueError:
                        continue
            land5 = sorted(landMass,key=lambda x: x[1], reverse=True)[:5]
            file.write("\n\nQuestion c: \n" + str(land5) )
            return land5
        question_c(rows) #function call
         
        # ========================================================================================
        # D) How many countries gained independence between the years 1960 and 1980 (inclusive)?
        # =======================================================================================
        #Thando: This code counts the number of countries that have independence year between 1960 and 1980, then shows the total of thos countries in File2
        #Karabo: Added a set to store the countries with independence in the relevant years and removed repetitions.
        def question_d(rows):
            uniqueSet = set()
            count_indep = 0
            for row in rows:
                if 'IndepYear' in row and 'CountryName' in row:
                    try:
                        Year = int(row['IndepYear'])
                        if 1960 <= Year <= 1980:
                            if row['CountryName'] not in uniqueSet: #To avoid counting the same country multiple times
                                uniqueSet.add(row['CountryName']) # Add country name to the set
                                count_indep += 1
                    except ValueError:
                        #Skip invalid entries like 'NULL' or non-numeric values
                        continue
            file.write("\n\nQuestion d: \n" + str(count_indep) )
            return count_indep
        question_d(rows)

        # ======================================================
        # e) Countries with independence year between 1830-1850
        # =====================================================
        #Karabo: Changed the list to a set to avoid duplicates 
        def question_e(rows):
            countries_indep = set()
            for row in rows:
                if 'IndepYear' in row and 'CountryName' in row:
                    try:
                        Years = int(row['IndepYear'])
                        if 1830 <= Years <= 1850:
                            # Add county name to the list
                            countries_indep.add(row['CountryName'])
                    except ValueError:
                        #Skip invalid entries like 'NULL' or non-numeric values
                        continue
            file.write("\n\nQuestion e: \n" + str(countries_indep))
            return countries_indep
        question_e(rows) #function call
            
        # ====================================================================================
        # f) List the five African countries that have the highest life expectancy.
        # ====================================================================================
        #Jessie: Added comments to this section
        def question_f(rows):
            African = set() #An empty set to contain the filtered countries
            for row in rows:
                    Cont = row['Continent']   #calls to the dictionary for header Continent
                    if Cont == "Africa":   #creates a condition to check if a continent is equal to africa
                        life = float(row['LifeExpectancy']) #converts the string in the dictionary rows into float
                        Country = row['CountryName']
                        African.add((Country,life))
            Afri5 = sorted(African,key=lambda z: z[1], reverse=True)[:5]
            file.write("\n\nQuestion f: \n " + str(Afri5))
            return Afri5
        question_f(rows) #function call

        # ====================================================================================
        # G) Which are the 5 most commonly spoken languages in the world?
        # ====================================================================================
        #Thando
        def question_g(rows):
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
            #Sort languages by count in descending order and select the top 5
            sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
            top5_langs = [lang for lang, count in sorted_langs[:5]]
            file.write("\n\nQuestion g: \n" + str(top5_langs))
            return top5_langs
        question_g(rows) #function call
            
        # ==================================================================================== 
        # List the country names that end with the letter ‘a’, without any repetitions
        # ====================================================================================
        #Jessie
        def question_h(rows):
            Base = set()
            for row in rows:
                country = row['CountryName'] # calls to dictionary rows to find the header CountryName
                if country.endswith("a"):  # searches through the dictionary for countries that end with a 
                    Base.add(country)
            file.write("\n\nQuestion h: \n" + str(Base))
            return Base
        question_h(rows) #function call

       
        
except FileNotFoundError:
    print("That's not a file") 
except FileExistsError:
    print("File already exists")

#edited all code to their respective functions - Karabo
#headings for consistency - Karabo
    



