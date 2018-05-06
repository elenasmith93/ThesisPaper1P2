import pandas as pd

df = pd.read_csv('NESdata.csv')'
df2 = pd.read_csv('NESdata.csv')

''' Replace all D and S values with 0 '''
df = df.replace('D', 0)
df = df.replace('S', 0)


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
data = pd.DataFrame(columns = ['County', 'Year', 'Industry', 'Share', 'Total'])

''' Compute the total number of iterations needed '''
total_passes = len(df['Geographic area name'].unique()) * len(df['Year'].unique()) * len(df['Meaning of 2007 NAICS code'].unique())

''' Iterate through all passes. Note: this could probably be vectorized as an outer product '''
for county in df['Id2'].unique():
    for year in df['Year'].unique():
        for industry in df['Meaning of 2007 NAICS code'].unique():
            temp = pd.DataFrame(index = [len(data)], columns = ['County', 'Year', 'Industry', 'Share', 'Total'])
            temp[['County', 'Year', 'Industry']] = [county, year, industry]
#            try:
            temp['Share'], temp['Total'] = variable(df, industry, county, year)
            data = data.append(temp)
#            except ValueError:
#                continue
            
            percent_done = len(data) / total_passes
            print(percent_done*100, '% done.')
            
            
''' The dataframe 'data' is now filled out. Save to file '''

def var2(df2, industry, county, year):
    ''' A function which returns the industry share and total employment across all given industries
        for a given industry, county, and year '''
    df2 = df2[(df2['Year']==year) & (df2['Id2']==county)]           # restrict df to only relevant year
    industry_df = df[df['Meaning of 2007 NAICS code'] == industry]  # get a subset corresponding to industry
    total_employment = df['Number of establishments'].astype(float).sum()/2      # don't forget to convert strings to floats before summing
    industry_employment = industry_df['Number of establishments'].astype(float).sum()

    return industry_employment/total_employment, total_employment