# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# static data
year = [1941,1942,1943,1944,1945,1946,1947,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,
        1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977
        ,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996
        ,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
unemployment_percentage = [9.9,4.7,1.9,1.2,1.9,3.9,3.9,3.9,3.8,5.9,5.3,3.3,3,2.9,5.5,4.4,4.1,4.3,6.8,5.5,5.5,6.7
                ,5.5,5.7,5.2,4.5,3.8,3.8,3.6,3.5,4.9,5.9,5.6,4.9,5.6,8.5,7.7,7.1,6.1,5.8,7.1,7.6,9.7,9.6
                ,7.5,7.2,7,6.2,5.5,5.3,5.6,6.8,7.5,6.9,5.6,5.4,4.9,4.5,4.2,4,4.7,5.8,6,5.5,5.1,4.6,4.6,5.8,9.3,9.6]

employment_percentage = 
# TODO: working on this file to add more codes...

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Line Chart'),

    # a div to put a short description
    html.Div(children='''
        Data courtesy of Datahub.io
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                {'x': year, 'y': unemployment_percentage, 'type': 'line', 'name': 'Unemployment Percentage'},
            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Percentage of Unemployed People in USA'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)


