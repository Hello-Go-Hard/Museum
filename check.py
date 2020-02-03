def b():
    data = pd.read_csv('cstmc-CSV-en.csv', sep='|', error_bad_lines=False)
    some_series = data[['ObjectName', 'BeginDate', 'EndDate']]
    duration = []
    some_series_of_nan = data[['BeginDate', 'EndDate']].isna()
    count_of_nan = 0
    for i in some_series_of_nan.index:
        if some_series_of_nan['BeginDate'][i] == False or some_series_of_nan['EndDate'][i] == False:
            count_of_nan += 1
    for i in some_series.index:
        try:
            duration.append(int(some_series['EndDate'][i]) - int(some_series['BeginDate'][i]))
        except ValueError:
            duration.append(0)
    some_series.insert(3, 'new column', duration)
    print(some_series.loc[some_series['new column'].astype(float).idxmax()][['ObjectName', 'new column']])
 #   print("Unknown  ", count_of_nan)
    dict = {'Object': [some_series.loc[some_series['new column'].astype(float).idxmax()]['ObjectName'], 'NaN date'], 'Duration': [ some_series['new column'].max(), count_of_nan]}
    output = pd.DataFrame(dict)
    #output.to_csv('general-stats.csv')