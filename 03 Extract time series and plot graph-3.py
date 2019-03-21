import cdstoolbox as ct

 
@ct.application(title='Extract a time series and plot graph')
@ct.input.dropdown('variable', values=[
    '2m_temperature', '10m_u_component_of_wind', '10m_v_component_of_wind',
    'mean_sea_level_pressure'
])
@ct.input.text('longitude', type=float, default=75.)
@ct.input.text('latitude', type=float, default=43.)
@ct.output.livefigure()
def plot_time_series(
    variable,
    longitude,
    latitude,
):
    """
    Application main steps:
    
    - retrieve a variable over a defined time range
    - select a location, defined by longitude and latitude coordinates
    - compute the daily average
    - show the result as a timeseries on an interactive chart
    
    """

    # Time range
    data = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'variable': variable,
            'grid': ['3', '3'],
            'product_type': 'reanalysis',
            'year': [
                '2008','2009','2010',
                '2011','2012','2013',
                '2014','2015','2016',
                '2017'
            ],
            'month': [
                '01', '02', '03', '04', '05', '06',
                '07', '08', '09', '10', '11', '12'
            ],
            'day': [
                '01', '02', '03', '04', '05', '06',
                '07', '08', '09', '10', '11', '12',
                '13', '14', '15', '16', '17', '18',
                '19', '20', '21', '22', '23', '24',
                '25', '26', '27', '28', '29', '30',
                '31'
            ],
            'time': ['00:00', '06:00', '12:00', '18:00'],
        }
    )    
    
    # Location selection
    
    # Extract the closest point to selected lon/lat (no interpolation). 
    # If wrong number is set for latitude, the closest available one is chosen:
    # e.g. if lat = 4000 -> lat = 90.
    # If wrong number is set for longitude, first a wrap in [-180, 180] is made,
    # then the closest one present is chosen:
    # e.g. if lon = 200 -> lat = -160.
    data_sel = ct.geo.extract_point(data, lon=longitude, lat=latitude)
        
    fig = ct.chart.line(data_daily)
    
    return fig
