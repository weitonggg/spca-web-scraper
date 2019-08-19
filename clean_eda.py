### data cleaning ####
def split_age(x):
    age_mths = []
    for i in range(0,31):
        if 'yrs' in x.age[i] and 'mth' in x.age[i]:
            yr_index = x.age[i].find('yr')
            mth_index = x.age[i].find('mth')
            yr = int(x.age[i][:yr_index])
            mth = int(x.age[i][yr_index+3:mth_index])
            age_mths.append(yr * 12 + mth)
            
        elif 'yr' in x.age[i] and 'mth' in x.age[i]:
            yr_index = x.age[i].find('yr')
            mth_index = x.age[i].find('mth')
            yr = int(x.age[i][:yr_index])
            mth = int(x.age[i][yr_index+2:mth_index])
            age_mths.append(yr * 12 + mth)
            
        elif 'yr' in x.age[i]:
            yr_index = x.age[i].find('yr')
            yr = int(x.age[i][:yr_index])
            age_mths.append(yr*12)
            
        elif 'mth' in x.age[i]: 
            mth_index = x.age[i].find('mth')
            mth = int(x.age[i][:mth_index])
            age_mths.append(mth)

        else: 
            age_mths.append(0)
    return age_mths

adoptcats['age_mths']  =  split_age(adoptcats)

adoptcats.colour = adoptcats.colour.replace({'Tri':'Calico',
                          'BlackandWhite':'BlackWhite',
                          'Tabby/White':'TabbyWhite'})
    
adoptcats.breed = adoptcats.breed.replace({'x-Burmese': 'Burmese',
                         'XSiamesePersian': 'SiamesePersian'})
    
## Explore dataset ###
ageplot = sns.distplot(adoptcats.age_mths, kde = False)
ageplot.set_title('Distribution of Age (Months)')
ageplot.set_xlabel('Months')
ageplot

sns.boxplot(x = adoptcats.gender, y = adoptcats.age_mths)

adoptcats.gender.value_counts()
adoptcats.breed.value_counts()
adoptcats.colour.value_counts()

