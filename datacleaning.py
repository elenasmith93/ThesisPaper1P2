import pandas as pd
import os

os.chdir('/Users/work-pc/Documents/GitHub/ThesisPaper1P2')
df = pd.read_csv('NESdata.csv')


###FOR MARKET SHARES
''' Replace all D and S values with 0 '''
df = df.replace('D', 0)
df = df.replace('S', 0)
df = df.replace('a', 9)
df=df.replace('b', 59)
df=df.replace('c',174)
df=df.replace('e',374)  
df=df.replace('f', 749)
df=df.replace('g',1750)
df=df.replace('h',3749) 
df=df.replace('i',7499)
df=df.replace('j',17499)

#df = df.replace('S', 0)


def variable(df, industry, county, year):
    ''' A function which returns the industry share and total employment across all given industries
        for a given industry, county, and year '''
    df = df[(df['Year']==year) & (df['Id2']==county)]           # restrict df to only relevant year
    industry_df = df[df['Meaning of 2007 NAICS code'] == industry]  # get a subset corresponding to industry
    total_employment = df['Number of establishments'].astype(float).sum()/2      # don't forget to convert strings to floats before summing
    industry_employment = industry_df['Number of establishments'].astype(float).sum()

    return industry_employment/total_employment, total_employment
    
#year = 2008
#industry = 'Utilities'
#county = 'Fairfield County, Connecticut'
#industry_employment, total_employment = variable(df, industry, county, year)

''' Create a new dataframe to store share data for all counties, industries, and years '''
shares = pd.DataFrame(columns = ['County', 'Year', 'Industry', 'Share', 'Total'])

''' Compute the total number of iterations needed '''
total_passes = len(df['Geographic area name'].unique()) * len(df['Year'].unique()) * len(df['Meaning of 2007 NAICS code'].unique())

''' Iterate through all passes. Note: this could probably be vectorized as an outer product '''
for county in df['Id2'].unique():
    for year in df['Year'].unique():
        for industry in df['Meaning of 2007 NAICS code'].unique():
            temp = pd.DataFrame(index = [len(shares)], columns = ['County', 'Year', 'Industry', 'Share', 'Total'])
            temp[['County', 'Year', 'Industry']] = [county, year, industry]
#            try:
            temp['Share'], temp['Total'] = variable(df, industry, county, year)
            shares = shares.append(temp)
#            except ValueError:
#                continue
            
            percent_done = len(shares) / total_passes
            print(percent_done*100, '% done.')
            shares.sort_values(['County','Year'])
            shares.to_csv('marketshares.csv')
          
''' The dataframe 'data' is now filled out. Save to file '''



df=pd.read_csv('NESdata.csv', header=0)
df = df.replace('D', 0)
df = df.replace('S', 0)
df = df.replace('a', 9)
df=df.replace('b', 59)
df=df.replace('c',174)
df=df.replace('e',374)  
df=df.replace('f', 749)
df=df.replace('g',1750)
df=df.replace('h',3749) 
df=df.replace('i',7499)
df=df.replace('j',17499)
df=df.replace('31-33',32)
df=df.replace('44-45',44)
df=df.replace('48-49',48)

mask = (df['2007 NAICS code'] != "0")
df = df.loc[~mask]


def var_rates(df, county, year):
   df = df[(df['Year']==year) & (df['Id2']==county)]           # restrict df to only relevant year
   emprate = df['Employment'].astype(float) .sum()    # don't forget to convert strings to floats before summing
   return emprate
    
growth = pd.DataFrame(columns = ['Id2', 'Year', 'Employment', 'Rate'])

index = len(df['Id2'].unique()) * len(df['Year'].unique()) * len(df['2007 NAICS code'].unique())
for county in df['Id2'].unique():
    for year in df['Year'].unique():
        temp = pd.DataFrame(index = [len(growth)], columns = ['Id2', 'Year', 'Employment', 'Rate'])
        temp[['Id2', 'Year']] = [county, year]
        temp['Employment']= var_rates(df, county, year)
        growth = growth.append(temp)
        
        percent_done = len(growth) / index
        print(percent_done*100, '% done.')
        df.to_csv('totalemp.csv')

''' The dataframe 'data' is now filled out. Saved to file '''        




df=pd.read_csv('NESdata.csv', header=0)
df = df.replace('D', 0)
df = df.replace('S', 0)
df = df.replace('a', 9)
df=df.replace('b', 59)
df=df.replace('c',174)
df=df.replace('e',374)  
df=df.replace('f', 749)
df=df.replace('g',1750)
df=df.replace('h',3749) 
df=df.replace('i',7499)
df=df.replace('j',17499)
df=df.replace('31-33',32)
df=df.replace('44-45',44)
df=df.replace('48-49',48)

df.sort_values(['Id2','Year'])


